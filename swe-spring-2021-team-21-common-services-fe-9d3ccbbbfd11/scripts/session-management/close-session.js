// Call this function to log out the user and clear the session
function clearSession() {
    const redirectUrl = `https://${window.location.hostname}/signout-confirmation.html`;
    sessionStorage.setItem('name', localStorage.getItem('name'));
    localStorage.clear();
    window.location.assign(redirectUrl);
}