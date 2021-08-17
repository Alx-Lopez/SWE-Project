// load this file into any page that you do not want to show up when the user is logged in
var checkSessionExists;
(checkSessionExists = function(){
    let cloud = window.location.hostname.split('.')[0];
    const redirectUrl = `https://${window.location.hostname}/${cloud}-fe/`;
    // check if the user is currently logged in and has a session
    if (localStorage.getItem('email') != null)
        // trigger a redirect to dashboard page
        window.location.assign(redirectUrl);
})();