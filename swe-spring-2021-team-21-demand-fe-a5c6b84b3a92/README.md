# README #
## WeGo Demand (Front-end) ##
>*At WeGo, our mission is to create unique, high-value, first-of-a-kind software applications for the Transportation Industry.*

This is the front end repository for the Demand Cloud of WeGo.  
Demand functionalities include: requesting a service. This repository is responsible for the look and front-end functionality of these webpages.

## How do I get set up? ##

### **Summary of set up** ###
To work with the front end, it is highly recommended for you to download [Visual Studio Code](https://code.visualstudio.com/ "Visual Studio Code Main Page") and add the extension *Live Server*. Regardless of your editor choice, be sure to install [git](https://git-scm.com/ "Git Main Page") so you can clone the repository to your machine. To get a basic understanding of git, be sure to check out the "*Git Documentation*" file found in the team's Google Drive under the folder "*General Documentation*". From there, you can create branches for your features and contribute to the deployment of the front end for WeGo's Demand Services!

### **Deployment Instructions** ###
Once your individual components are tested in their own branches and are successfully merged together with the development branch, the development branch needs to be merged with the **test-deployment** branch for a real test on our droplet. In order to do this, you need to create a **Pull Request** on BitBucket to have your code reviewed before testing. Please view the *Code Review* section for more details related to creating and resolving a Pull Request. Once the Pull Request is approved and merged, be sure to reach out to the current DevOps member to inform them to pull the code to the site. Upon successful testing on the test-deployment branch, conduct another Pull Request to merge the test-deployment branch with the master branch.  

### Additional Notes: ###
When notifying your DevOps member, please inform them of the following if they are included in your commit:

* New pages or files that require a separate location block

## Contribution Guidelines ##

### **Code Review** ###
Code Reviews are required and are conducted when creating a Pull Request from development --> test-deployment and test-deployment --> master. Pull Requests are **required** when merging between these branches. Be sure to include a summary of changes and specific commits in the description of your Pull Request, and list at least one other team member as a reviewer.  
A Pull Request is approved if no apparent flaws are present within the code, and if new features are properly documented.  
There are also some simple standards to have within your code.  
Variable names should be meaningful and related to its data, not generic. A variable that stores the first name of a user could be  
```javascript
    var fName = "Cristina";
    var firstName = "Cristina";
    var first_name = "Cristina";
```
but not  
```javascript
    var foo = "Cristina";
    var fn = "Cristina";
    var x = "Cristina";
```
Function names should follow a similar naming scheme.  
As seen in the above code block, all javascript code should end with a semicolon where applicable.  
Proper formatting and indentations are required.  
As an additional best practice, leave `// TODO:` comments for yourself and others when you know *where* something needs to be done, but aren't sure quite how to do it yet. This helps keep the code organized as well as leaving a reminder that it is not finished.  
Feel free to reach out to the team if you want a second look at your code for readability or functionality advice as you see fit.

### **Branching Conventions** ###
When a new feature is set to be implemented for this repository, a new branch with the name of the feature can be created. When the feature is seen as complete, a merge should be done with the **development** branch first. If there are any faults on the development branch, continue to merge any fixes to the development branch until it is successfully working as intended. Once conflicts are resolved and the code is running as intended on the development branch, it can then be merged into the **test-deployment** branch to test it on the droplet. Upon a successful deployment, the branch will be closed. See *Code Review* for further information on how to merge to **test-deployment** and see *Deployment Instructions* for further information to achieve a successful deployment.

### **UI Style Guide** ###
Front end styling *must* follow the established UI Style Guide found in the team [Google Drive](https://docs.google.com/document/d/1yQMzaPrCx96RAMumibdKoF74SZI7UsgTa_vAMWkGkWc/edit?usp=sharing "UI Style Guide Google Drive Link").  
Reach out to the team if you have a different style idea so that the UI Style Guide could be iterated.

### **CSS Documentation** ###
A clear table of contents is required for all CSS pages with multiple components.  
It should begin with more general/global stylings ( *, body, or other HTML tags) and be followed with more component-specific styles in order of appearance on the HTML page.  
An example of a table of contents is as follows:
``` css
/* 
    ========================
        Table of Contents
    ========================

    1) Variables (Colors) 

    2) Global Styles
    
    3) Typography

    4) Components
        4.1) Header
        4.2) Buttons
*/
```
For navigation and readability sake, these headings should also precede the actual section of styling.  
An example of this is as followed:
``` css
/* 
    ========================
    ========================
        2) Global Styles
    ========================
    ========================
*/

* {
    margin: 0px;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
    color: #66265D;
}
```
An exception can be made for CSS styling with a single component. However, they should still have a comment at the top of the file that names the styled component.  

## Who do I talk to? ##
For any further clarification or questions regarding this README or additional information to contribute to this specific repository, reach out to Cristina as soon as possible as I have created this initial README and primarily worked on this repository. A DM or general message through Discord or Slack works best.  
Any fundamental suggestions/changes to components in this repository is best done by reaching out to the entire team.