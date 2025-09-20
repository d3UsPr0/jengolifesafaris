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

document.addEventListener("DOMContentLoaded", function () {
  // Initialize scrolling for both sections
  initCarouselScroll("destinations");
  initCarouselScroll("safaris");
});

function initCarouselScroll(sectionId) {
  const scrollContainer = document.querySelector(
    `#${sectionId} .safari-packages-scroll`
  );
  const leftBtn = document.querySelector(`#${sectionId} .carousel-btn-left`);
  const rightBtn = document.querySelector(`#${sectionId} .carousel-btn-right`);

  if (scrollContainer && leftBtn && rightBtn) {
    const scrollAmount = 320; // Width of card + gap

    leftBtn.addEventListener("click", function () {
      scrollContainer.scrollBy({ left: -scrollAmount, behavior: "smooth" });
    });

    rightBtn.addEventListener("click", function () {
      scrollContainer.scrollBy({ left: scrollAmount, behavior: "smooth" });
    });
  }
}

// Quotation Form Submission
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quotationForm');
    const messageDiv = document.getElementById('formMessage');
    const submitUrl = document.getElementById('submit_quotation_url').value;
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitButton = form.querySelector('button[type="submit"]');
        
        // Show loading state
        submitButton.disabled = true;
        submitButton.textContent = 'Sending...';
        messageDiv.style.display = 'none';
        
        // Collect form data
        const formData = new FormData(form);
        const jsonData = {};
        
        for (let [key, value] of formData.entries()) {
            jsonData[key] = value;
        }
        
        // Send AJAX request
        fetch(submitUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify(jsonData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                messageDiv.className = 'alert alert-success mt-3';
                messageDiv.innerHTML = data.message;
                form.reset();
            } else {
                messageDiv.className = 'alert alert-danger mt-3';
                messageDiv.innerHTML = data.message;
                
                // Show errors if available
                if (data.errors) {
                    const errors = Object.values(data.errors).join('<br>');
                    messageDiv.innerHTML += '<br>' + errors;
                }
            }
            messageDiv.style.display = 'block';
            
            // Scroll to message
            messageDiv.scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            messageDiv.className = 'alert alert-danger mt-3';
            messageDiv.innerHTML = 'An error occurred. Please try again. Error: ' + error.message;
            messageDiv.style.display = 'block';
            console.error('Error:', error);
        })
        .finally(() => {
            submitButton.disabled = false;
            submitButton.textContent = 'Get a Quote';
        });
    });
});