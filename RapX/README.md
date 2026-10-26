# FitnessCh Landing Page

A single-page, dark-themed fitness hero page ("Reach Your Best Shape for Life") served by a minimal Flask app. No database, no sessions. The only dynamic pieces are `POST /api/book` (called by the **Book a Class** button) and a `GET /health` probe.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open <http://localhost:8009>. The layout is tuned for a 1024px-wide desktop window; narrower viewports fall back to a stacked layout.

`app.py` runs with `debug=True`, which is for local development only. Turn it off (or run behind a WSGI server such as gunicorn) before exposing the app to anyone else.

### Port 8009 already in use

If `python app.py` fails with "Address already in use", either free the port:

```bash
lsof -i :8009          # see what owns it
fuser -k 8009/tcp      # kill it
```

or change the `port=8009` argument to `app.run(...)` at the bottom of `app.py`.

## Images

The shipped images are generated placeholders:

- `static/img/model.png` – the hero photo (400×520 gradient with a silhouette)
- `static/img/avatar-1.png`, `avatar-2.png`, `avatar-3.png` – 48×48 flat grey client avatars

To use real photos, overwrite those files keeping the same names. A portrait-oriented PNG around 400px wide works best for `model.png`; the CSS mask fades its bottom and side edges into the background, so no editing is needed. Avatars are shown as 48px circles, so square images are ideal.

To regenerate the placeholders:

```bash
python scripts/make_placeholders.py
```

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

## Project layout

```
app.py                      Flask app (routes: /, /health, /api/book)
templates/index.html        page template
static/css/style.css        color tokens, layout, narrow-viewport fallback
static/js/main.js           Book a Class button handler
static/img/                 model photo and avatars
scripts/make_placeholders.py  placeholder image generator
tests/                      pytest suite
```
