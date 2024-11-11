// Select necessary elements
const container = document.getElementById('container');
const loginToggle = document.getElementById('loginToggle');
const registerToggle = document.getElementById('registerToggle');

// Event listeners for toggling between forms
loginToggle.addEventListener('click', () => {
    container.classList.remove('sign-up-mode');
});

registerToggle.addEventListener('click', () => {
    container.classList.add('sign-up-mode');
});
