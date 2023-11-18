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

  $("#formularioPerfilDire").validate({
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
      Swal.fire({
        title: "¿Está seguro de que desea editar su perfil educativo?",
        text: "Una vez que se edite su perfil, los cambios no se podrán revertir.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, editar",
        cancelButtonText: "Cancelar",
      }).then((result) => {
        if (result.isConfirmed) {
          form.submit();
        }
      });
    },
  });
});
