$(document).ready(function () {
  $("#formularioPerfilPers").validate({
    rules: {
      rut_usuario: {
        required: true,
        minlength: 8,
        maxlength: 9,
      },
      dv_usuario: {
        required: true,
        minlength: 1,
        maxlength: 1,
      },
      nombre: {
        required: true,
        minlength: 2,
        maxlength: 50,
      },
      segundo_nombre: {
        minlength: 2,
        maxlength: 50,
      },
      primer_apellido: {
        required: true,
        minlength: 2,
        maxlength: 50,
      },
      segundo_apellido: {
        minlength: 2,
        maxlength: 50,
      },
      fecha_nacimiento: {
        required: true,
        date: true,
      },
      nacionalidad: {
        required: true,
      },
      telefono: {
        required: true,
        minlength: 9,
        maxlength: 12,
      },
      correo: {
        required: true,
        email: true,
      },
    },
    messages: {
      rut_usuario: {
        required: "El RUT es obligatorio",
        minlength: "El RUT debe tener al menos 8 dígitos",
        maxlength: "El RUT no debe tener más de 9 dígitos",
      },
      dv_usuario: {
        required: "El DV es obligatorio",
        minlength: "El DV debe tener un solo carácter",
        maxlength: "El DV no debe tener más de un carácter",
      },
      nombre: {
        required: "El nombre es obligatorio",
        minlength: "El nombre debe tener al menos 2 caracteres",
        maxlength: "El nombre no debe tener más de 50 caracteres",
      },
      segundo_nombre: {
        minlength: "El segundo nombre debe tener al menos 2 caracteres",
        maxlength: "El segundo nombre no debe tener más de 50 caracteres",
      },
      primer_apellido: {
        required: "El primer apellido es obligatorio",
        minlength: "El primer apellido debe tener al menos 2 caracteres",
        maxlength: "El primer apellido no debe tener más de 50 caracteres",
      },
      segundo_apellido: {
        minlength: "El segundo apellido debe tener al menos 2 caracteres",
        maxlength: "El segundo apellido no debe tener más de 50 caracteres",
      },
      fecha_nacimiento: {
        required: "La fecha de nacimiento es obligatoria",
        date: "Ingrese un formato de fecha válido (YYYY-MM-DD)",
      },
      nacionalidad: {
        required: "La nacionalidad es obligatoria",
      },
      telefono: {
        required: "El teléfono es obligatorio",
        minlength: "El teléfono debe tener al menos 9 dígitos",
        maxlength: "El teléfono no debe tener más de 12 dígitos",
      },
      correo: {
        required: "El correo es obligatorio",
        email: "Ingrese un correo electrónico válido",
      },
    },
    submitHandler: function (form) {
      Swal.fire({
        title: "Datos Actualizados",
        text: "Sus datos personales han sido actualizados exitosamente",
        icon: "success",
        confirmButtonColor: "#3085d6",
        confirmButtonText: "Guardar",
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          form.submit();
        }
      });
    },
  });
});
