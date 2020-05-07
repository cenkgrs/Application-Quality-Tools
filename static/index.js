$(document).delegate(".navbar-toggler","click", function(){
    $(".navbar-collapse").fadeToggle();
});


function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
