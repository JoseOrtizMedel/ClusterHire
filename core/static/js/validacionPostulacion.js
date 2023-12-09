$(document).ready(function() {
  // Función para verificar si una fecha es válida
  function isValidDate(fecha_formulario) {
    var regEx = /^\d{4}-\d{2}-\d{2}$/;
    if (!fecha_formulario.match(regEx)) return false;  // Formato incorrecto
    var fecha = new Date(fecha_formulario);
    if (!fecha.getTime() && d.getTime() !== 0) return false; // No es una fecha válida
    return fecha.toISOString().slice(0, 10) === fecha_formulario;
  }

  // Esta función se ejecutará después de que se haya recargado la página
  function resetSubmitButton() {
    var button = document.getElementById("enviarPostulacion");
    if (button) {
      button.disabled = false;
      button.value = "Postular"; // Restablece el texto del botón
    }
  }
    // Esta función se llama cuando se hace clic en el botón de enviar
  function disableSubmitButton(button) {
    // Deshabilita el botón
    button.disabled = true;

    // Cambia el texto del botón para indicar que se está procesando
    button.value = "Enviando...";

    // Puedes mostrar un mensaje de espera aquí si lo deseas

    // Establece un temporizador para restablecer el botón después de un tiempo determinado
    setTimeout(resetSubmitButton, 30000); // 30000 milisegundos (5 segundos) como ejemplo
  }

  var formulario = $("#formularioPostulacion");

  formulario.validate({
    rules: {
      fecha_nacimiento: {
        required: true,
        date: true,
      },
      pretencion_renta: {
        required: true,
        min: 460000,
        max: 10000000
      },
    },
    messages: {
      fecha_nacimiento: {
        required: "Este campo es obligatorio",
        date: "Ingrese un formato de fecha válido (YYYY-MM-DD)"
    },
      pretencion_renta: {
        required: "Este campo es obligatorio",
        min: "La pretensión de renta debe ser mayor o igual a 460000",
        max: "La pretensión de renta debe ser mayor o igual a 10000000"
    },
  },

    submitHandler: function(form) {
      console.log("Formulario enviado");
    
      // Validamos la fecha antes de enviarla
      var fecha = $("#fecha_formulario").val();
      if (!isValidDate(fecha)) {
        // La fecha no es válida, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en la fecha',
          text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.'
        });
        return false;
      } 

          // Si la validación es exitosa, muestra una notificación de éxito
          Swal.fire({
            icon: 'success',
            title: '¡Formulario enviado correctamente!',
            text: 'Tu formulario se ha enviado con éxito.',
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Hecho!",
            allowOutsideClick: false,
            showCloseButton: true // Mostrar el botón de cierre manual
          });
        
          // Envía el formulario
          form.submit();
        
          // Deshabilita el botón y muestra "Enviando..."
          disableSubmitButton($("#enviarPostulacion")[0]);
        
      }
  });

  // Agregamos una regla personalizada para validar la fecha
  $.validator.addMethod("customDateValidation", function(value, element) {
    return /^\d{4}-\d{2}-\d{2}$/.test(value); // Expresión regular para validar el formato YYYY-MM-DD
  }, "Ingresa una fecha válida en el formato YYYY-MM-DD");
});
