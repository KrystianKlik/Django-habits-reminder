﻿$(function () {

    // -------------- Index page ----------------------
    $(".habit-checkbox").click(function () {
        let id = $(this).val();
        console.log(id)
    $.ajax({
        method: "POST",
        url: "/habits/"+id+"/habitstatus",
    })
        .done(function () {
            alert("You have change habit id: " + id);
        });
    });
    // -------------- end Index page -------------------

});