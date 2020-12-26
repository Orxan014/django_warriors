$('.join').each(function () {
	$(this).click(function (e) {



		e.preventDefault()

		let user = $(this).data("user")
		// console.log('user=',user)

		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

		let id = $(this).data("id")

		// $(document).ajaxStop(function () {
		// 	window.location.reload();
		// });
		if (user != 'undefined') {


			if (($(this).val() == "Join")) {

				$(this).val("Joined")
				// if ($('.interest').val() == 'intersed') {
				// 	alert('clicked')
				// 	$('.interest').trigger("click")
				// }
				let str_count = $(this).data("count")
				let int_count = parseInt($(this).data("count"))
				int_count += 1
				str_count = $(this).data("count", int_count)
				console.log('salam')
				$(this).attr('data-count', int_count)
				console.log(int_count)
				console.log('salam')
				console.log($(this).parent())
				// $(this).parent().parent().parent().parent().siblings('span').eq(0).html(int_count)
				

			}
			else if (($(this).val() == "Joined")) {
				$(this).val("Join")
				console.log('cixdi')

				let str_count = $(this).data("count")
				let int_count = parseInt($(this).data("count"))
				int_count -= 1
				str_count = $(this).data("count", int_count)

				$(this).attr('data-count', int_count)
				// $(this).parent().parent().parent().parent().siblings('span').eq(0).html(int_count)
				console.log($(this).parent())

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


				},

			}).then(function (resp) {
				// console.log(resp)
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
		// console.log('user=',user)
	
		console.log(id)
		let count = $(this).data('count1')
	
		var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
		 
		if (user !== 'undefined') {
		 
			if (($(this).val()) == "interest") {
				$(this).val("interested")
				let str_count = $(this).data("count1")
				let int_count = parseInt($(this).data("count1"))
				int_count += 1
				str_count = $(this).data("count1", int_count)

				$(this).attr('data-count1', int_count)

				$(this).parent().siblings('p').html(int_count)
				console.log($(this).find('img'))
				//yellow-christmas-star-png-18.png
				let a= "aa "
				console.log($(this).find('img').attr("src"))
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
				console.log($(this).find('img'))
				let a= "jh "
				console.log($(this).find('img').attr("src"))
				$(this).find('img').attr("src",escape('/static/assets/images/A_Black_Star.png'))

				// $(this).attr("src", "images/card-front.jpg");

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
				// , error: function () {
				// 	console.log('error salam');
				// }
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


