import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace filters with tabs
content = re.sub(
    r'<div class="fleet__filters" id="fleet-filters">.*?</div>',
    '''<div class="fleet__tabs" id="fleet-tabs">
                    <button class="tab-btn active" data-filter="all">Вся техника (14)</button>
                    <button class="tab-btn" data-filter="excavators">Экскаваторы (4)</button>
                    <button class="tab-btn" data-filter="loaders">Погрузчики (4)</button>
                    <button class="tab-btn" data-filter="dump_trucks">Самосвалы (3)</button>
                    <button class="tab-btn" data-filter="manipulators">Манипуляторы (2)</button>
                    <button class="tab-btn" data-filter="tractors">Тракторы (1)</button>
                </div>''',
    content,
    flags=re.DOTALL
)

# Replace fleet__grid with carousel track wrapper
content = content.replace('<div class="fleet__grid" id="fleet-grid">', '''<div class="carousel-wrapper">
                    <button class="carousel-btn carousel-btn--prev" id="carousel-prev" aria-label="Предыдущие">◀</button>
                    <div class="carousel-track" id="fleet-track">''')

# Now add closing div and next button
content = content.replace('''                </div>
            </div>
        </section>

        <!-- Секция 4: Процесс работы -->''', '''                    </div>
                    <button class="carousel-btn carousel-btn--next" id="carousel-next" aria-label="Следующие">▶</button>
                </div>
            </div>
        </section>

        <!-- Секция 4: Процесс работы -->''')

# Update images
images_mapping = [
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=JCB+3CX', 'https://loremflickr.com/600/400/backhoe,jcb/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=CAT+428F', 'https://loremflickr.com/600/400/caterpillar,backhoe/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=XCMG+LW300', 'https://loremflickr.com/600/400/frontloader,construction/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Bobcat+S530', 'https://loremflickr.com/600/400/skidsteer,bobcat/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Doosan+225', 'https://loremflickr.com/600/400/excavator,doosan/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Hitachi+330', 'https://loremflickr.com/600/400/excavator,hitachi/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Hyundai+140w', 'https://loremflickr.com/600/400/wheeled,excavator/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Kubota+3.5t', 'https://loremflickr.com/600/400/miniexcavator/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=KAMAZ+15t', 'https://loremflickr.com/600/400/dumptruck,kamaz/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=KAMAZ+20t', 'https://loremflickr.com/600/400/dumptruck,construction/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Shacman+25t', 'https://loremflickr.com/600/400/tippertruck/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=Isuzu+5t', 'https://loremflickr.com/600/400/crane,truck/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=KAMAZ+KMU', 'https://loremflickr.com/600/400/kamaz,crane/all'),
    ('https://placehold.co/600x400/1A1A1A/FFC107?text=MTZ+82.1', 'https://loremflickr.com/600/400/tractor,mtz/all')
]

for old, new in images_mapping:
    content = content.replace(old, new)


# Update prices to include footer and button
# Each ends like this:
#                             <div class="card__price">от XXX ₽/ч</div>
#                         </div>
#                     </article>
import re
content = re.sub(
    r'<div class="card__price">(.*?)</div>\s*</div>\s*</article>',
    r'''<div class="card__footer">
                                <div class="card__price">\1</div>
                                <a href="#quiz-section" class="btn btn-primary btn--small">Рассчитать</a>
                            </div>
                        </div>
                    </article>''',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done index.html")
