document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");
    const passwordInput = document.getElementById("password-input");
    const emailInput = document.getElementById("email-input");
    const passwordToggler = document.getElementById("password-toggler");
    const createButton = document.getElementById("login-button");
    const initCreateButtonText = createButton.innerText;
  
    const formData = new URLSearchParams();
  
    passwordInput.addEventListener("input", function () {
      formData.set("password", passwordInput.value);
      createButton.innerText = initCreateButtonText;
    });

    emailInput.addEventListener("input", function () {
      formData.set("username", emailInput.value);
    });
  
    form.addEventListener("submit", async function (event) {
      event.preventDefault(); // Prevent the default form submission action
      createButton.innerText = "...";
      fetch("http://localhost:5049/api/login", {
        method: "POST",
        body: formData.toString(),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      }).then((response) => {
        return response.json();
      }).then((body) => {
        console.log(body);
        if (body.detail == "LOGIN_BAD_CREDENTIALS") {
          createButton.innerText = "Invalid email or password";
          return;
        }
        localStorage.setItem("token", body.access_token)
        createButton.innerText = initCreateButtonText;
        location.href = 'index.html';
      }).catch((error) => {
        console.log(error);
        createButton.innerText = "Error occured";
        return undefined;
      });
    });
  });
