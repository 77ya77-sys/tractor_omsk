import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace images
replacements = [
    ('https://loremflickr.com/600/400/backhoe,jcb/all', 'assets/images/fleet/loader-jcb-3cx.webp'),
    ('https://loremflickr.com/600/400/caterpillar,backhoe/all', 'assets/images/fleet/loader-cat-428f.webp'),
    ('https://loremflickr.com/600/400/frontloader,construction/all', 'assets/images/fleet/loader-xcmg-lw300.webp'),
    ('https://loremflickr.com/600/400/skidsteer,bobcat/all', 'assets/images/fleet/loader-bobcat-s530.webp'),
    ('https://loremflickr.com/600/400/excavator,doosan/all', 'assets/images/fleet/excavator-doosan-225.webp'),
    ('https://loremflickr.com/600/400/excavator,hitachi/all', 'assets/images/fleet/excavator-hitachi-330.webp'),
    ('https://loremflickr.com/600/400/wheeled,excavator/all', 'assets/images/fleet/excavator-hyundai-140w.webp'),
    ('https://loremflickr.com/600/400/miniexcavator/all', 'assets/images/fleet/excavator-kubota-3-5t.webp'),
    ('https://loremflickr.com/600/400/dumptruck,kamaz/all', 'assets/images/fleet/dump-truck-kamaz-15t.webp'),
    ('https://loremflickr.com/600/400/dumptruck,construction/all', 'assets/images/fleet/dump-truck-kamaz-20t.webp'),
    ('https://loremflickr.com/600/400/tippertruck/all', 'assets/images/fleet/dump-truck-shacman-25t.webp'),
    ('https://loremflickr.com/600/400/crane,truck/all', 'assets/images/fleet/manipulator-isuzu-5t.webp'),
    ('https://loremflickr.com/600/400/kamaz,crane/all', 'assets/images/fleet/manipulator-kamaz-kmu.webp'),
    ('https://loremflickr.com/600/400/tractor,mtz/all', 'assets/images/fleet/tractor-mtz-82-1.webp')
]

for old, new in replacements:
    content = content.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
