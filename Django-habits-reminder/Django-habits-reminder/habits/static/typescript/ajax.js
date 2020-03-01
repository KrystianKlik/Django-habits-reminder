"use strict";
$(function () {
    // -------------- Index page ----------------------
    $(".habit-checkbox").click(function () {
        var id = $(this).val();
        //console.log(id)
        $.ajax({
            method: "POST",
            url: "/habits/" + id + "/habitstatus",
        })
            .done(function () {
            alert("You have change habit id: " + id);
        });
    });
    //In case when there are all habits checked or all - 1
    $(".habit-checkbox").change(function () {
        if ($('.habit-checkbox:checked').length == $('.habit-checkbox').length || $('.habit-checkbox:checked').length == $('.habit-checkbox').length - 1) {
            console.log($('.habit-checkbox:checked').length);
            $.ajax({
                method: "POST",
                url: "/habits/allhabbitsarecompleted",
            })
                .done(function () {
                if ($('.habit-checkbox:checked').length == $('.habit-checkbox').length) {
                    alert("You did all habits, congratulations");
                }
            });
        }
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