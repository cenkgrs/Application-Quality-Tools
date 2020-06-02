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
                open_dashboard()
            }

        });
    })


    $(".send-read").click(function(){
        url = $("#url").val()

        send_ajax(url, "readability")
    })

    $(".form-send").click(function(){

        test_type = $('select[name=select-type] option').filter(':selected').val()
        url = $("#form_url").val()

        send_ajax(url, test_type)

        console.log(test_type)
    })


});

function send_ajax(url, test_type){
     $.ajax({
            contentType: "application/json",
            url: '/'+ test_type +'-test',
            type: 'POST',
            data: JSON.stringify({'url': url}),
            success: function (result) {
                 console.log(result)
                 //sessionStorage.setItem("readability", JSON.stringify(result));

                 if (test_type == "performance"){
                    fill_performance_result(result)
                 }else{
                    sessionStorage.setItem("readability", result);
                 }
                 open_dashboard()
            },
            error: function (result) {
                alert("error!");
            }
        });   //end ajax
}

function fill_performance_result(result){
    open_dashboard()
    console.log(result)
}