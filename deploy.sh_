#!/bin/bash
# -----------------------------------------------------
# Deploy Flask-Freeze Build to gh-pages branch
# -----------------------------------------------------

# 1️⃣ Stelle sicher, dass wir auf main sind
git checkout main || { echo "Checkout main failed"; exit 1; }

# 2️⃣ Build erzeugen
echo "Freezing Flask app..."
python app.py freeze || { echo "Freeze failed"; exit 1; }

# 3️⃣ Wechsle zu gh-pages
git checkout gh-pages || { echo "Checkout gh-pages failed"; exit 1; }

# 4️⃣ Alte Dateien löschen
echo "Cleaning gh-pages branch..."
git rm -rf . || true         # entfernt getrackte Dateien
rm -rf * || true             # entfernt untracked Dateien (aber nicht dotfiles)
rm -rf .* 2>/dev/null || true # entfernt dotfiles außer .git

# 5️⃣ Build in Root verschieben
echo "Copying build files..."
cp -r build/* .
rm -rf build

# 6️⃣ Commit & Force-Push
git add .
git commit -m "Deploy latest build from main" || echo "Nothing to commit"
echo "Pushing to gh-pages..."
git push origin gh-pages --force

# 7️⃣ Zurück zu main
git checkout main
echo "Deployment complete!"
