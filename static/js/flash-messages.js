document.addEventListener("DOMContentLoaded", function () {
    prepareFlashMessages();
});

function prepareFlashMessages() {
    const closeButtons = document.querySelectorAll(".js-flash-message-close-button");

    closeButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const flashMessage = button.closest(".js-flash-message");
            if (flashMessage) {
                flashMessage.remove();
            }
        });
    });
}
