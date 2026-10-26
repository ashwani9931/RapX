# Requirements Document

## Introduction

FitnessCh Landing Page is a single-page, dark-themed fitness hero page that reproduces a reference screenshot as closely as possible (same background, logo, colors, typography, and element positions). The page is served by a Flask application (`app.py`) listening on port 8009. The scope is one static view with a small Flask backend; no authentication, database, or multi-page navigation is included.

## Glossary

- **Landing_Page**: The single HTML page rendered at `/`, consisting of the Nav_Bar, Hero_Headline, Model_Image, Social_Column, Tagline, Client_Stats, and Book_Button.
- **Flask_Server**: The Python Flask application defined in `app.py` at the repository root.
- **Nav_Bar**: The top row of the Landing_Page containing the Logo on the left and five navigation links on the right.
- **Logo**: The text mark "FitnessCh" at the top-left of the Landing_Page.
- **Hero_Headline**: The two-line centered headline "Reach Your Best" / "Shape for Life".
- **Model_Image**: The centered image of a fitness model whose edges blend into the page background.
- **Social_Column**: The vertical stack of YouTube, Facebook, and Instagram icons plus a thin vertical line on the left edge of the Landing_Page.
- **Tagline**: The three-line grey paragraph on the right-middle of the Landing_Page.
- **Client_Stats**: The bottom-left group of three overlapping ring-bordered avatars and the "1.2k Happy Clients" text.
- **Book_Button**: The neon-green pill-shaped "BOOK A CLASS" button at the bottom-right of the Landing_Page.
- **Desktop_Viewport**: A browser viewport at least 1024px wide.
- **Narrow_Viewport**: A browser viewport narrower than 1024px.
- **Static_Asset**: Any file served under the `/static/` URL prefix (CSS, images, JavaScript).
- **Color_Token**: A named CSS custom property that holds a color value used by the Landing_Page.

## Requirements

### Requirement 1: Page Background and Theme

**User Story:** As a visitor, I want the page to have the same dark background as the reference, so that the page looks identical to the screenshot.

#### Acceptance Criteria

1. THE Landing_Page SHALL render a flat near-black navy background with the Color_Token `--bg` set to `#0B0B14`.
2. THE Landing_Page SHALL apply a subtle radial darkening toward the viewport edges using only the `--bg` color and black, with no visible color banding.
3. WHILE displayed on a Desktop_Viewport, THE Landing_Page SHALL occupy exactly 100vh in height and SHALL render without a vertical scrollbar.
4. THE Landing_Page SHALL define every color used by the page as a Color_Token in `static/css/style.css`.

### Requirement 2: Navigation Bar and Logo

**User Story:** As a visitor, I want to see the FitnessCh logo and navigation links at the top, so that the header matches the reference.

#### Acceptance Criteria

1. THE Nav_Bar SHALL display the Logo text "FitnessCh" in white (`#FFFFFF`) at a font size of 28px using the heading font family.
2. THE Nav_Bar SHALL position the Logo at the top-left of the Landing_Page with its left edge at 60px from the viewport left edge.
3. THE Nav_Bar SHALL display exactly five links in this order: "Home", "About", "How It Works", "Results", "Testimonials".
4. THE Nav_Bar SHALL render each link in light grey (`#C9C9D1`) at 14px with no text underline and a horizontal gap of 40px between adjacent links.
5. THE Nav_Bar SHALL place the links on the same horizontal row as the Logo, right-aligned with the row's right padding at 60px from the viewport right edge.
6. WHEN a visitor hovers over a Nav_Bar link, THE Nav_Bar SHALL change that link's color to white (`#FFFFFF`).

### Requirement 3: Hero Headline

**User Story:** As a visitor, I want a large gradient headline reading "Reach Your Best / Shape for Life", so that the page's main message matches the reference.

#### Acceptance Criteria

1. THE Hero_Headline SHALL display the text "Reach Your Best" on the first line and "Shape for Life" on the second line.
2. THE Hero_Headline SHALL be horizontally centered within the Landing_Page.
3. THE Hero_Headline SHALL use the heading font family at a font weight of 700, a font size of 104px, a letter spacing of -0.03em, and a line height of 0.95 on a Desktop_Viewport.
4. THE Hero_Headline SHALL fill its text with a vertical gradient from white (`#FFFFFF`) at the top to light grey (`#B5B5BD`) at the bottom.
5. THE Hero_Headline SHALL be stacked beneath the Model_Image so that the Model_Image overlaps the second headline line.
6. THE Hero_Headline SHALL position its top edge at 110px from the viewport top on a Desktop_Viewport.

### Requirement 4: Model Image

**User Story:** As a visitor, I want the central model photo to blend into the dark background, so that the composition matches the reference.

#### Acceptance Criteria

1. THE Landing_Page SHALL load the Model_Image from the Static_Asset path `/static/img/model.png`.
2. THE Model_Image SHALL be horizontally centered within the Landing_Page with a rendered width of 400px on a Desktop_Viewport.
3. THE Model_Image SHALL position its top edge at 200px from the viewport top and extend to the bottom edge of the Landing_Page on a Desktop_Viewport.
4. THE Model_Image SHALL fade to transparent along its bottom edge and left and right edges using a CSS mask so that no hard image border is visible against the background.
5. THE Model_Image SHALL be rendered above the Hero_Headline and below the Social_Column, Tagline, Client_Stats, and Book_Button in stacking order.
6. IF the file `/static/img/model.png` is missing, THEN THE Landing_Page SHALL render all other elements in their specified positions without layout shift.

### Requirement 5: Social Column

**User Story:** As a visitor, I want the vertical social icon column on the left, so that the side decoration matches the reference.

#### Acceptance Criteria

1. THE Social_Column SHALL display three icons in this top-to-bottom order: YouTube, Facebook, Instagram.
2. THE Social_Column SHALL render each icon in white (`#FFFFFF`) at a size of 20px.
3. THE Social_Column SHALL center the icons on a vertical axis 68px from the viewport left edge, with icon centers at 295px, 365px, and 435px from the viewport top on a Desktop_Viewport.
4. THE Social_Column SHALL display a white vertical line 1px wide and 60px tall, centered on the same vertical axis, with its top edge at 465px from the viewport top on a Desktop_Viewport.
5. THE Social_Column SHALL render each icon as a link element with an `aria-label` naming the platform.

### Requirement 6: Tagline

**User Story:** As a visitor, I want the short descriptive paragraph on the right, so that the supporting copy matches the reference.

#### Acceptance Criteria

1. THE Tagline SHALL display the text "Get stronger, leaner, and more energized with custom fitness and nutrition coaching that fits your lifestyle".
2. THE Tagline SHALL render in light grey (`#C9C9D1`) at 14px with a line height of 20px.
3. THE Tagline SHALL constrain its width to a maximum of 260px so that the text wraps onto three lines.
4. THE Tagline SHALL position its top-left corner at 697px from the viewport left edge and 355px from the viewport top on a Desktop_Viewport.

### Requirement 7: Client Stats

**User Story:** As a visitor, I want the client avatars and "1.2k Happy Clients" counter at the bottom-left, so that the social proof block matches the reference.

#### Acceptance Criteria

1. THE Client_Stats SHALL display three circular avatars, each 48px in diameter, overlapping horizontally by 16px.
2. THE Client_Stats SHALL render a 2px solid neon-green ring (`#2DFF2D`) around each avatar.
3. THE Client_Stats SHALL display the text "1.2k" in white (`#FFFFFF`) at 40px using the heading font family, with "Happy Clients" in white at 14px to its right, aligned on the same text baseline.
4. THE Client_Stats SHALL position its top-left corner at 60px from the viewport left edge and 590px from the viewport top on a Desktop_Viewport.
5. THE Client_Stats SHALL load avatar images from Static_Asset paths under `/static/img/`.

### Requirement 8: Book Button

**User Story:** As a visitor, I want a neon-green "BOOK A CLASS" button at the bottom-right, so that the call to action matches the reference.

#### Acceptance Criteria

1. THE Book_Button SHALL display the uppercase text "BOOK A CLASS" in black (`#000000`) at 13px with a font weight of 700.
2. THE Book_Button SHALL render a neon-green background using the Color_Token `--accent` set to `#2CFF2C`.
3. THE Book_Button SHALL be 150px wide and 44px tall with fully rounded corners (border radius of at least 22px).
4. THE Book_Button SHALL render a soft green glow using a box shadow derived from the `--accent` color.
5. THE Book_Button SHALL position its top-left corner at 755px from the viewport left edge and 625px from the viewport top on a Desktop_Viewport.
6. WHEN a visitor clicks the Book_Button, THE Landing_Page SHALL send a POST request to `/api/book` and display the returned message text below the Book_Button.

### Requirement 9: Typography and Fonts

**User Story:** As a visitor, I want the page to use the same geometric sans-serif typeface as the reference, so that text rendering matches.

#### Acceptance Criteria

1. THE Landing_Page SHALL load the "Poppins" font family from Google Fonts in weights 400, 500, 600, and 700.
2. THE Landing_Page SHALL define the heading font family Color_Token-style variable `--font-heading` as `"Poppins", "Inter", system-ui, sans-serif`.
3. IF the Google Fonts request fails, THEN THE Landing_Page SHALL render all text using the next available font in the fallback list without layout errors.

### Requirement 10: Responsive Fallback

**User Story:** As a visitor on a narrow screen, I want the page to remain readable, so that the content is usable even though the design is desktop-first.

#### Acceptance Criteria

1. WHILE displayed on a Desktop_Viewport, THE Landing_Page SHALL use the absolute positions specified in Requirements 2 through 8.
2. WHILE displayed on a Narrow_Viewport, THE Landing_Page SHALL stack the Nav_Bar, Hero_Headline, Model_Image, Tagline, Client_Stats, and Book_Button vertically in that order with no horizontal overflow.
3. WHILE displayed on a Narrow_Viewport, THE Hero_Headline SHALL reduce its font size to 48px.
4. WHILE displayed on a Narrow_Viewport, THE Landing_Page SHALL hide the Social_Column.

### Requirement 11: Flask Server and Routing

**User Story:** As a developer, I want a Flask app that serves the page on port 8009, so that I can run the site with a single command.

#### Acceptance Criteria

1. THE Flask_Server SHALL be defined in the file `app.py` at the repository root.
2. WHEN `python app.py` is executed, THE Flask_Server SHALL listen on host `0.0.0.0` and port `8009`.
3. WHEN an HTTP GET request is made to `/`, THE Flask_Server SHALL respond with status 200 and the rendered `templates/index.html` content.
4. WHEN an HTTP GET request is made to `/health`, THE Flask_Server SHALL respond with status 200 and the JSON body `{"status": "ok"}`.
5. WHEN an HTTP POST request is made to `/api/book`, THE Flask_Server SHALL respond with status 200 and a JSON body containing a `message` key with a non-empty string value.
6. WHEN an HTTP request is made to a path that does not match any route, THE Flask_Server SHALL respond with status 404.

### Requirement 12: Static Asset Serving

**User Story:** As a developer, I want CSS and images served from `/static`, so that the page's styling and images load correctly.

#### Acceptance Criteria

1. THE Flask_Server SHALL serve files from the `static/` directory under the `/static/` URL prefix.
2. WHEN an HTTP GET request is made to `/static/css/style.css`, THE Flask_Server SHALL respond with status 200 and a `Content-Type` header containing `text/css`.
3. WHEN an HTTP GET request is made to `/static/img/model.png` and the file exists, THE Flask_Server SHALL respond with status 200 and a `Content-Type` header containing `image/png`.
4. THE Landing_Page SHALL reference every Static_Asset using Flask's `url_for('static', filename=...)` helper.

### Requirement 13: Project Setup and Documentation

**User Story:** As a developer, I want dependency and run instructions, so that I can install and start the project quickly.

#### Acceptance Criteria

1. THE project SHALL include a `requirements.txt` file at the repository root listing `Flask` with a pinned major version.
2. THE project SHALL include a `README.md` at the repository root with the commands to create the virtual environment, install dependencies, and run `python app.py`.
3. THE `README.md` SHALL state that the page is reachable at `http://localhost:8009`.
