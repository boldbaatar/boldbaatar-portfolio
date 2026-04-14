document.addEventListener('DOMContentLoaded', () => {
    // Custom Cursor tracking
    const cursor = document.querySelector('.cursor');
    const follower = document.querySelector('.cursor-follower');

    if (window.innerWidth > 900 && cursor && follower) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            setTimeout(() => {
                follower.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            }, 60);
        });

        // Hover effect for interactive elements (Anchors and Buttons)
        const hoverables = document.querySelectorAll('a, button');
        hoverables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                follower.style.width = '60px';
                follower.style.height = '60px';
                follower.style.background = 'rgba(233, 193, 118, 0.1)';
                follower.style.borderColor = 'transparent';
                cursor.style.transform = 'translate(-50%, -50%) scale(0.5)';
            });
            
            el.addEventListener('mouseleave', () => {
                follower.style.width = '36px';
                follower.style.height = '36px';
                follower.style.background = 'transparent';
                follower.style.borderColor = 'rgba(233, 193, 118, 0.4)';
                cursor.style.transform = 'translate(-50%, -50%) scale(1)';
            });
        });
    }

    // Scroll reveal
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(element => {
        observer.observe(element);
    });

    // Smooth Scrolling for in-page anchors
    document.querySelectorAll('.fade-target').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId && targetId.startsWith('#')) {
                const target = document.querySelector(targetId);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
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
        // Intercept target="_blank"
        document.querySelectorAll('a[target="_blank"]').forEach(link => {
            link.addEventListener('click', function(e) {
                // Not for mailto
                if (this.href.startsWith('mailto:')) return;
                
                // Allow modal UI link to bypass its own interception
                if (this.id === 'modalExternalLink') return;

                e.preventDefault();
                const targetUrl = this.href;
                
                // Show modal
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
                
                // Reset State
                modalImg.style.display = 'none';
                modalLoader.style.display = 'block';
                
                // Set Title
                try {
                    const host = new URL(targetUrl).hostname.replace('www.', '');
                    modalTitle.innerText = "Exploring " + host;
                } catch(err) {
                    modalTitle.innerText = "External Link";
                }

                // Generative Screenshot
                modalImg.src = `https://api.microlink.io/?url=${encodeURIComponent(targetUrl)}&screenshot=true&meta=false&embed=screenshot.url`;
                
                modalExternalLink.href = targetUrl;
            });
        });

        modalImg.addEventListener('load', () => {
            modalLoader.style.display = 'none';
            modalImg.style.display = 'block';
        });

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

        if(closeBtn) closeBtn.addEventListener('click', closeModal);
        if(modalBg) modalBg.addEventListener('click', closeModal);
    }
});
