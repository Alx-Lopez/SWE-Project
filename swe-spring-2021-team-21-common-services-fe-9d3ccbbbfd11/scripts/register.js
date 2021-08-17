$(document).ready(function(){
    // Setting up for our event listener
    const submitButton = document.getElementById("submitRegistration");
    const requestUrl = '/common-services/register';
    const redirectUrl = `https://${window.location.hostname}/login.html`;
    const MAX_LENGTH = 255;

    // TODO: allow this function to work when user presses the enter key
    $(submitButton).click(function() {
        const first_name = document.getElementById("firstName").value.trim();
        const last_name = document.getElementById("lastName").value.trim();
        const email = document.getElementById("email").value;
        const userPassword = document.getElementById("password").value;

        const isFirstNameValid = (first_name.length > 0) && (first_name.length <= MAX_LENGTH);
        const isLastNameValid = (last_name.length > 0) && (last_name.length <= MAX_LENGTH);

        const emailCheckRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)$/;
        const isEmailValid = (emailCheckRegex.test(email)) && (email.length <= MAX_LENGTH);

        const passwordCheckRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$/;
        const isPasswordValid = passwordCheckRegex.test(userPassword);

        if (!isFirstNameValid || !isLastNameValid)
            invalidInputMessage("Invalid name entry.");
        else if (!isEmailValid)
            invalidInputMessage("Invalid email.");
        else if (!isPasswordValid)
            invalidInputMessage("Invalid password.");
        else {
            const salt = sha256(email);
            const password = sha256(salt + userPassword);
            const credentials = { first_name, last_name, email, password };
            
            $.ajax({
                url: requestUrl,
                type:"POST",
                data: JSON.stringify(credentials),
                contentType: "application/json; charset=utf-8",
                statusCode: {
                    200: function(){
                        window.location.assign(redirectUrl);
                    },
                    400: function(){
                        invalidInputMessage('Invalid email.');
                    }
                },
                error: function() {
                    invalidInputMessage('An error occurred.');
                }
            }) // End of AJAX
        } // End of if-else chain
    }) // End of click Event Listener

    // Elements for password icon functions
    const questionIcon = document.getElementById("passwordDetails");
    const passwordReqDiv = document.getElementById("passwordReq");
    const toggleIcon = document.getElementById("visibilityIcon");

    // Shows password requirements when mouse is hovered over question mark icon
    $(questionIcon).on({
        'mouseenter':function(){
            passwordReqDiv.style.visibility = 'visible';
            passwordReqDiv.style.opacity = 1;
        },
        'mouseleave':function(){
            passwordReqDiv.style.visibility = 'hidden';
            passwordReqDiv.style.opacity = 0;
        }
    })

    // Allows the user to unmask and view their password before submission
    $(toggleIcon).click(function() {
        const passwordElement = document.getElementById("password");
        const type = passwordElement.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordElement.setAttribute('type', type);
        toggleIcon.classList.toggle('fa-eye-slash');
    });
}) // End of document ready Event Listener