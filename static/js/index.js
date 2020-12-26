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
  $('.post-wrapper').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: true,
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
    $(".card-add").css("display", "block");
    $("#joined-text").html("Joined")
  });
});
$(document).ready(function () {
  $(".post").mouseleave(function () {
    $(".card-add").css("display", "none");
    $("#joined-text").html("member")
  });
});

