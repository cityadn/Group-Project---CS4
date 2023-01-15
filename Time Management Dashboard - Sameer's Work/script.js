const header = document.querySelector("Header");
window.addEventListener("scroll", function() {
    header.classList.toggle ("sticky", window.scroll > 100);
});