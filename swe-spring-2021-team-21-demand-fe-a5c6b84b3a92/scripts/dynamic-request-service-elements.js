// Setting title of tab and form
const h2_formTitle = document.getElementById('formTitle');

const pluginName = sessionStorage.getItem('pluginName');
const str_request = `Request ${pluginName}`;

document.title = `${str_request} - WeGo`;
h2_formTitle.textContent = str_request;