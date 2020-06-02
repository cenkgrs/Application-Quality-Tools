$(document).ready(function(){

    $('#dashboard-link').on('click', function() {
        open_dashboard()
    });

    $('#index-link').on('click', function() {
        open_index()
    });

    $('#readability-link').on('click', function() {
        open_readability()
    });

    $('#selenium-link').on('click', function() {
        open_selenium()
    });

    $('#performance-link').on('click', function() {
        open_performance()
    });


})
const open_dashboard = function(){
    alert("dashboard")
    sections = $(".section")
    sections.not( $("#dashboard-section") ).css({"display": "none"})
    $("#dashboard-section").fadeIn()
    fill_logs()
    fill_readability()
}
const open_index = function(){
    sections = $(".section")
    sections.not( $("#index-section") ).css({"display": "none"})
    $("#index-section").fadeIn()
}
const open_readability = function(){
    sections = $(".section")
    sections.not( $("#readability-section") ).css({"display": "none"})
    $("#readability-section").fadeIn()
}
const open_selenium = function(){
    sections = $(".section")
    sections.not( $("#selenium-section") ).css({"display": "none"})
    $("#selenium-section").fadeIn()
}
const open_performance = function(){
    sections = $(".section")
    sections.not( $("#performance-section") ).css({"display": "none"})
    $("#performance-section").fadeIn()
}

