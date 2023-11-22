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

    function isValidDateInicio(fecha_inicio_exp) {
      var regEx = /^\d{4}-\d{2}-\d{2}$/;
      if (!fecha_inicio_exp.match(regEx)) return false;
      var fecha = new Date(fecha_inicio_exp);
      if (!fecha.getTime() && fecha.getTime() !== 0) return false;
      return fecha.toISOString().slice(0, 10) === fecha_inicio_exp;
    }

    function isValidDateFin(fecha_termino_exp) {
      var regEx = /^\d{4}-\d{2}-\d{2}$/;
      if (!fecha_termino_exp.match(regEx)) return false;
      var fecha = new Date(fecha_termino_exp);
      if (!fecha.getTime() && fecha.getTime() !== 0) return false;
      return fecha.toISOString().slice(0, 10) === fecha_termino_exp;
    }

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
          maxlength: 70
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
          maxlength: "La descripción no debe tener más de 70 caracteres"
        }
      },

      submitHandler: function(form) {

      // Validamos la fecha antes de enviarla
      var fechaInicio = $("#fecha_inicio_exp").val();
      var fechaFin = $("#fecha_termino_exp").val();
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
          title: "¿Está seguro de que desea editar sus datos laborales?",
          text: "Sus datos laborales están siendo modificados",
          icon: "warning",
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Sí, editar",
          showCancelButton: true,
          cancelButtonColor: "#d33",
          cancelButtonText: "Cancelar",
          allowOutsideClick: false,
        }).then((result) => {
          if (result.isConfirmed) {
            form.submit();
          } else {
            
          }
        });
      },
    });
  });
  