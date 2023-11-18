$(document).ready(function () {
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
                confirmButtonText: "Aceptar",
            }).then((result) => {
                if (result.isConfirmed) {
                    // Aquí puedes enviar el formulario si es necesario
                    form.submit();
                }
            });
        },
    });
});
