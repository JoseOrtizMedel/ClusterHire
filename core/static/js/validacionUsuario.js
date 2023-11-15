function validarUsuario() {
    // Obtener el nombre de usuario del formulario
    const username = document.getElementById("username").value;

    // Realizar la solicitud AJAX
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({
        username: username
    }));

    // Resolver la solicitud
    xhr.onload = function() {
        if (xhr.status === 200) {
            const usuario = JSON.parse(xhr.response);
            if (usuario.exists) {
                // El usuario existe
                // Habilitar el botón de inicio de sesión
                document.getElementById("btnEntrar").disabled = false;
            } else {
                // El usuario no existe
                // Deshabilitar el botón de inicio de sesión
                //document.getElementById("btnEntrar").disabled = true;
                // Mostrar un mensaje de error
                alert("El usuario no existe");
            }
        } else {
            // Ocurrió un error
            alert("Ocurrió un error al validar el usuario");
        }
    };
}

// Asignar el evento al botón de inicio de sesión
document.getElementById("btnEntrar").addEventListener("click", validarUsuario);
