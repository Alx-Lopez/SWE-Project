#!/usr/bin/python3
import logging
import json
import user
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

# Class Logger we can use for debugging our Python service. You can add an additional parameter here for
# specifying a log file if you want to see a stream of log data in one file.
logging.basicConfig(level=logging.DEBUG)


# BaseHTTPRequestHandler is a class from the http.server python module. http.server is a simple
# module used for creating application servers. BaseHTTPRequestHandler will help us respond to requests that arrive
# at our server, matching a specified hostname and port. For additional documentation on this module,
# you can read: https://docs.python.org/3/library/http.server.html
class CmnSrv(BaseHTTPRequestHandler):

    # HTTP Response code dictionary constant we can reuse inside our responses back to the client. Typically this
    # would be in a configuration file where you store constants you repeatedly use throughout your services.
    HTTP_STATUS_RESPONSE_CODES = {
        'OK': HTTPStatus.OK,
        'FORBIDDEN': HTTPStatus.FORBIDDEN,
        'NOT_FOUND': HTTPStatus.NOT_FOUND,
        'BAD_REQUEST': HTTPStatus.BAD_REQUEST
    }

    # Here's how we extract the POST body of data attached to the request by the client.
    def extract_POST_Body(self):
        # The content-length HTTP header is where our POST data will be in the request. So we'll need to
        # read the data using an IO input buffer stream built into the http.server module.
        postBodyLength = int(self.headers['content-length'])
        postBodyString = self.rfile.read(postBodyLength)
        postBodyDict = json.loads(postBodyString)
        logging.info('POST Body received: ' + json.dumps(postBodyDict, indent=4, sort_keys=True))
        return postBodyDict

    # The do_POST(self) function is how we respond to POST requests from clients.
    # we should only need POST for Register/Login
    def do_POST(self):
        path = self.path
        # Extract the POST body data from the HTTP request, and store it into a Python
        # dictionary we can utilize inside of any of our POST endpoints.
        postBody = self.extract_POST_Body()
        status = self.HTTP_STATUS_RESPONSE_CODES['BAD_REQUEST']

        # initialize the response body
        responseBody = {}

        # REGISTRATION PATH
        if '/register' in path:
            first_name = postBody['first_name']
            last_name = postBody['last_name']
            email = postBody['email']
            password = postBody['password']  # should already be hashed & salted

            # create an instance of user with received credentials
            new_user = user.User(email, first_name, last_name)

            # attempt to register a new user and record whether it is successful
            successful_register = new_user.register(password)

            # if the user was successfully registered, send back a 200 OK response
            if successful_register:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']

        # LOGIN PATH
        elif '/login' in path:
            email = postBody['email']
            entered_password = postBody['password']

            # create an instance of user with received credentials
            existing_user = user.User(email)

            # attempt to login the user and record whether it is successful
            successful_login, name = existing_user.login(entered_password)

            # if the user was successfully logged in, send back a 200 OK response and the user's name
            if successful_login:
                status = self.HTTP_STATUS_RESPONSE_CODES['OK']
                responseBody['data'] = name

        # RESPONSE
        # sending the HTTP response
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # When using the json.dumps() method, you may encounter data types which aren't easily serializable into
        # a string. When working with these types of data you can include an additional parameters in the dumps()
        # method, 'default=str' to let the serializer know to convert to a string when it encounters a data type
        # it doesn't automatically know how to convert.
        response = json.dumps(responseBody)
        logging.info('Response: ' + response)
        byteStringResponse = response.encode('utf-8')
        self.wfile.write(byteStringResponse)


# Turn the application server on at port 8082 on localhost and fork the process.
if __name__ == '__main__':
    hostName = "localhost"
    # Ports are part of a socket connection made between a server and a client. Ports 0-1023 are
    # reserved for common TCP/IP applications and shouldn't be used here. Communicate with your
    # DevOps member to find out which port you should be running your application off of.
    serverPort = 8082
    appServer = HTTPServer((hostName, serverPort), CmnSrv)
    logging.info('Server started http://%s:%s' % (hostName, serverPort))

    # Start the server and fork it. Use 'Ctrl + c' command to kill this process when running it in the foreground
    # on your terminal.
    try:
        appServer.serve_forever()
    except KeyboardInterrupt:
        pass

    appServer.server_close()
    logging.info('Server stopped')
