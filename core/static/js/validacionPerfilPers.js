$(document).ready(function() {
  
/*     function isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(email);
  }    */

  function isValidDV(dv_usuario) {
    if (dv_usuario.length !== 1) {
      return false;
    }
    const regex = /^[0-9kK]{1}$/;
    return regex.test(dv_usuario);
  }
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
      var button = document.getElementById("enviarPerfilPers");
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
      setTimeout(resetSubmitButton, 15000); // 15000 milisegundos (5 segundos) como ejemplo
    }
  
    var formulario = $("#formularioPerfilPers");
  
    formulario.validate({
      rules: {
        rut_usuario: {
          required: true,
          minlength: 8,
          maxlength: 8,
        },
        dv_usuario: {
          required: true,
          minlength: 1,
          maxlength: 1,
        },
        nombre: {
          required: true,
          minlength: 2,
          maxlength: 50,
        },
        segundo_nombre: {
          minlength: 2,
          maxlength: 50,
        },
        primer_apellido: {
          required: true,
          minlength: 2,
          maxlength: 50,
        },
        segundo_apellido: {
          minlength: 2,
          maxlength: 50,
        },
        fecha_nacimiento: {
          required: true,
          customDateValidation: true // Utilizamos una regla personalizada para la validación
        },
        nacionalidad: {
          required: true,
        },
        telefono: {
          required: true,
          minlength: 8,
          maxlength: 8,
        },
        correo: {
          required: true,
          email: true,
        },

        //ExperienciaForm
        nombre_empleo: "required",
        descripcion: "required",
        fecha_inicio_exp: {
          required: true,
          customDateValidation: true // Utilizamos una regla personalizada para la validación
        },
        fecha_termino_exp: {
          required: true,
          customDateValidation: true // Utilizamos una regla personalizada para la validación
        }

      },
      messages: {
        rut_usuario: {
          required: "El rut es obligatorio",
          minlength: "El RUT debe tener al menos 8 dígitos",
          maxlength: "El RUT no debe tener más de 8 dígitos",
        },
        dv_usuario: {
          required: "El dv es obligatorio",
          minlength: "El DV debe tener un solo carácter",
          maxlength: "El DV no debe tener más de un carácter",
        },
        nombre: {
          required: "El primer nombre es obligatorio",
          minlength: "El nombre debe tener al menos 2 caracteres",
          maxlength: "El nombre no debe tener más de 50 caracteres",
        },
        segundo_nombre: {
          required: "El segundo nombre es obligatorio",
          minlength: "El segundo nombre debe tener al menos 2 caracteres",
          maxlength: "El segundo nombre no debe tener más de 50 caracteres",
        },
        primer_apellido: {
          required: "El primer apellido es obligatorio",
          minlength: "El primer apellido debe tener al menos 2 caracteres",
          maxlength: "El primer apellido no debe tener más de 50 caracteres",
        },
        segundo_apellido: {
          required: "El segundo apellido es obligatorio",
          minlength: "El segundo apellido debe tener al menos 2 caracteres",
          maxlength: "El segundo apellido no debe tener más de 50 caracteres",
        },
        fecha_nacimiento: {
          required: "La fecha de nacimiento es obligatoria",
          date: "Ingrese un formato de fecha válido (YYYY-MM-DD)",
        },
        nacionalidad: {
          required: "La nacionalidad es obligatoria",
        },
        telefono: {
          required: "El teléfono es obligatorio",
          minlength: "El teléfono debe tener al menos 8 dígitos",
          maxlength: "El teléfono no debe tener más de 8 dígitos",
        },
        correo: {
          required: "El correo es obligatorio",
          email: "Ingrese un correo electrónico válido",
        },
      },

      submitHandler: function(form) {
        // Validamos la fecha antes de enviarla
        var fecha = $("#fecha_nacimiento").val();
        var dv = $("dv_usuario").val();
        if (!isValidDate(fecha)) {
          // La fecha no es válida, muestra un mensaje de error
          Swal.fire({
            icon: 'error',
            title: 'Error en la fecha',
            text: 'Ingresa una fecha válida en el formato YYYY-MM-DD.',
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Entendido",
          });
          return false; // Evita que se envíe el formulario
        }

        if (!isValidDV(dv)) {
          // El dv no es válido, muestra un mensaje de error
          Swal.fire({
            icon: 'error',
            title: 'Error en el DV',
            text: 'Ingresa un DV válido (números entre 1-9 o letra k).',
            confirmButtonColor: "#3085d6",
            confirmButtonText: "Entendido",
          });

          return false; // Evita que se envíe el formulario
  
        }
  
        // Si la validación es exitosa, muestra una notificación de éxito
        Swal.fire({
          icon: 'success',
          title: '¡Formulario enviado correctamente!',
          text: 'Tu formulario se ha enviado con éxito.',
          confirmButtonColor: "#3085d6",
          confirmButtonText: "Guardar",
          showCloseButton: true // Mostrar el botón de cierre manual
          
        });
  
        // Envía el formulario
        form.submit();
  
        // Deshabilita el botón y muestra "Enviando..."
        disableSubmitButton($("#enviarPerfilPers")[0]);
      }
    });
  
    // Agregamos una regla personalizada para validar la fecha
    $.validator.addMethod("customDateValidation", function(value, element) {
      return /^\d{4}-\d{2}-\d{2}$/.test(value); // Expresión regular para validar el formato YYYY-MM-DD
    }, "Ingresa una fecha válida en el formato YYYY-MM-DD");
  });
  