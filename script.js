const FREE_PLAN_URL = 'downloads/how-to-gym-arm-workout-plan.pdf';
const FORM_NAME = 'contact';

// Mobile navigation
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

navToggle?.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', isOpen);
  navToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
});

navLinks?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
    navToggle?.setAttribute('aria-label', 'Open menu');
  });
});

// Header shadow on scroll
const header = document.querySelector('.site-header');
window.addEventListener('scroll', () => {
  header?.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

function triggerDownload(url, filename) {
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  link.rel = 'noopener';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

function encodeFormData(form) {
  const params = new URLSearchParams();
  params.append('form-name', FORM_NAME);

  form.querySelectorAll('input, select, textarea').forEach((field) => {
    if (!field.name || field.type === 'submit' || field.type === 'button') return;
    if ((field.type === 'radio' || field.type === 'checkbox') && !field.checked) return;
    params.append(field.name, field.value);
  });

  return params.toString();
}

async function submitToNetlify(form) {
  const response = await fetch('/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: encodeFormData(form),
  });

  if (!response.ok) {
    throw new Error(`Netlify returned ${response.status}`);
  }

  return response;
}

// Contact form — submit to Netlify, then download PDF
const form = document.querySelector('.contact-form');
const successMessage = form?.querySelector('.form-success');
let allowNativeSubmit = false;

form?.addEventListener('submit', async (e) => {
  if (allowNativeSubmit) return;

  e.preventDefault();

  const btn = form.querySelector('button[type="submit"]');
  const original = btn.textContent;

  btn.textContent = 'Submitting...';
  btn.disabled = true;

  try {
    await submitToNetlify(form);

    triggerDownload(FREE_PLAN_URL, 'how-to-gym-arm-workout-plan.pdf');

    btn.textContent = 'Download Started!';
    successMessage?.removeAttribute('hidden');

    setTimeout(() => {
      btn.textContent = original;
      btn.disabled = false;
      successMessage?.setAttribute('hidden', '');
      form.reset();
    }, 5000);
  } catch (error) {
    console.error('Form submission failed, falling back to native submit:', error);
    allowNativeSubmit = true;
    btn.textContent = original;
    btn.disabled = false;
    form.submit();
  }
});

// Fade-in on scroll
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
);

document.querySelectorAll(
  '.lead-magnet-content, .contact-form, .service-card, .step, .plan-card, .about-content, .about-image, .cta-banner-inner'
).forEach((el) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});

const style = document.createElement('style');
style.textContent = '.visible { opacity: 1 !important; transform: translateY(0) !important; }';
document.head.appendChild(style);