$(document).ready(function () {
    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarResetPassword");
        if (button) {
        button.disabled = false;
        button.value = "Enviar"; // Restablece el texto del botón
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
        setTimeout(resetSubmitButton, 30000); // 30000 milisegundos (5 segundos) como ejemplo
    }

    $('#formularioResetPass').validate({
        rules: {
            id_new_password1: {
                required: true,
                minlength: 8,
                maxlength: 8,
                },
                id_new_password2: {
                required: true,
                minlength: 8,
                maxlength: 8,
                },
            },
        messages: {
            id_new_password1: {
                    required: 'Por favor ingrese su email',
                    minlength: "La contraseña debe tener al menos 8 dígitos",
                    maxlength: "La contraseña no debe tener más de 8 dígitos",
                },
                id_new_password2: {
                    required: 'Por favor ingrese su email',
                    minlength: "La contraseña debe tener al menos 8 dígitos",
                    maxlength: "La contraseña no debe tener más de 8 dígitos",
                },

            },
        
        submitHandler: function (form) {
            Swal.fire({
                title: 'Datos personales guardados con éxito',
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            })
                form.submit();
    
                // Deshabilita el botón y muestra "Enviando..."
                disableSubmitButton($("#enviarResetPassword")[0]);

        },
    });
});
