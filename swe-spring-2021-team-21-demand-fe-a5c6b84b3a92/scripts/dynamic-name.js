$(document).ready(function() {
    const name = localStorage.getItem('name');
    var welcome = document.getElementById("welcomeMessage");
    welcome.textContent = `Welcome, ${name}!`;
})