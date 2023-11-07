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
        var button = document.getElementById("enviarPerfilDire");
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

  var formulario = $("#formularioPerfilDire");
  
    formulario.validate({
      rules: {
        numeracion: "required",
        nombre_calle: "required",

      },
      messages: {
        numeracion: "required",
        nombre_calle: "required",
      },

      submitHandler: function(form) {
        
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
        disableSubmitButton($("#enviarPerfilDire")[0]);
      }
    });
  
    // Agregamos una regla personalizada para validar la fecha
    $.validator.addMethod("customDateValidation", function(value, element) {
      return /^\d{4}-\d{2}-\d{2}$/.test(value); // Expresión regular para validar el formato YYYY-MM-DD
    }, "Ingresa una fecha válida en el formato YYYY-MM-DD");
  });
  