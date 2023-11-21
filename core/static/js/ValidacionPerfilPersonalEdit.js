$(document).ready(function () {

  function isValidDV(dv_usuario) {
    if (dv_usuario.length !== 1) {
      return false;
    }
    const regex = /^[0-9kK]{1}$/;
    return regex.test(dv_usuario);
  }
    // Función para verificar si una fecha es válida
    function isValidDate(fecha_nacimiento) {
      var regEx = /^\d{4}-\d{2}-\d{2}$/;
      if (!fecha_nacimiento.match(regEx)) return false;
      var fecha = new Date(fecha_nacimiento);
      if (!fecha.getTime() && d.getTime() !== 0) return false;
      return fecha.toISOString().slice(0, 10) === fecha_nacimiento;
    }

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
        minlength: 8,
        maxlength: 8,
      },
      correo: {
        required: true,
        email: true,
      },
    },
    messages: {
      rut_usuario: {
        required: "El rut es obligatorio",
        minlength: "El RUT debe tener al menos 8 dígitos",
        maxlength: "El RUT no debe tener más de 8 dígitos",
      },
      dv_usuario: {
        required: "El dv es obligatorio",
        minlength: "El DV debe tener un solo carácter",
        maxlength: "El DV no debe tener más de un carácter",
      },
      nombre: {
        required: "El primer nombre es obligatorio",
        minlength: "El nombre debe tener al menos 2 caracteres",
        maxlength: "El nombre no debe tener más de 50 caracteres",
      },
      segundo_nombre: {
        required: "El segundo nombre es obligatorio",
        minlength: "El segundo nombre debe tener al menos 2 caracteres",
        maxlength: "El segundo nombre no debe tener más de 50 caracteres",
      },
      primer_apellido: {
        required: "El primer apellido es obligatorio",
        minlength: "El primer apellido debe tener al menos 2 caracteres",
        maxlength: "El primer apellido no debe tener más de 50 caracteres",
      },
      segundo_apellido: {
        required: "El segundo apellido es obligatorio",
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
        minlength: "El teléfono debe tener al menos 8 dígitos",
        maxlength: "El teléfono no debe tener más de 8 dígitos",
      },
      correo: {
        required: "El correo es obligatorio",
        email: "Ingrese un correo electrónico válido",
      },
    },
    submitHandler: function (form) {

      // Validamos la fecha antes de enviarla
      var fecha = $("#fecha_nacimiento").val();
      var dv = $("#dv_usuario").val();
      if (!isValidDate(fecha)) {
        // La fecha no es válida, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en la fecha',
          text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.',
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Entendido",
        });

        return false; // Evita que se envíe el formulario

      }

      if (!isValidDV(dv)) {
        // El dv no es válido, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en el DV',
          text: 'Ingresa un DV válido (números entre 1-9 o letra k).',
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Entendido",
        });

        return false; // Evita que se envíe el formulario

        }

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
