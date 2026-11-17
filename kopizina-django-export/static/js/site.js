const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('[data-menu-button]');
const nav = document.querySelector('[data-nav]');
const year = document.querySelector('[data-year]');

if (year) year.textContent = new Date().getFullYear();

const reservationForm = document.querySelector('[data-reservation-form]');
const reservationSuccess = document.querySelector('[data-reservation-success]');
const reservationReset = document.querySelector('[data-reservation-reset]');
const reservationError = document.querySelector('[data-reservation-error]');
const reservationSubmit = reservationForm?.querySelector('button[type="submit"]');

if (reservationForm && reservationSuccess) {
  const dateField = reservationForm.querySelector('input[name="preferred_date"]');
  if (dateField) {
    const today = new Date();
    const localDate = new Date(today.getTime() - today.getTimezoneOffset() * 60000).toISOString().split('T')[0];
    dateField.min = localDate;
  }

  reservationForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!reservationForm.checkValidity()) {
      reservationForm.reportValidity();
      return;
    }
    const submitButton = reservationSubmit || reservationForm.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.setAttribute('aria-busy', 'true');
    submitButton.dataset.originalLabel = submitButton.innerHTML;
    submitButton.textContent = 'Saving your request…';
    if (reservationError) reservationError.hidden = true;
    const values = Object.fromEntries(new FormData(reservationForm).entries());
    const csrf = reservationForm.querySelector('[name="csrfmiddlewaretoken"]')?.value || '';
    try {
      const response = await fetch('/api/public/reservations/', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrf, 'X-Requested-With': 'XMLHttpRequest' },
        body: new URLSearchParams(values),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || 'Unable to prepare your request');
      reservationForm.hidden = true;
      reservationSuccess.hidden = false;
      reservationSuccess.focus();
    } catch (error) {
      if (reservationError) {
        reservationError.textContent = error.message || 'Unable to prepare your request. Please try again.';
        reservationError.hidden = false;
      }
      submitButton.disabled = false;
      submitButton.removeAttribute('aria-busy');
      submitButton.innerHTML = submitButton.dataset.originalLabel || 'Prepare reservation request ↗';
    }
  });

  reservationReset?.addEventListener('click', () => {
    reservationForm.reset();
    reservationForm.hidden = false;
    reservationSuccess.hidden = true;
    if (reservationError) reservationError.hidden = true;
    reservationForm.querySelector('input')?.focus();
  });
}

const setHeaderState = () => {
  if (header) header.classList.toggle('is-scrolled', window.scrollY > 20);
};
setHeaderState();
window.addEventListener('scroll', setHeaderState, { passive: true });

if (menuButton && nav) {
  const closeMenu = (restoreFocus = false) => {
    nav.classList.remove('is-open');
    document.body.classList.remove('menu-open');
    menuButton.setAttribute('aria-expanded', 'false');
    if (restoreFocus) requestAnimationFrame(() => menuButton.focus());
  };

  menuButton.addEventListener('click', () => {
    const open = !nav.classList.contains('is-open');
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('menu-open', open);
    menuButton.setAttribute('aria-expanded', String(open));
    if (open) nav.querySelector('a')?.focus();
  });

  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) closeMenu(true);
  });
  document.addEventListener('click', (event) => {
    if (nav.classList.contains('is-open') && !nav.contains(event.target) && !menuButton.contains(event.target)) closeMenu();
  });
  window.addEventListener('resize', () => { if (window.innerWidth > 620) closeMenu(); });
}

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealElements = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window && !prefersReducedMotion) {
  document.documentElement.classList.add('motion-ready');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  revealElements.forEach((element) => observer.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add('is-visible'));
}
