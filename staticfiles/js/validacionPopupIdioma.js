$(document).ready(function () {
    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilIdioma");
        if (button) {
        button.disabled = false;
        button.value = "Guardar"; // Restablece el texto del botón
        }
    }
        // Esta función se llama cuando se hace clic en el botón de enviar
    function disableSubmitButton(button) {
        // Deshabilita el botón
        button.disabled = true;

        // Cambia el texto del botón para indicar que se está procesando
        button.value = "Enviando...";

        // Puedes mostrar un mensaje de espera aquí si lo deseas

        // Establece un temporizador para restablecer el botón después de un tiempo determinado
        setTimeout(resetSubmitButton, 5000); // 5000 milisegundos (5 segundos) como ejemplo
    }

    $('#formularioPerfilIdi').validate({
        rules: {
            fk_id_idioma: "required",
        },
        messages: {
            fk_id_idioma: {
                required: 'Por favor ingresa un idioma',
            }
        },
        submitHandler: function (form) {
            // Aquí puedes mostrar la confirmación con SweetAlert2
            Swal.fire({
                title: "Idioma agregado correctamente!",
                icon: "success",
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();

                    // Deshabilita el botón y muestra "Enviando..."
                    disableSubmitButton($("#enviarPerfilIdioma")[0]);

                }
            });
        },
    });
});