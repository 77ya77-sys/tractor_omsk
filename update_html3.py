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
                </div>
"""

html = re.sub(r'<!-- Фильтры -->.*?</div>\s*</div>\s*<div class="carousel-wrapper">', tabs_replacement + '\n                <div class="carousel-wrapper">', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
