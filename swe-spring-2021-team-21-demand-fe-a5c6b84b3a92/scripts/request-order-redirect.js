$(document).ready(function() {
    const pluginCard = document.getElementsByClassName('pluginCard');

    $(pluginCard).click(function(event) {
        const plugin_id = event.currentTarget.id;
        const plugin_name = event.currentTarget.children[1].textContent;
        
        sessionStorage.setItem('plugin', plugin_id);
        sessionStorage.setItem('pluginName', plugin_name);
        window.location.assign(`https://${window.location.hostname}/demand-fe/request-service.html`);
    }) // End of click Event Listener
}) // End of document.ready