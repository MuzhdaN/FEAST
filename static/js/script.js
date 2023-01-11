    // Navbar will change its color after scrolling
    const navScroll = document.querySelector('.navbar');

    window.addEventListener('scroll', () => {
      if (window.scrollY >= 370) {
        navScroll.classList.add('nav-scrolled');
      }
      else if (window.scrollY <= 370) {
        navScroll.classList.remove('nav-scrolled')
      }
    });

    // Message timeout 
    setTimeout(function () {
            let messages = document.getElementById('msg');
            let alert = new bootstrap.Alert(messages);
            alert.close();
        }, 2500);


    /* -- following code has been taken from stackoverflow and altered --
    with following function, after clicking a navbar item(section) 
    and closing the offcanvas, it will position at that section */

    document.addEventListener("DOMContentLoaded", function(){
    var myOffcanvas = document.getElementById('offcanvasNavbar');
    var bsOffcanvas = new bootstrap.Offcanvas(myOffcanvas);
    document.getElementById("OpenMenu").addEventListener('click',function (e){
      e.preventDefault();
      e.stopPropagation();
      bsOffcanvas.toggle();
    });
    });