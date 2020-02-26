"use strict";
$(function () {
    // -------------- Index page ----------------------
    $(".habit-checkbox").click(function () {
        var id = $(this).val();
        console.log(id);
        $.ajax({
            method: "POST",
            url: "/habits/" + id + "/habitstatus",
        })
            .done(function () {
            alert("You have change habit id: " + id);
        });
    });
    // -------------- end Index page -------------------
    $(".habit-implement").click(function () {
        var id = $(this).val();
        console.log(id);
        $.ajax({
            method: "POST",
            url: "/habits/" + id + "/implementstatus",
        })
            .done(function () {
            alert("You have implemented habit id: " + id);
        });
    });
});
//# sourceMappingURL=ajax.js.map