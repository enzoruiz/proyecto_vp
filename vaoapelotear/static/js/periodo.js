$(document).on('ready', function(){
	$("#frmPeriodos").validate({
	    rules: {
	        cboLocal: {                
	            required: true 
	        },
	        cboCancha: {
	            required: true
	        }        
	    },
	    submitHandler: function(form){
	      	if(validarHoras()){
				form.submit();
	      	}
		    else{
		    	alert('Seleccione un rango de horas correcto porfavor.');
		    }
	    }
	}); 
});

function dameCanchas(){
	$('#cboCancha').empty();
	$('#cboCancha').append("<option value=''>Cancha</option>");
	$.ajax({
        type: "POST",
        data: {'idlocal': $('#cboLocal option:selected').val(), 
                   'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        url: '../../../damecanchas/',
        success: function(data) {
            for (var i = 0; i < data.length ; i++) {
        		$('#cboCancha').append("<option value='" + data[i].pk + "'>" + data[i].fields.descripcion + "</option>");
        	}
        }
    });
}

function validarHoras(){
	var res = true;
	var valInicio = parseInt($('#cboHoraInicio').val());
	var valFin = parseInt($('#cboHoraFin').val());

	if (valFin <= valInicio) {
		res = false;
	}

	return res;
}