const usernameInput = document.getElementById('id_username');
const firstNameInput = document.getElementById('id_first_name');
const lastNameInput = document.getElementById('id_last_name');
const emailInput = document.getElementById('id_email');
const password1Input = document.getElementById('id_password1');
const password2Input = document.getElementById('id_password2');
const registerForm = document.getElementById('register-form');

registerForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const errors = [];

  // Validate username
  const username = usernameInput.value.trim();
  if (!username) {
    errors.push('El nombre de usuario es requerido');
  } else if (username.length > 150) {
    errors.push('El nombre de usuario debe tener como máximo 150 caracteres');
  } else if (!/^[a-zA-Z0-9@+.-_]+$/.test(username)) {
    errors.push('El nombre de usuario solo debe contener letras, dígitos y los símbolos @/./+/-/_');
  }

  // Validate first name
  const firstName = firstNameInput.value.trim();
  if (!firstName) {
    errors.push('El primer nombre es requerido');
  } else {
    firstNameInput.value = firstName.charAt(0).toUpperCase() + firstName.slice(1);
  }

  // Validate last name
  const lastName = lastNameInput.value.trim();
  if (!lastName) {
    errors.push('El apellido es requerido');
  } else {
    lastNameInput.value = lastName.charAt(0).toUpperCase() + lastName.slice(1);
  }

  // Validate email
  const email = emailInput.value.trim();
  if (!email) {
    errors.push('El correo electrónico es requerido');
  } else if (!/^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
    errors.push('El correo electrónico no es válido');
  }

  // Validate password1
  const password1 = password1Input.value.trim();
  if (!password1) {
    errors.push('La contraseña es requerida');
  } else if (password1.length < 8) {
    errors.push('La contraseña debe tener al menos 8 caracteres');
  } else if (!/[a-zA-Z0-9!@#\$%\^&*()-_=+\{}\[\]\|:;<>\/?,.'"“”‘’]/.test(password1)) {
    errors.push('La contraseña debe contener al menos un carácter especial y un dígito');
  }

  // Validate password2
  const password2 = password2Input.value.trim();
  if (!password2) {
    errors.push('La confirmación de contraseña es requerida');
  } else if (password2 !== password1) {
    errors.push('Las contraseñas no coinciden');
  }

  // Show error messages if any
  if (errors.length > 0) {
    Swal.fire({
      icon: 'error',
      title: 'Errores de validación',
      html: errors.join('<br />'),
    });
    return;
  }

  // Submit the form if no errors are found
  Swal.fire({
    title: '¡Registro completado correctamente!',
    icon: 'success',
    confirmButtonText: 'Aceptar',
  });
  registerForm.submit();
});