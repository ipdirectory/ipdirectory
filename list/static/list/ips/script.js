$(document).ready(function(){

	var deviceName;

	$('.reserve').click(function(){
		deviceName = prompt('Device name');
		var req = new FormData();
		req.append('csrfmiddlewaretoken',$("input[name='csrfmiddlewaretoken']").val());
		$.ajax({

			type: "POST",
			data: req,
			contentType: false,
			processData: false,
			url:"/edit/ip/",
			success: function(data){

				console.log("1");
			}
		})

	})


})