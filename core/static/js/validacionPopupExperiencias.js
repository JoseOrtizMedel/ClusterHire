$(document).ready(function () {

    // Función para verificar si una fecha es válida
    function isValidFechaInicio(fecha_inicio_exp) {
        var regEx = /^\d{4}-\d{2}-\d{2}$/;
        if (!fecha_inicio_exp.match(regEx)) return false; 
        var fecha = new Date(fecha_inicio_exp);
        if (!fecha.getTime() && fecha.getTime() !== 0) return false;
        return fecha.toISOString().slice(0, 10) === fecha_inicio_exp;
      }
  
      function isValidFechaFin(fecha_termino_exp) {
        var regEx = /^\d{4}-\d{2}-\d{2}$/;
        if (!fecha_termino_exp.match(regEx)) return false; 
        var fecha = new Date(fecha_termino_exp);
        if (!fecha.getTime() && fecha.getTime() !== 0) return false;
        return fecha.toISOString().slice(0, 10) === fecha_termino_exp;
      }
  
      function validarFechaTermino(fecha_inicio, fecha_termino) {
        // Crea objetos Date a partir de los valores de los inputs
        var date1 = new Date(fecha_inicio);
        var date2 = new Date(fecha_termino);
      
        // Compara los componentes de la fecha
        return date1.getFullYear() < date2.getFullYear() ||
          (date1.getFullYear() === date2.getFullYear() &&
            date1.getMonth() < date2.getMonth()) ||
          (date1.getFullYear() === date2.getFullYear() &&
            date1.getMonth() === date2.getMonth() &&
            date1.getDate() < date2.getDate());
      }
      

    // Esta función se ejecutará después de que se haya recargado la página
    function resetSubmitButton() {
        var button = document.getElementById("enviarPerfilExp");
        if (button) {
        button.disabled = false;
        button.value = "Guardar"; // Restablece el texto del botón
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
          },
          descripcion: {
            required: true,
            minlength: 20, 
            maxlength: 2000,
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
            maxlength: "La descripción no debe tener más de 2000 caracteres"
          }
      },

      submitHandler: function (form) {

      // Validamos la fecha antes de enviarla
      var fechaInicio = $("#fecha_inicio_exp").val();
      var fechaFin = $("#fecha_termino_exp").val();
      if (!isValidFechaInicio(fechaInicio)) {
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

        if (!isValidFechaFin(fechaFin)) {
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

        if (!validarFechaTermino(fechaInicio, fechaFin)) {
          // La fecha no es válida, muestra un mensaje de error
          Swal.fire({
            icon: 'error',
            title: 'Error en la fecha de término',
            text: 'La fecha de término debe ser posterior a la fecha de inicio.',
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Entendido",
          });

          return false; // Evita que se envíe el formulario
        }

        // ...

        // Mostrar mensaje de éxito con SweetAlert2
        Swal.fire({
            title: 'Experiencia laboral guardada con éxito',
            icon: 'success',
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Continuar",
        })
            form.submit();

            // Deshabilita el botón y muestra "Enviando..."
            disableSubmitButton($("#enviarPerfilExp")[0]);
        },
    });
});
