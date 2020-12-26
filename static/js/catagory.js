$(document).ready(function () {
    $("#main-card").mouseover(function () {
        $(".card-add").css("display", "block");
        $("#joined-text").html("Joined")
    });
});
$(document).ready(function () {
    $("#main-card").mouseleave(function () {
        $(".card-add").css("display", "none");
        $("#joined-text").html("member")
    });
});        

