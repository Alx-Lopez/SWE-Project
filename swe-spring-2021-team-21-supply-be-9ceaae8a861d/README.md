# README #
## WeGo Supply (Backend) ##
>*At WeGo, our mission is to create unique, high-value, first-of-a-kind software applications for the Transportation Industry.*

This is the back end repository for the Supply Cloud of WeGo.  
Supply functionalities include: Fleet Manager Dashboard, adding/removing a fleet, and adding/removing a vehicle. This repository is responsible for the backend code necessary for processing and handling those requests.

## How do I get set up? ##

### **Summary of set up** ###
To work with the backend, it is highly recommended for you to use [Pycharm](https://www.jetbrains.com/pycharm/ "Pycharm Main Page"), which comes with git bundled and enabled by default. If you wish to use something else, be sure to install [git](https://git-scm.com/ "Git Main Page") so you can clone the repository to your machine. To get a basic understanding of git, be sure to check out the "*Git Documentation*" file found in the team's Google Drive under the folder "*General Documentation*". It is also recommended to read a tutorial on how to properly use git in your choice of editor.  
We are working with Python version 3.8.5. You can find and install all of our required packages via requirements.txt. Just run the command:  
```bash
pip install -r requirements.txt -v
```  
From there, you can create branches for your features and contribute to the deployment of the backend for WeGo's Supply Services!

### **How to Run Tests** ###
All of our classes should be unit tested before creating a Pull Request to ensure that our system continues to work as intended regardless of whatever features/changes are made. We can confirm this by using the coverage module before you push your code. Click [here](https://bitbucket.org/swe-spring-2021-team-21/documentation/src/master/unittestcoverageKPI.md "Coverage Documentation") for more information on how to use the coverage module to test your code. Make sure the classes are [dynamically importing](https://bitbucket.org/swe-spring-2021-team-21/documentation/src/master/dynamicImports.md "Python Dynamic Importing Documentation") any files in external folders to properly run these tests. Include the coverage report at the end of your Pull Request description.  

### **Deployment Instructions** ###
Once your individual components are tested in their own branches and are successfully merged together with the development branch, the development branch needs to be merged with the **test-deployment** branch for gray box testing on the droplet. In order to do this, you need to create a **Pull Request** on BitBucket to have your code reviewed before testing. Please view the *Code Review* section for more details related to creating and resolving a Pull Request. Once the Pull Request is approved and merged, reach out to the current DevOps member to inform them to pull the code to the site. Upon successful testing on the test-deployment branch, conduct another Pull Request to merge the test-deployment branch with the master branch.

### Additional Notes: ###
When notifying your DevOps member, please inform them of the following if they are included in your commit:  

* New/changed ports  
* New pages or files that require a separate location block  
* New files that require a new service to run  

## Contribution Guidelines ##

### **Writing Tests** ###
All classes and their functions should be rigorously tested to ensure that they're working as we intend them to. This may seem a bit tricky since our system is heavily integrated with the use of our database, but the [mock](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library - Python Documentation") module helps us cover this.  
An example use of mock is provided below:  
```python
# Necessary import
from unittest import mock

# Mock the function before defining the test_function
# Example: 'user.User.register'
@mock.patch('class.Class.class_function')
def test_function_name(self, mock_class_function):
    print('Testing test_function_name')

    # Setting up mock for the test
    mock_class_function.return_value = "Result"
    
    # Initialize and call the tested function
    class_instance = Class()
    result = class_instance.class_function()

    # Assert that your values are equal
    self.assertEqual("Result", result)
```  
With this in mind, all unit tests should properly make use of setUp() and tearDown() methods when applicable. The first version of a unit test should have at least two test cases per function, one that passes and one that fails. Proper documentation and naming conventions as seen in the *Code Review* section applies.

### **Code Review** ###
Code Reviews are required and are conducted when creating a Pull Request from development --> test-deployment and test-deployment --> master. Pull Requests are **required** when merging between these branches. Be sure to include a summary of changes and specific commits in the description of your Pull Request, and list at least one other team member as a reviewer. It is also important to include the test coverage output at the end of your Pull Request description. See *How to Run Tests* for more information relating to test coverage.  
A Pull Request is approved if no apparent flaws are present within the code, and if new features are properly documented.  
There are some simple standards to have within your code.  
Some of the Supply code on the backend will be copied from templates for receiving POST requests, accessing the database, and sending HTTP responses. That being said, when applicable, it is still important to use good naming conventions on variables, and include many comments explaining what the code you are writing does to ensure anyone else can easily understand what is going on.
For example:
```python
    ...
    # extract the password from the POST request
    password = postBody['password']

    # create an instance of user with received credentials
    newUser = user.User(email, first_name, last_name)

    # attempt to register a new user and record whether it is successful
    successfulRegister = newUser.register(password)
```
**Please follow Python naming conventions, and use proper formatting as shown below**  
```python
class UpperCaseCamelCase()
    def functions_use_underscores()
        variables_use_underscores = 123
``` 
As an additional best practice, leave `# TODO:` comments for yourself and others when you know *where* something needs to be done, but aren't sure quite how to do it yet. This helps keep the code organized as well as leaving a reminder that it is not finished.  
Feel free to reach out to the team if you want a second look at your code for readability or functionality advice as you see fit.

### **Branching Conventions** ###
When a new feature is set to be implemented for this repository, a new branch with the name of the feature can be created. When the feature is seen as complete, a merge should be done with the **development** branch first, where code components should be tested with other components in the program. If there are any faults on the development branch, continue to merge bug fixes from component branches to the development branch until it is successfully working as intended.  Once conflicts are resolved and the code is running as intended in the development branch, it can then be merged into the **test-deployment** branch for gray box testing on the droplet. Upon successful testing, the branch will be closed. See *Code Review* for further information on how to merge to **test-deployment** and see *Deployment Instructions* for further information to achieve a successful deployment.

### Who do I talk to? ###
For any further clarification or questions regarding this README or additional information to contribute to this specific repository, reach out to Suhas, Keaton, or Cristina, the authors of the supply side cloud and code. A DM or general message through Discord or Slack works best.  
Any fundamental suggestions/changes to components in this repository is best done by reaching out to the entire team.