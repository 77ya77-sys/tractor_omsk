# Артефакты по задаче: Переработка секции каталога (Автопарк)

## 1. Task List (План задач)
- [x] Анализ текущей верстки и стилей (определение конфликтов классов).
- [x] Обновление HTML-разметки: замена старой сетки `.fleet__grid` на карусель (`.carousel-wrapper > .carousel-track`).
- [x] Замена кнопок фильтров в HTML (с `filter-btn` на `tab-btn`) для синхронизации с CSS и JS-логикой.
- [x] Внедрение реалистичных placeholder-изображений спецтехники с платформы LoremFlickr на базе ключевых слов (запрет ИИ и пустых квадратов).
- [x] Обновление карточек: интеграция цены и кнопки "Рассчитать" в единый подвал карточки `.card__footer`.
- [x] Проверка JS-логики свайпера и табов (гарантия точного скролла и корректного скрытия/показа табов).

## 2. Implementation Plan (План внедрения)
**Технологический стек**: `HTML5`, `CSS3` (индустриальный стиль), `Vanilla JS`.

**Архитектурные решения**:
- **Разметка табов**: Адаптирован `<div class="fleet__tabs">`. Классы кнопок заменены на `.tab-btn` со встроенным `data-filter`.
- **Логика карусели**: Внедрен переполненный flex-контейнер (`overflow-x: auto`), использующий `scroll-snap-type` для плавного позиционирования карточек на мобильных и десктоп устройствах. 
- **Карточки (Cards)**: Flex-карточки, принимающие ширину в процентах (`flex: 0 0 X%`) в зависимости от `@media` запросов.
- **Интерактивность**: В VanillaJS реализовано управление скроллом кнопками (prev/next) с пересчетом `scrollLeft` и обновлением видимости кнопок навигации карусели.
- **Изображения**: Прямая привязка к тематическим фотостокам с параметризацией запросов `https://loremflickr.com/600/400/...`. Гарантия реальных фотографий для каждой категории (экскаваторы, погрузчики, самосвалы, манипуляторы, тракторы).

## 3. Code Diffs & Placeholders

### Разметка карусели (index.html, Секция 3)
```diff
- <div class="fleet__filters" id="fleet-filters">
-     <button class="filter-btn active" data-filter="all">Вся техника (14)</button>
+ <div class="fleet__tabs" id="fleet-tabs">
+     <button class="tab-btn active" data-filter="all">Вся техника (14)</button>
```

```diff
- <div class="fleet__grid" id="fleet-grid">
+ <div class="carousel-wrapper">
+     <button class="carousel-btn carousel-btn--prev" id="carousel-prev" aria-label="Предыдущие">◀</button>
+     <div class="carousel-track" id="fleet-track">
```

### Подвал карточки с кнопкой 'Рассчитать' (index.html)
```diff
- <div class="card__price">от 2 800 ₽/ч</div>
+ <div class="card__footer">
+     <div class="card__price">от 2 800 ₽/ч</div>
+     <a href="#quiz-section" class="btn btn-primary btn--small">Рассчитать</a>
+ </div>
```

### Ссылки на внедренные фото-плейсхолдеры
Для подбора изображений, полностью соответствующих реализму, использовался сервис **LoremFlickr** с конкретными тематическими тегами индустрии:
1. `https://loremflickr.com/600/400/backhoe,jcb/all` (Экскаватор-погрузчик JCB)
2. `https://loremflickr.com/600/400/caterpillar,backhoe/all` (CAT)
3. `https://loremflickr.com/600/400/frontloader,construction/all` (XCMG)
4. `https://loremflickr.com/600/400/skidsteer,bobcat/all` (Bobcat)
5. `https://loremflickr.com/600/400/excavator,doosan/all` (Гусеничный Doosan)
6. `https://loremflickr.com/600/400/excavator,hitachi/all` (Hitachi 330)
7. `https://loremflickr.com/600/400/wheeled,excavator/all` (Колесный Hyundai)
8. `https://loremflickr.com/600/400/miniexcavator/all` (Kubota 3.5т)
9. `https://loremflickr.com/600/400/dumptruck,kamaz/all` (Самосвал КАМАЗ 15т)
10. `https://loremflickr.com/600/400/dumptruck,construction/all` (Самосвал КАМАЗ 20т)
11. `https://loremflickr.com/600/400/tippertruck/all` (Самосвал Shacman)
12. `https://loremflickr.com/600/400/crane,truck/all` (Манипулятор Isuzu)
13. `https://loremflickr.com/600/400/kamaz,crane/all` (Манипулятор КАМАЗ КМУ)
14. `https://loremflickr.com/600/400/tractor,mtz/all` (Трактор МТЗ)
