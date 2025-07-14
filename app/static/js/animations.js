// Interactive animations for Alan's portfolio
document.addEventListener("DOMContentLoaded", function () {
  // Intersection Observer for scroll animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, observerOptions);

  // Observe fade-in elements
  document.querySelectorAll(".fade-in-up").forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(30px)";
    el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    observer.observe(el);
  });

  // Enhanced tech badge interactions
  document.querySelectorAll(".tech-badge").forEach((badge) => {
    badge.addEventListener("click", function () {
      // Create sparkle effect
      createSparkle(this);
    });
  });

  // Stats counter animation
  document.querySelectorAll(".stat-counter").forEach((counter) => {
    animateCounter(counter);
  });

  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Add parallax effect to floating elements
  window.addEventListener("scroll", () => {
    const scrolled = window.pageYOffset;
    document.querySelectorAll(".float-animation").forEach((el) => {
      const rate = scrolled * -0.5;
      el.style.transform = `translateY(${rate}px)`;
    });
  });

  // Interactive hover effects for cards
  document.querySelectorAll(".hover-lift").forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-8px) rotateY(5deg)";
    });

    card.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0) rotateY(0)";
    });
  });

  // Random tilt for tech badges
  document.querySelectorAll(".tech-badge").forEach((badge) => {
    const randomTilt = (Math.random() - 0.5) * 4; // Random tilt between -2 and 2 degrees
    badge.style.transform = `rotate(${randomTilt}deg)`;
  });
});

// Create sparkle effect function
function createSparkle(element) {
  const sparkle = document.createElement("div");
  sparkle.style.position = "absolute";
  sparkle.style.width = "4px";
  sparkle.style.height = "4px";
  sparkle.style.background = "#ffd700";
  sparkle.style.borderRadius = "50%";
  sparkle.style.pointerEvents = "none";
  sparkle.style.zIndex = "1000";

  const rect = element.getBoundingClientRect();
  sparkle.style.left = rect.left + Math.random() * rect.width + "px";
  sparkle.style.top = rect.top + Math.random() * rect.height + "px";

  document.body.appendChild(sparkle);

  // Animate sparkle
  sparkle
    .animate(
      [
        { transform: "scale(0) rotate(0deg)", opacity: 1 },
        { transform: "scale(1) rotate(180deg)", opacity: 1 },
        { transform: "scale(0) rotate(360deg)", opacity: 0 },
      ],
      {
        duration: 800,
        easing: "ease-out",
      }
    )
    .addEventListener("finish", () => {
      document.body.removeChild(sparkle);
    });
}

// Animate counter function
function animateCounter(element) {
  const target = parseInt(element.textContent.replace(/\D/g, ""));
  const suffix = element.textContent.replace(/[0-9]/g, "");
  let current = 0;
  const increment = target / 50;
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current) + suffix;
  }, 30);
}

// Add cursor trail effect
document.addEventListener("mousemove", (e) => {
  if (Math.random() > 0.9) {
    // Only create trails occasionally
    createCursorTrail(e.clientX, e.clientY);
  }
});

function createCursorTrail(x, y) {
  const trail = document.createElement("div");
  trail.style.position = "fixed";
  trail.style.width = "6px";
  trail.style.height = "6px";
  trail.style.background = "rgba(0, 123, 255, 0.7)";
  trail.style.borderRadius = "50%";
  trail.style.pointerEvents = "none";
  trail.style.zIndex = "999";
  trail.style.left = x + "px";
  trail.style.top = y + "px";

  document.body.appendChild(trail);

  trail
    .animate(
      [
        { transform: "scale(1)", opacity: 1 },
        { transform: "scale(0)", opacity: 0 },
      ],
      {
        duration: 1000,
        easing: "ease-out",
      }
    )
    .addEventListener("finish", () => {
      if (document.body.contains(trail)) {
        document.body.removeChild(trail);
      }
    });
}
