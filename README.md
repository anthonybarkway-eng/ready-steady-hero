# Ready, Steady, Hero!

A calm-down, listening and early English game for a three to four year old, built as a
web app for an iPad. One session is a "mission" of nine short slides: balloon breathing,
waiting for a green light, flash cards, karuta listening, shape building, counting, painting
a letter, a go/no-go fish game, and a goodbye that ends the session itself.

A second mission, in Taiwan Mandarin, sits beside START on the start screen (see below).

Everything runs in the browser from a single page. Nothing is uploaded anywhere: the child's
name, settings and progress stay in the iPad's own storage.

## Mission Taiwan (Mandarin)

Tapping the lantern offers two ways to play, each a short mission of its own.

**Words** (the lantern): seven short slides of first words for a family trip to Taiwan: hello,
thank you and bye-bye; Grandpa and Grandma; counting cars to ten; four colours; want, don't want
and more with Finn's snacks; head, hands and feet; and a cheering goodbye.

**The trip** (the suitcase): two longer challenges on the way to Taiwan.

1. *Packing the suitcase.* The things to take lie around the room: passport, shirt, pants,
   jacket, socks, shoes, hat, nappy, toothbrush, toy, books and water bottle. Tapping a thing
   shows its name card (picture, English word, characters, pinyin) and says the name in English
   and in Mandarin. Then each thing is asked for, in a new order every time, and is dragged into
   the suitcase. Six things at first, then eight, ten and all twelve as the level rises; the
   ones met least often are chosen first. If things are only touched, not carried, Whiskers says
   how to pack.
2. *The airport.* The things on the trolley (suitcase, backpack, passport and plane ticket) get
   their names; the plane and the trolley say theirs too when tapped, but need not be. Then the
   suitcase rides away on the check-in belt, the passport gets its stamp, the backpack goes
   through the scanner (the screen shows who is hiding inside), the ticket turns the gate light
   green, and the little hero gets on the plane.

A request is made in Mandarin first, and only the Mandarin names the thing: 我們把牙刷收起來！
and then "Let's put it away!". So the thing has to be found from its Mandarin name. After a
wrong move the Mandarin is said again at half speed, then the English as before. When the right
thing arrives, it is named in both languages.

Whiskers gives the instructions in English. Every Mandarin word is shown as a large Traditional
character with small pinyin, is spoken by the iPad's own Taiwan Mandarin voice, and says itself
again when it is tapped. The rules are the same as in Mission 1: nothing can be failed, the
screen is off while a voice is speaking, a wrong answer gets the "Stop… think… and try again"
pause with the word (in the trip, the request) said again, nothing points at the answer, each
slide keeps a level, and the mission ends itself with the goodbye.

- The mission needs a Chinese (Taiwan) voice on the device; iPads come with one (Meijia). If no
  such voice is found, the button is greyed out, and Mandarin is never read by an English voice.
  A better-sounding voice: Settings → Accessibility → Spoken Content → Voices → Chinese, and
  download the Enhanced Meijia under Chinese (Taiwan).
- To hide the mission, hold the gear and untick **Show Mission Taiwan on the start screen**.
  The same panel switches its slides on and off one by one (with both trip slides off, or all
  the word slides off, the lantern starts the other way to play at once), and
  **▶ Test Mandarin** speaks three words with the voice the game found.
- It keeps its own levels and its own count of finished missions. Mission 1 is untouched.

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
- To jump to a slide while testing, type `__rsh.go(3)` in the browser console (Mission 1), or
  `__rsh.mission('taiwan')` (the words) or `__rsh.mission('trip')` (the trip) and then
  `__rsh.go(1)` for a Mission Taiwan slide.
- Commit and push; GitHub Pages serves the `main` branch.

## Links

Opening the page with `#Zachy` sets the name on that device; `#Zachy~Zacky` also sets how it
is spoken. The Home Screen app has its own storage, so set the name once inside it.
