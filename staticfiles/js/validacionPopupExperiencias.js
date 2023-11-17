$(document).ready(function() {
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
        }
      },
      submitHandler: function(form) {
        Swal.fire({
          title: "¿Está seguro de guardar la experiencia laboral?",
          text: "No podrá revertir esta acción.",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Sí, guardar',
          cancelButtonText: 'Cancelar',
          timer: 0
        }).then((result) => {
          if (result.isConfirmed) {
            // Enviar formulario
            form.submit();
          }
        });
      }
    });
  });
  