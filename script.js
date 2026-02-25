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

    const tabTypeBtns = document.querySelectorAll('.fleet__tabs--types .tab-btn');
    let currentType = 'all';

    function filterCards() {
        let visibleCount = 0;
        cards.forEach(card => {
            const categories = card.dataset.category ? card.dataset.category.split(' ') : [];
            const matchType = currentType === 'all' || categories.includes(currentType);

            if (matchType) {
                card.style.display = 'flex';
                visibleCount++;
                card.style.animation = 'none';
                card.offsetHeight;
                card.style.animation = 'slideUp 0.4s ease forwards';
            } else {
                card.style.display = 'none';
            }
        });

        if (track) {
            if (visibleCount > 0 && visibleCount < 4) {
                track.classList.add('is-centered');
            } else {
                track.classList.remove('is-centered');
            }
            track.scrollTo({ left: 0, behavior: 'instant' });
            setTimeout(updateCarouselButtons, 50);
        }
    }

    tabTypeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabTypeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentType = btn.dataset.type;
            filterCards();
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

    /* ==============================
       3. СТРОГАЯ МАСКА ДЛЯ ТЕЛЕФОНА
       ============================== */
    function initPhoneMask(phoneInput) {
        if (!phoneInput) return;
        const prefix = '+7 ';

        phoneInput.addEventListener('input', function (e) {
            let val = this.value.replace(/\D/g, '');
            if (val.length > 0 && (val[0] === '7' || val[0] === '8')) {
                val = val.substring(1);
            }
            if (val.length === 0) {
                this.value = prefix;
                return;
            }

            val = val.substring(0, 10);

            let formatted = prefix;
            if (val.length > 0) formatted += '(' + val.substring(0, 3);
            if (val.length >= 4) formatted += ') ' + val.substring(3, 6);
            if (val.length >= 7) formatted += '-' + val.substring(6, 8);
            if (val.length >= 9) formatted += '-' + val.substring(8, 10);

            this.value = formatted;
        });

        const moveCursorToEnd = (el) => {
            setTimeout(() => el.setSelectionRange(el.value.length, el.value.length), 10);
        };

        phoneInput.addEventListener('focus', function () {
            if (this.value.trim() === '' || this.value === '+7') this.value = prefix;
            moveCursorToEnd(this);
        });

        phoneInput.addEventListener('click', function () {
            moveCursorToEnd(this);
        });

        phoneInput.addEventListener('keydown', function (e) {
            if ((e.key === 'Backspace' || e.key === 'Delete') && this.value.length <= prefix.length) {
                e.preventDefault();
            }
            if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(e.key)) {
                e.preventDefault();
            }
        });
    }

    initPhoneMask(document.getElementById('quiz-phone'));
    initPhoneMask(document.getElementById('bottom-phone'));

    /* ==============================
       4. МОДАЛЬНОЕ ОКНО КАРТОЧЕК
       ============================== */
    const modal = document.getElementById('equipment-modal');
    const modalBody = document.getElementById('modal-body');
    const modalClose = document.getElementById('modal-close');
    const modalOverlay = document.getElementById('modal-overlay');

    function openModal(cardData) {
        if (!modal || !modalBody) return;

        let specsHtml = '';
        if (cardData.specs) {
            const specsObj = JSON.parse(cardData.specs);
            specsHtml = Object.entries(specsObj).map(([key, value]) => `<li><span>${key}</span><span>${value}</span></li>`).join('');
        }

        let idealHtml = '';
        if (cardData.ideal) {
            const idealArr = JSON.parse(cardData.ideal);
            idealHtml = idealArr.map(item => `<li>${item}</li>`).join('');
        }

        modalBody.innerHTML = `
            <img src="${cardData.img}" class="modal-detail__img" alt="${cardData.model}">
            <div class="modal-detail__body">
                <h3 class="modal-detail__title">${cardData.model}</h3>
                <div class="modal-detail__price">${cardData.price}</div>
                
                ${specsHtml ? `
                <div class="modal-detail__section">
                    <div class="modal-detail__section-title">Характеристики</div>
                    <ul class="modal-detail__specs">${specsHtml}</ul>
                </div>` : ''}
                
                ${idealHtml ? `
                <div class="modal-detail__section">
                    <div class="modal-detail__section-title">Идеально подходит для...</div>
                    <ul class="modal-detail__ideal">${idealHtml}</ul>
                </div>` : ''}
                
                <a href="#quiz-section" class="btn btn-primary btn-block modal-detail__cta" onclick="document.getElementById('equipment-modal').classList.remove('is-active'); document.body.style.overflow = '';">Оставить заявку на эту модель</a>
            </div>
        `;

        modal.classList.add('is-active');
        document.body.style.overflow = 'hidden';
    }

    function closeModal() {
        if (!modal) return;
        modal.classList.remove('is-active');
        document.body.style.overflow = '';
        setTimeout(() => { if (modalBody) modalBody.innerHTML = ''; }, 300);
    }

    cards.forEach(card => {
        if (card.classList.contains('js-open-modal')) {
            card.addEventListener('click', () => {
                openModal(card.dataset);
            });
        }
    });

    if (modalClose) modalClose.addEventListener('click', closeModal);
    if (modalOverlay) modalOverlay.addEventListener('click', closeModal);

    /* ==============================
       5. FAQ АККОРДЕОНЫ
       ============================== */
    const faqBtns = document.querySelectorAll('.faq-btn');
    faqBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const parent = btn.parentElement;
            parent.classList.toggle('is-open');
        });
    });

    // Инициализация
    updateQuiz();
});
