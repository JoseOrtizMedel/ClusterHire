$(document).ready(function () {
    // Verifica si la tabla ya es una DataTable
    if (!$.fn.dataTable.isDataTable('#datatable')) {
        // Si no es una DataTable, inicialízala
        $('#datatable').DataTable({
            paging: false,
            searching: true,
            language: {
                search: "Buscar: " // Cambia el texto de búsqueda aquí
            }
        });
    }
});
