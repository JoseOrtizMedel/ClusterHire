document.addEventListener('DOMContentLoaded', function () {
    var analizarBotones = document.querySelectorAll('.btn-success[data-num-postulantes]');

    analizarBotones.forEach(function (boton) {
        boton.addEventListener('click', function (event) {
            event.preventDefault();

            var numPostulantes = parseInt(boton.getAttribute('data-num-postulantes'));

            if (numPostulantes >= 3) {
                window.location.href = boton.href;
            } else {
                Swal.fire({
                    icon: 'error',
                    title: '¡No se puede analizar esta oferta!',
                    text: 'Para poder realizar el analisis, debe tener al menos 3 postulantes.',
                    showCloseButton: true // Mostrar el botón de cierre manual
                });
            }
        });
    });
});