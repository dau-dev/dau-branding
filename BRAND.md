# dau Brand Guide

Canonical source for the dau identity. The tokens and components in
`@dau-dev/branding` are the machine-readable version of this page; consume them
rather than re-implementing.

## Identity

dau is workload-shaped FPGA acceleration for analytical software. It maps
selected Polars, dataframe, and time-series operations onto right-sized
streaming hardware and leaves everything else in software, where it runs as
before.

It is not a database appliance, not a GPU replacement, and not a per-query
hardware compiler. The goal it is measured against: the host and the device
together beat the host alone.

Write the name in lowercase, `dau`, including at the start of a sentence.
In running text the wordmark's period is dropped; `dau.` appears only as a
mark.

## Mark

A half-filled disk inside a chip package.

- **The disk** comes from the original favicon. The line across it stands
  for the split dau makes between work that runs in hardware and work that
  stays in software.
- **The package** (body plus three pins a side) marks it as a device.
- **Two colors only**: pins, outlines, ring, and the filled half take the
  foreground; everything else takes the background of the surface the mark
  sits on. On shadow that is off-white on dark grey, on lit the reverse.
- **Wordmark**: `dau.` in Hanken Grotesk, light 300 with a heavy 800 period.

| Variant | Use                                | Minimum |
| ------- | ---------------------------------- | ------- |
| `chip`  | Default, anywhere 32px or larger   | 32px    |
| `disk`  | Favicons, inline icons, under 32px | 16px    |

Clear space is the width of one pin on every side (a tenth of the mark's
height). The filled half is always on the left. Do not rotate, outline, or
recolor the mark outside the two surfaces below.

Files are in `assets/logo/`, each as SVG and high-resolution PNG with a
transparent background. `-on-shadow` is for dark mode, `-on-lit` for light
mode.

| File          | Content                       | PNG size    |
| ------------- | ----------------------------- | ----------- |
| `lockup-on-*` | Chip mark and `dau.` wordmark | 2663 × 1024 |
| `mark-on-*`   | Chip mark                     | 2048 × 2048 |
| `disk-on-*`   | Disk mark                     | 2048 × 2048 |
| `avatar-on-*` | Chip on a solid square tile   | 1024 × 1024 |

The avatar is the one file with a background: the chip is drawn in ink only,
its inside left open to the tile. Use it where an image cannot follow the
viewer's theme, such as a GitHub organization picture.

The wordmark in the SVGs is outlined, so they render without the font
installed. Regenerate with `python3 scripts/logos.py` after changing the mark
or wordmark. `assets/favicon.svg` is a self-contained tile that reads on any
tab color.

## Color

Two colors and the steps between them. There is no accent hue; emphasis
comes from flipping a surface from shadow to lit or back.

| Token             | Lit       | Shadow    | Usage                             |
| ----------------- | --------- | --------- | --------------------------------- |
| `--dau-bg`        | `#eeede9` | `#202021` | Page background                   |
| `--dau-bg-raised` | `#e4e3de` | `#28282a` | Raised surfaces, hover            |
| `--dau-border`    | `#cfcdc7` | `#3a3a3c` | Rules and outlines                |
| `--dau-fg-muted`  | `#5d5c58` | `#9b9a96` | Supporting text, labels           |
| `--dau-fg`        | `#202021` | `#eeede9` | Text, the filled half, focus ring |

`--dau-shadow` and `--dau-lit` hold the two anchor values for places that
must not follow the theme (social cards, print).

The page theme (`data-theme="dark"` on `<html>`) selects shadow or lit.
`.dau-shadow` and `.dau-lit` pin a single element to one side regardless of
theme. `.dau-inverse` takes whichever side the page is not on; `Split` uses
it for the software half.

Every foreground passes WCAG AA (4.5:1) on both `bg` and `bg-raised` in both
surfaces, and the focus ring passes 3:1. `src/lib/tokens.test.ts` asserts it,
so change a value there and the test tells you if it broke.

Semantic color (errors, warnings) is not part of the brand palette. If a
surface ever needs one, add a role-named token and keep it out of marketing
pages.

## Typography

| Role    | Face           | Weights                 | Usage                                |
| ------- | -------------- | ----------------------- | ------------------------------------ |
| Text    | Hanken Grotesk | 300, 400, 600, 700, 800 | Headlines, body, UI                  |
| Utility | Fragment Mono  | 400                     | Labels, tables, register names, code |

Both are self-hosted through `@dau-dev/branding/fonts.css` so pages make no
requests to third-party font hosts.

Weight carries the same split as the mark: light 300 for what software does,
heavy 700–800 for what hardware does. Use that contrast deliberately and
rarely, in one headline per view, not as decoration.

Scale: display 300 at 4.5rem / -0.04em; heading 600 at 2rem / -0.02em; body
400 at 1.0625rem / 1.6; mono labels 0.75rem uppercase / +0.08em. Numbers in
tables use tabular figures.

## Composition

- **Flat surfaces, hard edges.** Radius is `--dau-radius` (2px) on controls
  and 0 on buttons. No shadows, no gradients, no glow.
- **Split, don't decorate.** The signature layout is two halves side by
  side: hardware on the left on the page's own surface, software on the
  right on the inverse. In dark mode hardware is dark and software light;
  in light mode the reverse. Use it where the content is a real
  two-sided comparison (software and hardware, host and device), not as a
  generic hero.
- **Tables for facts.** Measurements, board specs, and register maps go in
  `SpecTable`, set in mono. Do not turn numbers into big decorative tiles
  unless the number is the point of the page.
- **Line drawings for hardware.** Boards and systems are drawn as 2px
  outline illustrations in `currentColor`. No stock photography.
- **No background grids or texture.**

## Motion

Almost none. Hover states change fill, not position. The disk may change
phase slowly in a single hero; it stays still under
`prefers-reduced-motion: reduce`.

## Voice

- Plain, specific, measured. State what was run, on what, and what came out.
- Every performance claim names the workload and the hardware and was
  bit-exact. Lead with the speedup from adding the device; leave the
  host-only, device-only, and combined breakdown to the benchmark log.
- Sentence case for headings and buttons. Buttons say what happens:
  "Become a design partner", "See the code on GitHub".
- Avoid "revolutionary", "blazing", "next-gen", and claims of speed with no
  number behind them.

## Components

| Component      | Purpose                                                 |
| -------------- | ------------------------------------------------------- |
| `BrandMark`    | Mark plus optional wordmark, as a link or a plain image |
| `Button`       | Primary or secondary action, link or button             |
| `Split`        | Hardware (page surface) and software (inverse) halves   |
| `SpecTable`    | Parameter/value datasheet table with optional notes     |
| `CookieNotice` | Dismissible notice fixed to the bottom of the viewport  |
| `ThemeToggle`  | Lit/shadow switch, persisted in localStorage            |
