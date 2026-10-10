@echo off
title Math Quest - publish to GitHub (and the iPad/Android link)
cd /d "%~dp0.."
if not exist .git (
  git init
  git add -A
  git commit -m "Math Quest v2: 5 worlds, 34 levels, RSM-style skills, pet, wardrobe, music"
  gh repo create virvkh-ux/math-quest --public --source=. --remote=origin --push --description "Math practice game"
  gh api -X POST repos/virvkh-ux/math-quest/pages -f "source[branch]=main" -f "source[path]=/"
) else (
  git add -A
  git commit -m "Math Quest update"
  git push
)
echo.
echo Code: https://github.com/virvkh-ux/math-quest
echo Game link (ready 1-2 minutes after first publish): https://virvkh-ux.github.io/math-quest/
timeout /t 20
