# Instructions for AI assistants

Single source of truth for Claude, Gemini and any other AI tool. Edit this file, not CLAUDE.md / GEMINI.md.

- **Goal:** Fun, level-based math game that helps a 2nd grader (Russian School of Mathematics) catch up on addition/subtraction and get ready for multiplication. Encouraging, never punishing.
- **Player:** 7-8 year old. Big buttons, short text, read-aloud for word problems, hints before answers.
- **Stack:** One file, `src/index.html` (vanilla HTML/CSS/JS). No build step, no network, no external libraries or fonts. Saves to localStorage key `mathquest.v2`.
- **Run:** `Play Math Quest.cmd` (opens Edge in app mode on the local file).
- **Test:** open in a browser; every generator in `GEN` must return integer, non-negative answers. Play one level of each world. Bump VERSION in src/sw.js on every release so devices update.
- **Add a level:** add a generator to `GEN`, a row to `LEVELS`, a label to `SKILL_NAMES`.
- **Conventions:** keep each level 8 questions; first-try accuracy decides stars (90% = 3, 70% = 2); wrong answer -> hint with a visual, second wrong -> show answer and re-ask a similar question later.
- **Never put** the child's name, photos or the family code in this repo (it is public).
- **Do not touch:** the save format without a migration (it holds her progress).

Also follow the factory-wide rules in D:\AGENTS.md.
