$(document).ready(function () {
    // Agrega un controlador de eventos para el botón de eliminar
    $('.eliminar-btn').click(function (event) {
        event.preventDefault();  // Evita la solicitud GET por defecto
        var botonEliminar = $(this);  // Guarda una referencia al botón que se hizo clic
        if (confirm("¿Estás seguro de que deseas eliminar esta oferta?")) {
            var ofertaId = botonEliminar.data('oferta-id');
            console.log('ID de oferta:', ofertaId);  // Agrega este console.log para verificar el ID
            // Realiza una solicitud AJAX para eliminar la oferta
            $.ajax({
                type: 'POST', // Usamos el método POST
                url: '/eliminar_oferta/' + ofertaId + '/',  // La URL para la vista que maneja la eliminación
                data: {
                    oferta_id: ofertaId
                },
                success: function (data) {
                    // Maneja la respuesta exitosa si es necesario
                    if (data.success) {
                        // Elimina la fila de la tabla
                        botonEliminar.closest('tr').remove();
                        // Recarga la página después de eliminar
                        location.reload();
                    } else {
                        alert('No se pudo eliminar la oferta.');
                    }
                },
                error: function (xhr, status, error) {
                    // Maneja los errores si es necesario
                    alert('Se produjo un error al intentar eliminar la oferta.');
                }
            });
        }
    });
});
