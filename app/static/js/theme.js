document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("theme-toggle");
    const body = document.body;
  
    // Load saved theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
      body.className = savedTheme;
    }
  
    toggleBtn.addEventListener("click", () => {
        if (body.classList.contains("dark-theme")) {
          body.classList.replace("dark-theme", "light-theme");
          toggleBtn.textContent = "🌙";
          localStorage.setItem("theme", "light-theme");
        } else {
          body.classList.replace("light-theme", "dark-theme");
          toggleBtn.textContent = "🌞";
          localStorage.setItem("theme", "dark-theme");
        }
      });      
  });
  