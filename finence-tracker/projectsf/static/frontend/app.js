const { createApp } = Vue;

const app = createApp({
  data() {
    return {
      formData: {
        username: "",
        first_name: "",
        last_name: "",
        email: "",
        password1: "",
        password2: "",
      },
      errors: {},
    };
  },
  methods: {
    validateForm() {
      this.errors = {};
      if (!this.formData.username) this.errors.username = "Username is required.";
      if (!this.formData.email) this.errors.email = "Email is required.";
      if (this.formData.password1 !== this.formData.password2) {
        this.errors.password2 = "Passwords do not match.";
      }
      return Object.keys(this.errors).length === 0;
    },
    async registerUser() {
      if (!this.validateForm()) return;

      try {
        const response = await fetch("/accounts/singup/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": this.getCSRFToken(),
          },
          body: JSON.stringify(this.formData),
        });
        if (!response.ok) {
          const data = await response.json();
          this.errors = data.errors || {};
        } else {
          alert("User registered successfully!");
          window.location.href = "/login/";
        }
      } catch (error) {
        console.error("Error registering user:", error);
      }
    },
    getCSRFToken() {
      const cookieValue = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="))
        ?.split("=")[1];
      return cookieValue || "";
    },
  },
});

app.mount("#app");
