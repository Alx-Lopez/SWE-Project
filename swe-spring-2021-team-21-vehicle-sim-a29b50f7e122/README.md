# README #
## WeGo Vehicle Simulator ##
>*At WeGo, our mission is to create unique, high-value, first-of-a-kind software applications for the Transportation Industry.*

This is the repository for WeGo's Vehicle Simulator.

## How do I get set up? ##

### **Summary of set up** ###
To work with the vehicle simulator, it is highly recommended for you to use [Pycharm](https://www.jetbrains.com/pycharm/ "Pycharm Main Page"), which comes with git bundled and enabled by default. If you wish to use something else, be sure to install [git](https://git-scm.com/ "Git Main Page") so you can clone the repository to your machine. To get a basic understanding of git, be sure to check out the "*Git Documentation*" file found in the team's Google Drive under the folder "*General Documentation*". It is also recommended to read a tutorial on how to properly use git in your choice of editor. From there, you can create branches for your features and contribute to the deployment of WeGo's Vehicle Simulator!

### **How to Run Tests** ###
All of our classes should be unit tested before creating a Pull Request to ensure that our system continues to work as intended regardless of whatever features/changes are made. We can confirm this by using the coverage module before you push your code. Click [here](https://bitbucket.org/swe-spring-2021-team-21/documentation/src/master/unittestcoverageKPI.md "Coverage Documentation") for more information on how to use the coverage module to test your code. Make sure the classes are [dynamically importing](https://bitbucket.org/swe-spring-2021-team-21/documentation/src/master/dynamicImports.md "Python Dynamic Importing Documentation") any files in external folders to properly run these tests. Include the coverage report at the end of your Pull Request description.  

### **Deployment Instructions** ###
Once your individual components are tested in their own branches and are successfully merged together with the development branch, the development branch needs to be merged with the **test-deployment** branch for testing. In order to do this, you need to create a **Pull Request** on BitBucket to have your code reviewed before testing. Please view the *Code Review* section for more details related to creating and resolving a Pull Request. Once the Pull Request is approved and merged, reach out to another team member to test the simulator. Upon successful testing on the test-deployment branch, conduct another Pull Request to merge the test-deployment branch with the master branch.

## Contribution Guidelines ##

### **Writing Tests** ###
All classes and their functions should be rigorously tested to ensure that they're working as we intend them to. This may seem a bit tricky since our system is heavily integrated with the use of our database, but the [mock](https://docs.python.org/3/library/unittest.mock.html "unittest.mock — mock object library - Python Documentation") module helps us cover this.  
With this in mind, all unit tests should properly make use of setUp() and tearDown() methods when applicable. The first version of a unit test should have at least two test cases per function, one that passes and one that fails. Proper documentation and naming conventions as seen in the *Code Review* section applies.

### **Code Review** ###
Code Reviews are required and are conducted when creating a Pull Request from development --> test-deployment and test-deployment --> master. Pull Requests are **required** when merging between these branches. Be sure to include a summary of changes and specific commits in the description of your Pull Request, and list at least one other team member as a reviewer. It is also important to include the test coverage output at the end of your Pull Request description. See *How to Run Tests* for more information relating to test coverage.  
A Pull Request is approved if no apparent flaws are present within the code, and if new features are properly documented.  
There are some simple standards to have within your code.  
It is important to use good naming conventions on variables, and include many comments explaining what the code you are writing does to ensure anyone else can easily understand what is going on.
For example:
```python
    ...
    # extract the password from the POST request
    password = postBody['password']

    # create an instance of user with received credentials
    newUser = user.User(email, fname, lname)

    # attempt to register a new user and record whether it is successful
    successfulRegister = newUser.register(password)
```
Proper formatting and indentations are of course required.  
As an additional best practice, leave `# TODO:` comments for yourself and others when you know *where* something needs to be done, but aren't sure quite how to do it yet. This helps keep the code organized as well as leaving a reminder that it is not finished.  
Feel free to reach out to the team if you want a second look at your code for readability or functionality advice as you see fit.

### **Branching Conventions** ###
When a new feature is set to be implemented for this repository, a new branch with the name of the feature can be created. When the feature is seen as complete, a merge should be done with the **development** branch first, where code components should be tested with other components in the program. If there are any faults on the development branch, continue to merge bug fixes from component branches to the development branch until it is successfully working as intended.  Once conflicts are resolved and the code is running as intended in the development branch, it can then be merged into the **test-deployment** branch for additional testing. Upon successful testing, the branch will be closed. See *Code Review* for further information on how to merge to **test-deployment** and see *Deployment Instructions* for further information to achieve a successful deployment.

### Who do I talk to? ###
For any further clarification or questions regarding this README or additional information to contribute to this specific repository, reach out to Alex as soon as possible as I have created this initial README and primarily worked on this repository. A DM or general message through Discord or Slack works best.  
Any fundamental suggestions/changes to components in this repository is best done by reaching out to the entire team.