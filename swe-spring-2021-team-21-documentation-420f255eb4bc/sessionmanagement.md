# Session Management #

## What is a Session? ##
A Session is essentially a container for a user's interactions with a site that take place within a certain amount of time.  It is used to remember what a user has done.

## Why Do They Matter? ##
Sessions are important because they allow the persistence of data across pages without interacting with a database.  This can be done in a variety of different ways, with the common ones being cookies, and localStorage.  For this application, we will prefer localStorage as it is secure and easier to implement correctly.  Cookies are more useful for other tasks such as saving a user's shopping cart.

## How to Use localStorage ##
As mentioned above, we will be persisting user login sessions using localStorage.  We can do this by storing the user's email in localStorage upon a successful login, and then when viewing locked pages, verifying that this storage is not empty before displaying the page, and redirecting if it is empty.  Then of course when the user logs out, we'll want to clear this localStorage so nobody else can access that user's pages without logging into their account.

### Example Calls ###
```Javascript
// setting local storage to remember a user's email
localStorage.setItem('email', 'example@gmail.com');

// retrieving an item from local storage
const email = localStorage.getItem('email');

// clearing local storage (should be done on logout)
localStorage.clear()
```

### Application of Examples ###
This code will be very similar to what will actually be included in our system to persist logins.

Login:
```Javascript
// in the success section of the login script, you'll want to set both the email for interacting with the database, and the user's name for displaying on the header once the user is successfully logged in
localStorage.setItem('email', '<get the email from the form input>')
localStorage.setItem('name', '<name pulled from server response>')
```
Logout:
```Javascript
// once the user has logged out, we'll want to clear the localStorage so the user has to log in again before accessing any locked pages
localStorage.clear()
// trigger a redirect to the signed out page
```
Locked pages:
```Javascript
// On each 'locked' page after login (dashboard, order screen, etc), include the following code at the beginning to test if these values are set.  If not, trigger a redirect to the login page
if (localStorage.getItem('email') == null)
    // trigger a redirect to login page

// additionally while a user is logged in, we do not want them to see the login and register pages, so we want the previous check in reverse
if (localStorage.getItem('email') != null)
    // trigger a redirect to the dashboard
```
Header:
```Javascript
// in the header file, when a user is logged in, we'll want to display a logout button and potentially their name on the header
if (localStorage.getItem('email') == null)
{
    // put in some default things to be displayed in the header when the user is not logged in
}
else
{
    // display the logout button
    // OPTIONAL:
    // possibly grab the name
    username = localStorage.getItem('name')
    // then display it next to the logout button
}
```