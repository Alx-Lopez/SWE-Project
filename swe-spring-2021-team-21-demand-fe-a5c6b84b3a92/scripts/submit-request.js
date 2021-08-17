const invalidAccessRedirectUrl = `https://${window.location.hostname}/demand-fe/`;
// If no plugin was selected, redirect to the customer dashboard
//     We currently check if a plugin was selected by checking
//     if a plugin was recorded in the user's session storage
if (sessionStorage.getItem('plugin') == null)
    window.location.assign(invalidAccessRedirectUrl);

$(document).ready(function() {
    const plugin = sessionStorage.getItem('plugin');
    const submitButton = document.getElementById('submitRequest');
    const requestUrl = '/demand/request-service';
    const redirectUrl = `https://${window.location.hostname}/demand-fe/order-confirmation.html`;

    $(submitButton).click(function() {
        const formContainer = document.getElementById('requestServiceForm');
        const allInputs = formContainer.getElementsByTagName('input');
        
        var allInputsAreValid = areValidInputs(allInputs);

        if (allInputsAreValid) {
            const email = localStorage.getItem('email');
            var orderDetails = {'plugin': plugin, 'email': email};
            var address = {};
            
            // Looping through all inputs
            // inputs.length - 1 because the last input is our submit button
            index = 0;
            while (index < allInputs.length - 1) {
                const element = allInputs[index];
                const element_ID = element.id;
                const element_value = element.value.trim();
                
                // If an element is a part of the address input, append it to the address object
                // otherwise, append it directly to orderDetails
                if (element.className == 'address')
                    address[element_ID] = element_value;
                else
                    orderDetails[element_ID] = element_value;
        
                index++;
            }

            // Appending address parameters to orderDetails
            orderDetails['address'] = address;
        
            $.ajax({
                url: requestUrl,
                type: "POST",
                data: JSON.stringify(orderDetails),
                contentType: "application/json; charset=utf-8",
                statusCode: {
                    200: function(response) {
                        // Set session storage to include vehicle information and order number
                        sessionStorage.setItem('orderNumber', response['order_number'])
                        sessionStorage.setItem('vehicle', JSON.stringify(response['vehicle']));

                        window.location.assign(redirectUrl);
                    }
                },
                error: function() {
                    invalidInputMessage('An error occurred.');
                }
            }) // End of AJAX
        } // End of allInputsAreValid check
        else
            invalidInputMessage('At least one input is empty.');
    }) // End of click Event Listener
}) // End of document.ready

// Checks if any inputs are empty
// False if an empty input is found
// True if all inputs have data
function areValidInputs(inputs) {
    allInputsAreValid = true;

    // Looping through all inputs
    index = 0;
    while(allInputsAreValid && index < inputs.length) {
        const element = inputs[index];
        const element_value = element.value.trim();

        // TODO: further validate inputs
        // if the value is empty, it's invalid
        if (element_value.length == 0)
            allInputsAreValid = false;

        index++;
    }
    return allInputsAreValid;
}