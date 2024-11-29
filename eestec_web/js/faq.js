document.querySelectorAll('.accordion-header').forEach(button => {
    button.addEventListener('click', () => {
        const item = button.parentElement;
        const content = button.nextElementSibling;
        const isOpen = item.classList.contains('active');

        // Close all accordions
        document.querySelectorAll('.accordion-item').forEach(item => {
            item.classList.remove('active');
        });
        document.querySelectorAll('.accordion-content').forEach(content => {
            content.style.maxHeight = null;
        });

        // If the clicked accordion wasn't open, open it
        if (!isOpen) {
            item.classList.add('active');
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
});

