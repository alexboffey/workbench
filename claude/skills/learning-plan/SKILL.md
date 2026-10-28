---
name: learning-plan
description: Use when the user wants to learn or drill a subject with Claude as a teacher, e.g. "help me learn X", "plan some exercises on Y", "set up a practice repo for Z", "what should I focus on for this interview". Works out the goal, the level it tests and the gaps, then plans timeboxed exercises and scaffolds a practice repo with teacher rules.
argument-hint: "[subject and goal]"
---

# Learning plan

Turn "I want to get better at X" into a short plan and a practice repo where Claude grades and never writes the answers. Background and evidence: the vault note `ab/tech/AI Career & Learning/Learning With Claude.md`. Worked examples: `~/Projects/dojo/database-design` (exercises with runnable checks) and `~/Projects/dojo/system-design` (a course mapped to quizzes, drills and interviews).

`$ARGUMENTS` may name the subject and goal. Ask for anything missing in one round of questions, no more.

## 1. Goal and level

Pin down, in one line each:

- **Goal:** interview, a project, a job task, curiosity. If interview: which role and level
- **What that goal actually tests.** Be concrete ("write a left join count by hand", not "know SQL"). Cut anything the goal doesn't test, however interesting
- **Time:** total hours available, and per session
- **Background:** what they already know well, so new ideas can be mapped onto it (for example SQL as a JS array pipeline)

Check the vault (`ab/career/Study/`, `ab/tech/`) for an existing roadmap or notes on the subject first, and link to it rather than duplicate it.

## 2. Syllabus

If a respected course, book or curriculum covers the subject (Hello Interview for system design, for example), pull its outline first and use it as the spine. Write it into the track as `docs/<source>-outline.md`: each section and lesson with links, what's locked or paywalled, and where the track covers it. Empty cells in that map are the gaps to plan for.

- Don't copy paywalled content. Note it's locked, and find the free material that covers the same ground (often the source's own worked examples)
- Reuse its section names and order so the learner can move between the course and the repo
- If there's no good syllabus, skip this step

## 3. Gaps

Three short lists: can do, can't do yet, needed by the goal. The plan only covers "can't do" items that are also "needed". If unsure where they stand, give one 10-minute diagnostic task and judge from that, rather than asking them to self-rate.

## 4. Plan

Three kinds of practice. Use the ones the goal needs:

| Kind | Length | What it's for | Feedback |
| --- | --- | --- | --- |
| Quiz | About 10 min, 8 short questions | Learning one lesson's concepts | Marked and answered after each question |
| Drill | 15 to 20 min, spoken | Testing one area under interview conditions | No hints, marked at the end |
| Exercise | 45 min to 2 h | The full thing the goal tests | A runnable check, or a graded interview |

Quizzes follow the syllabus one to one. Drills cover a syllabus section each, with their own setting that isn't any exercise's. Exercises are the plan below.

- 3 to 6 exercises, in order, each adding one or two new skills. A table: number, name, new skills, timebox
- Default to the format the goal tests (for interviews: sketch, build, a few checks, one question answered out loud). One deep dive at most, and only for something that needs real understanding
- No write-up or documentation steps unless the goal tests them. Ceremony before the skill is the main way these plans go wrong
- Every exercise needs a runnable check: a script, tests, a database rebuild, a compiler. Feedback comes from running it, not from Claude reading it. Spoken practice (interviews, drills, quizzes) can't run, so it gets an answer key instead (below)
- Mark what Claude writes (seed data, fixtures, setup, boilerplate: anything that teaches nothing) and what the learner writes (the skill itself)
- Space new concepts out: no more than two or three new ideas per session

Show the plan and get a yes before scaffolding.

## 5. Scaffold the practice repo

As a new track in `~/Projects/dojo/<subject>` unless told otherwise (follow the track shape in the dojo README, and add it to the README table):

- `README.md`: the goal, the exercise table, how to run the checks
- One folder per exercise: `README.md` (the brief: stories or tasks and the questions to answer), blank work files, `notes.md`, `grades.md`
- The run script, tested end to end
- Test data with traps: every question gets a case it could get wrong (empty groups, missing children, duplicates, edge values). Avoid coincidences that make wrong answers pass, such as ids that line up across tables
- `CLAUDE.md` with the teacher rules below, filled in for this subject
- If there are quizzes or drills: `quizzes/<name>.md` and `drills/<name>.md` hold only what the learner sees (the questions, or a drill's short setting) plus a "Notes after" section. Say in each when to do it, and if it gives away an exercise, say to do it after that one
- `grader/` for every answer key, with one file per quiz, drill and spoken exercise. A key holds facts to give only when asked, what a solid answer covers, pushes for vague answers, and a "Marking" section. Label it clearly and exclude it from editor search. The teacher rules say never to open it except to run or grade that item

### Teacher rules template for `CLAUDE.md`

```markdown
# <subject>

Practice repo. The owner is learning, so you are a teacher who grades, not someone who writes the answers.

## Context
- Goal: <goal, level, why>
- Background: <what they know well, to map new ideas onto>
- Grade at <level> depth. No nitpicks beyond what that level expects

## Rules
- Hints before answers. Never write the owner's <the skill: queries, components, proofs> unprompted, including "a corrected version". If they explicitly ask for the answer to a point after a real attempt, give it with a short why, and leave the rest to them
- Generic syntax and concepts are fine, with examples from a domain that is in no exercise (<pick one, e.g. a library>)
- Tooling help is fine (setup, the run script, the debugger)
- You write what teaches nothing when asked: test data, fixtures, boilerplate
- Don't spoil later exercises

## Quizzes and drills
- "start the <name> quiz": read `grader/quizzes/<name>.md`, ask the questions one at a time. After each answer, mark it Right, Partly or Wrong and give the key's answer briefly. End with the score and the misses for "Notes after"
- "start the <name> drill": read `grader/drills/<name>.md`, give only the setting, ask its questions one at a time as an interviewer. No hints until the end, then mark as the key says
- Never open `grader/` otherwise, and never quote a key before the learner has answered

## Grading
1. Read the brief and every file the owner wrote
2. Run the checks: <command>
3. Grade each area as Solid, Getting there or Not yet, one or two sentences each
4. At most 3 to 5 pointers, most important first
5. One question an interviewer or reviewer might ask, for the owner to answer out loud. It must not give away a fix
6. Append the grade to `<folder>/grades.md` with the date

## Hint levels
Start at 1. Go one further only when asked again or clearly stuck on the same point.
1. Where: name the area or file with the problem
2. Question: a question that leads to the problem
3. Concept: name the concept to read up on, with a docs link
4. Analogy: a small worked example in the other domain. Never the exercise's own code
```

## 6. Hand over

- Link the plan from the relevant vault roadmap or study note, as a checklist, in syllabus order with a priority for the time available
- Tell them how to start: the first quiz, drill or exercise, and the phrases ("start the X quiz", "start the X drill", "grade exercise 1")
- Suggest the `learning-retro` skill at the end of each session

## Don'ts

- Don't write the learner's answers into the scaffold, not even "examples" from the exercise domain
- Don't pad the plan with optional reading. Two or three resources at most, each tied to an exercise
- Don't add steps the goal doesn't test
