document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("login-form");
  const passwordInput = document.getElementById("password-input");
  const usernameInput = document.getElementById("username-input");
  const passwordRepeatInput = document.getElementById("password-repeat-input");
  const emailInput = document.getElementById("email-input");
  const passwordToggler = document.getElementById("password-toggler");
  const createButton = document.getElementById("create-button");
  const initCreateButtonText = createButton.innerText;

  const formData = {};

  passwordInput.addEventListener("input", function () {
    formData.password = passwordInput.value;
    createButton.innerText = initCreateButtonText;
  });

  passwordRepeatInput.addEventListener("input", function () {
    createButton.innerText = initCreateButtonText;
  });

  emailInput.addEventListener("input", function () {
    formData.email = emailInput.value;
  });

  usernameInput.addEventListener("input", function () {
    formData.username = usernameInput.value;
  });

  passwordToggler.addEventListener("click", function() {
    if (passwordInput.getAttribute("type") == "password") {
      passwordInput.setAttribute("type", "text");
      passwordRepeatInput.setAttribute("type", "text");
    } else {
      passwordInput.setAttribute("type", "password");
      passwordRepeatInput.setAttribute("type", "password");
    }
  });

  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Prevent the default form submission action
    createButton.innerText = "...";
    console.log(formData);
    
    if (passwordInput.value !== passwordRepeatInput.value) {
      createButton.innerText = "Password don't match";
      return false;
    }

    fetch("http://localhost:5049/api/register", {
      method: "POST",
      body: JSON.stringify(formData),
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((error) => {
      console.log(error);
      createButton.innerText = "Error occured";
    }).then((response) => {
      return response.json();
    }).then((body) => {
      console.log(body);
      localStorage.setItem("userId", body.id);
      createButton.innerText = "Created!";
      location.href = 'login.html';
    });
  });
});