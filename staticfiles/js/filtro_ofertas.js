$(document).ready(function () {
    // Verifica si la tabla ya es una DataTable
    if (!$.fn.dataTable.isDataTable('#datatable')) {
        // Si no es una DataTable, inicialízala
        $('#datatable').DataTable({
            paging: false, // Deshabilita la paginación
            searching: true,
            info: false, // Deshabilita la información de registros mostrados
            language: {
                search: "Buscar: " // Cambia el texto de búsqueda aquí
            }
        });
    }
});
