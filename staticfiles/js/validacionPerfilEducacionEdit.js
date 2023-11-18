$(document).ready(function() {
    $("#formularioPerfilDire").validate({
      rules: {
        annio_inicio_educ: {
          required: true,
          min: 1900,
          max: 2023
        },
        annio_fin_educ: {
          required: true,
          min: 1900,
          max: 2023,
          greaterThan: "#annio_inicio_educ"
        },
        fk_id_institucion: {
          required: true
        },
        fk_id_formacion: {
          required: true
        },
        fk_id_titulo: {
          required: true
        }
      },
      messages: {
        annio_inicio_educ: {
          required: "El año de inicio es obligatorio.",
          min: "El año de inicio debe ser mayor o igual a 1900.",
          max: "El año de inicio debe ser menor o igual a 2023."
        },
        annio_fin_educ: {
          required: "El año de término es obligatorio.",
          min: "El año de término debe ser mayor o igual a 1900.",
          max: "El año de término debe ser menor o igual a 2023.",
          greaterThan: "El año de término debe ser mayor o igual al año de inicio."
        },
        fk_id_institucion: {
          required: "La casa de estudios es obligatoria."
        },
        fk_id_formacion: {
          required: "La formación es obligatoria."
        },
        fk_id_titulo: {
          required: "El título es obligatorio."
        }
      },
      submitHandler: function(form) {
        Swal.fire({
          title: "¿Está seguro de guardar los cambios?",
          text: "Una vez que guarde los cambios, no se podrán deshacer.",
          icon: "question",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Sí, guardar",
          cancelButtonText: "Cancelar"
        }).then((result) => {
          if (result.isConfirmed) {
            form.submit();
          }
        });
      }
    });
  });
  