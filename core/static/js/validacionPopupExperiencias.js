// validacionPopupExperiencias.js

$(document).ready(function () {
  // Configuración de la validación del formulario
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
          fk_id_tipo_empleo: "required",
          fk_id_modalidad: "required",
          fk_id_comuna: "required",
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
            icon: 'success',
            title: 'Experiencia laboral guardada con éxito',
            showConfirmButton: false,
            timer: 1500
        });
    
        // Obtener los datos del formulario
        var formData = $(form).serialize();
    
        // Enviar la solicitud AJAX
        $.ajax({
            type: "POST", // Método HTTP (puede ser GET o POST según tus necesidades)
            url: $(form).attr("action"), // URL a la que enviarás el formulario
            data: formData,
            success: function (response) {
                // Manejar la respuesta del servidor si es necesario
                console.log(response);
            },
            error: function (error) {
                // Manejar errores si es necesario
                console.error(error);
            }
        });
    
        return false; // Evita que el formulario se envíe de la manera estándar
    }
    
  });

  // Puedes agregar otras configuraciones o acciones necesarias aquí
});
