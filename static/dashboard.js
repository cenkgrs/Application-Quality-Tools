$(document).ready(function(){

readability_texts = [
    "Flesch Kincaid Reading Ease",
    "Gunning Fog Score",
    "SMOG Index",
    "Coleman Liau Index",
    "Automated Readability Index",
    "No. of sentences",
    "No. of words",
    "No. of complex words",
    "Percent of complex words",
    "Average words  per sentence",
    "Average syllables per word",
]
console.log(sessionStorage)

readability_metrics = [ "", "80", "6", "4", "6", "15", "2", ]

    readability = []
    var readability = sessionStorage.getItem('readability');
    console.log(readability)

    performance = []
    var performance = sessionStorage.getItem('performance');
    console.log(performance)
    console.log(performance[1])
    console.log(performance[2])
    console.log(performance[3])

    if (performance.hasOwnProperty("FCI")){
        console.log(performance.FCI)
    }


    // Showing Logs
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

    // Showing Readability Scores
    if ( readability != null) {
        readability = readability.split(",")

        console.log(readability)

        $(".readability-items").empty()
        $("#readability-section").fadeIn()

        Array.from(readability).forEach(function(entry, i) {
            if(i == 0){
                item = document.createElement("strong");
                item.className = "readability-score"
                item.innerHTML = entry
                $(".readability-items").append(item)
                $(".readability-items").append("<br> <br>")
                $(".readability-items").append("<h2> READABILITY INDICES </h2> ")
                return false
            }
            if(i > 10){
                return false;
            }
            if(i == 7){
                $(".readability-items").append("<h2> TEXT STATISTICS </h2> ")
            }


            item = document.createElement("strong");
            item.className = "readability-item";
            item.id = "readability-" + i;
            if(i < 7){
                item.innerHTML = readability_texts[i]  + " - " + entry + " / " + readability_metrics[i];
            }
            else{
                item.innerHTML = readability_texts[i]  + " - " + entry ;
            }
            $(".readability-items").append(item)
            $(".readability-items").append("<br/>")
        })
    }
})