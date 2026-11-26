---
name: short-form-video
description: "Script, shoot and edit short vertical videos (reels, stories, shorts) with the capcut MCP, then audit the CapCut project before export. Use when planning a reel or story, writing a talking-to-camera script, editing clips in CapCut through the MCP, adding captions or overlays, or landing a joke in a video."
---

# Short-form video

Rules for vertical talking-to-camera videos (Instagram reels and stories, TikTok, Shorts) edited in CapCut through the `capcut` MCP. Generic: the project's own brand, tone and shot list live in that project's notes. Read them first and follow them over anything here.

## Before anything

1. Find the project's brand and tone notes (a `TONE.md`, a brand file, a playbook note) and its shot list. Ask if there are none.
2. Ask which CapCut project to edit, or whether to make a new one.
3. The user must quit CapCut before every save (see "CapCut rules").

## Script

- One line per shot, sayable in one breath. Put the point in the first 2 seconds: open on the news, not "hey".
- Speech or a face in the first 3 seconds. 15 to 30 seconds for anything with a joke, 5 to 15 per story.
- Write joke pauses into the script, with what the face does: `you... [look to camera] can get a record in it.` A pause that wasn't performed can't be created in the edit.
- Run all copy through the project's tone rules and the `humanizer` skill.

## Shoot (tell the user)

- Vertical. Face in the top half, product in the middle, bottom 300 px clear.
- Two or three takes a line, talking from the first frame.
- Play the beat: a look to the side or a deadpan stare, held a full second. Stay in frame for the reaction.
- A close-up of the main subject for the cover frame.
- Screen recordings: log out of any admin UI first, use a normal tab (Android records incognito as black), scroll slowly.

## Edit

Transcribe every clip (`capcut_transcribe`) and fix the transcript spellings before captions.

- **Dead air:** `capcut_add_video_without_pauses` removes pauses over `min_pause`, including comedy beats. Find joke pauses in the transcript first and keep them, or add that clip with `capcut_add_video`.
- **Jokes:** one zoom per joke. Zoom in on the setup (smooth, about 0.7 s, scale 1.2), hold through the pause, hard cut back to wide when the punchline shows something. Two zooms back to back, freeze frames and slowed pieces read as glitches. Check framing with `capcut_view_frames` across the whole zoom range: if the subject drifts, shorten the range rather than chasing them with position moves.
- **Pace:** change the shot every 3 seconds or so (cut, zoom or overlay). At most one camera move every 10 to 20 seconds.
- **Overlays:** never show the punchline in an overlay before it's said. Cut overlays in hard.
- **Look:** follow the project's grade. Never colour-grade footage of products whose colour matters.

## Captions

Every video gets captions, all in ONE style: same font, weight, size, colour, outline and box.

- Captions from different routes come out different: `capcut_add_auto_subtitles` takes the style arguments, `capcut_add_subtitle` (SRT) does not apply an outline and may pick another font. Use auto-subtitles for everything, including voiceovers: transcribe the voiceover file and run `capcut_add_auto_subtitles` on it.
- Over busy footage (screen recordings), add a box (`background_color #000000`, `background_alpha 0.6`) and use it for the whole video, or keep the outline and check legibility.
- Safe zone for 9:16: keep text inside the middle ~900 × 1400 px. Nothing important in the bottom 300 px or right 120 px.
- The punchline word gets its own caption.

## CapCut rules

- **Quit CapCut before saving.** It holds the open project in memory and writes it back when the project closes, overwriting saved changes. The MCP refuses to save while CapCut runs.
- **Opening a project in CapCut changes it.** Reopen it with `capcut_open_project` before saving, or the save is refused.
- Existing clips change only through `capcut_edit_clip` (trim, move), keyframes and camera moves. Existing captions can't be restyled through the MCP.
- **Sped-up clips take no keyframes or camera moves.** For a static crop or restyle the MCP can't do, edit `draft_info.json` directly with CapCut closed, back up the folder first, and write every copy CapCut keeps: `draft_info.json`, `draft_info.json.bak`, `template-2.tmp`, and the same under `Timelines/<id>/`. Never hand-write motion (keyframes, speed pieces): use the MCP.
- New projects only appear after CapCut restarts.

## Before handing over

Run the audit on every project you touched:

```bash
python3 ~/.claude/skills/short-form-video/audit_capcut.py "<project name or folder>"
```

It flags captions in more than one style, text outside the safe zone, gaps on the main track, and CapCut copies that disagree. Fix everything it flags, then look at frames around each joke and overlay with `capcut_view_frames`. Tell the user what to scrub in CapCut (time stamps), since you can't preview the render.
