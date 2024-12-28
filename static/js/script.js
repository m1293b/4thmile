// Hamburger menu script

document.getElementById('hamburger-menu').addEventListener('click', function() {
    this.classList.toggle('active');
    $('.fa-bars').is(':visible') ? $('.fa-bars').slideUp(100) : $('.fa-bars').slideDown(100);
    $('.fa-chevron-down').is(':visible') ? $('.fa-chevron-down').slideUp(100) : $('.fa-chevron-down').slideDown(100); 
    $('.nav-links').toggleClass('nav-links-down');
});