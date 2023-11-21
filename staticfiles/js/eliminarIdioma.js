$(document).ready(function () {
            $('#btnEliminarIdioma').on('click', function () {
                // Aquí puedes mostrar la notificación con SweetAlert2
                Swal.fire({
                  title: "¿Está seguro de que desea eliminar este idioma?",
                  text: "Una vez que se elimine el idioma, no se podrá recuperar.",
                  icon: "warning",
                  showCancelButton: true,
                  confirmButtonColor: "#3085d6",
                  cancelButtonColor: "#d33",
                  confirmButtonText: "Sí, eliminar",
                  cancelButtonText: "Cancelar",
                });
            });
        });
    