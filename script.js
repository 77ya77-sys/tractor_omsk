document.addEventListener('DOMContentLoaded', () => {

    /* ==============================
       1. ЛОГИКА ТАБОВ И КАРУСЕЛИ (АВТОПАРК)
       ============================== */
    const tabBtns = document.querySelectorAll('.tab-btn');
    const cards = document.querySelectorAll('.card');
    const track = document.getElementById('fleet-track');
    const nextBtnFleet = document.getElementById('carousel-next');
    const prevBtnFleet = document.getElementById('carousel-prev');

    function updateCarouselButtons() {
        if (!track || !nextBtnFleet || !prevBtnFleet) return;
        const maxScrollLeft = track.scrollWidth - track.clientWidth;
        // Small threshold to fix rounding issues
        if (track.scrollLeft <= 1) {
            prevBtnFleet.style.opacity = '0.5';
            prevBtnFleet.style.pointerEvents = 'none';
        } else {
            prevBtnFleet.style.opacity = '1';
            prevBtnFleet.style.pointerEvents = 'auto';
        }

        if (Math.ceil(track.scrollLeft) >= maxScrollLeft - 1) {
            nextBtnFleet.style.opacity = '0.5';
            nextBtnFleet.style.pointerEvents = 'none';
        } else {
            nextBtnFleet.style.opacity = '1';
            nextBtnFleet.style.pointerEvents = 'auto';
        }
    }

    if (track && nextBtnFleet && prevBtnFleet) {
        track.addEventListener('scroll', updateCarouselButtons);
        // Recalculate on resize
        window.addEventListener('resize', updateCarouselButtons);

        nextBtnFleet.addEventListener('click', () => {
            const cardElement = track.querySelector('.card:not([style*="display: none"])');
            if (cardElement) {
                const cardWidth = cardElement.offsetWidth;
                const gap = parseFloat(getComputedStyle(track).gap) || 16;
                track.scrollBy({ left: cardWidth + gap, behavior: 'smooth' });
            }
        });

        prevBtnFleet.addEventListener('click', () => {
            const cardElement = track.querySelector('.card:not([style*="display: none"])');
            if (cardElement) {
                const cardWidth = cardElement.offsetWidth;
                const gap = parseFloat(getComputedStyle(track).gap) || 16;
                track.scrollBy({ left: -(cardWidth + gap), behavior: 'smooth' });
            }
        });
    }

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Убираем активный класс у всех
            tabBtns.forEach(b => b.classList.remove('active'));
            // Добавляем текущей
            btn.classList.add('active');

            const filter = btn.dataset.filter;

            let visibleCount = 0;
            cards.forEach(card => {
                // Если фильтр all или совпадает с data-category - показываем
                if (filter === 'all' || card.dataset.category === filter) {
                    card.style.display = 'flex';
                    visibleCount++;
                    // Анимация плавного появления
                    card.style.animation = 'none';
                    card.offsetHeight; /* trigger reflow */
                    card.style.animation = 'slideUp 0.4s ease forwards';
                } else {
                    card.style.display = 'none';
                }
            });

            // Reset scroll to 0 when changing tabs
            if (track) {
                if (visibleCount > 0 && visibleCount < 4) {
                    track.classList.add('is-centered');
                } else {
                    track.classList.remove('is-centered');
                }
                track.scrollTo({ left: 0, behavior: 'instant' });
                setTimeout(updateCarouselButtons, 50);
            }
        });
    });

    // Initial check
    setTimeout(updateCarouselButtons, 100);

    /* ==============================
       2. ЛОГИКА КВИЗ-КАЛЬКУЛЯТОРА
       ============================== */
    const steps = document.querySelectorAll('.quiz__step');
    const nextBtn = document.getElementById('quiz-next');
    const prevBtn = document.getElementById('quiz-prev');
    const progressFill = document.getElementById('quiz-progress-fill');
    const stepText = document.getElementById('quiz-step-text');
    const actions = document.getElementById('quiz-actions');
    const successMsg = document.getElementById('quiz-success');
    const form = document.getElementById('quiz-form');

    let currentStep = 0;
    const totalSteps = steps.length;

    function updateQuiz() {
        steps.forEach((step, index) => {
            step.classList.toggle('active', index === currentStep);
        });

        const progressPercent = ((currentStep + 1) / totalSteps) * 100;
        progressFill.style.width = `${progressPercent}%`;
        stepText.textContent = `Шаг ${currentStep + 1} из ${totalSteps}`;

        prevBtn.style.display = currentStep === 0 ? 'none' : 'inline-flex';

        if (currentStep === totalSteps - 1) {
            nextBtn.style.display = 'none'; // Скрываем "Далее" на последнем шаге (там кнопка отправки формы)
        } else {
            nextBtn.style.display = 'inline-flex';
            checkStepValidity();
        }
    }

    function checkStepValidity() {
        const currentInputs = steps[currentStep].querySelectorAll('input[type="radio"]');
        if (currentInputs.length > 0) {
            const isChecked = Array.from(currentInputs).some(input => input.checked);
            nextBtn.disabled = !isChecked;
        } else {
            nextBtn.disabled = false;
        }
    }

    // Обработка кликов по карточкам с радиокнопками
    steps.forEach(step => {
        const inputs = step.querySelectorAll('input[type="radio"]');
        inputs.forEach(input => {
            input.addEventListener('change', () => {
                // Стилизуем выбранный вариант
                const options = step.querySelectorAll('.quiz__option');
                options.forEach(opt => opt.classList.remove('selected'));
                input.closest('.quiz__option').classList.add('selected');

                checkStepValidity();

                // Автоматический переход на следующий шаг после выбора
                setTimeout(() => {
                    if (currentStep < totalSteps - 1 && document.activeElement !== document.getElementById('quiz-next')) {
                        currentStep++;
                        updateQuiz();
                    }
                }, 400);
            });
        });
    });

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            if (currentStep < totalSteps - 1) {
                currentStep++;
                updateQuiz();
            }
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            if (currentStep > 0) {
                currentStep--;
                updateQuiz();
            }
        });
    }

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            // Здесь должна быть логика отправки (fetch / XMLHttpRequest)

            // Симуляция успешной отправки
            steps.forEach(step => step.style.display = 'none');
            actions.style.display = 'none';
            stepText.style.display = 'none';
            progressFill.style.width = '100%';

            successMsg.style.display = 'block';
        });
    }

    // Инициализация
    updateQuiz();
});
