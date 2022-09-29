const ojo = document.querySelector(".ojo-password");
const img = ojo.querySelector("img");
const input = ojo.previousElementSibling;

ojo.addEventListener("click", () => {
  if (ojo.classList.contains("abierto")) {
    img.src = "/static/Login/img/icons/ojo-cerrado-contraseña.svg";
    input.type = "text";
    ojo.classList = "ojo-password cerrado";
    return;
  }

  img.src = "/static/Login/img/icons/ojo-abierto-contraseña.svg";
  input.type = "password";
  ojo.classList = "ojo-password abierto";
});
