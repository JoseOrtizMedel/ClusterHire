$(document).ready(function() {
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

    $("#formularioPerfilExp").validate({
      rules: {
        nombre_empleo: {
          required: true,
          minlength: 5,
          maxlength: 50
        },
        fecha_inicio_exp: {
          required: true,
          dateISO: true
        },
        fecha_termino_exp: {
          required: true,
          dateISO: true,
          greaterThan: "#fecha_inicio_exp"
        },
        descripcion: {
          required: true,
          minlength: 20,
          maxlength: 255
        },
        fk_id_comuna: {
          required: true
        },
        fk_id_tipo_empleo: {
          required: true
        }
      },
      messages: {
        nombre_empleo: {
          required: "El nombre del empleo es obligatorio",
          minlength: "El nombre del empleo debe tener al menos 5 caracteres",
          maxlength: "El nombre del empleo no debe tener más de 50 caracteres"
        },
        fecha_inicio_exp: {
          required: "La fecha de inicio de la experiencia laboral es obligatoria",
          dateISO: "Ingrese una fecha válida (YYYY-MM-DD)"
        },
        fecha_termino_exp: {
          required: "La fecha de término de la experiencia laboral es obligatoria",
          dateISO: "Ingrese una fecha válida (YYYY-MM-DD)",
          greaterThan: "La fecha de término debe ser posterior a la fecha de inicio"
        },
        descripcion: {
          required: "La descripción de la experiencia laboral es obligatoria",
          minlength: "La descripción debe tener al menos 20 caracteres",
          maxlength: "La descripción no debe tener más de 255 caracteres"
        },
        fk_id_comuna: {
          required: "Seleccione una comuna."
        },
        fk_id_tipo_empleo: {
          required: "Seleccione un tipo de empleo."
        }
      },
      submitHandler: function(form) {
        Swal.fire({
          title: "Datos Actualizados",
          text: "Sus datos laborales han sido actualizados exitosamente",
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
  