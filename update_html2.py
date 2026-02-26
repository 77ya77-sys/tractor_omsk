import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tabs_replacement = """
                <!-- Фильтры -->
                <div class="fleet__filters">
                    <!-- Ряд 1: Тип техники -->
                    <div class="fleet__tabs fleet__tabs--types" id="fleet-tabs-type">
                        <button class="tab-btn active" data-type="all">Вся техника</button>
                        <button class="tab-btn" data-type="excavators">Экскаваторы</button>
                        <button class="tab-btn" data-type="loaders">Погрузчики</button>
                        <button class="tab-btn" data-type="dump_trucks">Самосвалы</button>
                        <button class="tab-btn" data-type="manipulators">Манипуляторы</button>
                        <button class="tab-btn" data-type="tractors">Тракторы</button>
                    </div>
                    <!-- Ряд 2: Задачи (JTBD) -->
                    <div class="fleet__tabs fleet__tabs--jtbd" id="fleet-tabs-jtbd">
                        <button class="jtbd-pill active" data-task="all">Все задачи</button>
                        <button class="jtbd-pill" data-task="trenches">Копка траншей</button>
                        <button class="jtbd-pill" data-task="pits">Котлованы</button>
                        <button class="jtbd-pill" data-task="narrow">Узкий проезд</button>
                        <button class="jtbd-pill" data-task="planning">Планировка участка</button>
                        <button class="jtbd-pill" data-task="demolition">Демонтаж</button>
                    </div>
                </div>
"""

html = re.sub(r'<!-- Фильтры \(JTBD\) -->.*?</div>', tabs_replacement, html, flags=re.DOTALL)

# Add missing articles
missing_articles = """
                        <!-- 9. Самосвал КАМАЗ 15т -->
                        <article class="card js-open-modal" data-category="dump_trucks" 
                            data-model="Самосвал КАМАЗ 65115 (15 т)" 
                            data-price="от 2 000 ₽/ч" 
                            data-img="assets/images/fleet/dump-truck-kamaz-15t.webp" 
                            data-specs='{"Грузоподъемность":"15 т","Объем кузова":"10 м³"}' 
                            data-ideal='["Вывоз строительного мусора", "Доставка грунта", "Вывоз снега"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/dump-truck-kamaz-15t.webp" alt="КАМАЗ 15т" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Самосвал КАМАЗ 65115 (15 т)</h3>
                                <div class="card__price">от 2 000 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 10. Самосвал КАМАЗ 20т -->
                        <article class="card js-open-modal" data-category="dump_trucks" 
                            data-model="Самосвал КАМАЗ 6520 (20 т)" 
                            data-price="от 2 200 ₽/ч" 
                            data-img="assets/images/fleet/dump-truck-kamaz-20t.webp" 
                            data-specs='{"Грузоподъемность":"20 т","Объем кузова":"12 м³"}' 
                            data-ideal='["Повышенная грузоподъемность", "Сыпучие грузы", "Массовый вывоз"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/dump-truck-kamaz-20t.webp" alt="КАМАЗ 20т" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Самосвал КАМАЗ 6520 (20 т)</h3>
                                <div class="card__price">от 2 200 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 11. Shacman 25т -->
                        <article class="card js-open-modal" data-category="dump_trucks" 
                            data-model="Самосвал Shacman (25 т)" 
                            data-price="от 2 500 ₽/ч" 
                            data-img="assets/images/fleet/dump-truck-shacman-25t.webp" 
                            data-specs='{"Грузоподъемность":"25 т","Объем кузова":"19 м³"}' 
                            data-ideal='["Масштабные выработки", "Крупные стройки"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/dump-truck-shacman-25t.webp" alt="Shacman 25т" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Самосвал Shacman (25 т)</h3>
                                <div class="card__price">от 2 500 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 12. Манипулятор Isuzu 5т -->
                        <article class="card js-open-modal" data-category="manipulators" 
                            data-model="КМУ Isuzu (Борт 5т / Стрела 3т)" 
                            data-price="от 2 300 ₽/ч" 
                            data-img="assets/images/fleet/manipulator-isuzu-5t.webp" 
                            data-specs='{"Борт":"5 тонн, длина 6 м","Стрела":"3 тонны, вылет 8 м"}' 
                            data-ideal='["Стройматериалы", "Бытовки"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/manipulator-isuzu-5t.webp" alt="Isuzu 5т" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">КМУ Isuzu (Борт 5т / Стрела 3т)</h3>
                                <div class="card__price">от 2 300 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 13. Манипулятор КАМАЗ 7т -->
                        <article class="card js-open-modal" data-category="manipulators" 
                            data-model="КМУ КАМАЗ 43118 (Вездеход)" 
                            data-price="от 3 000 ₽/ч" 
                            data-img="assets/images/fleet/manipulator-kamaz-kmu.webp" 
                            data-specs='{"Борт":"10 тонн, длина 6.2 м","Стрела":"7 тонн, вылет 19 м"}' 
                            data-ideal='["Сложные грунты", "Бездорожье"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/manipulator-kamaz-kmu.webp" alt="КАМАЗ КМУ" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">КМУ КАМАЗ 43118 (Вездеход)</h3>
                                <div class="card__price">от 3 000 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>

                        <!-- 14. МТЗ 82.1 -->
                        <article class="card js-open-modal" data-category="tractors planning" 
                            data-model="Колесный трактор МТЗ 82.1" 
                            data-price="от 2 200 ₽/ч" 
                            data-img="assets/images/fleet/tractor-mtz-82-1.webp" 
                            data-specs='{"Масса":"4 т","Навесное":"Щетка, отвал, ковш"}' 
                            data-ideal='["Уборка снега", "Планировка"]'>
                            <div class="card__photo">
                                <div class="card__status">Свободен</div>
                                <img src="assets/images/fleet/tractor-mtz-82-1.webp" alt="МТЗ 82.1" class="card__img" loading="lazy">
                            </div>
                            <div class="card__content card__content--minimal">
                                <h3 class="card__title">Колесный трактор МТЗ 82.1</h3>
                                <div class="card__price">от 2 200 ₽/ч</div>
                                <button class="btn btn-primary btn-block btn--small card__cta">Рассчитать</button>
                            </div>
                        </article>
"""

html = html.replace('<!-- 8. Kubota 3.5t -->', missing_articles + '\n                        <!-- 8. Kubota 3.5t -->')

# Add demolition to some excavators
html = html.replace('data-category="loaders narrow planning"', 'data-category="loaders narrow planning demolition"')
html = html.replace('data-category="excavators pits"', 'data-category="excavators pits demolition"')

# Replace tractor icon with SVG
truck_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="var(--color-primary)" class="metric__icon-svg">
<path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM17 12V3h-2v9h2z"/>
</svg>'''
html = html.replace('<span class="metric__icon">🚛</span>', f'<span class="metric__icon">{truck_svg}</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
