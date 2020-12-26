$(document).ready(function () {

    $('.explore-events').click(function () {
        $('html, body').animate({
            scrollTop: $('.page-wrapper').offset().top
        }, 2000);

    });


    // card add div 

    $(".post").mouseover(function () {
        $(this).closest("div").find('.card-add').css("display", "block")
        // $(this).closest("div").find('.joined-text').html("joined")

    });


    $(".post").mouseleave(function () {
        $(this).closest("div").find('.card-add').css("display", "none")
        // $(this).closest("div").find('.joined-text').html("member")

    });


   
});

