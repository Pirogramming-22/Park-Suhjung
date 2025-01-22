document.getElementById('favorite-button').addEventListener('click', function () {
    this.classList.toggle('active');
  });
  
  document.addEventListener("DOMContentLoaded", () => {
    // Handle interest adjustment
    const interestButtons = document.querySelectorAll(".interest-btn");

    interestButtons.forEach(button => {
        button.addEventListener("click", () => {
            const ideaId = button.dataset.id;
            const adjustment = parseInt(button.dataset.adjustment);
            const interestSpan = document.getElementById(`interest-${ideaId}`);

            let currentInterest = parseInt(interestSpan.textContent);
            currentInterest += adjustment;

            // Update UI
            interestSpan.textContent = currentInterest;

            // (Optional) Send request to server
            // Example:
            // fetch(`/api/interest/${ideaId}/adjust/`, {
            //     method: "POST",
            //     headers: {
            //         "Content-Type": "application/json",
            //     },
            //     body: JSON.stringify({ adjustment }),
            // });
        });
    });

    // Handle like button toggle
    const likeButtons = document.querySelectorAll(".like-btn");

    likeButtons.forEach(button => {
        button.addEventListener("click", () => {
            const ideaId = button.dataset.id;

            // Toggle star icon
            if (button.textContent.trim() === "★") {
                button.textContent = "☆";
            } else {
                button.textContent = "★";
            }

            // (Optional) Send request to server
            // Example:
            // fetch(`/api/like/${ideaId}/toggle/`, {
            //     method: "POST",
            // });
        });
    });
});
