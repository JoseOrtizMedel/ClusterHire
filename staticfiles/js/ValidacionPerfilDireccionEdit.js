$(document).ready(function() {
    $("#formularioPerfilDire").validate({
      rules: {
        numeracion: {
          required: true,
          number: true,
          digits: true
        },
        nombre_calle: {
          required: true,
          minlength: 3,
          maxlength: 50
        },
        fk_d_comuna: {
          required: true
        },
        comuna: {
          required: true
        }
      },
      messages: {
        numeracion: {
          required: "Ingrese la numeración.",
          number: "Ingrese un número válido.",
          digits: "La numeración debe ser un número"
        },
        nombre_calle: {
          required: "Ingrese el nombre de la calle.",
          minlength: "Ingrese al menos 3 caracteres.",
          maxlength: "Ingrese máximo 50 caracteres."
        },
        fk_d_comuna: {
          required: "Seleccione una comuna."
        },
        comuna: {
          required: "Seleccione una comuna."
        }
      }
    });
  
    $("#formularioPerfilDire").submit(function() {
      Swal.fire({
        title: "Datos Actualizados",
        text: "Sus datos personales han sido actualizados exitosamente",
        icon: "success",
        confirmButtonText: "Aceptar",
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
          // Enviar formulario
          this.submit();
        }
      });
    });
  });
  