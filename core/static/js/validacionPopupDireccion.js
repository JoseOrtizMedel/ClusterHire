$(document).ready(function () {

    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilDire");
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
        setTimeout(resetSubmitButton, 30000); // 30000 milisegundos (5 segundos) como ejemplo
    }

    // Configuración de la validación del formulario con jQuery Validate
    $("#formularioPerfilDire").validate({
        rules: {
            numeracion: "required",
            nombre_calle: "required",
            // Agrega reglas de validación para otros campos si es necesario
        },
        messages: {
            numeracion: "Por favor, ingresa la numeración",
            nombre_calle: "Por favor, ingresa el nombre de la calle",
            // Agrega mensajes de validación para otros campos si es necesario
        },
        errorElement: "span",
        errorPlacement: function (error, element) {
            error.addClass("invalid-feedback");
            element.closest(".form-group").append(error);
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass("is-invalid");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).removeClass("is-invalid");
        },
        submitHandler: function (form) {
            // Aquí puedes mostrar la confirmación con SweetAlert2
            Swal.fire({
                title: "¡Dirección agregada correctamente!",
                icon: "success",
                showCancelButton: false,
                confirmButtonColor: "#3085d6",
                confirmButtonText: "Continuar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();

                    // Deshabilita el botón y muestra "Enviando..."
                    disableSubmitButton($("#enviarPerfilDire")[0]);

                }
            });
        },
    });
});
