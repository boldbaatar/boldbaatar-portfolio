document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.querySelector('.cursor');
    const follower = document.querySelector('.cursor-follower');

    if (window.innerWidth > 900) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            
            setTimeout(() => {
                follower.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            }, 60);
        });

        const hoverables = document.querySelectorAll('a, .btn, .project-card, .agency-box, .portrait');
        hoverables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                follower.style.width = '64px';
                follower.style.height = '64px';
                follower.style.background = 'rgba(255, 255, 255, 0.05)';
                follower.style.borderColor = 'transparent';
                cursor.style.transform = 'translate(-50%, -50%) scale(0.5)';
            });
            
            el.addEventListener('mouseleave', () => {
                follower.style.width = '36px';
                follower.style.height = '36px';
                follower.style.background = 'transparent';
                follower.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            });
        });
    }

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(element => {
        observer.observe(element);
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
