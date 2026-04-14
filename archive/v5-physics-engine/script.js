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

        // Magnetic Gravity Effect for Buttons
        const magneticElements = document.querySelectorAll('.metallic-gradient, .border-outline-variant\\/30');
        magneticElements.forEach((el) => {
            el.classList.add('magnetic');
            el.addEventListener('mousemove', (e) => {
                const rect = el.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                el.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
            });
            el.addEventListener('mouseleave', () => {
                el.style.transform = `translate(0px, 0px)`;
            });
        });

        // Hover effect for interactive elements
        const hoverables = document.querySelectorAll('a, button');
        hoverables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                follower.style.width = '70px';
                follower.style.height = '70px';
                follower.style.background = 'rgba(233, 193, 118, 0.15)';
                follower.style.borderColor = 'rgba(233, 193, 118, 0)';
                cursor.style.transform = 'translate(-50%, -50%) scale(0.3)';
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

    // Initialize Premium Smooth Scroll (Lenis)
    if(typeof Lenis !== 'undefined') {
        const lenis = new Lenis({
            duration: 1.4,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
        });

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);
    }

    // Parallax Logic
    const parallaxImgs = document.querySelectorAll('.parallax-bg, .group > img');
    window.addEventListener('scroll', () => {
        let scrollY = window.scrollY;
        parallaxImgs.forEach(img => {
            let speed = 0.08;
            let rect = img.getBoundingClientRect();
            if(rect.top < window.innerHeight && rect.bottom > 0) {
               img.style.transform = `translateY(${(rect.top - window.innerHeight/2) * speed}px) scale(1.15)`;
            }
        });
    });

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
