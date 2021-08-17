$(document).ready(function() {
    // Allows us to show recently ordered information
    const redirectUrl = `https://${window.location.hostname}/demand-fe/`;

    // If no order exists, redirect to the customer dashboard
    //     We currently check if an order exists by checking if
    //     a vehicle was chosen with a successful recorded order
    // TODO: this same check but with an order number
    if (sessionStorage.getItem('orderNumber') == null)
        window.location.assign(redirectUrl);
    
    orderNumber = sessionStorage.getItem('orderNumber');
    showOrderNumber(orderNumber);
    vehicle = JSON.parse(sessionStorage.getItem('vehicle'));
    showVehicleInformation(vehicle);

    sessionStorage.clear();

    // Shows order number
    function showOrderNumber(orderNumber) {
        const p_orderNumber = document.getElementById('orderNumber');
        p_orderNumber.textContent = `Your order number: ${orderNumber}`;
    }

    // Shows vehicle information
    // TODO: split by '_' and capitalize string
    function showVehicleInformation(vehicle) {
        const div_vehicleInfo = document.getElementById('vehicleInfo');
        
        // Loop to create and append p tags for each vehicle variable
        for (const type in vehicle) {
            const p_tag = document.createElement('p');
            const valueOfType = vehicle[type];
            p_tag.textContent = `${type}: ${valueOfType}`;
            div_vehicleInfo.append(p_tag);
        }
    }
})