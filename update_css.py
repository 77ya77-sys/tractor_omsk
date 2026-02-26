import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove jtbd styling
css = re.sub(r'\.jtbd-pill.*?font-weight: 600;\n}', '', css, flags=re.DOTALL)

# Delete scrollbar hiding for smooth standard scrolling
# We leave width:100% and overflow-x: auto so it still scrolls, 
# but no more strict scroll anchoring or snapping that might break smooth wheel scroll.
css = re.sub(r'scroll-snap-type: x mandatory;\n\s*scroll-behavior: smooth;', '', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
