$(document).delegate(".navbar-toggler","click", function(){
    $(".navbar-collapse").fadeToggle();
});
console.log("a")

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

$(document).ready(function(){

    $(".selenium-test").click(function() {
        type = $(this).data("type");
        $.ajax({
            url: "http://localhost:5000/selenium-test",
            type: "POST",
            contentType: "application/json;charset=UTF-8",
            data: JSON.stringify({"type": type})
        }).done(function(data) {
            console.log(data)
            if(data){
                sessionStorage.setItem('youtube_logs', data);
                location.href = "/dashboard"
            }

        });
    })


    $(".send-read").click(function(){
        url = $("#url").val()
        $.ajax({
            contentType: "application/json",
            url: '/readability-test',
            type: 'POST',
            data: JSON.stringify({'url': url}),
            success: function (result) {
                 console.log(result)
                 //sessionStorage.setItem("readabality", JSON.stringify(result));
                 sessionStorage.setItem('readabality', result);
                 location.href = "/dashboard"
            },
            error: function (result) {
                alert("error!");
            }
        });   //end ajax
    })


});

