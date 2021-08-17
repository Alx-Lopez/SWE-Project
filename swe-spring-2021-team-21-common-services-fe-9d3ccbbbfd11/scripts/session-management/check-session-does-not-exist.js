// load this file on any page that you do not want the user access without being logged in
var checkSessionDoesNotExist;
(checkSessionDoesNotExist = function(){
    const redirectUrl = `https://${window.location.hostname}/login.html`;
    // check if an email does not exist in localStorage
    if (localStorage.getItem('email') == null)
        // trigger a redirect to login page
        window.location.assign(redirectUrl);
})();