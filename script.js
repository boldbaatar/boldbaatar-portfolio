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

    // Screenshot Modal Logic
    const modal = document.getElementById('linkModal');
    const modalBg = document.getElementById('modalBg');
    const modalImg = document.getElementById('modalImg');
    const modalExternalLink = document.getElementById('modalExternalLink');
    const modalTitle = document.getElementById('modalLinkTitle');
    const modalLoader = document.getElementById('modalLoader');
    const closeBtn = document.getElementById('closeModal');

    if (modal && modalImg) {
        document.querySelectorAll('a[target="_blank"]').forEach(link => {
            link.addEventListener('click', function(e) {
                // Ignore mailto links natively
                if (this.href.startsWith('mailto:')) return;
                
                e.preventDefault();
                const targetUrl = this.href;
                
                // Show modal UI
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
                
                // Set Up Loader
                modalImg.style.display = 'none';
                modalLoader.style.display = 'block';
                
                // Extract clean domain for title
                try {
                    const host = new URL(targetUrl).hostname.replace('www.', '');
                    modalTitle.innerText = "Exploring " + host;
                } catch(e) {
                    modalTitle.innerText = "External Link";
                }

                // API for Screenshot Generation
                modalImg.src = `https://api.microlink.io/?url=${encodeURIComponent(targetUrl)}&screenshot=true&meta=false&embed=screenshot.url`;
                
                // Link button
                modalExternalLink.href = targetUrl;
            });
        });

        // When Image finishes loading, hide loader
        modalImg.addEventListener('load', () => {
            modalLoader.style.display = 'none';
            modalImg.style.display = 'block';
        });

        // Handle Image error natively
        modalImg.addEventListener('error', () => {
            modalLoader.innerText = "Preview unavailable. Click below to visit manually.";
        });

        const closeModal = () => {
            modal.classList.remove('active');
            document.body.style.overflow = '';
            setTimeout(() => { 
                modalImg.src = ''; 
                modalLoader.innerText = "Generating Live Preview...";
            }, 400);
        };

        closeBtn.addEventListener('click', closeModal);
        modalBg.addEventListener('click', closeModal);
    }
});
