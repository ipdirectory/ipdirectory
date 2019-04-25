$(document).ready(function(){

	var deviceName;
	var selectedUnit = $('#select-unit').val();
	var ipsDiv = $('#ip-content');
	var ipContainer = $($.parseHTML('<div id="" class="line"><div class="ip inline"></div><div class="branch inline"></div><div class="userName inline"></div><div class="device inline"></div><div class="reserved inline"><div class="reserve"><i class="fas fa-pen"></i></div></div></div>'))
	var ipContainer_ip = ipContainer.find('.ip');
	var ipContainer_branch = ipContainer.find('.branch');
	var ipContainer_userName = ipContainer.find('.userName');
	var ipContainer_device = ipContainer.find('.device');
	var ipContainer_reserved = ipContainer.find('.reserved');
	var emptyIpContainer = ipContainer.html('');
	var unitFilterChanged = false;




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

	$('#select-reserved').change(function(){
		
		$('.line').removeClass('display-none');

		if($(this).val() == 'Free'){
			$('.reserved-True').addClass('display-none');
		}

		if($(this).val() == 'Reserved'){
			$('.reserved-False').addClass('display-none');
		}
		console.log('change');
	})

	$('#select-unit').change(function(){

		unitFilterChanged = true;

	})


	$('#search-button').click(function(){

		$('#select-reserved').val('sad');
		var req = new FormData();
		selectedUnit = $('#select-unit').val()
		req.append('csrfmiddlewaretoken',$("input[name='csrfmiddlewaretoken']").val());
		req.append('current_unit_name', selectedUnit);

		if (!unitFilterChanged){
			return;
		}

		$.ajax({

				type: "POST",
				data: req,
				contentType: false,
				processData: false,
				url:"/test/",
				success: function(data, branch = selectedUnit){
					ipsDiv.html('');
					for (var i = 0; i < data.length; i++) {
						createIpLine(data[i][0], data[i][1], selectedUnit, data[i][2], data[i][3], data[i][4]);
					}
					console.log(data[0]);
					
				}
			})

		unitFilterChanged = false;
	})

	function createIpLine(id, ipAdress, branch, userName, device, reserved ){

		var clonedIpContainer = emptyIpContainer.clone();
		clonedIpContainer.attr('id', id);

		if (reserved) {
			clonedIpContainer.attr('class', 'line reserved-True');
		}
		else {
			clonedIpContainer.attr('class', 'line reserved-False');
		}

		clonedIpContainer.append(ipContainer_ip.clone().text(ipAdress));
		clonedIpContainer.append(ipContainer_branch.clone().text(selectedUnit))
		clonedIpContainer.append(ipContainer_userName.clone().text(userName));
		clonedIpContainer.append(ipContainer_device.clone().text(device));
		clonedIpContainer.append(ipContainer_reserved.clone().text(reserved));

		ipsDiv.append(clonedIpContainer);

	}

	$('#test').dialog();

	console.log($('#select-unit').val());



})