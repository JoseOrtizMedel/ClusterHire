function ocultarBoton() {
    // Obtiene el botón
    const boton = document.getElementById("btnDireModal");

    // Esconde el botón
    boton.style.display = "none";
}

// Llama a la función al hacer clic en el botón
document.getElementById("btnDireModal").addEventListener("click", ocultarBoton);

