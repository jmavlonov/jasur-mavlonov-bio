document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".contact-form");
  const button = form.querySelector("button");
  const resultMessage = document.getElementById("resultMessage");

  // Kichik delay funksiyasi
  const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const oldHTML = button.innerHTML;
    button.disabled = true;
    button.innerHTML = `<span class="spinner"></span><span>Sending...</span>`;

    resultMessage.textContent = "";

    // Foydalanuvchi ko‘rishi uchun 200ms delay
    await delay(400);

    const formData = new FormData(form);
    const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    try {
      const response = await fetch(form.action, {
        method: "POST",
        headers: { "X-CSRFToken": csrfToken },
        body: formData,
      });

      const data = await response.json();

      if (data.success) {
        resultMessage.style.color = "green";
        resultMessage.textContent = data.message;
        form.reset();
      } else {
        resultMessage.style.color = "red";
        resultMessage.textContent = data.message || "❌ Failed to send your message.";
      }
    } catch (error) {
      console.error("Error:", error);
      resultMessage.style.color = "red";
      resultMessage.textContent = "⚠️ Server connection error.";
    } finally {
      // Tugmani tiklaymiz
      button.disabled = false;
      button.innerHTML = oldHTML;
    }
  });
});
