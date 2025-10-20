const hamburger = document.getElementById("hamburger");
const mainNav = document.getElementById("mainNav");

hamburger.addEventListener("click", () => {
  mainNav.classList.toggle("open");
});

// Smooth anchor scrolling (if needed)
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click', (e)=>{
    const target = a.getAttribute('href');
    if(target.length > 1){
      e.preventDefault();
      const el = document.querySelector(target);
      if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
      // close mobile nav after click
      mainNav.classList.remove('open');
    }
  });
});
const skills = document.querySelectorAll('.skill-card');
skills.forEach(skill => {
    skill.addEventListener('mouseover', () => {
      skill.style.transform = 'scale(1.1)';
    });
    skill.addEventListener('mouseout', () => {
      skill.style.transform = 'scale(1)';
    });
});
document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();

  if (!name || !email || !message) {
    alert("Please fill out all fields!");
    return;
  }

  fetch('/submit-contact/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ name, email, message })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("Server error: " + response.status);
    }
    return response.json();
  })
  .then(data => {
    if (data.status === 'success') {
      alert("✅ Thank you for reaching out, " + name + "! I’ll get back to you soon.");
      document.getElementById("contactForm").reset();
    } else {
      alert("⚠️ Error: " + data.message);
    }
  })
  .catch(error => {
    console.error("Submission failed:", error);
    alert("❌ Something went wrong. Please try again later.");
  });
});
// certification modal functions
function openModal(src) {
    const modal = document.getElementById("certModal");
    const modalImg = document.getElementById("modalImage");
    modal.style.display = "flex";
    modalImg.src = src;
  }

  function closeModal() {
    document.getElementById("certModal").style.display = "none";
  }
const certCarousel = document.getElementById('certCarousel');
  const carousel = new bootstrap.Carousel(certCarousel, {
    interval: 4000,   // Rotate every 4 seconds
    ride: 'carousel'
  });
