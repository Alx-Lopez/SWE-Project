// Error Message upon invalid form entries or server error
function invalidInputMessage (invalidProperty) {
    const invalidMessage = document.getElementById('errorMessage');
    invalidMessage.textContent = invalidProperty + " Please try again.";    
    invalidMessage.style.visibility = 'visible';
}