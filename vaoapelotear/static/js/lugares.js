$(document).on('ready', function(){
    $.ajax({
        type: "POST",
        url: "../../damedepartamentos/",
        data: {'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        success: function(data) {
            for (var i = 0; i < data.length ; i++) {
                $('#cboDepartamentos').append("<option value='" + data[i].pk + "'>" + data[i].fields.nombre + "</option>");
            }
        }
    });
    $('#cboDepartamentos').change(function(){
    	$('#cboProvincias, #cboDistritos').empty();
        $('#cboProvincias').append("<option value=''>PROVINCIA</option>");
        $('#cboDistritos').append("<option value=''>DISTRITO</option>");
        $.ajax({
            type: 'POST',
            data: {'iddepartamento': $('#cboDepartamentos option:selected').val(), 
                   'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
            url: '../../dameprovincias/',
            success: function(data) {
                for (var i = 0; i < data.length ; i++) {
                    $('#cboProvincias').append("<option value='" + data[i].pk + "'>" + data[i].fields.nombre + "</option>");
                }
            }
        });
    });
    $('#cboProvincias').change(function(){
        $('#cboDistritos').empty();
        $('#cboDistritos').append("<option value=''>DISTRITO</option>");
        $.ajax({
            type: "POST",
            data: {'idprovincia': $('#cboProvincias option:selected').val(), 
                   'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
            url: '../../damedistritos/',
            success: function(data) {
                for (var i = 0; i < data.length ; i++) {
                    $('#cboDistritos').append("<option value='" + data[i].pk + "'>" + data[i].fields.nombre + "</option>");
                }
            }
        });
    });
});