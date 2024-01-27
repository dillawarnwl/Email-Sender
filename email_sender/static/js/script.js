document.addEventListener("DOMContentLoaded", function () {
    const navItems = document.querySelector('.nav-item');
    const hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', function () {
        navItems.classList.toggle('active');
    });
});