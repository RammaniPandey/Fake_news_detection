document.addEventListener("DOMContentLoaded", function() {
    // Function to add an animation class to an element
    function animateElement(element, animationClass) {
        element.classList.add(animationClass);
        
        // Remove animation class after the animation ends to allow re-triggering
        element.addEventListener('animationend', () => {
            element.classList.remove(animationClass);
        });
    }

    // Fade-in animation for sections as the user scrolls
    const sections = document.querySelectorAll('section');
    const fadeInClass = 'fade-in';
    
    // Detect when an element is in the viewport to trigger fade-in animation
    function checkSectionInView() {
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= window.innerHeight && rect.bottom >= 0) {
                animateElement(section, fadeInClass);
            }
        });
    }

    // Add fade-in class to sections when they are in view
    window.addEventListener('scroll', checkSectionInView);
    checkSectionInView(); // Initial check in case the sections are already in view

    // Button hover animation
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('mouseover', function() {
            animateElement(button, 'pulse');
        });
    });

    // Animate prediction result
    const result = document.getElementById('result');
    if (result) {
        animateElement(result, 'bounce-in');
    }
});

// Additional animations can be defined as CSS keyframes

// CSS Keyframes for various animations

// Fade-in animation
document.styleSheets[0].insertRule(`
    @keyframes fade-in {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
`, 0);

// Pulse animation for button hover
document.styleSheets[0].insertRule(`
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
`, 0);

// Bounce-in animation for result
document.styleSheets[0].insertRule(`
    @keyframes bounce-in {
        0% { transform: scale(0); opacity: 0; }
        60% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); }
    }
`, 0);

// Adding classes to trigger animations

document.styleSheets[0].insertRule(`
    .fade-in {
        animation: fade-in 1s ease-out forwards;
    }
`, 0);

document.styleSheets[0].insertRule(`
    .pulse {
        animation: pulse 0.5s infinite;
    }
`, 0);

document.styleSheets[0].insertRule(`
    .bounce-in {
        animation: bounce-in 1s ease-out forwards;
    }
`, 0);
