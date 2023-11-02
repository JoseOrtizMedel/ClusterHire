document.getElementById("formulario").addEventListener("submit", function (event) {
    event.preventDefault();
    const direccionForm = new FormData(this);
    
    // Envía el formulario de dirección
    fetch("/guardar_direccion/", {
        method: "POST",
        body: direccionForm,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Si la dirección se guardó con éxito, envía el formulario de usuario
            const usuarioForm = new FormData(document.getElementById("formulario"));
            fetch("/guardar_usuario/", {
                method: "POST",
                body: usuarioForm,
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Ambos formularios se guardaron con éxito, redirige a la página de inicio
                    window.location.href = "/home/";
                } else {
                    alert("Error al guardar el formulario de usuario.");
                }
            });
        } else {
            alert("Error al guardar el formulario de dirección.");
        }
    });
});
