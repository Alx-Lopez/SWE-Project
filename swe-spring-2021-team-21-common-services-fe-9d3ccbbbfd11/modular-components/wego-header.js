document.body.onload= addHeader;

function addHeader() {
    // Initializing the Header and global elements (Logo and ul)
    const body = document.querySelector('body');
    const header = document.createElement('header');
    const divLogo = document.createElement('div');
    const h4_textLogo = document.createElement('h4');
    const a_textLogo = document.createElement('a');
    const ulHeaderLinks = document.createElement('ul');

    let cloud = window.location.hostname.split('.')[0];
    const textContent_textLogo = cloud === 'demand' ? 'WeGo' : 'WeGo Fleet Managers'

    // Setting classes, attributes, and href for Logo
    divLogo.setAttribute('class','logo');
    ulHeaderLinks.setAttribute('class', 'headerLinks');
    a_textLogo.textContent = textContent_textLogo;
    a_textLogo.setAttribute('href', '/');

    // Appending Logo and ul
    body.insertBefore(header, body.firstChild);
    header.append(divLogo);
    divLogo.append(h4_textLogo);
    h4_textLogo.append(a_textLogo);
    header.append(ulHeaderLinks);

    // Check if user is logged in for appropriate header link(s)
    if (localStorage.getItem('email') != null) {
        // User is logged in, so list User Dashboard link

        // Creating User Dashboard li and link
        const li_dashboard = document.createElement('li');
        const a_dashboard = document.createElement('a');
        const li_signOut = document.createElement('li');
        const a_signOut = document.createElement('a');
        
        // Setting attribute and href
        a_dashboard.textContent = "My Dashboard";
        a_dashboard.setAttribute('href', `/${cloud}-fe/`);
        a_signOut.textContent = "Sign Out"

        // Setting event listener to Sign Out
        $(a_signOut).click(function() {
            clearSession();
        })

        // Appending to ul
        ulHeaderLinks.append(li_dashboard);
        li_dashboard.append(a_dashboard);
        ulHeaderLinks.append(li_signOut);
        li_signOut.append(a_signOut);
    }
    else {
        // User is not logged in, so list Register and Log In links
        
        // Creating Register and Login li and link
        const li_register = document.createElement('li');
        const a_register = document.createElement('a');
        const li_login = document.createElement('li');
        const a_login = document.createElement('a');

        // Setting attribures and href
        a_register.textContent = "Register";
        a_login.textContent = "Log In";
        a_register.setAttribute('href', 'register.html');
        a_login.setAttribute('href', 'login.html');
        
        // Appending to ul
        ulHeaderLinks.append(li_register);
        li_register.append(a_register);
        ulHeaderLinks.append(li_login);
        li_login.append(a_login);
    }
}