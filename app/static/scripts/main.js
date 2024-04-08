const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");


menuBtn.addEventListener("click", (e) => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
  navLinks.classList.remove("open");
  menuBtnIcon.setAttribute("class", "ri-menu-line");
});

const scrollRevealOption = {
  distance: "50px",
  origin: "bottom",
  duration: 1000,
};

// header container
ScrollReveal().reveal(".header__container h1", {
  ...scrollRevealOption,
});

ScrollReveal().reveal(".header__container p", {
  ...scrollRevealOption,
  delay: 500,
});

ScrollReveal().reveal(".header__container form", {
  ...scrollRevealOption,
  delay: 1000,
});

ScrollReveal().reveal(".header__container a", {
  ...scrollRevealOption,
  delay: 1500,
});

// index.js
document.getElementById("searchForm").addEventListener("submit", function(event) {
  event.preventDefault();
  var searchTerm = document.getElementById("searchInput").value;
  var searchUrl = "https://te.wikipedia.org/wiki/Special:Search/+";
  searchUrl += encodeURIComponent(searchTerm) ;
  window.location.href = searchUrl;
});


/* const scriptURL = "https://script.google.com/macros/s/AKfycbzVifHPnuGwvQ6lq-_2Jg7RZuzQNZDtmAzl6cc4PcrU97DToXJabOrTt-9k5PSpo6s_/exec";
    const form = document.forms['contact-form']; // corrected the form name

    form.addEventListener('submit', e => {
        e.preventDefault();
        fetch(scriptURL, { method: 'POST', body: new FormData(form) })
        .then(response => console.log('Success!', response))
        .catch(error => console.error('Error!', error.message))
    }) */

  

document.addEventListener('contextmenu', function(e) {
  e.preventDefault();
});

const swiper = new Swiper(".swiper", {
  loop: true,
  pagination: {
    el: ".swiper-pagination",
  },
});

