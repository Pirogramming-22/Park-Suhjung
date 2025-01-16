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


document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".idea-star").forEach(star => {
        star.addEventListener("click", () => {
            const ideaId = star.dataset.id;  // 아이디어 ID 가져오기

            fetch(`/api/idea/${ideaId}/toggle-star/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value  // CSRF 토큰 추가
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.is_starred) {
                    star.textContent = "★";  // 찜 상태 업데이트
                } else {
                    star.textContent = "☆";
                }
            })
            .catch(err => console.error("찜하기 요청 실패:", err));
        });
    });
});
