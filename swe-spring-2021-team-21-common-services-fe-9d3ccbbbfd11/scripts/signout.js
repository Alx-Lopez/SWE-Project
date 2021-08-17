// Prevent users from directly navigating to this page without having signed out
const redirectUrl = `https://${window.location.hostname}/`;
// check if a name does not exist in sessionStorage
if (sessionStorage.getItem('name') == null)
    // trigger a redirect to the landing page
    window.location.assign(redirectUrl);

$(document).ready(function() {
    const p_personalThanks = document.getElementById('personalThanks');
    const name = sessionStorage.getItem('name');
    p_personalThanks.textContent = `Thank you for using our service, ${name}!`;
    sessionStorage.clear();
}); // End of document.ready