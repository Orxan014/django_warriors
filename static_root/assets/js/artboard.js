// Add active class to the current button (highlight it)
var header = document.getElementById("profile-list");
var btns = header.getElementsByClassName("list-inline-item");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}

if(window.innerWidth < 800){
    document.querySelector('.afterImg').style.display = 'block';
    document.querySelector('.profile').style.display = 'none';
    document.querySelector('.collapseMe').style.display = 'none';
    document.querySelector('.afterBtn').style.display = 'block'
}
// $(document).ready(function () {
//     $("#main-card").mouseover(function () {
//         $(".card-add").css("display", "block");
//         $("#joined-text").html("Joined")
//     });
// });
$(document).ready(function () {
    // $("#main-card").mouseleave(function () {
    //     $(".card-add").css("display", "none");
    //     $("#joined-text").html("member")
    // });
    // $(".log-out-img").click(function () {
    //     $("button.log-out").css("display", "block");
    // });


    $(".post").mouseover(function () {
        // $(".card-add").css("display", "block");
        // $("#joined-text").html("Joined")
        $(this).closest("div").find('.card-add').css("display", "block")
        $(this).closest("div").find('.joined-text').html("joined")
        // $(this).closest("div").find(".joined-text").html("member")
    });


    $(".post").mouseleave(function () {
        // $(".card-add").css("display", "block");
        // $("#joined-text").html("Joined")
        $(this).closest("div").find('.card-add').css("display", "none")
        $(this).closest("div").find('.joined-text').html("member")
        // $(this).closest("div").find(".joined-text").html("member")
    });

    $(".joined-list").click(function () {
        $(".interested-posts").css("display", "none");
        $(".events-posts").css("display", "none");
        $(".joined-posts").css("display", "block");

    });

    $(".interested-list").click(function () {
        $(".joined-posts").css("display", "none");
        $(".events-posts").css("display", "none");
        $(".interested-posts").css("display", "block");
    });

    $(".events-list").click(function () {
        $(".joined-posts").css("display", "none");
        $(".interested-posts").css("display", "none");
        $(".events-posts").css("display", "block");
    });
    
});
