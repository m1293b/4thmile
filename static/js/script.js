window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');
    navbar.classList.toggle('navbar-sticky', window.scrollY > 0);
});

// Hamburger menu script

document.getElementById('hamburger-menu').addEventListener('click', function() {
    this.classList.toggle('active');
    $('.fa-bars').is(':visible') ? $('.fa-bars').slideUp(100) : $('.fa-bars').slideDown(100);
    $('.fa-chevron-down').is(':visible') ? $('.fa-chevron-down').slideUp(100) : $('.fa-chevron-down').slideDown(100); 
    if (this.classList.contains('active')) {
        document.querySelector('.nav-links').style.display = 'block';
    } else {
        document.querySelector('.nav-links').style.display = 'none';
    }
});