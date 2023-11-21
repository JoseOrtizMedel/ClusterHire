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

    // Función para verificar si una fecha es válida
    function isValidFechaInicio(fecha_inicio_exp) {
        var regEx = /^\d{4}-\d{2}-\d{2}$/;
        if (!fecha_inicio_exp.match(regEx)) return false; 
        var fecha = new Date(fecha_inicio_exp);
        if (!fecha.getTime() && d.getTime() !== 0) return false;
        return fecha.toISOString().slice(0, 10) === fecha_inicio_exp;
      }
  
      function isValidFechaFin(fecha_termino_exp) {
        var regEx = /^\d{4}-\d{2}-\d{2}$/;
        if (!fecha_termino_exp.match(regEx)) return false; 
        var fecha = new Date(fecha_termino_exp);
        if (!fecha.getTime() && d.getTime() !== 0) return false;
        return fecha.toISOString().slice(0, 10) === fecha_termino_exp;
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
        setTimeout(resetSubmitButton, 5000); // 5000 milisegundos (5 segundos) como ejemplo
    }

  $("#formularioPerfilExp").validate({
      rules: {
          nombre_empleo: "required",
          fecha_inicio_exp: {
              required: true,
              date: true
          },
          fecha_termino_exp: {
              required: true,
              date: true
          },
          descripcion: {
            required: true,
            minlength: 20, 
            maxlength: 70,
            // Añadimos la nueva regla
            wrap: 35
          },
          fk_id_comuna: "required",
          fk_id_tipo_empleo: "required",
          fk_id_modalidad: "required",
          fk_id_tipo_cargo: "required"
      },
      messages: {
          nombre_empleo: "Por favor, ingrese el nombre del empleo",
          fecha_inicio_exp: {
              required: "Por favor, ingrese la fecha de inicio",
              date: "Ingrese una fecha válida"
          },
          fecha_termino_exp: {
              required: "Por favor, ingrese la fecha de término",
              date: "Ingrese una fecha válida"
          },
          descripcion: {
            required: "Por favor, ingrese una descripción",
            minlength: "La descripción debe tener al menos 20 caracteres",
            maxlength: "La descripción no debe tener más de 100 caracteres"
          },
          fk_id_tipo_empleo: "Seleccione el tipo de empleo",
          fk_id_modalidad: "Seleccione la modalidad",
          fk_id_comuna: "Seleccione la comuna",
          fk_id_tipo_cargo: "Seleccione el tipo de cargo"
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

        // Mostrar mensaje de éxito con SweetAlert2
        Swal.fire({
            title: 'Experiencia laboral guardada con éxito',
            icon: 'success',
            showCancelButton: false,
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Continuar",
        }).then((result) => {
            if (result.isConfirmed) {
                // Aquí puedes enviar el formulario si es necesario
                form.submit();

                // Deshabilita el botón y muestra "Enviando..."
                disableSubmitButton($("#enviarPerfilExp")[0]);

                }
            });
        },
    });
});
