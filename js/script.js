// Theme: "light" | "dark" | "auto" (follows the OS). Stored per browser.
(function () {
    const root = document.documentElement;
    const order = ['auto', 'light', 'dark'];
    const icons = { auto: 'fa-circle-half-stroke', light: 'fa-sun', dark: 'fa-moon' };

    function read() { try { return localStorage.getItem('theme') || 'auto'; } catch (e) { return 'auto'; } }
    function write(v) { try { localStorage.setItem('theme', v); } catch (e) { /* storage blocked */ } }
    function apply(v) {
        if (v === 'auto') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', v);
        const btn = document.querySelector('.theme-btn');
        if (btn) {
            btn.innerHTML = '<i class="fas ' + icons[v] + '"></i>';
            btn.title = 'Theme: ' + v + ' (click to change)';
            btn.setAttribute('aria-label', btn.title);
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
        let theme = read();
        apply(theme);
        const btn = document.querySelector('.theme-btn');
        if (btn) btn.addEventListener('click', function () {
            theme = order[(order.indexOf(theme) + 1) % order.length];
            write(theme); apply(theme);
        });

        // Mobile menu
        const menuBtn = document.querySelector('.menu-btn');
        const links = document.querySelector('.nav-links');
        if (menuBtn && links) {
            menuBtn.addEventListener('click', function () {
                const open = links.classList.toggle('open');
                menuBtn.setAttribute('aria-expanded', open);
            });
            links.addEventListener('click', function (e) { if (e.target.closest('a')) links.classList.remove('open'); });
        }

        // Active nav link
        const page = window.location.pathname.split('/').pop() || 'index.html';
        document.querySelectorAll('.nav-links a').forEach(function (a) {
            if (a.getAttribute('href') === page) a.classList.add('active');
        });

        // Filter tabs (notes, projects)
        document.querySelectorAll('.filters').forEach(function (bar) {
            const target = document.querySelector(bar.dataset.target);
            if (!target) return;
            const items = target.querySelectorAll('[data-tags]');
            bar.querySelectorAll('.filter').forEach(function (f) {
                const key = f.dataset.filter;
                const n = key === 'all' ? items.length
                    : Array.from(items).filter(function (it) { return it.dataset.tags.split(' ').includes(key); }).length;
                const c = document.createElement('span'); c.className = 'count'; c.textContent = n; f.appendChild(c);
                f.addEventListener('click', function () {
                    bar.querySelectorAll('.filter').forEach(function (o) { o.classList.remove('active'); o.setAttribute('aria-pressed', 'false'); });
                    f.classList.add('active'); f.setAttribute('aria-pressed', 'true');
                    items.forEach(function (it) {
                        it.dataset.hidden = !(key === 'all' || it.dataset.tags.split(' ').includes(key));
                    });
                });
            });
        });

        // Gentle reveal on scroll
        const els = document.querySelectorAll('.reveal');
        if ('IntersectionObserver' in window) {
            const io = new IntersectionObserver(function (entries) {
                entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
            }, { rootMargin: '0px 0px -40px 0px' });
            els.forEach(function (el) { io.observe(el); });
        } else {
            els.forEach(function (el) { el.classList.add('in'); });
        }

        const y = document.getElementById('year');
        if (y) y.textContent = new Date().getFullYear();
    });
})();
