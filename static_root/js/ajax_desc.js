

$('.join12').on('click', function (e) {
	e.preventDefault()
 
})
$('.interest').each(function () {
	if (($(this).val()) == "interested") {
		
		$(this).find('img').attr("src",escape('/static/assets/images/yellow-christmas-star-png-18.png'))

	}
	$(this).click(function (e) {

		e.preventDefault()
		let id = $(this).data("id")
		let user = $(this).data("user")
		let count=$(this).data('count1')
		if (user.trim() != 'AnonymousUser'.trim()){ 
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
		if (($(this).val()) == "interest") {
			$(this).val("interested")
			let str_count = $(this).data("count1")
			let int_count = parseInt($(this).data("count1"))
			int_count += 1
			str_count = $(this).data("count1", int_count)

			$(this).attr('data-count1', int_count)

			$(this).parent().siblings('p').html(int_count)
            // console.log($(this).parent().siblings('p').html(int_count))
			$(this).find('img').attr("src",escape('/static/assets/images/yellow-christmas-star-png-18.png'))

		}
		else if (($(this).val()) == "interested") {
			$(this).val("interest")
			let str_count = $(this).data("count1")
			let int_count = parseInt($(this).data("count1"))
			int_count -= 1
			str_count = $(this).data("count1", int_count)

			$(this).attr('data-count1', int_count)
			$(this).parent().siblings('p').html(int_count)
			$(this).find('img').attr("src",escape('/static/assets/images/A_Black_Star.png'))

		}
		let value = ($(this).val())
		$.ajax({
			url: "/ajaxify_interest_form/",
			method: 'POST',
			data: {
				"csrfmiddlewaretoken": csrftoken,
				"user": user,
				'id': id,
				"value": value,
				
			}
		}).then(function (resp) {
			console.log(resp)
		})

	}
	else{
		window.location.href="/auth/signupface/";
		 
	}
	})


}
)

 
