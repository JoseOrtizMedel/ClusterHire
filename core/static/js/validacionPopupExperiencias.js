$(document).ready(function () {

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
          descripcion: "required",
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
          descripcion: "Por favor, ingrese una descripción",
          fk_id_tipo_empleo: "Seleccione el tipo de empleo",
          fk_id_modalidad: "Seleccione la modalidad",
          fk_id_comuna: "Seleccione la comuna",
          fk_id_tipo_cargo: "Seleccione el tipo de cargo"
      },
      submitHandler: function (form) {
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
