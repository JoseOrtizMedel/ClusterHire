// fecha_actual.js
document.addEventListener("DOMContentLoaded", function() {
    // Obtén la fecha actual en el formato 'YYYY-MM-DD'
    var today = new Date();
    var year = today.getFullYear();
    var month = String(today.getMonth() + 1).padStart(2, "0");
    var day = String(today.getDate()).padStart(2, "0");
    var currentDate = year + "-" + month + "-" + day;

    // Asigna la fecha actual al campo de fecha oculto
    document.getElementById("fecha_formulario").value = currentDate;
});
