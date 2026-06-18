const track = document.querySelector('.carousel-track');
const items = document.querySelectorAll('.carousel-item');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let index = 0;

function updateCarousel() {
  if (!track || items.length === 0) return;
  track.style.transform = `translateX(-${index * 100}%)`;
}

if (nextBtn) {
  nextBtn.addEventListener('click', () => {
    index = (index + 1) % items.length;
    updateCarousel();
  });
}

if (prevBtn) {
  prevBtn.addEventListener('click', () => {
    index = (index - 1 + items.length) % items.length;
    updateCarousel();
  });
}

if (items.length > 0) {
  updateCarousel();
  setInterval(() => {
    index = (index + 1) % items.length;
    updateCarousel();
  }, 5000);
}
