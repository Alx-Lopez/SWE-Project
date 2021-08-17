$(document).ready(function() {
    let cloud = window.location.hostname.split('.')[0];
    // Event listener when user submits Log In Form
    const submitButton = document.getElementById("submitLogin");
    const requestUrl = '/common-services/login';
    const redirectUrl = `https://${window.location.hostname}/${cloud}-fe/`;

    // TODO: allow this function to work when user presses the enter key
    $(submitButton).click(function(){
        const email = document.getElementById("email").value;
        const userPassword = document.getElementById("password").value;

        const salt = sha256(email);
        const password = sha256(salt + userPassword);

        const credentials = { email, password };

        // TODO: use fetch instead of AJAX
        $.ajax({
            url: requestUrl,
            type:"POST",
            data: JSON.stringify(credentials),
            contentType: "application/json; charset=utf-8",
            statusCode: {
                200: function(response) {
                    // selecting user's name from backend response
                    const name = response.data;
                    // add the email to localStorage for session persistence
                    // add the name to localStorage for personal welcome message in dashboard
                    localStorage.setItem('email', email);
                    localStorage.setItem('name', name);
                    window.location.assign(redirectUrl);
                },
                400: function() {
                    invalidInputMessage('Invalid credentials.');
                }
            },
            error: function() {
                invalidInputMessage('An error occurred.');
            }
        }) // End of AJAX
    }) // End of click Event Listener
}) // End of document ready Event Listener