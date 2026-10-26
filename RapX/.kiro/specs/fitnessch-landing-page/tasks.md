# Implementation Plan: FitnessCh Landing Page

## Overview

Build a Flask app (`app.py`, port 8009) that serves a single dark-themed hero page reproducing the reference screenshot. Work proceeds from the Flask scaffold → base HTML → CSS tokens and stage layout → each visual section in turn → button wiring → tests → run on port 8009. Language: Python (backend), HTML/CSS/vanilla JS (frontend). Use the venv at `/home/rishab/Videos/RapX/venv`.

## Tasks

- [x] 1. Scaffold the Flask project
  - [x] 1.1 Create `requirements.txt` with `Flask>=3,<4` and `requirements-dev.txt` with `pytest`; install both into the venv
    - _Requirements: 13.1_
  - [x] 1.2 Create `app.py` with the Flask app, `GET /` rendering `index.html`, `GET /health` returning `{"status": "ok"}`, `POST /api/book` returning `{"message": ...}` tolerant of missing/invalid JSON, and `app.run(host="0.0.0.0", port=8009, debug=True)` under `__main__`
    - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5, 11.6_
  - [x] 1.3 Create directories `templates/`, `static/css/`, `static/js/`, `static/img/`, `tests/`
    - _Requirements: 12.1_
  - [ ]* 1.4 Write backend tests in `tests/test_app.py` for `/`, `/health`, `/api/book` (empty body, `{"name":"Sam"}`, invalid JSON), unknown path → 404, and a static check that `app.py` contains `port=8009` and `host="0.0.0.0"`
    - _Requirements: 11.2, 11.3, 11.4, 11.5, 11.6_

- [x] 2. Create the base HTML template
  - [x] 2.1 Write `templates/index.html` with `<head>` (charset, viewport, title, Google Fonts Poppins 400/500/600/700 with preconnect, `url_for` link to `css/style.css`) and a `<main class="stage">` containing the empty section skeleton: `.nav`, `.headline`, `.model`, `.social`, `.tagline`, `.stats`, `.cta`; include the deferred `url_for` script tag for `js/main.js`
    - _Requirements: 9.1, 12.4_
  - [x] 2.2 Generate placeholder images with a standard-library Python script (`zlib`/`struct`): `static/img/model.png` (400×520 dark red→black vertical gradient) and `static/img/avatar-1.png`, `avatar-2.png`, `avatar-3.png` (48×48 flat grey)
    - _Requirements: 4.1, 7.5, 12.3_

- [x] 3. Write CSS tokens, background, and stage layout
  - [x] 3.1 In `static/css/style.css` define `:root` tokens (`--bg #0B0B14`, `--bg-edge #000000`, `--text #FFFFFF`, `--text-muted #C9C9D1`, `--headline-top #FFFFFF`, `--headline-bot #B5B5BD`, `--accent #2CFF2C`, `--accent-ring #2DFF2D`, `--btn-text #000000`, `--line #FFFFFF`, `--font-heading`, `--font-body`)
    - _Requirements: 1.1, 1.4, 9.2_
  - [x] 3.2 Add reset, `body` background (`--bg` with radial darkening to `--bg-edge`), `overflow: hidden`, body font, and `.stage` (relative, 1024px wide, 100vh tall, centered, overflow hidden)
    - _Requirements: 1.1, 1.2, 1.3_

- [x] 4. Implement the navigation bar and logo
  - [x] 4.1 Fill `.nav` in `index.html` with the `FitnessCh` logo (`Fitness<span>Ch</span>`) and the five links Home, About, How It Works, Results, Testimonials
    - _Requirements: 2.1, 2.3_
  - [x] 4.2 Style `.nav` (absolute, top 36px, left/right 60px, flex space-between), `.logo` (28px, weight 700, white, `span` weight 500), `.nav__links a` (14px, `--text-muted`, 40px gap, no underline, hover → `--text`)
    - _Requirements: 2.1, 2.2, 2.4, 2.5, 2.6_

- [x] 5. Implement the hero headline
  - [x] 5.1 Add `<h1 class="headline">Reach Your Best<br>Shape for Life</h1>` and style it: absolute top 110px, full width centered, `700 104px/0.95 var(--font-heading)`, `letter-spacing: -0.03em`, vertical gradient text fill from `--headline-top` to `--headline-bot` via `background-clip: text`, `z-index: 1`
    - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.6_

- [x] 6. Implement the model image
  - [x] 6.1 Add `<img class="model" src="{{ url_for('static', filename='img/model.png') }}" alt="" aria-hidden="true">` and style it: absolute top 200px, centered via `left:50%; translateX(-50%)`, width 400px, height `calc(100vh - 200px)`, `object-fit: cover; object-position: top`, `z-index: 2`, and the combined bottom + side fade `mask-image` (with `-webkit-` prefixes and `mask-composite: intersect`)
    - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_

- [x] 7. Implement the social column
  - [x] 7.1 Fill `.social` with three `<a>` links carrying `aria-label` YouTube, Facebook, Instagram, each wrapping an inline SVG (`fill="currentColor"`), followed by `<span class="social__line">`
    - _Requirements: 5.1, 5.5_
  - [x] 7.2 Style `.social` (absolute, left 68px, top 285px, `translateX(-50%)`, flex column, white, icons 20px, gap so centers land at 295/365/435px), `.social__line` (1px × 60px, `--line`, top edge at 465px), `z-index: 3`
    - _Requirements: 5.2, 5.3, 5.4_

- [x] 8. Implement the tagline
  - [x] 8.1 Add `<p class="tagline">` with the copy "Get stronger, leaner, and more energized with custom fitness and nutrition coaching that fits your lifestyle" and style it: absolute left 697px, top 355px, max-width 260px, 14px / 20px, `--text-muted`, `z-index: 3`
    - _Requirements: 6.1, 6.2, 6.3, 6.4_

- [x] 9. Implement the client stats block
  - [x] 9.1 Fill `.stats` with `.stats__avatars` (three `url_for` avatar `<img>`s) and `.stats__text` (`<span class="stats__num">1.2k</span><span class="stats__label">Happy Clients</span>`)
    - _Requirements: 7.3, 7.5_
  - [x] 9.2 Style `.stats` (absolute left 60px, top 590px, `z-index: 3`), avatars (48×48, `border-radius: 50%`, 2px solid `--accent-ring`, `margin-left: -16px` except first), `.stats__text` (flex, `align-items: baseline`, gap 10px), `.stats__num` (40px, 700, heading font, white), `.stats__label` (14px, white)
    - _Requirements: 7.1, 7.2, 7.3, 7.4_

- [x] 10. Implement the BOOK A CLASS button and API wiring
  - [x] 10.1 Fill `.cta` with `<button class="btn-book" type="button">Book a Class</button>` and `<p class="cta__msg" role="status" aria-live="polite"></p>`; style `.btn-book` (absolute left 755px, top 625px, 150×44px, `border-radius: 22px`, `--accent` background, `--btn-text`, `700 13px`, uppercase, no border, green `box-shadow` glow, `z-index: 3`) and `.cta__msg` (below the button, 12px, `--text-muted`)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 10.2 Write `static/js/main.js`: on `.btn-book` click, `fetch("/api/book", {method:"POST", headers JSON, body "{}"})`, write `data.message` into `.cta__msg`, and show a fallback message on network error
    - _Requirements: 8.6, 11.5_

- [x] 11. Add the narrow-viewport fallback
  - [x] 11.1 Add `@media (max-width: 1023px)` to `style.css`: `body { overflow: auto }`, `.stage` becomes a full-width flex column with padding and gap, all children `position: static; transform: none`, ordering nav → headline → model → tagline → stats → cta, `.headline { font-size: 48px }`, `.model` fluid up to 400px, `.social { display: none }`
    - _Requirements: 10.1, 10.2, 10.3, 10.4_

- [x] 12. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 13. Static content tests and documentation
  - [ ]* 13.1 Extend `tests/test_app.py` with checks that `GET /` HTML contains `FitnessCh`, `Reach Your Best`, `Shape for Life`, the five nav links in order, the three social `aria-label`s in order, and `url_for`-generated `/static/css/style.css` and `/static/img/model.png` paths; that `/static/css/style.css` returns `text/css` and `/static/img/model.png` returns `image/png`
    - _Requirements: 2.3, 3.1, 5.1, 5.5, 12.2, 12.3, 12.4_
  - [ ]* 13.2 Add tests asserting `style.css` contains the token values (`--bg: #0B0B14`, `--accent: #2CFF2C`, `--accent-ring: #2DFF2D`, `--text-muted: #C9C9D1`, `--headline-bot: #B5B5BD`), `font-size: 104px`, `line-height: 0.95`, `letter-spacing: -0.03em`, `width: 400px`, `width: 150px`, `height: 44px`, and a `@media (max-width: 1023px)` block containing `font-size: 48px`
    - _Requirements: 1.1, 1.4, 3.3, 4.2, 7.2, 8.2, 8.3, 10.3_
  - [x] 13.3 Write `README.md` at the repo root: venv creation, `pip install -r requirements.txt`, `python app.py`, the URL `http://localhost:8009`, how to replace `static/img/model.png` with the real photo, how to run tests, and a note about freeing port 8009 if it is in use
    - _Requirements: 13.2, 13.3_

- [x] 14. Final checkpoint - Run the server and verify
  - Start `python app.py` in a background process, confirm `GET http://localhost:8009/` and `/health` return 200 via `curl`, then stop the process. Ensure all tests pass, ask the user if questions arise (including visual comparison of `http://localhost:8009` at 1024×720 against the reference screenshot).
  - _Requirements: 11.2, 11.3, 11.4_

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- No property-based tests: the design has no Correctness Properties section (UI rendering plus trivial routes)
- Pixel values are tuned for a 1024px-wide stage; the user supplies the real model photo at `static/img/model.png` for exact visual parity
