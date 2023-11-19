$(document).ready(function () {
    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilEduc");
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

    $('#formularioPerfilEduc').validate({
        rules: {
            'annio_inicio_educ': {
                required: true,
                minlength: 4,
                maxlength: 4,
            },
            'annio_fin_educ': {
                required: true,
                minlength: 4,
                maxlength: 4,
            },
            fk_id_institucion: "required",
            fk_id_formacion: "required",
            fk_id_titulo: "required"
        },
        messages: {
            'annio_inicio_educ': {
                required: 'Por favor ingrese el año en que inició sus estudios',
                minlength: 'El año debe tener al menos 4 caracteres',
                maxlength: 'El año no debe exceder los 4 caracteres',
            },
            'annio_fin_educ': {
                required: 'Por favor ingrese el año en que finalizó sus estudios',
                minlength: 'El año debe tener al menos 4 caracteres',
                maxlength: 'El año no debe exceder los 4 caracteres',
            },
            fk_id_institucion: "Porfavor ingrese una institución",
            fk_id_formacion: "Porfavor ingrese una formación",
            fk_id_titulo: "Porfavor ingrese un título"
        },
        submitHandler: function (form) {
            // Aquí puedes mostrar la confirmación con SweetAlert2
            Swal.fire({
                title: "¡Datos académicos agregados correctamente!",
                icon: "success",
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();

                    // Deshabilita el botón y muestra "Enviando..."
                    disableSubmitButton($("#enviarPerfilEduc")[0]);

                    // Añade un mensaje de depuración
                    console.log("El botón de enviar se ha activado correctamente");

                }
            });
        },
    });
});

    
    

