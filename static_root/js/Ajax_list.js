$('.join').each(function () {
	$(this).click(function (e) {

	

		e.preventDefault()
		
		let user = $(this).data("user")


		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		let id = $(this).data("id")

		// $(document).ajaxStop(function () {
		// 	window.location.reload();
		// });
		if (user.trim() != 'AnonymousUser'.trim()){
		if (($(this).val() == "Join")) {
			
			$(this).val("Joined")
			
			let str_count = $(this).data("count")
			let int_count = parseInt($(this).data("count"))
			int_count += 1
			str_count = $(this).data("count", int_count)

			$(this).attr('data-count', int_count)
			
			// $(this).parent().parent().parent().parent().siblings('span').eq(0).html(int_count)
			$(this).parent().parent().parent().parent().parent().siblings('div').eq(2).children().eq(2).html(int_count)
			console.log(int_count)
		}
		else if (($(this).val() == "Joined")) {
			$(this).val("Join")
			console.log('cixdi')
			 
			let str_count = $(this).data("count")
			let int_count = parseInt($(this).data("count"))
			int_count -= 1
			str_count = $(this).data("count", int_count)

			$(this).attr('data-count', int_count)
			$(this).parent().parent().parent().parent().parent().siblings('div').eq(2).children().eq(2).html(int_count)
			console.log(int_count)
		}
		let value = ($(this).val())

		$.ajax({
			url: "/ajaxify_join_form/",
			method: 'POST',
			data: {
				"csrfmiddlewaretoken": csrftoken,
				"user": user,
				'id': id,
		
				"value": value,


			},
			success: function (data) {
				// $(".count-join").html(count);
				// console.log(data)
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

 
