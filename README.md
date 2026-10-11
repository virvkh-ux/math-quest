# Math Quest

A level-by-level math adventure for a 2nd grader (RSM): catch up on addition and subtraction, then move into multiplication.

## Status
building (v1)

## Play
Double-click **Play Math Quest** on the desktop, or `Play Math Quest.cmd` in this folder.
Runs fully offline in a Microsoft Edge app window. Progress saves automatically on this computer.

## Play
- Desktop: double-click **Play Math Quest** on the desktop (works offline).
- iPad / Android: open https://virvkh-ux.github.io/math-quest/ in Safari/Chrome, then Share -> "Add to Home Screen". Works offline after the first visit.
- First open on each device asks for the family code (kept out of this repo). Progress is per device; use Grown-ups corner -> backup code to move it.

## Worlds (55 levels)
1. Ten Town - bonds to 10, add/subtract within 10
2. Twenty Forest - make-a-10, within 20, fact families, compare
3. Column Canyon - Martian numbers, mental tens, column add/subtract, carrying, borrowing, missing digits
4. Puzzle Planet - X equations, balance scale, chains, parentheses, smart compare, dimes & pennies, story problems
5. Times Castle - skip counting, equal groups, crossing lines, area/arrays, x0/1/2/10, x3/4/5, missing factor
6. Robot Rule Lab (Grade 2) - guess my rule, easiest-way computing, hundreds/tens/ones, number riddles, odd/even, largest/smallest
7. Hundreds Harbor (Grade 2) - 3-digit column add/subtract, rounding, think-of-a-number, compare without calculating, mystery bags, perimeter
8. Multiply Moon (Grade 2) - x2/x3, halves & X + X, sharing equally, groups & rates, ( ) then x

## Fun
Pet egg that hatches and evolves, hero wardrobe, pet shop, themes, stickers, daily chest, boss battles, streaks, ranks Rookie -> LEGEND, gentle music, read-aloud, Pip's picture lessons, skip tests, My Progress page, optional daily play limit.

## Layout
- `src/index.html` whole game; `src/sw.js` + `manifest.webmanifest` make it installable/offline
- `index.html` (root) redirects to `src/` for GitHub Pages
- `scripts/` desktop shortcut + publish
