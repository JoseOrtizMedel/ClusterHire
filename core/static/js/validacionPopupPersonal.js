$(document).ready(function () {
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
