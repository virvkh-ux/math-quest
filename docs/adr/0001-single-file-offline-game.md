# ADR-0001: Single HTML file, launched in Edge app mode

- **Date:** 2026-10-10
- **Status:** accepted

## Context
Needs to launch from the desktop like a game, work offline, and be easy for any AI tool to change.

## Decision
One self-contained `src/index.html`; desktop shortcut opens it with `msedge --app=file:///...` so it looks like its own app window.

## Consequences
No install or build. Progress lives in that browser profile's localStorage (one computer). If we later want phone/tablet or sync, wrap it as a PWA or Electron app.
