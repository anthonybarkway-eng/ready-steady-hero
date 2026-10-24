# Ready, Steady, Hero!

A calm-down, listening and early English game for a three to four year old, built as a
web app for an iPad. One session is a "mission" of nine short slides: balloon breathing,
waiting for a green light, flash cards, karuta listening, shape building, counting, painting
a letter, a go/no-go fish game, and a goodbye that ends the session itself.

Everything runs in the browser from a single page. Nothing is uploaded anywhere: the child's
name, settings and progress stay in the iPad's own storage.

## Put it on the iPad

1. Open the site in Safari on the iPad (first time online).
2. Tap the Share button, then **Add to Home Screen**, then Add.
3. Open it from the new Home Screen icon. It runs full screen, sideways, and works offline
   after that first open.
4. On the start screen, hold **Parents: hold to set name & voice** for a second to type the
   child's name, how it is said, and pick a voice. The same panel is behind the small gear
   at the top right during play (hold it for 1.5 seconds).
5. Optional: Settings → Accessibility → Guided Access lets you lock the iPad to the game
   (triple-click the top button to start and stop it).

Better voice: Settings → Accessibility → Spoken Content → Voices → English (UK) → download
the Enhanced version of Daniel or Kate, then choose it in the parent panel.

## Change the game

- `src/body.html` is the game. Edit it.
- `python build.py` writes `index.html` and `sw.js` (the offline cache, stamped with a
  content hash so iPads pick up the new build on their next launch).
- `python make_icons.py` redraws the icons.
- Commit and push; GitHub Pages serves the `main` branch.

## Links

Opening the page with `#Zachy` sets the name on that device; `#Zachy~Zacky` also sets how it
is spoken. The Home Screen app has its own storage, so set the name once inside it.
