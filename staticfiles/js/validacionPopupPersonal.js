$(document).ready(function () {

    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilPers");
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

    $('#formularioPerfilPers').validate({
        rules: {
            'rut_usuario': {
                required: true,
                minlength: 7,
                maxlength: 12,
            },
            'dv_usuario': {
                required: true,
                minlength: 1,
                maxlength: 1,
            },
            'nombre': 'required',
            'primer_apellido': 'required',
            'fecha_nacimiento': 'required',
            'nacionalidad': 'required',
            'telefono': {
                required: true,
                minlength: 9,
                maxlength: 15,
            },
            'correo': {
                required: true,
                email: true,
            },
        },
        messages: {
            'rut_usuario': {
                required: 'Por favor, ingresa tu Rut',
                minlength: 'El Rut debe tener al menos 7 caracteres',
                maxlength: 'El Rut no debe exceder los 12 caracteres',
            },
            'dv_usuario': {
                required: 'Por favor, ingresa tu DV',
                minlength: 'El DV debe tener al menos 1 caracter',
                maxlength: 'El DV no debe exceder los 1 caracteres',
            },
            'nombre': 'Por favor, ingresa tu primer nombre',
            'primer_apellido': 'Por favor, ingresa tu primer apellido',
            'fecha_nacimiento': 'Por favor, ingresa tu fecha de nacimiento',
            'fecha_nacimiento': 'Ingresa una fecha válida en el formato YYYY-MM-DD',
            'nacionalidad': 'Por favor, ingresa tu nacionalidad',
            'telefono': {
                required: 'Por favor, ingresa tu número de teléfono',
                minlength: 'El número de teléfono debe tener al menos 10 dígitos',
                maxlength: 'El número de teléfono no debe exceder los 15 dígitos',
            },
            'correo': {
                required: 'Por favor, ingresa tu correo electrónico',
                email: 'Por favor, ingresa una dirección de correo electrónico válida',
            },
        },
        submitHandler: function (form) {
            // Aquí puedes mostrar la confirmación con SweetAlert2
            Swal.fire({
                title: "¡Datos personales agregados correctamente!",
                icon: "success",
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();

                    // Deshabilita el botón y muestra "Enviando..."
                    disableSubmitButton($("#enviarPerfilPers")[0]);

                }
            });
        },
    });
});
