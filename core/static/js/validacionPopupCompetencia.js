$(document).ready(function () {
    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilCompe");
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

        // Establece un temporizador para restablecer el botón después de un tiempo determinado
        setTimeout(resetSubmitButton, 30000); // 30000 milisegundos (30 segundos) como ejemplo
    }

    $('#formularioPerfilCompe').validate({
        rules: {
            fk_id_competencia: "required",
            nivel: "required"
        },
        messages: {
            fk_id_competencia: {
                required: 'Por favor ingresa una competencia.',
            },
            nivel: {
                required: 'Por favor elija seleccione su nivel.',
            }
        },
        errorPlacement: function (error, element) {
            if (element.attr("name") == "nivel") {
                error.insertAfter(element.closest('.row'));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass('is-invalid');
            $(".form-check-inline").addClass('is-invalid');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).removeClass('is-invalid');
            $(".form-check-inline").removeClass('is-invalid');
        },
        submitHandler: function (form) {
            // Aquí puedes mostrar la confirmación con SweetAlert2
            Swal.fire({
                title: "¡Competencia agregada correctamente!",
                icon: "success",
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();
                    // Deshabilita el botón y muestra "Enviando..."
                    disableSubmitButton($("#enviarPerfilCompe")[0]);
                }
            });
        },
    });
});
