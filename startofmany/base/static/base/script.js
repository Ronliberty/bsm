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

ScrollReveal().reveal(".header__image img", {
  ...scrollRevealOption,
  origin: "right",
});
ScrollReveal().reveal(".header__content h2", {
  ...scrollRevealOption,
  delay: 500,
});
ScrollReveal().reveal(".header__content h1", {
  ...scrollRevealOption,
  delay: 1000,
});
ScrollReveal().reveal(".header__content p", {
  ...scrollRevealOption,
  delay: 1500,
});
ScrollReveal().reveal(".header__content .header__btn", {
  ...scrollRevealOption,
  delay: 2000,
});
ScrollReveal().reveal(".header__content .socials", {
  ...scrollRevealOption,
  delay: 2500,
});
ScrollReveal().reveal(".header__bar", {
  ...scrollRevealOption,
  delay: 3000,
});


// Select all video containers
const videoContainers = document.querySelectorAll('.video-container');

videoContainers.forEach(container => {
    const video = container.querySelector('video');

    // Show controls on mouse enter
    container.addEventListener('mouseenter', () => {
        video.controls = true; // Enable video controls
        video.play(); // Automatically play video on hover
    });

    // Hide controls and pause video on mouse leave
    container.addEventListener('mouseleave', () => {
        video.controls = false; // Disable video controls
        video.pause(); // Pause the video
    });
});


document.querySelectorAll('.box a button').forEach(button => {
  button.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link action
    alert('Thank you for checking out the ' + this.closest('.box').querySelector('.title').textContent + ' plan!');
  });
});
