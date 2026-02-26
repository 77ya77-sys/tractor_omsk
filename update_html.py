import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

fleet_replacement = """
                <!-- Фильтры (JTBD) -->
                <div class="fleet__tabs" id="fleet-tabs">
                    <button class="tab-btn active" data-filter="all">Вся техника</button>
                    <button class="tab-btn" data-filter="excavators">Экскаваторы</button>
                    <button class="tab-btn" data-filter="loaders">Погрузчики</button>
                    <button class="tab-btn" data-filter="trenches">Копка траншей</button>
                    <button class="tab-btn" data-filter="pits">Котлованы</button>
                    <button class="tab-btn" data-filter="narrow">Узкий проезд</button>
                    <button class="tab-btn" data-filter="planning">Планировка участка</button>
                </div>

                <div class="carousel-wrapper">
                    <button class="carousel-btn carousel-btn--prev" id="carousel-prev" aria-label="Предыдущие">◀</button>
                    <div class="carousel-track" id="fleet-track">
                        <!-- 1. JCB 3CX -->
                        <article class="card js-open-modal" data-category="loaders trenches pits planning" 
                            data-model="Экскаватор-погрузчик JCB 3CX" 
                            data-price="от 2 800 ₽/ч" 
                            data-img="assets/images/fleet/loader-jcb-3cx.webp" 
                            data-specs='{"Фронтальный ковш":"1 м³","Глубина копания":"4.2 м","Навесное":"гидромолот, ямобур"}' 
                            data-ideal='["Копка траншей под кабели и трубы", "Планировка небольших участков", "Погрузка сыпучих стройматериалов"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/loader-jcb-3cx.webp" alt="Экскаватор-погрузчик JCB 3CX" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Экскаватор-погрузчик JCB 3CX</h3>
                                <div class="card__price">от 2 800 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 2. CAT 428F -->
                        <article class="card js-open-modal" data-category="loaders trenches pits planning" 
                            data-model="Экскаватор-погрузчик CAT 428F" 
                            data-price="от 2 900 ₽/ч" 
                            data-img="assets/images/fleet/loader-cat-428f.webp" 
                            data-specs='{"Фронтальный ковш":"1.03 м³","Глубина копания":"4.3 м","Особенность":"Повышенная проходимость"}' 
                            data-ideal='["Работа на сложных грунтах", "Рытье котлованов под фундамент", "Обратная засыпка"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/loader-cat-428f.webp" alt="CAT 428F" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Экскаватор-погрузчик CAT 428F</h3>
                                <div class="card__price">от 2 900 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 3. XCMG -->
                        <article class="card js-open-modal" data-category="loaders planning" 
                            data-model="Фронтальный погрузчик XCMG" 
                            data-price="от 2 600 ₽/ч" 
                            data-img="assets/images/fleet/loader-xcmg-lw300.webp" 
                            data-specs='{"Объем ковша":"1.8 м³","Грузоподъемность":"3 т","Назначение":"Сыпучие материалы"}' 
                            data-ideal='["Погрузка песка, щебня, грунта", "Перемещение масс грунта", "Снежные отвалы"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/loader-xcmg-lw300.webp" alt="XCMG LW300" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Фронтальный погрузчик XCMG</h3>
                                <div class="card__price">от 2 600 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 4. Bobcat -->
                        <article class="card js-open-modal" data-category="loaders narrow planning" 
                            data-model="Мини-погрузчик Bobcat S530" 
                            data-price="от 2 400 ₽/ч" 
                            data-img="assets/images/fleet/loader-bobcat-s530.webp" 
                            data-specs='{"Грузоподъемность":"869 кг","Ширина":"1.7 м","Навесное":"щетка, вилы, ковш"}' 
                            data-ideal='["Работа в стесненных условиях", "Уборка узких проездов и дворов", "Демонтаж внутри помещений"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/loader-bobcat-s530.webp" alt="Bobcat S530" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Мини-погрузчик Bobcat S530</h3>
                                <div class="card__price">от 2 400 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 5. Doosan 22т -->
                        <article class="card js-open-modal" data-category="excavators pits" 
                            data-model="Гусеничный экскаватор Doosan (22 т)" 
                            data-price="от 3 500 ₽/ч" 
                            data-img="assets/images/fleet/excavator-doosan-225.webp" 
                            data-specs='{"Ковш":"1.2 м³","Глубина копания":"6.6 м","Масса":"22 т"}' 
                            data-ideal='["Разработка тяжелых грунтов", "Рытье глубоких котлованов", "Демонтаж конструкций"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/excavator-doosan-225.webp" alt="Doosan 225" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Гусеничный экскаватор Doosan (22 т)</h3>
                                <div class="card__price">от 3 500 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 6. Hitachi 330 -->
                        <article class="card js-open-modal" data-category="excavators pits" 
                            data-model="Гусеничный экскаватор Hitachi 330" 
                            data-price="от 4 200 ₽/ч" 
                            data-img="assets/images/fleet/excavator-hitachi-330.webp" 
                            data-specs='{"Масса":"33 т","Ковш":"1.6 м³","Глубина копания":"7.4 м"}' 
                            data-ideal='["Крупномасштабные земляные работы", "Карьерные работы", "Глубокие котлованы"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/excavator-hitachi-330.webp" alt="Hitachi 330" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Гусеничный экскаватор Hitachi 330</h3>
                                <div class="card__price">от 4 200 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 7. Hyundai 140w -->
                        <article class="card js-open-modal" data-category="excavators trenches pits" 
                            data-model="Колесный экскаватор Hyundai 140w" 
                            data-price="от 3 300 ₽/ч" 
                            data-img="assets/images/fleet/excavator-hyundai-140w.webp" 
                            data-specs='{"Масса":"14 т","Ковш":"0.6 м³","Шасси":"колесное"}' 
                            data-ideal='["Работа в городских условиях", "Раскопка коммуникаций", "Частые перемещения по асфальту"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/excavator-hyundai-140w.webp" alt="Hyundai 140w" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Колесный экскаватор Hyundai 140w</h3>
                                <div class="card__price">от 3 300 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 8. Kubota 3.5t -->
                        <article class="card js-open-modal" data-category="excavators narrow trenches" 
                            data-model="Мини-экскаватор Kubota (3.5 т)" 
                            data-price="от 2 500 ₽/ч" 
                            data-img="assets/images/fleet/excavator-kubota-3-5t.webp" 
                            data-specs='{"Гусеницы":"резиновые","Глубина копания":"3.2 м","Ширина":"1.5 м"}' 
                            data-ideal='["Работа на газонах и плитке", "Копка траншей в узких местах", "Установка септиков"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/excavator-kubota-3-5t.webp" alt="Kubota 3.5т" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Мини-экскаватор Kubota (3.5 т)</h3>
                                <div class="card__price">от 2 500 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                    </div>
                    <button class="carousel-btn carousel-btn--next" id="carousel-next" aria-label="Следующие">▶</button>
                </div>
"""

html = re.sub(r'<!-- Фильтры -->.*?<button class="carousel-btn carousel-btn--next" id="carousel-next" aria-label="Следующие">▶</button>\s*</div>', fleet_replacement, html, flags=re.DOTALL)

faq_form_replacement = """
        <!-- Секция 5: Факты -->
        <section id="facts" class="facts section hero--industrial text-white">
            <div class="container">
                <h2 class="section__title text-center" style="color: #fff;">Мы не диспетчеры. Мы собственники.</h2>
                <div class="fact-grid">
                    <div class="fact-item">
                        <div class="fact-item__val">14</div>
                        <div class="fact-item__lbl">Единиц техники в парке</div>
                    </div>
                    <div class="fact-item">
                        <div class="fact-item__val">2018</div>
                        <div class="fact-item__lbl">Год основания компании</div>
                    </div>
                    <div class="fact-item">
                        <div class="fact-item__val">0 ₽</div>
                        <div class="fact-item__lbl">Наценок посредников</div>
                    </div>
                    <div class="fact-item">
                        <div class="fact-item__val">100%</div>
                        <div class="fact-item__lbl">Машин с пройденным ТО</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Блок FAQ -->
        <section class="section faq-section bg-light">
            <div class="container">
                <h2 class="section__title text-center">Частые вопросы</h2>
                <div class="faq-list">
                    <div class="faq-item">
                        <button class="faq-btn">Топливо включено? <span class="faq-icon">+</span></button>
                        <div class="faq-content">
                            <p>Да, вся наша техника сдается в аренду с уже включенным топливом (ГСМ) и услугами опытного оператора. Никаких доплат на объекте.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-btn">Какие способы оплаты? <span class="faq-icon">+</span></button>
                        <div class="faq-content">
                            <p>Мы работаем с юридическими лицами (с НДС и без НДС) по безналичному расчету с предоставлением закрывающих документов (ЭДО). Для физических лиц доступна оплата наличными или переводом.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-btn">Сколько ждать подачу? <span class="faq-icon">+</span></button>
                        <div class="faq-content">
                            <p>Если машина свободна, подача по городу Омск занимает от 2 часов. Для доставки тяжелой гусеничной техники (габарит/негабарит) мы используем собственный трал.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-btn">Работаете с оператором? <span class="faq-icon">+</span></button>
                        <div class="faq-content">
                            <p>Вся техника предоставляется исключительно с нашим экипажем. Опыт машинистов позволяет выполнять ювелирные задачи и работать на сложных грунтах.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Простая форма захвата перед подвалом -->
        <section class="section cta-section">
            <div class="container">
                <div class="simple-lead-card">
                    <div class="simple-lead-card__text">
                        <h2>Остались вопросы?</h2>
                        <p>Оставьте номер, обсудим задачу напрямую. Без менеджеров-посредников.</p>
                    </div>
                    <form class="simple-form" id="bottom-form">
                        <input type="tel" name="phone_simple" id="bottom-phone" class="form-control" placeholder="+7 (___) ___-__-__" required>
                        <button type="submit" class="btn btn-primary">Позвонить мне</button>
                    </form>
                </div>
            </div>
        </section>

    </main>

    <!-- Модальное окно Карточки -->
    <div class="modal" id="equipment-modal">
        <div class="modal__overlay" id="modal-overlay"></div>
        <div class="modal__content">
            <button class="modal__close" id="modal-close">×</button>
            <div class="modal__body" id="modal-body">
                <!-- Контент инжектится через JS -->
            </div>
        </div>
    </div>
"""

html = re.sub(r'<!-- Секция 5: Факты -->.*?</section>\s*</main>', faq_form_replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
