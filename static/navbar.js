const navbarToggleBtn = document.querySelector(".navbar__toggleBtn");
const navbar = document.querySelector(".navbar__menu");

navbarToggleBtn.addEventListener("click", () => {
  navbar.classList.toggle("active");
});
