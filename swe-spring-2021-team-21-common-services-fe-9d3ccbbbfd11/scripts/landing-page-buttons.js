$(document).ready( function() {
    const div_landing_page_content = document.getElementById('landing-page-content');
    
    // TODO: optimize this code to reduce redundancy
    if (localStorage.getItem('email') == null) {
        const button_register = document.createElement('button');
        const button_login = document.createElement('button');

        button_register.textContent = "REGISTER NOW";
        button_login.textContent = "LOGIN NOW";

        button_register.addEventListener('click', function() {
            window.location.assign(`https://${window.location.hostname}/register.html`);
        })
        button_login.addEventListener('click', function() {
            window.location.assign(`https://${window.location.hostname}/login.html`);
        })

        div_landing_page_content.append(button_register);
        div_landing_page_content.append(button_login);
    }
    else {
        const button_dashboard = document.createElement('button');
        
        let cloud = window.location.hostname.split('.')[0];
        
        button_dashboard.addEventListener('click', function() {
            window.location.assign(`https://${window.location.hostname}/${cloud}-fe/`);
        })

        button_dashboard.textContent = "MY ACCOUNT";

        div_landing_page_content.append(button_dashboard);
    } // end of if-else
}); // End of document.ready