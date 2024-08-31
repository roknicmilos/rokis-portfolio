document.addEventListener("DOMContentLoaded", function () {
    if (isMobileDevice()) {
        initMobileDevicePDFButton();
    } else {
        initDesktopDevicePDFButton();
    }
});

function isMobileDevice() {
    return (
        /Mobi|Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop/.test(navigator.userAgent)
        || window.matchMedia("(max-width: 767px)").matches
    );
}

function initMobileDevicePDFButton() {
    const pdfButton = document.querySelector(".pdf-button");
    let isExpanded = false;

    /**
     * Prevent default action of the button if it is not expanded and expand it.
     * Allow the default action if the button is expanded and collapse it.
     */
    pdfButton.addEventListener("click", function (event) {
        isExpanded = !isExpanded;
        if (isExpanded) {
            event.preventDefault();
            pdfButton.classList.add("expanded");
        } else {
            pdfButton.classList.remove("expanded");
        }
    });

    /**
     * Collapse the button if the user clicks outside the button.
     */
    document.addEventListener("click", function (event) {
        if (isExpanded && !pdfButton.contains(event.target)) {
            pdfButton.classList.remove("expanded");
            isExpanded = false;
        }
    });
}

function initDesktopDevicePDFButton() {
    const pdfButton = document.querySelector(".pdf-button");
    let isExpanded = false;

    /**
     * Expand the button when the user hovers over it.
     */
    pdfButton.addEventListener("mouseover", function () {
        isExpanded = true;
        pdfButton.classList.add("expanded");
    });

    /**
     * Collapse the button when the user moves the cursor away from it.
     */
    pdfButton.addEventListener("mouseout", function () {
        pdfButton.classList.remove("expanded");
        isExpanded = false;
    });
}
