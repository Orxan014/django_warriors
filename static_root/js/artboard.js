// Add active class to the current button (highlight it)
// var header = document.getElementById("profile-list");
// var btns = header.getElementsByClassName("list-inline-item");
// for (var i = 0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function () {
//         var current = document.getElementsByClassName("active");
//         current[0].className = current[0].className.replace(" active", "");
//         this.className += " active";
//     });
// }
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

