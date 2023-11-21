$(document).ready(function () {
  $.validator.addMethod(
    "greaterThan",
    function (value, element, param) {
      var target = $(param).val();
      if (value && target) {
        return parseInt(value) > parseInt(target);
      }
      return true;
    },
    "El año de término debe ser mayor que el año de inicio."
  );

function isValidDateInicio(annio_inicio_educ) {
  // La regex solo coincide con los cuatro números asociados al año
  var regex = /^[0-9]{4}$/;
  // Si la cadena no coincide con la regex, el año es inválido
  if (!regex.test(annio_inicio_educ)) return false;
  // Si el año es válido, se devuelve true
  return annio_inicio_educ.length === 4;
}

function isValidDateFin(annio_fin_educ) {
    // La regex solo coincide con los cuatro números asociados al año
    var regex = /^[0-9]{4}$/;
    // Si la cadena no coincide con la regex, el año es inválido
    if (!regex.test(annio_fin_educ)) return false;
    // Si el año es válido, se devuelve true
    return annio_fin_educ.length === 4;
}

  
  $("#formularioPerfilEduc").validate({
    rules: {
      annio_inicio_educ: {
        required: true,
        minlength: 4,
        maxlength: 4,
        number: true,
      },
      annio_fin_educ: {
        required: true,
        minlength: 4,
        maxlength: 4,
        number: true,
        greaterThan: "#annio_inicio_educ"
      },
      fk_id_institucion: {
        required: true,
      },
      fk_id_formacion: {
        required: true,
      },
      fk_id_titulo: {
        required: true,
      },
    },
    messages: {
      annio_inicio_educ: {
        required: "Ingrese el año de inicio de la formación.",
        minlength: "El año de inicio debe tener 4 caracteres.",
        maxlength: "El año de inicio debe tener 4 caracteres.",
        number: "El año de inicio debe ser un número.",
      },
      annio_fin_educ: {
        required: "Ingrese el año de término de la formación.",
        minlength: "El año de término debe tener 4 caracteres.",
        maxlength: "El año de término debe tener 4 caracteres.",
        number: "El año de término debe ser un número.",
        greaterThan: "El año de término debe ser mayor que el año de inicio.",
      },
      fk_id_institucion: {
        required: "Seleccione una casa de estudios.",
      },
      fk_id_formacion: {
        required: "Seleccione una formación.",
      },
      fk_id_titulo: {
        required: "Seleccione un título.",
      },
    },
    submitHandler: function (form) {

      // Validamos la fecha antes de enviarla
      var fechaInicio = $("#annio_inicio_educ").val();
      var fechaFin = $("#annio_fin_educ").val();
      if (!isValidDateInicio(fechaInicio)) {
        // La fecha no es válida, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en la fecha de inicio',
          text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.',
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Entendido",
        });

        return false; // Evita que se envíe el formulario

      }

      if (!isValidDateFin(fechaFin)) {
        // La fecha no es válida, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en la fecha de término',
          text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.',
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Entendido",
        });

        return false; // Evita que se envíe el formulario

      }

      Swal.fire({
/*         title: "¿Está seguro de que desea editar su perfil educativo?",
        text: "Una vez que se edite su perfil, los cambios no se podrán revertir.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, editar",
        cancelButtonText: "Cancelar", */
        title: "Datos Actualizados",
        text: "Sus datos académicos han sido actualizados exitosamente",
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
