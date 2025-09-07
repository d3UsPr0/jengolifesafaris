/* eslint-disable no-plusplus */
// Counter animation
const animateCounters = () => {
  const counters = document.querySelectorAll(".counter");
  const speed = 200; // lower = faster

  counters.forEach((counter) => {
    const updateCount = () => {
      const target = +counter.getAttribute("data-target");
      const count = +counter.innerText;
      const increment = Math.ceil(target / speed);

      if (count < target) {
        counter.innerText = count + increment;
        setTimeout(updateCount, 30);
      } else {
        counter.innerText = `${target}+`;
      }
    };
    updateCount();
  });
};

// Intersection Observer setup
const observer = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      // Check if the observed element is intersecting the viewport
      if (entry.isIntersecting) {
        // Run the counter animation
        animateCounters();
        // Stop observing once the animation has been triggered
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.5, // Trigger when 50% of the element is visible
  }
);

// Start observing the stats section
const statsSection = document.getElementById("stats");
if (statsSection) {
  observer.observe(statsSection);
}
// End of Counter animation

    // Back to Top Button
  const backToTopBtn = document.getElementById("backToTopBtn");

  window.addEventListener("scroll", function () {
    if (window.pageYOffset > 300) {
      backToTopBtn.style.display = "flex";
      backToTopBtn.style.justifyContent = "center";
      backToTopBtn.style.alignItems = "center";
    } else {
      backToTopBtn.style.display = "none";
    }
  });

  backToTopBtn.addEventListener("click", function () {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

// Navbar toggle icon change
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.getElementById('navbarToggler');
    const navbarCollapse = document.getElementById('navbarNav');
    const togglerIcon = navbarToggler.querySelector('.navbar-toggler-icon');
    const closeIcon = navbarToggler.querySelector('.close-icon');
    
    // Toggle icons when navbar is shown/hidden
    navbarCollapse.addEventListener('show.bs.collapse', function () {
        togglerIcon.style.display = 'none';
        closeIcon.style.display = 'inline-block';
    });
    
    navbarCollapse.addEventListener('hide.bs.collapse', function () {
        togglerIcon.style.display = 'inline-block';
        closeIcon.style.display = 'none';
    });
    
    // Close menu when clicking on a nav link (optional)
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function(navLink) {
        navLink.addEventListener('click', function() {
            const bsCollapse = new bootstrap.Collapse(navbarCollapse);
            bsCollapse.hide();
        });
    });
    
    // Remove focus outline after click
    navbarToggler.addEventListener('click', function() {
        this.blur(); // Remove focus after click
    });
});