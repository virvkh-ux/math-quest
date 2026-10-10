# Architecture

## Components
- Screens: welcome, map, play, result, stickers, grown-ups (one HTML file, toggled sections).
- `GEN`: question generators per skill -> {text, answer, visual, hint, hintVis, explain, key}.
- `LEVELS` / `WORLDS`: level config mapping to generators; boss levels mix generators.

## Data
localStorage `mathquest.v1`: name, avatar, stars per level, unlocked, coins, stickers, stats per skill, missed facts.

## Deployment
Local file opened by Edge `--app` (desktop shortcut). No server.
