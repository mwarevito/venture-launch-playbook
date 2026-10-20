# Content, motion video and ad creative without AI slop

Agents can produce a month of posts, films and ad images in an afternoon. That is the danger. On Givi the asset that worked was a plain static ad made in about 20 minutes, while 30-40 agent-hours of polished films produced no sign-up anyone could trace. This file covers what to make, in what order, how to make it with code, the checks that keep it from reading as AI slop, how to post it, how to test it as ads, and how to review it every day.

**Done when:** every public post and ad has passed the checklist in section 2; the first paid test ran as one ad set with 2-3 statics (3-5 made, the rest held as replacements) and ended in a winner or a stop; the brand's profile grid has been checked as a signed-out visitor sees it; any video opens on its finished headline and its processed length was checked after upload; and a daily review reports yesterday against the 7-day trend with at most 3 changes.

Platform specs, tool behaviour and the Remotion API were checked on 13 Oct 2026 (sources at the end). Every command and code block in section 4 was run that day with Remotion 4.0.535, Playwright 1.64 and ffmpeg 8.1 on macOS.

---

## What happened on Givi

- **Films against a static.** About 30-40 agent-hours went into films between 1 and 11 Oct 2026: an intro film, a team film, 7 industry spots and several ad cuts, all built as code with Remotion plus an HTML-to-video pipeline. No sign-up could be traced to any of them. A static ad made from an HTML template in about 20 minutes ("$1,000+ of work. $49 a month.") took about 96% of UK and US Meta spend, at a link click-through rate of 5.6% against 2.6% for the other images. **(learned the hard way)**
- **Re-renders.** The ad set was rendered five times in one day, then again for a price change and a trial change, because the offer was printed inside the pictures. Meanwhile a card hold kept the ad account from spending for two days. **(learned the hard way)**
- **Organic social.** 47 posts in 5 days across Instagram, TikTok, YouTube and X produced 0 site visits from those networks (the post links carried no tracking tags, which also made them harder to measure). TikTok turned out to have about 1,800 plays, but its profile had no link field and no visits followed. LinkedIn comments on buyers' posts produced all 5 buyer conversations the launch had by 12 Oct 2026. **(learned the hard way)**
- **The Instagram audit, 12 Oct 2026.** Vito opened the brand's Instagram and judged that the page looked full of AI slop. What he saw:
  - 13 of 17 posts were the same template card;
  - most posts still showed old prices and trial terms;
  - square art was cut off by Instagram's 3:4 profile grid, so one headline read "keting agency";
  - two "Meta Review Test" placeholder posts were left on the live grid by the platform-review session;
  - films that opened on a black or blank first frame showed up as empty tiles, because Instagram used the first frame as the grid tile.
- **The fixes agreed after the audit.** Every film opens on its finished headline. Images are 1080x1440 (3:4), or keep every word inside the centre 3:4 area. Nothing test-like goes on a live account; use a Story or a test account. Posts with old offer terms come down when the offer changes. Films were kept only until a new look is approved.
- **The direction proposed after the audit.** Real work, shown the way it really looks: (1) a real job recorded off the phone screen, sped up to about 20 seconds, with a one-line caption; (2) "the product runs the business" screenshots, plain and unstyled; (3) real people's words, with permission. Invented businesses in polished films ("a studio in Denver") feel like ads, not life. None of the three had been published by 12 Oct 2026.

---

## 1. What slop is, and why it costs you money

Slop is content whose form tells the viewer that nobody checked it. People rarely name it, but they spot it in under a second: the same card for the tenth time, a face that belongs to nobody, a business that does not exist, a headline cut in half, a price that changed last week, an "Example" badge, a black tile. It costs you in three places.

**The ad system starves sameness.** Meta's retrieval system (Andromeda, Meta engineering blog, Dec 2024) picks a few thousand candidate ads per person from millions, and practitioner analyses from 2025-2026 report that it groups near-identical ads and treats them as one **(recommended, not tested by us)**. Within an ad set, once one ad performs, Meta puts almost all the money behind it: on Givi one static took about 96% of spend, and abstract hooks such as "Fire your to-do list." were starved within hours **(done on Givi)**. So variants must differ in the idea (hook, proof, format). A colour swap is the same ad.

**Viewers punish fakery in public.** Every later viewer sees the comments. On Givi an image built around the phrase "AI agents" drew "#aiSlop" and a vomit emoji, and 5 of its first 42 UK viewers blocked the Page; it was paused the same day. The concrete value-for-price image drew no such reaction. **(learned the hard way)**

**The profile is the shop window.** People who click an ad or a comment check the profile first. Identical cards, stale prices and test posts say "fake or abandoned". **(learned the hard way)**

**Platforms add slop for you.** TikTok's ad builder silently added AI text suggestions (one read "Get a £1,000+ Vehicle") and invented "selling points". Meta's "add music" was accepted on 12 ads, including videos that already had their own soundtrack, and nobody listened to the mix. **(learned the hard way)**

---

## 2. The anti-slop checklist (run it before anything is published)

The agent runs every item and records the result next to the asset on the review page; the founder sees only assets that passed. The first item of each new kind under the brand (first static, first reel, first post on a new network) still needs the founder's own yes.

### 2.1 Truth

1. **Every claim exists in the product today,** checked against the code and production usage (a read-only query showing real users hit it). Docs and landing copy prove nothing. Givi's ads and landing pages showed "helper" assistants for about 3 days; production showed 0 uses in 149 owner conversations. **(learned the hard way)**
2. **The offer is copied, never written,** word for word from the one offer file. An agent-written end card misstated Givi's offer in 8 videos and 136 images. **(learned the hard way)**
3. **No offer terms inside images or video.** Price and trial go in the ad's text fields, the caption or the landing page, so a price change is a text edit. **(learned the hard way)**
4. **No invented proof:** no made-up testimonials, reviews, quotes, ratings or named customers (banned under the UK's DMCC Act 2024 and the US FTC's 2024 rule on reviews and testimonials). Real builds can appear as anonymous case cards once the client agrees in writing. **(done on Givi:** invented quotes were refused and real example jobs used instead.)
5. **Invented businesses only after a name check** of Google Maps in that city, the company register and a trademark database. A Givi dry run produced pages naming real cafés. **(learned the hard way)** Real work (section 3) avoids the problem.
6. **Competitors named at most once and never shown:** no competitor UI, logo or claims about what it cannot do. Vito later banned ChatGPT comparisons altogether ("other agents" instead). **(done on Givi)**

### 2.2 Look (Vito's taste rules, generalised)

7. **No "Example", "sample" or "demo" labels.** Vito ruled them sloppy on public materials. Honesty comes from showing only real things. **(done on Givi)**
8. **No fake chat screens imitating a known messenger.** Show your own product's UI; other products as plain panes with a text label; email as a simple envelope animation. **(done on Givi)**
9. **No cursive script or bookish serif display fonts.** **(done on Givi)**
10. **No stock or AI-generated faces or people.** Givi's films showed people as initials. Never use a personal photo found on disk; an agent once used one from the local machine without asking, and it was rejected. **(done on Givi)**
11. **No rainbow logo chips.** Tools appear as plain text names or a monochrome logo wall; coloured logos in ads also hit vendors' brand rules. **(done on Givi)**
12. **No pause, replay or "Play again" buttons.** Motion just runs; honour reduced-motion settings silently. **(done on Givi)**
13. **One signature device, used 3-4 times** (a dot, a stamp, an underline). A new trick in every section reads as generated. Cut the known tells too: uppercase eyebrows, decorative dots, coloured pills, empty slogans, repeated disclaimers. **(done on Givi)**
14. **Less text:** one hook of 12 words or fewer per image (8 on a carousel card). Givi's first ad images carried 35-45 words each. **(learned the hard way)**
15. **One currency,** the checkout currency, everywhere. Vito caught pounds and dollars in one sentence. **(learned the hard way)**

### 2.3 Frame and format

16. **Frame 0 is the finished headline:** no fade from black, no logo sting. Run the first-frame guard (section 4.4) and look at the frame. **(learned the hard way)**
17. **Every word survives the 3:4 grid crop.** Upload organic Instagram images at 1080x1440, or keep words in the centre 3:4 area; check with the grid-preview command. **(learned the hard way)**
18. **Text stays out of platform overlays:** in 9:16, between y 270 and y 1250, and at least 28 px tall after any zoom. **(done on Givi)**
19. **The ending holds** for the last 3 seconds, because Meta often trims about a second off uploads. **(learned the hard way)**

### 2.4 Sound

20. **A person has listened with sound on.** Agents cannot hear. On Givi, 8 films (24 scheduled posts) were queued with synthesised soundtracks nobody had played. Record "sound OK, <name>, <date>"; no listen, no post. **(learned the hard way)**
21. **AI voice is fine if it sounds professional.** Record provider, model and voice ID when you choose it (Givi did not, so its voice cannot be reproduced). Burn every spoken line in as a caption; most people watch muted. **(learned the hard way)**

### 2.5 Account hygiene

22. **Nothing test-like on a live account.** Review tests, dry runs and placeholders go to a test account or an expiring Story. **(learned the hard way)**
23. **Look at the grid as a signed-out visitor before every batch** (gstack `browse` or Playwright screenshot). **(recommended, not tested by us;** Givi skipped it until Vito complained.)
24. **Stale offers come down when the offer changes:** search every queued and live post, ad, bio and film for the old strings. **(learned the hard way)**
25. **AI labels are a deliberate choice.** TikTok asks for a label on realistic AI-generated or AI-edited content, including synthetic voices; YouTube and Meta have similar disclosures. Code-made motion graphics need none; an AI voice-over should carry one. Welder turns TikTok's AI label on by default (13 Oct 2026); Givi's script switched it off on every film, narrated ones included. **(recommended, not tested by us)**

### 2.6 A copy linter the agent runs

Keep the bans in one file in the venture repo (for example `brand/BANS.md`) and grep every caption, ad text file and image source before publishing:

```sh
grep -rniE "example|sample|demo|done for you|testimonial|limited time|places are limited|[£€].*\\$|\\$.*[£€]" content/ ads/ \
  && echo "FAIL: banned wording found" || echo "PASS"
```

---

## 3. Formats that work, ranked

| Rank | Format | Use it for | Evidence |
|---|---|---|---|
| 1 | Real work, shown as it looks: a phone screen recording of a real job (about 20 s, one-line caption), plain product screenshots, real people's words with permission | Organic posts; the picture inside statics; the source for the one short video | **(recommended, not tested by us):** Vito's direction after the audit; planned and dry-run on Givi, never published |
| 2 | Statics made fast with an HTML-to-PNG loop, 3-5 variants in an hour | The first paid test (2-3 running in one ad set, the rest held as replacements); organic posts | **(done on Givi):** the 20-minute static won 96% of spend |
| 3 | One short video (15-25 s, vertical) of the winning static's hook | Paid, only after a static has won | **(recommended, not tested by us):** Givi did this in the reverse order |
| Last | Produced motion films, showreels, 16:9 cuts | After 3 paying customers, and only once a channel shows video converts | **(learned the hard way):** 30-40 agent-hours, no traced sign-up |

### 3.1 Real-work screen recordings

1. **A filming account in week 1:** a fresh account on the live product under the venture's test identity, seeded with realistic data (inbox, calendar, a sheet, a test-mode payment product), all outgoing email routed to inboxes you own. Givi's waited about 3 days for a 2-minute founder sign-in, so every film used drawn scenes. **(learned the hard way)**
2. **A shot list:** per shot, the exact action, what must be on screen, the "moment", plus a do-not-film list of unready features. Dry-run every shot; Givi's dry runs found real bugs. **(done on Givi)**
3. **Record on the phone** with Do Not Disturb on, within 24 hours of a passed dry run, running the real job end to end. **(recommended, not tested by us)**
4. **Cut the waiting, keep the result readable:** speed up the working stretches 8-20x, hold the result at normal speed for 2-3 seconds, never speed up text appearing (command in section 4.4).
5. **One burned-in caption line** saying what happened: "It replied to 4 enquiries and booked a call while I was out." Frame 0 shows the result or the caption.
6. **Privacy pass:** read one frame per second for names, emails, phone numbers and notifications. Givi ran an OCR check for personal data over its review screencasts and real-job carousels. **(done on Givi)**

### 3.2 Plain screenshots and real words

- **Screenshots:** the product's own screen at 1080x1440, no device mockup, gradient or stickers; the caption goes in the post text, or a plain band above the screen.
- **Real words:** a customer's or tester's exact sentence, with their written OK, attributed as they agree. Never polish a quote into marketing language. Givi had no customers to quote by 12 Oct 2026.

### 3.3 Statics made fast

The loop: one HTML template, one text file of hooks, one command that screenshots each hook at the target size. Five variants take minutes; the review is the slow part.

`statics/ad.html` (4:5, 1080x1350; side padding keeps words inside the 3:4 grid crop):

```html
<!doctype html>
<html><head><meta charset="utf-8">
<style>
  :root { --bg:#f4f1ea; --ink:#16201b; }
  html,body { margin:0; width:1080px; height:1350px; background:var(--bg); }
  .frame { box-sizing:border-box; width:1080px; height:1350px; padding:96px 130px;
           display:flex; flex-direction:column; justify-content:space-between;
           font-family:-apple-system, "Inter", sans-serif; color:var(--ink); }
  h1 { font-size:118px; line-height:1.0; letter-spacing:-0.03em; margin:0; }
  .shot { flex:1; margin:56px 0; border-radius:28px; background:#fff center top / cover; }
  .foot { font-size:34px; display:flex; justify-content:flex-end; }
</style></head>
<body><div class="frame">
  <h1 id="hook"></h1>
  <div class="shot" id="shot"></div>
  <div class="foot"><b>yourbrand.com</b></div>
</div>
<script>
  const q = new URLSearchParams(location.search);
  document.getElementById('hook').textContent = q.get('hook');
  if (q.get('shot')) document.getElementById('shot').style.backgroundImage = `url(${q.get('shot')})`;
</script></body></html>
```

`statics/render.sh` (one PNG per line of `hooks.txt`; `--channel chrome` uses the installed Chrome, so no browser download is needed):

```sh
#!/bin/sh
dir="$(cd "$(dirname "$0")" && pwd)"; mkdir -p "$dir/out"; i=0
while IFS= read -r hook; do
  i=$((i+1))
  enc=$(node -e 'process.stdout.write(encodeURIComponent(process.argv[1]))' "$hook")
  npx playwright screenshot --channel chrome --viewport-size "1080, 1350" \
    "file://$dir/ad.html?hook=$enc&shot=shots/run-1.png" "$dir/out/hook-$i.png" >/dev/null
  echo "out/hook-$i.png: $hook"
done < "$dir/hooks.txt"
```

Hook rules:
- Concrete value against the price beats feelings: "$1,000+ of work. $49 a month." won at 5.6% against 2.6% click-through, at half to a third of the cost per visit. **(done on Givi)**
- The picture is a real product screen, never text to read.
- Look at what runs in your category first: the Meta Ad Library (meta-ads `ads_library_search`) and Motion Creative Analytics (`get_inspo_creatives`) if connected. Givi skipped this and its first invented hooks were rejected. **(recommended, not tested by us)**
- Put all options side by side on one review page with a recommendation; Vito picked 3 of 5 in a minute. **(done on Givi)**

---

## 4. Motion video with code

Use code (Remotion, or HTML captured headless) for anything that shows your product, words or numbers: it is exact, repeatable and cheap to re-render. Make one short video only after a static has won (section 3).

**Style first, then the batch (learned on 16 Oct 2026).** On a second product the same founder runs, a round of ten calm, carefully briefed product films was rejected whole in one line: "complete ugliness, boring". The founder approved a single 15-second energetic showreel the same day, and every later film was held to it. Before any batch of films, build one 10-15 second style piece (or three style frames plus a five-second motion test per direction) and get the founder's yes. What the approved style had: the product's interface rebuilt as separate components that each animate (never a static screenshot), the real strings and colours copied from the live product, big headline words revealed from masks, springs and shared-element transitions, something moving in every frame, motion blur, and a synthesised score cut on the beat.

**Engine choice.** HyperFrames (HTML plus GSAP, Apache-2.0, `npx hyperframes`) did that second product's films with no licence cost; Remotion did Givi's (it needs a company licence above three people). Use whichever the product's repo already has. Two HyperFrames gotchas cost time: animation callbacks never fire during a render (drive counters from a tweened property instead), and media created by script renders silent (write `<video>` and `<audio>` tags in the HTML).

**Every language is a render.** Keep every on-screen string in a texts file with one entry per language and a status (copied from the product's own translation, the speaker's own words, a draft, or reviewed by whom and when). One composition renders all languages; layout may change per language, timing never does, so the second language reuses the first one's soundtrack. A script builds a review sheet for the native-speaker reviewer beside draft renders and applies the edits back. Render text-free masters too: the team uses them for their own edits.

### 4.1 A props-driven Remotion composition

One composition, three shapes, every word passed in as props. Frame 0 shows the finished hook; captions are burned in inside the safe band; brand and call to action hold for the last 3 seconds; no price anywhere in the picture.

Set up (pin exact versions; Remotion warns when packages disagree, and an unneeded `zod` install triggered exactly that warning in our test):

```sh
npm init -y
npm i --save-exact remotion@4.0.535 @remotion/cli@4.0.535 react react-dom
npm i -D typescript @types/react
mkdir -p src public props out
```

`src/index.ts`:

```ts
import {registerRoot} from 'remotion';
import {Root} from './Root';
registerRoot(Root);
```

`src/Root.tsx` (`calculateMetadata` sets size and length from the props, so one composition renders 9:16, 4:5 and 1:1 at 30 fps):

```tsx
import React from 'react';
import {Composition, CalculateMetadataFunction} from 'remotion';
import {Spot, SpotProps} from './Spot';

const SIZES = {
  '9:16': {width: 1080, height: 1920},
  '4:5': {width: 1080, height: 1350},
  '1:1': {width: 1080, height: 1080},
} as const;
const FPS = 30;

const calculateMetadata: CalculateMetadataFunction<SpotProps> = ({props}) => ({
  ...SIZES[props.format],
  fps: FPS,
  durationInFrames: Math.round(props.durationSec * FPS),
});

export const Root: React.FC = () => (
  <Composition id="Spot" component={Spot} width={1080} height={1920} fps={FPS}
    durationInFrames={18 * FPS} calculateMetadata={calculateMetadata}
    defaultProps={{format: '9:16', hook: 'Your winning hook.', clip: '',
      captions: [], endCard: 'yourbrand.com', durationSec: 18} satisfies SpotProps} />
);
```

`src/Spot.tsx`:

```tsx
import React from 'react';
import {AbsoluteFill, OffthreadVideo, Sequence, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';

export type SpotProps = {
  format: '9:16' | '4:5' | '1:1';
  hook: string; // complete on frame 0, never animated in
  clip: string; // a screen recording in public/, or '' for none
  captions: {text: string; fromSec: number; toSec: number}[];
  endCard: string; // brand and domain only; price and trial live in the ad text
  durationSec: number;
};

const ink = '#16201b';
const paper = '#f4f1ea';

export const Spot: React.FC<SpotProps> = ({format, hook, clip, captions, endCard}) => {
  const frame = useCurrentFrame();
  const {fps, height, durationInFrames} = useVideoConfig();
  const vertical = format === '9:16';
  // Words stay out of platform overlays: in 9:16 only between y 270 and y 1250.
  const textTop = vertical ? 270 : 70;
  const textBottom = vertical ? height - 1250 : 70;
  // Instagram's profile grid shows the centre 3:4, so a square loses 135 px each side.
  const side = format === '1:1' ? 150 : 60;
  const endFrom = durationInFrames - 3 * fps; // brand and CTA hold the last 3 seconds

  return (
    <AbsoluteFill style={{backgroundColor: paper, fontFamily: 'Inter, -apple-system, sans-serif'}}>
      {clip ? (
        <OffthreadVideo src={staticFile(clip)} muted
          style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      ) : null}

      {frame < endFrom ? (
        <div style={{position: 'absolute', top: textTop, left: side, right: side,
          background: paper, borderRadius: 28, padding: '28px 36px',
          fontSize: vertical ? 76 : 64, fontWeight: 800, lineHeight: 1.05, color: ink}}>
          {hook}
        </div>
      ) : null}

      {captions.map((c) => (
        <Sequence key={c.fromSec} from={Math.round(c.fromSec * fps)}
          durationInFrames={Math.round((c.toSec - c.fromSec) * fps)} layout="none">
          <div style={{position: 'absolute', bottom: textBottom, left: side, right: side,
            textAlign: 'center', fontSize: 48, fontWeight: 700, color: 'white',
            background: 'rgba(22,32,27,0.88)', borderRadius: 18, padding: '16px 24px'}}>
            {c.text}
          </div>
        </Sequence>
      ))}

      <Sequence from={endFrom} layout="none">
        <AbsoluteFill style={{justifyContent: 'center', alignItems: 'center',
          fontSize: 96, fontWeight: 800, color: ink, background: paper}}>
          {endCard}
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};
```

`props/run-1.json` (the screen recording goes in `public/run-1.mp4`):

```json
{
  "format": "9:16",
  "hook": "It found 12 leads and sent 3 offers before lunch.",
  "clip": "run-1.mp4",
  "captions": [
    {"text": "One message: find cafés with an old website.", "fromSec": 0.5, "toSec": 4},
    {"text": "It drafts each offer. You tap Approve.", "fromSec": 4, "toSec": 9}
  ],
  "endCard": "yourbrand.com",
  "durationSec": 15
}
```

Check, then render all three shapes:

```sh
npx tsc --noEmit -p .                                   # needs a tsconfig with "jsx": "react-jsx"
npx remotion still src/index.ts Spot out/frame0.png --props=props/run-1.json --frame=0
# read out/frame0.png: the hook must be complete and readable

for fmt in "9:16" "4:5" "1:1"; do
  tag=$(echo "$fmt" | tr ':' 'x')
  node -e 'const p=require(process.argv[1]); p.format=process.argv[2]; console.log(JSON.stringify(p))' \
    ./props/run-1.json "$fmt" > "out/props-$tag.json"
  npx remotion render src/index.ts Spot "out/spot-$tag.mp4" --props="out/props-$tag.json" \
    --codec=h264 --crf=18 --color-space=bt709 --log=error
  ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of csv=p=0 "out/spot-$tag.mp4"
done
```

The three 15-second renders took about 30 seconds in total on a recent Apple-silicon laptop. Keep `--color-space=bt709`: Givi's first films shifted colour between players without it. **(done on Givi)** Reading frame 0 of our first draft caught a three-line hook running into the recording; always read the still before rendering.

**Word-level captions.** For a narrated video, transcribe the voice-over to captions JSON and render it with `@remotion/captions` (`createTikTokStyleCaptions` groups words into timed pages). The per-line `Sequence` above covers a one-line caption.

**Licence.** Remotion is free for individuals and for-profit companies with up to 3 employees; larger companies need a company licence (Remotion's LICENSE.md, checked 13 Oct 2026).

### 4.2 HTML and CSS animation, captured headless

For simple motion (rows appearing, a list ticking to done), animate plain HTML and CSS and capture it frame by frame: the script pauses every animation, seeks it to each frame's time and screenshots, so the output is exact and repeatable.

`capture.mjs` (run with `npm i -D playwright`, then `node capture.mjs card.html 5 30`):

```js
import {chromium} from 'playwright';
import {mkdirSync} from 'node:fs';
import {pathToFileURL} from 'node:url';

const [file, seconds = '5', fps = '30'] = process.argv.slice(2);
const total = Math.round(Number(seconds) * Number(fps));
mkdirSync('frames', {recursive: true});

const browser = await chromium.launch({channel: 'chrome'});
const page = await browser.newPage({viewport: {width: 1080, height: 1920}});
await page.goto(pathToFileURL(file).href);
await page.evaluate(() => document.fonts.ready);
for (let i = 0; i < total; i++) {
  const ms = (i * 1000) / Number(fps);
  await page.evaluate((t) => document.getAnimations().forEach((a) => { a.pause(); a.currentTime = t; }), ms);
  await page.screenshot({path: `frames/f-${String(i).padStart(5, '0')}.png`});
}
await browser.close();
```

Encode with `ffmpeg -framerate 30 -i frames/f-%05d.png -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart card.mp4` (a 5-second card took about 7 seconds). Leave the headline unanimated so frame 0 shows it.

### 4.3 Code, or a hosted AI video tool

| Situation | Use | Why |
|---|---|---|
| The product's screens, real numbers, words, the brand | Code (Remotion, HTML capture) or a real screen recording | Exact, checkable, re-renders when wording changes |
| A price, trial or claim | Neither: the ad text fields or the caption | A change costs nothing |
| Abstract atmosphere or b-roll (light, texture, an object) where the brand allows AI footage | A hosted AI video tool, labelled as AI where the platform asks | Cheap mood shots; not proof of anything |
| People, customers, a "day in the life" presented as real | Real people who agreed, or nothing | Generated faces passed off as customers read as fake and draw "AI slop" comments |
| A comedy sketch or a character the founder asks for (the product as a person, a scene everyone knows is staged) | AI-generated cast and AI image-to-video, through the gated pipeline in 4.3a | Nobody is asked to believe it is real; labelled as AI where the platform asks |

Check each tool's commercial-use terms before any footage goes into an ad.

### 4.3a Filmed with AI: a gated pipeline (used on 20 Oct 2026)

What happened on Givi: the founder asked for a 40-second film for the Georgian market in the manner of a well-known "if a search engine were a guy" sketch: Givi as a man at a desk in an old Tbilisi courtyard, small business owners queuing with one-line asks, Givi handing back each finished job. A first cut built from AI stills moved in code had no voices; the founder asked for it filmed, with voices, and added "make sure you don't waste money, the video needs to be top notch". The filmed cut cost about $11 in all; a remaster after his notes cost nothing. His two notes became rules: the character's lips moved with no sound before a line (the edit had muted a second take of the same word and kept the picture), and the product cards on screen looked worse than the product's own landing page.

The order, each step ending with something the founder can see:

1. **Brief and reference.** Pull the reference video's transcript (`yt-dlp --write-auto-subs --skip-download`). Read the live landing page, the offer line, the language glossary and any brand book before writing. Write the script as a cue list: every line, who says it, 2-4 seconds a shot. Quote the cost from the shot list.
2. **A look board before any paid footage.** One review page of real rendered frames: two or three subtitle styles (the brand book's font and the landing's font), the on-screen product UI rebuilt from the landing's own card styles (open the page headless and read its CSS: border, radius, shadow, app row, action row, status pill, primary button), title and end card options, and one still per character. The founder picks per row. Fonts and subtitles are taste, and taste is the founder's call.
3. **Stills for the cast.** An image model that returns a full-resolution file (Figma's `gpt-image-2.5` did; Canva's generator returned only a thumbnail outside Canva). Keep one character consistent with a fixed description and distinctive wardrobe and props, and shoot the other speakers over that character's shoulder.
4. **A bake-off on the hardest shot.** Run one close-up speaking a line in the target language on three or four image-to-video models at once, starting from the same still. Judge by transcribing each clip's audio and comparing it with the script word for word, and by full-size face crops side by side. Choose the cheapest model that ties the best. On 20 Oct 2026 through OpenRouter: Veo 3.1 Fast ($0.12 a second with audio) matched full Veo 3.1 ($0.40) on look and spoke the Georgian line exactly; Veo 3.1 Lite ($0.08) also spoke it exactly; Kling 3.0 Pro was 720p and softer with a slipped word; Seedance 2.0 refused first frames that looked like real people. The bake-off cost about $3.40.
5. **Generate, then QC every clip.** One clip per shot, in parallel, from the approved stills; "No dialogue, nobody speaks" on silent shots and "No subtitles, no on-screen text, no music" on all. For each clip make a 2 frames-per-second strip, a transcript and a speech-energy line, and for speaking shots an 8 fps strip of the mouth. Remake only the failures (a light flare across a face and a stranger's arm crossing the frame cost $0.48 each to remake).
6. **Voice.** Use the video model's own voice for on-camera lines when its transcript is exact: lip sync comes free. Use a voice model (ElevenLabs v4 through OpenRouter) for narration and round-trip every line through a transcription model, because it softened one Georgian consonant and turned a word into a different one.
7. **Edit and master.** An edit list in code; subtitles that end inside their cut; cards that never cover a speaking face; music low under dialogue and out where the scene's sound carries it; loudness at -14 LUFS. Never mute a visible moving mouth: trim to the take where the lips say the line. Transcribe the whole master once more and check every line is there.

Money rules: no paid footage before the look board is picked and the bake-off is done; the bake-off stays near 10% of the expected spend; a remaster reuses clips and costs nothing unless a shot itself fails, and the founder hears that number before it starts. One model router account covered stills-to-video, voices and the transcription checks; keep it separate from any account that pays for live customer services, so a video run can never drain it.

### 4.4 The ffmpeg toolbox (all run on 13 Oct 2026)

| Job | Command |
|---|---|
| Find a black lead-in | `ffmpeg -i film.mp4 -t 2 -vf blackdetect=d=0.03:pix_th=0.10 -an -f null - 2>&1 \| grep black_` |
| Cut the first second (or up to the finished headline) | `ffmpeg -ss 1 -i film.mp4 -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart film-cut.mp4` |
| Cover image from the headline frame | `ffmpeg -ss 1 -i film.mp4 -frames:v 1 -q:v 2 cover.jpg` |
| Last frame, to check the ending | `ffmpeg -sseof -0.1 -i film.mp4 -frames:v 1 last.png` |
| Preview the Instagram 3:4 grid tile of any image or frame | `ffmpeg -i in.png -vf "crop='if(gt(iw/ih,3/4),ih*3/4,iw)':'if(gt(iw/ih,3/4),ih,iw*4/3)'" tile.png` |
| Ads copy: 30 fps H.264, fast start | `ffmpeg -i master.mp4 -r 30 -c:v libx264 -profile:v high -level:v 4.2 -pix_fmt yuv420p -preset slow -crf 20 -c:a aac -b:a 128k -movflags +faststart ad-30fps.mp4` |
| Shrink for an upload limit, same resolution | `ffmpeg -i big.mp4 -c:v libx264 -preset slow -crf 20 -c:a copy smaller.mp4` |
| Loudness and true peak (aim near -14 LUFS, peak under -1 dBTP) | `ffmpeg -i film.mp4 -af ebur128=peak=true -f null -` |

Speed up a phone recording to about 20 seconds (here: the first 80 seconds of waiting at 8x, then the 10-second result at normal speed, cropped to 1080x1920 below the status bar):

```sh
ffmpeg -i run.mov -filter_complex "\
[0:v]trim=0:80,setpts=(PTS-STARTPTS)/8[wait];\
[0:v]trim=80:90,setpts=PTS-STARTPTS[result];\
[wait][result]concat=n=2:v=1[v];\
[v]scale=1080:-2,crop=1080:1920:0:110,setsar=1,fps=30,format=yuv420p[out]" \
-map "[out]" -an -c:v libx264 -crf 18 -preset slow -movflags +faststart run-20s.mp4
```

The first-frame guard (fails on a black or near-blank frame 0 and saves the frame for a person or agent to read):

```sh
#!/bin/sh
f="$1"
ffmpeg -v error -y -i "$f" -frames:v 1 frame0.png
e=$(ffmpeg -hide_banner -v error -i "$f" \
  -vf "select=eq(n\,0),format=yuv420p,entropy,metadata=print:file=-" -f null - \
  | sed -n 's/.*normalized_entropy.normal.Y=//p' | head -1)
echo "frame 0 detail score: $e"
if awk -v e="$e" 'BEGIN { exit !(e < 0.01) }'; then echo "FAIL: frame 0 looks blank"; exit 1; fi
echo "PASS (still open frame0.png and read the headline)"
```

In our test a black or flat frame scored 0, a frame with only a small logo about 0.001, and a frame with a two-line headline about 0.02-0.05. Tune the 0.01 threshold on your own look; the guard catches blank tiles, and reading the frame catches everything else.

### 4.5 Check the upload after it lands

- **Meta ads.** After upload (meta-ads MCP, `ads_creative_upload_media` first), wait 60-90 seconds, read `ads_get_ad_videos` (fields `id,length,status`) and compare with `ffprobe` of the local file. If shorter, download Meta's copy and check its last frame. Givi's 22-second videos once came back at 4-16 seconds, and later about a second short; the cause was never proven. **(learned the hard way)**
- **Organic.** Open the live post signed out; read duration and first frame. **(done on Givi)**
- "Ready" means checked after upload. A Givi agent reported "all three channels are ready" while live uploads were truncated and showed a feature that did not exist. **(learned the hard way)**

---

## 5. Platform specs (checked 13 Oct 2026)

Re-check before a big batch; these move. "Text zone" means where words are safe from the platform's own buttons and captions.

| Placement | Size and shape | Length | Text zone and notes |
|---|---|---|---|
| Instagram profile grid | Tiles are 3:4 (since Jan 2025) | n/a | Upload 1080x1440 so the post matches its tile. A 1:1 loses 135 px each side; a 4:5 loses about 34 px each side; a 9:16 reel shows its centre 1080x1440 (240 px off top and bottom) |
| Instagram feed post | 1080x1440 (3:4) organic; 1080x1350 (4:5) for feed ads | Video up to 15 min via API (Welder) | Up to 10 images per carousel; JPEG (Welder converts PNG) |
| Instagram Reels | 1080x1920 (9:16) | Up to 3 min in the app; up to 15 min uploaded | Keep words out of the top about 14% (270 px) and bottom about 35% (670 px), sides about 6% |
| Instagram and Facebook Stories | 1080x1920 | Video up to 60 s per story (Welder) | Same text zone as Reels; good home for anything temporary or test-like |
| TikTok | 1080x1920 | 3 s to 10 min (Welder) | In-feed text zone (third-party guide): about 250 px clear at top, 700 px at bottom, 240 px on the right (buttons), 120 px on the left, so end text near y 1210, a little above the Reels line. Captions up to 2,200 characters |
| YouTube Shorts | Vertical or square, 1080x1920 | Up to 3 min (uploads since 15 Oct 2024) | Vertical video of 3 min or less publishes as a Short (Welder). Same text zone as Reels is a safe default |
| LinkedIn | 1080x1920 vertical video now surfaces in a vertical video feed; 1:1 and 16:9 also supported; images 1:1 or 4:5 | Company page video up to 10 min (third-party guide) | Not supported by Welder; post by hand or through LinkedIn's own tools |
| X | 16:9, 1:1 or 9:16; up to 1920x1200 | Up to 140 s on a standard account | 280-character text; 4 images per post. Through Welder it needs a paid add-on and credits (a post with a link cost 8 credits) |
| Meta ads (Feed, Reels, Stories) | 4:5 for feed, 9:16 for Reels and Stories | Short: 15-25 s for cold traffic | Primary text shows about 125 characters before "See more"; headline 40 characters or fewer (about 27 show on a phone). Preview every placement with `ads_get_ad_preview` before publishing |

Sizes used across this file: 9:16 = 1080x1920, 4:5 = 1080x1350, 3:4 = 1080x1440, 1:1 = 1080x1080.

---

## 6. Scheduling and posting through Welder's MCP

Welder posts videos, images and carousels to the brand's own Instagram, TikTok, YouTube, Threads, Bluesky and X accounts from code. It does not post to Facebook or LinkedIn. **(done on Givi)**

**Before the first post.** One Welder profile holding only this venture's brand accounts; the founder connects each network on their phone (Instagram and TikTok in Welder's dashboard, others through `connect_account` links). `create_post`, `cancel_post` and `delete_post` stay off the agent's allow-list until the founder has approved the first post on each network.

**Every post** (about 2 minutes, plus the review):

1. `get_context`: confirm only this venture's accounts are connected. Every time; a shared login can post as the wrong brand.
2. `get_capabilities`: current per-network limits (length, size, caption).
3. Run section 2 and the first-frame guard on the file.
4. `create_upload` (`filename`, `mime`, `bytes`) returns a signed URL, headers and a `media_id`; send the file with `curl -X PUT --upload-file film.mp4 -H "<each returned header>" "<signed url>"`.
5. `finalize_upload` with the `media_id`.
6. `validate_post` with exactly what you will post. It checks ownership, quotas, caption length, formats and network rules without publishing.
7. `create_post` with a caption written per network (one caption on four networks was part of why Givi's 47 posts went nowhere), `schedule_at`, an `idempotency_key` so a retry cannot double-post, `instagram.kind` (`reel`, `image`, `carousel` or `story`) and the AI-label fields (section 2, item 25).
8. Once live, open it signed out: duration, first frame, caption. Log the post ID.

**Cover frames.** Givi set no cover, so Instagram used frame 0 as the grid tile and the black tiles followed. Welder's current schema (13 Oct 2026) lists cover fields (`instagram.cover_media_id`, `thumb_offset_ms`, `tiktok.cover_index`, `cover_timestamp_ms`, `youtube.thumbnail_media_id`), but Givi did not use them and we have not tested them. The rule stays: open every film on its finished headline, because previews, shares and any network that ignores the cover setting show frame 0. Setting a cover as well does no harm. **(learned the hard way)**

**Swapping posts after an offer change:** create the new post, `cancel_post` the old one, then count with `list_posts` (status `queued`). Post IDs change on every re-create, so update the log. Givi swapped 24 queued posts in one evening. **(done on Givi)**

**Upload size.** On Givi a film over Welder's limit at the time (about 50 MB) failed and went through re-encoded to about 30 MB at the same resolution. `get_capabilities` now lists 300-500 MB per network, so check it and keep the re-encode as fallback. **(done on Givi)**

**Rules from incidents:**
- Drop hashtags if spam bots arrive; Givi did after "Send me this post" comments. **(done on Givi)**
- Keep media in the repo or run folder. An unattended Givi review hung about 8 hours on a macOS permission pop-up because it read the Desktop. **(learned the hard way)**
- New accounts with no followers get almost no reach. Organic posting on brand accounts waits for 3 paying customers (`01-framework.md`); before that, buyer conversations come from section 8 and from outreach (`08-outreach.md`).

---

## 7. Ad creative testing

Campaign setup, budgets and the funnel gate are in `10-paid-ads.md`. These are the creative rules.

1. **Statics first, sized to the budget.** Make 3-5 static hooks in one shape (4:5) for one market. Givi built 136 images for about £15 a day, re-rendered them at least four times, and the comparison never reached a result. **(learned the hard way)**
2. **Render only what can run:** the offer is frozen and the ad account can spend within 48 hours. **(learned the hard way)**
3. **The first paid test is one ad set with 2-3 statics.** Meta will put most of the money on one of them within about a day; on Givi one static took about 96% of spend **(done on Givi)**. That concentration is your winner signal. Pause any ad that trips the day-1 rule and swap in one of the statics you held back. Below about 1,000 visitors per arm in 14 days, or about £20 a day on Meta, a split test cannot conclude, so do not build one. Never create a Meta A/B test object at launch; it holds delivery until the next midnight and cost Givi a day **(learned the hard way)**.
4. **Kill rules written before launch:** day-1 link click-through under 0.5% pauses that ad; the capped test (about 100 in the checkout currency, run only after the funnel gate and with the founder's dated yes) stops at its cap or at 150 landing visits with 0 sign-ups, whichever comes first (`10-paid-ads.md`, `01-framework.md`). **(recommended, not tested by us)**
5. **Offer terms in the text fields only,** so a price change is a text edit. Givi's ads were set to launch at midnight with a retired price; Vito caught it. **(learned the hard way)**
6. **Preview every placement** with `ads_get_ad_preview_screenshot` (formats such as `INSTAGRAM_REELS`, `INSTAGRAM_STORY`, `FACEBOOK_REELS_MOBILE`). **(recommended, not tested by us)**
7. **Switch off enhancements you have not checked:** Meta's automatic music and text variations; TikTok's text suggestions, selling points, music refresh and dubbing. **(learned the hard way)**
8. **Video only after a static wins:** one 15-25 second vertical cut of the winning hook, 30 fps, captions, a cover cut from the headline frame, its own tracked link. It earns its own ad set only if its hook rate (3-second views divided by impressions) or click rate beats the static. **(recommended, not tested by us)**
9. **Read the review outcome** (`ads_get_ad_entities`, `ads_get_errors`) the same day and next morning; fix and resubmit rejections as new ads. Givi never recorded the outcome of its last 9 video ads. **(learned the hard way)**
10. **Watch day-1 comments.** Hide (do not delete) hostile and spam comments, and read hostility as a verdict on the framing. **(done on Givi)**

---

## 8. Founder-led content on the founder's own accounts

The founder decides this per channel, once, in the intake. Vito chose no posts under his own name and no photo or face anywhere.

### What happened on Givi

- Daily LinkedIn comments on target buyers' posts (owners of agencies, studios, small service businesses) produced all 5 buyer conversations by 12 Oct 2026. **(done on Givi)**
- The rule: agents draft and the founder posts. LinkedIn's User Agreement forbids bots and automated posting. **(recommended, not tested by us)**

### The recipe, for founders who opt in (recommended, not tested by us)

**What to post:** things that really happened, useful to someone a step behind you.
- **Real numbers:** what the first £100 of ads bought, static against films, sign-ups per visit.
- **Real mistakes:** "We spent 30-40 hours on films and a 20-minute static beat them" beats any film.
- **Real artifacts:** the winning ad, the review sheet, the shot list, a chart from the daily review, a screen recording of a real job.

Skip engagement bait, "thrilled to announce", polls for reach, hashtag strings, generated images and any number you cannot show.

**How drafts are made.**
1. The agent mines the week: daily reviews, merged changes, the decisions log, new assets.
2. It drafts 2-3 posts in the founder's voice, modelled on their past writing (their vocabulary, short sentences), and runs the section 2.6 linter.
3. Drafts go to the review page with the artifact attached; the founder edits and posts them.
4. Buyer comments: the agent finds 3-5 recent posts by target buyers, drafts a specific comment for each (the product in at most 1 of 3), opens the post and copies the comment to the clipboard; the founder posts it.

**Hard rules.**
- Never automate posting, commenting, liking or messaging as the founder, on any network, even with them watching. LinkedIn forbids it, and the founder's personal account is at risk.
- A separate yes per channel, with the first post shown. A "Go!" to a plan is not consent to speak as the founder.
- Never catch up a missed run in the founder's name; tell them it was missed.
- Drafts that must not go out live where no scheduled job can read them.

**Weekly rhythm (founder time about an hour a week).**

| When | Agent | Founder |
|---|---|---|
| Monday | Drafts 2-3 posts from last week's real material, each with its artifact | Picks, edits, posts one (15 min) |
| Weekday mornings | Drafts 3-5 buyer comments and lines them up for the clipboard | Posts them (5 min a day) |
| Wednesday or Thursday | Updates the second post with any new number | Posts it (10 min) |
| Friday | Notes which posts and comments led to replies, profile views or conversations | Nothing |

---

## 9. The daily review loop

One short review every morning, written by the agent that owns content and ads, read by the founder in about 2 minutes. Givi moved this from weekly to daily on 11 Oct 2026 at Vito's request; its first daily run found more than a dozen replies that nobody had read for up to 3 days. **(learned the hard way)**

**Inputs (each with its source and the time it was read):**
- Ads: spend, impressions, link click-through, cost per landing visit, and for video the hook rate and ThruPlays (meta-ads insights; Motion Creative Analytics `get_creative_insights` with `SPEND` first if connected).
- Site: visits, Start clicks and sign-ups by tracked link (every post and ad link carries UTM tags; Givi's early posts had none).
- Organic: Welder `get_analytics` and `get_post_analytics` for what it can see (YouTube, X); Instagram insights through the Graph API with a read-only token; TikTok plays from the public video pages (Welder could not read TikTok views on Givi).
- People: every new comment and reply (`list_comments` in Welder, the networks' own inboxes, LinkedIn notifications). Replies are leads and are answered the same day.

**Output (paste this as the agent's brief):**

```text
Daily content and ads review for <brand>, <date>.
1. Yesterday against the 7-day average, one line per channel: spend, visits, sign-ups,
   click-through, hook rate; each number with its source and read time. Flag anything
   more than 30% off the average.
2. What worked: the one asset or comment that drove the most visits or replies, and why
   you think so, labelled as a guess if it is one.
3. Replies and comments: count, who they are, which are buyers; draft answers.
4. Up to 3 changes for today (pause, swap a static, a new hook, a post to take down),
   each with the number that justifies it. Do not change anything that has run under
   3 days unless a kill rule fired.
5. Anything that needs the founder, as one line each with a recommendation and a default.
```

Rules for the loop:
- At most 3 changes a day, logged in an experiment log, so you can tell what caused what.
- Silent unless something is wrong or needs the founder; numbers go into the morning digest (`13-daily-ops.md`).
- Collect reach for every network before diagnosing. Givi's reset called TikTok silent; about 1,800 plays were found the next day. **(learned the hard way)**
- Hard time limits on every unattended run, and a separate watcher that alerts when a run did not finish. **(learned the hard way)**

---

## Checklist

- [ ] The offer, prices and claims live in one file; no image or video prints price or trial terms
- [ ] Every shown feature has been checked against code and real production use
- [ ] The bans list exists in the repo and the copy linter passes on every caption and ad text
- [ ] No "Example" labels, fake messenger screens, invented testimonials or named fake customers, cursive or bookish serif display fonts, stock or AI faces passed off as real people, rainbow logo chips, or pause and replay buttons
- [ ] AI-filmed video: look board picked before paid footage, model bake-off on one hard shot, every clip transcribed and lip-checked, on-screen UI matches the landing
- [ ] One signature device per page or film, used 3-4 times
- [ ] A filming account exists in week 1, seeded, with outgoing email routed to owned inboxes
- [ ] 3-5 statics made with the HTML-to-PNG loop, one shape, one market
- [ ] Hooks researched in the Meta Ad Library before writing; concrete value against price tried first
- [ ] The first paid test runs 2-3 statics in one ad set, after the funnel gate and the founder's dated yes; the ad Meta concentrates spend on is the winner; the other statics wait as replacements; no Meta A/B test object; kill rules written down
- [ ] Platform enhancements (Meta music and text variations, TikTok text suggestions, selling points, music refresh, dubbing) reviewed and switched off where unchecked
- [ ] Video made only after a static won: one 15-25 s vertical cut, 30 fps, captions, brand held for the last 3 s
- [ ] Every video passes the first-frame guard and a person has read frame 0
- [ ] Every image's grid tile previewed; words inside the centre 3:4 area, or uploaded at 1080x1440
- [ ] A person has listened to every soundtrack with sound on, recorded with name and date
- [ ] AI voice provider, model and voice ID recorded; AI labels decided per asset and per network
- [ ] Processed length and last frame checked after every ad upload; live organic posts checked signed out
- [ ] Welder `get_context` checked before every post; `validate_post` before `create_post`; post IDs logged
- [ ] Nothing test-like on any live account; the public grid screenshotted as a visitor before every batch
- [ ] Old offer terms swept from posts, ads, bios and films on every offer change
- [ ] Founder content: a per-channel yes on record, drafts posted by the founder, nothing automated in their name
- [ ] Daily review running: yesterday against the 7-day trend, what worked, at most 3 changes, replies answered the same day

---

## Sources checked on 13 Oct 2026

- Remotion docs through Context7 (`/websites/remotion_dev`): composition props, `calculateMetadata`, `npx remotion still --frame`, render flags including `--color-space`, `@remotion/captions`. Remotion licence: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
- Welder MCP `get_capabilities` and the `create_post` and `validate_post` tool schemas (per-network limits, cover and AI-label options).
- Meta engineering blog on Andromeda (Dec 2024): https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ ; practitioner summaries of ad grouping, for example https://nikhil.pro/meta-ads-creative-similarity-explained/
- Instagram 3:4 profile grid and 3-minute Reels (Jan 2025): https://www.businesstoday.in/technology/news/story/instagram-head-announces-big-changes-3-minute-reels-and-new-look-for-profile-grid-461527-2025-01-21
- YouTube Shorts length and shape: https://1of10.com/blog/how-long-can-youtube-shorts-be/
- TikTok in-feed safe zone: https://www.trymypost.com/blog/tiktok-ad-specs-2026-safe-zones ; TikTok AI labelling: https://www.cinerads.com/blog/tiktok-ai-content-policy
- Reels safe zone summary: https://houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories-reels/
- LinkedIn video: https://ligosocial.com/blog/linkedin-video-post-best-practices ; X video: https://postfa.st/sizes/x/video
