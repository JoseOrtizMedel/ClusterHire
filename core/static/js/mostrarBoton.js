// Obtiene el botón
const boton = document.getElementById("btnDireModal");

const boton2 = document.getElementById("btnEnviarModalDire");

// Agrega un evento "click" al formulario
document.getElementById("formularioPerfilDire").addEventListener("click", function(e) {
    // Si el clic no fue en el botón
    if (e.target !== boton) {
        // Muestra el botón
        boton.style.display = "";
    }

    if (e.target === boton2) {
        boton.style.display = "none";
    }

});
