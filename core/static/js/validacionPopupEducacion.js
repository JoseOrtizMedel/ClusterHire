$(document).ready(function () {
    // Agrega la validación del formulario usando jQuery Validate
    $("#formularioPerfilExp").validate({
        submitHandler: function (form) {
            // Aquí puedes mostrar un SweetAlert2 para confirmar el envío del formulario
            Swal.fire({
                title: '¿Guardar cambios?',
                text: '¿Estás seguro de que deseas guardar los cambios?',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Guardar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Envía el formulario si el usuario confirma
                    form.submit();
                }
            });
        }
    });
});
