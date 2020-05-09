$(document).ready(function(){
    line_array = []
    var line_array = sessionStorage.getItem('youtube_logs');

    if( line_array != null ){
        console.log(line_array)
        line_array = line_array.split("\n")
        $(".log-items").empty();
        $("#logs-section").fadeIn();

        Array.from(line_array).forEach(function(entry, i) {
            item = document.createElement("strong");
            item.className = "log-item";
            item.id = "log-" + i;
            item.innerHTML = "Log - " + (i = i + 1) + " - " + entry;
            $(".log-items").append(item)
        })
    }
})