window.addEventListener('load', function() {
    let base_url = 'http://localhost:8000/';
    $('.btnOper').on('click', function() {
        var operation = $(this).data('oper');
        $.ajax({
            headers: {'X-CSRFToken': document.getElementById('csrf').querySelector('input').value},
            url: base_url+operation+"/",
            type: 'POST',
            data: JSON.stringify({
                'A': $('#first').val(),
                'B': $('#second').val(),
            }),
        }) .done(
            function(data) {
                $('#response').text(data['response']).css("background-color", "#00CC00");
            }
        ).fail( function () {
        $('#operErrors').text("Only Numbers please").css("background-color", "#FF0000");
            },
        )
    });
})
