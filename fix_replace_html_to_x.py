import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("done")
