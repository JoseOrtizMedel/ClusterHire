$(document).ready(function() {
  // Función para verificar si una fecha es válida
  function isValidDate(dateString) {
    var regEx = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateString.match(regEx)) return false;  // Formato incorrecto
    var d = new Date(dateString);
    if (!d.getTime() && d.getTime() !== 0) return false; // No es una fecha válida
    return d.toISOString().slice(0, 10) === dateString;
  }

  // Esta función se ejecutará después de que se haya recargado la página
  function resetSubmitButton() {
    var button = document.getElementById("enviar");
    if (button) {
      button.disabled = false;
      button.value = "Ingresar"; // Restablece el texto del botón
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
    setTimeout(resetSubmitButton, 5000); // 5000 milisegundos (5 segundos) como ejemplo
  }

  var formulario = $("#formulario");

  formulario.validate({
    rules: {
      nom_oferta: "required",
      anhos_experiencia:"required",
      fecha_oferta: {
        required: true,
        customDateValidation: true // Utilizamos una regla personalizada para la validación
      }
    },
    messages: {
      nom_oferta: "Este campo es obligatorio",
      anhos_experiencia: "Este campo es obligatorio",
      fecha_oferta: {
        required: "Este campo es obligatorio",
        customDateValidation: "Ingresa una fecha válida en el formato YYYY-MM-DD"
      }
    },
    submitHandler: function(form) {
      // Validamos la fecha antes de enviarla
      var fecha = $("#fecha_oferta").val();
      if (!isValidDate(fecha)) {
        // La fecha no es válida, muestra un mensaje de error
        Swal.fire({
          icon: 'error',
          title: 'Error en la fecha',
          text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.'
        });
        return false; // Evita que se envíe el formulario
      }

      // Si la validación es exitosa, muestra una notificación de éxito
      Swal.fire({
        icon: 'success',
        title: '¡Formulario enviado correctamente!',
        text: 'Tu formulario se ha enviado con éxito.',
        showCloseButton: true // Mostrar el botón de cierre manual
        
      });

      // Envía el formulario
      form.submit();

      // Deshabilita el botón y muestra "Enviando..."
      disableSubmitButton($("#enviar")[0]);
    }
  });

  // Agregamos una regla personalizada para validar la fecha
  $.validator.addMethod("customDateValidation", function(value, element) {
    return /^\d{4}-\d{2}-\d{2}$/.test(value); // Expresión regular para validar el formato YYYY-MM-DD
  }, "Ingresa una fecha válida en el formato YYYY-MM-DD");
});