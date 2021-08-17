# README #
## WeGo Selenium Test Cases ##
>*At WeGo, our mission is to create unique, high-value, first-of-a-kind software applications for the Transportation Industry.*  

This is the automated black box test case repository for our Demand services of WeGo.  
Current test cases include: login, requesting the 'Disability Ride Share' service, and signing out.  

## How do I get set up? ##

### **Summary of set up** ###
We use [Selenium](https://www.selenium.dev/ "Selenium Home Page") for our automated black box test cases, specifically [Selenium IDE](https://www.selenium.dev/downloads/ "Selenium IDE main page") which is available as an extension on [Chrome](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd "Chrome extension page") and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/ "Firefox extension page"). The scripts provided in this repository are pytest files, but provide a good idea in understanding the use of Selenium and even how to automate these scenarios in python.  
It's also important to note that when exporting, Selenium kinda forgot to include the `logout()` function in `test_placeOrder.py`. You can find that function in `test_logout.py`.

### Who do I talk to? ###
For more information regarding automated black box tests or a live demo of these scripts, reach out to me: Cristina!  
I know this README is kinda unnecessary at this point, but I thought I'd include resource links and all that regardless because what else am I gonna do? Not be a tryhard???? Too late for that. 🤪