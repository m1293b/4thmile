$(window).on("load", function() {
    const navLinks= $('.nav-links')
    const navMid= $('.nav-mid')

    if(window.innerWidth < 768){
    navLinks.addClass('display-none');
    navMid.addClass('display-none');
    }
    // $(".loader").fadeOut();
}),

// Hamburger menu script

$('#hamburger-menu').on('click', function() {
    this.classList.toggle('active');
    
    const navLinks= $('.nav-links')
    const navMid= $('.nav-mid')

    $('.fa-bars').is(':visible') ? $('.fa-bars').slideUp(100) : $('.fa-bars').slideDown(100);
    $('.fa-chevron-down').is(':visible') ? $('.fa-chevron-down').slideUp(100) : $('.fa-chevron-down').slideDown(100); 

    // 

    if(navLinks.hasClass('nav-links-down')) {
        navLinks.removeClass('nav-links-down').addClass('nav-links-up').removeClass('display-none');
        navMid.removeClass('nav-mid-down').addClass('nav-mid-up').removeClass('display-none');
    }
    else {
        navLinks.removeClass('nav-links-up').addClass('nav-links-down');
        navMid.removeClass('nav-mid-up').addClass('nav-mid-down');
    }
});

$(window).on('resize', function(){
    const win = $(this);
    const navLinks= $('.nav-links')
    const navMid= $('.nav-mid')

    if (win.width() >= 768) {
        navLinks.removeClass('nav-links-up').removeClass('nav-links-down').removeClass('display-none');
        navMid.removeClass('nav-mid-up').removeClass('nav-mid-down').removeClass('display-none');
    } // else if(win.width() < 768) { 
    //     navLinks.addClass('nav-links-up');
    //     navMid.addClass('nav-mid-up');
    // }
});