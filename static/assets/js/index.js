(function ($) {
  "use strict";

  // manual carousel controls
  $('.next').click(function () { $('.carousel').carousel('next'); return false; });
  $('.prev').click(function () { $('.carousel').carousel('prev'); return false; });

})(jQuery);
$('#bs4-multi-slide-carousel').carousel({
  interval: 1500
})

// $("#main-card").animate({left: '250px'}, 6000);

// $(document).ready(function(){
//     $("#main-card").mouseover(function(){
//       $(".card-add").toggle();
//     });
//   });

$(document).ready(function () {
  $('.explore-events').click(function(){
    $('html, body').animate({
        scrollTop: $('.page-wrapper').offset().top
    }, 1000);
}); 
  $('.post-wrapper').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 2000,
    nextArrow: $('.next'),
    prevArrow: $('.prev'),
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });
})
$(document).ready(function () {
  $(".post").mouseover(function () {
    // $(".card-add").css("display", "block");
    // $("#joined-text").html("Joined")
    $(this).closest("div").find('.card-add').css("display", "table")

    $(this).closest("div").find('.card-add').css("transition", "display, 1s")


    $(this).closest("div").find('.joined-text').html("joined")
    $(this).closest("div").find(".joined-text").html("member")
  });
});
$(document).ready(function () {
  var count= 0;
  $(".post").mouseleave(function () {
    // $(".card-add").css("display", "block");
    // $("#joined-text").html("Joined")
    $(this).closest("div").find('.card-add').css("display", "none")
    $(this).closest("div").find('.joined-text').html("member")
    $(this).closest("div").find(".joined-text").html("member")
  });
  $('.join').click(function(){
    count++;
    $('.joint-count').html(count)
  })
});
