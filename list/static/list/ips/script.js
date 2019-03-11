$(document).ready(function(){

	var deviceName;

	$('.reserve').click(function(eventObj){


		ipId = $(this).parent().parent().attr('id');
		deviceName = prompt('device name');

		if(deviceName) {

			var req = new FormData();

			req.append('csrfmiddlewaretoken',$("input[name='csrfmiddlewaretoken']").val());
			req.append('ipId', ipId);
			req.append('deviceName', deviceName);

			$.ajax({

				type: "POST",
				data: req,
				contentType: false,
				processData: false,
				url:"/edit/ip/",
				success: function(data){

					console.log("1");
					location.reload(true);
				}
			})

		}

		
	})

	$('.free').click(function(eventObj){


		ipId = $(this).parent().parent().attr('id');
		freeIp = confirm('free up this ip?');

		if(freeIp) {

			var req = new FormData();

			req.append('csrfmiddlewaretoken',$("input[name='csrfmiddlewaretoken']").val());
			req.append('ipId', ipId);
			
			$.ajax({

				type: "POST",
				data: req,
				contentType: false,
				processData: false,
				url:"/edit/free/",
				success: function(data){

					console.log("1");
					location.reload();
				}
			})

		}

		
	})	


})