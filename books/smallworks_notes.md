# Small works notes (papers, essays, videos)

## Dansey & Eglin 2008 — A Systems Approach to Play for Game Design (9pp, read in full)
- Proposal: a collaborative IDEA-GENERATION GAME where playing = designing games. Iterated sessions: generate many ideas (each = 3-5 rules, 1 point per idea; need not be good/serious/feasible, just theoretically possible; any format; public domain; no copying existing games but inspiration allowed) → review the shared idea pool → repeat → vote "which would I actually play". Two winners: most ideas + most 'good game' votes. Comparing your ideas against the pool forces questioning assumptions/biases → double-loop learning → better designers over time.
- EMERGENCE principles cited (useful for us): Salen & Zimmerman — emergent systems provide variety, novelty, surprise; "a successfully emergent game will continue to offer new experiences as players explore permutations." Johnson (Emergence): needs "the right kind and right number" of interactions — BETTER A DENSELY INTERCONNECTED SYSTEM OF SIMPLE ELEMENTS THAN A SPARSE SYSTEM OF COMPLEX ELEMENTS. Rose: "game designs are usually most notable for what they DON'T include."
- Two interaction types: mental (player's mind × allowed game space — emergence through mental interaction ≈ creativity; keep the space unobstructed) and social (compare/comment). More iterations/time/wider access = more interactions = more emergence. Brainstorm-fast beats polishing each idea (keeps interaction count up).
- Spectra model (fig 2): complexity-of-restrictions × number-of-interactions. Everyday life = many interactions, many restrictions; confinement = restrictions without interactions; death = zero/zero; "freedom" = godlike. Traditional games = FEWER restrictions than real life (allow godlike fantasy) but limited interactions; MMORPGs = same restrictions + many more interactions (→ emergent player law systems, LambdaMOO); ideation games = freedom-driven interactions; this game aims at max interactions / min restrictions (few rules only for ethics + preventing breakdown).
- vs Group Support Systems: GSS judged externally on creativity/paradigm-breaking; games should be judged HOLISTICALLY — "would I actually play it? is it fun?" — a game design is more than the sum of its parts; voluntary participation (Huizinga) self-selects motivated judges → internal group consensus is valid evaluation.
- Use for us: formalizes our Challenge Lab / idea-pool approach; backs "measure designs by want-to-play votes, not expert checklists"; dense-simple-elements > sparse-complex = Mossfolk merge design confirmation.

## Wetzel FDG 2025 — Game Design Games: Designing Games for Teaching Game Design (10pp, CC BY 4.0, READ IN FULL — ACM DOI 10.1145/3723498.3723713)
User steer: "ركز اوي على الplayability و الchallenge fun وهكذا" — playability/challenge-fun findings flagged ★ below.

### Setup
- 4 Unity "game design games" (games whose play = doing design), built by students over semesters, each used in multiple classroom interventions; 164 participants, 12 interventions, reflexive thematic analysis (Braun & Clarke), Miro boards, German-majority data. Games public at itch.io/c/5559078/game-design-games.
- JumpCrafter = 2D platformer + built-in level editor (annotate cells with text comments + 3 highlight colors; JSON export + versioning; instant edit↔play switch). Teaches level design via Super Mario design patterns, 2D level-design patterns, Kishōtenketsu.
- FPS Balancing = multiplayer FPS, students balance weapons live. REMOVED from teaching (see 6.2).
- RaceKart = kart balancing, 0–100 sliders, laps 20–60s, can tweak WHILE racing.
- Pac-Mön = 7 Pac-Man variants, each targets a different player experience (MDA aesthetics / Gamer Motivation Profile); students analyze rather than build.
- Background: analog exercise-driven teaching is standard (Challenges for Game Designers; The Rules We Break; Cat On Yer Head; That Ball Game); digital versions rare (Harmony = transitive balance w/ AI-vs-AI eval; Game Studies; Doors; Taxonomy of Narrative Choices). Kolb experiential learning cycle: concrete experience → reflective observation → abstract conceptualization → active experimentation.

### The 4 themes
- **T1 The Unexpected Complexity**: hands-on design made students *feel* how hard design is. ★"the level should be challenging, so that it is fun, but not impossible" (JUMP-1-6-5) — students derive the challenge-fun-fairness triangle themselves within minutes of designing. ★Small balancing changes have outsized player-experience effects; balancing "almost impossible without testing."
- **T2 The Value of Experimentation**: theory+practice mix; rapid iteration loved; ★effects of a change must be observable fast or experimentation dies (FPS stats too noisy → tedious; RaceKart immediate → joy).
- **T3 The Diversity in Designing**: same brief → wildly different levels/karts; exchanging + annotating each other's designs = where the deepest learning happened ("evaluate a level → recognize weaknesses"); one student invented DESIGN CONSTRAINTS as a feature: "task like 'add an Enemy Valley and a Risk and Reward'… Or 'only use 20 blocks'".
- **T4 The Trouble with Perspectives** (full): students default to GAMER mindset, not designer. Compare any simple game to commercial benchmarks (Super Meat Boy wall jump "very good"; Hollow Knight input response; "not quite at the optimum that is Super Mario"). Improvement wishes = more features/content/polish (grenades, ducking, biomes, map creator, car skins) — ★i.e. players asked to improve a game almost always ask for MORE, which would make the *design problem* worse, not the game better. Students gamified balancing itself (point-buy budgets for stats — actually a good mechanic idea: ★"each configuration only has N points; the stronger an option, the more points it costs"). Few took true designer stance (asking for reference values, test shooting-range, statistics context). ★Players disliking a genre self-reported designing worse in it and enjoying it less ("I never quite 'got' racing games… so I did a poor job and knew it"). BUT: doing the design tasks themselves = joy ("when I got the cart feeling just right", "changing the weapon attributes is fun", "the game got increasingly more interesting").

### Per-game verdicts (discussion §6)
- JumpCrafter (best): seen as TOOL not game → designer mindset easiest; annotation = killer feature; resist feature requests — more options = less focused exercises; mitigation = instructor-gated features, block budgets.
- FPS Balancing (worst, removed): multiplayer → instant gamer mindset + competitive pull; genre familiarity → endless feature wishes; effects hard to observe (needs stats + large data); sessions long, connectivity issues. Lesson: ★a single-player version would serve balancing practice better.
- RaceKart: initially treated as game (fastest lap) but correct FRAMING flipped students to design task; simplicity is load-bearing — keep it; live-tweak while racing = immediacy win; weakness: design thinking not captured in-artifact (unlike JumpCrafter annotations).
- Pac-Mön: no build activity → gamer mindset harmless here; small mechanical deltas between variants ★taught how tiny rule changes transform experience.

### The 7 design considerations (verbatim-level)
1. **Develop Quality Games** — students compare against real games; be simple WITHOUT feeling inferior: solid feature set, good game feel, decent visual fidelity.
2. **Separate Tool and Game** — clear boundary between designing and playing, or users optimize their own play results instead of designing for the player.
3. **Limit the Design Space** — don't overwhelm with options; artificial constraints can help; too many options → meaningful changes too hard to observe.
4. **Foster Flexibility** — multiple valid ways to reach the design goal; encourages creativity + experimentation; balance against (3).
5. **Enable Rapid Iterations** — effect of a decision must be NOTICEABLE fast, no multi-playthrough confirmation loops; instant tool↔play switching crucial.
6. **Support Exchange of Designs** — sharing fast + frictionless; built-in annotation documents design decisions, fosters feedback.
7. **Connection to Theory** — support both theory-first (apply) and practice-first (construct theory); don't mandate either.

### Conclusion/limits
- Self-reported data only; instruction quality confounded with game quality; first-class students only; future: randomness/math (dice battler, RPG combat) as next domain; analog + digital complement each other.

### What this gives OUR studio (Mossfolk lens)
- ★T1 is literally our players' definition of fun: challenging-but-not-impossible is the first thing even novices name. Difficulty audit should ask this question per level.
- ★T4 = why player feature-requests are a trap: players ask for MORE (features/content), designers remove/constrain. Filter app-tester + review-mining suggestions through this: a "more stuff" wish usually signals an engagement gap, not a content gap.
- ★Consideration 3+4 = our level design law: constrain the space (block budgets! the students reinvented them) while keeping multiple viable solutions — exactly the Loop Sort houses/moves skill-expression finding.
- ★Consideration 5 = tuning pipeline requirement: a design change must show its effect in ONE quick run; if our tuner needs multiple long sims to see an effect, the knob is wrong (echoes "balancing impossible without testing").
- ★Genre affinity bias (T4): calibrate tester/raters per genre affection — a tester who dislikes the genre underrates and underperforms, by their own admission.
- ★Point-budget balancing (the students' invention) is a ready-made side-quest/variant mechanic: N points to distribute over stats, strongest options cost more.

## Kierkegaard (icycalm) 2007 — "The Stupidest Word in Videogames" (insomnia.ac/commentary/gameplay/, read in full via archive; the CAG thread the user sent is a repost of this — thread itself Cloudflare-blocked + not archived)
- Opens with Orwell (Politics and the English Language): sloppy language → sloppy thought → worse language, a feedback loop.
- Thesis: 'gameplay' is useless + misleading. Parody: "this book has good bookread / this record has good recordlisten / this movie has good moviewatch." "Great gameplay but shitty graphics" = "great game with shitty graphics" — the word adds nothing.
- Misleading because all-encompassing: "bad gameplay" carries no more information than "bad game"; no accepted definition; signals the writer can't be bothered to specify WHAT is wrong.
- Anonymous working designer quoted: 'gameplay' is the higher-up's "get out of jail free" card for not explaining a critique; in practice it means "it is/isn't like my favourite game in some way"; his fix = force SPECIFIC vocabulary: **mechanic, loop, system, world, rule, mode, flow, object, behaviour** (his exec producer called an explosion effect "wrong gameplay").
- Prescription: strike 'gameplay'; replace with 'game' or the specific term (mechanics, controls, level design…).
- FOR US: this is the language rule our audit pipeline already half-follows — make it explicit: any tester/director/review finding phrased as "الجيم بلاي" or "gameplay feels off" is UNFINISHED; it must name the mechanic/rule/control/feedback/curve. Same law as Norman (name the signifier failure), Koster (name the pattern exhausted), Schell (name the lens).

## Kierkegaard 2008 — "The Second Stupidest Word in Videogames" ('retro'; same source, read in full)
- 'Retro' = imitating the design of the recent past; applying it to 2D visuals or whole genres confuses REPRESENTATION with RULES/possibility-space. A new 2D game can be more evolved (possibility-space-wise) than a new 3D one.
- ★Buried metric worth keeping: "we can measure a game's complexity by measuring the maximum distance between the best and worst possible players — this is the measure of the depth of its possibility-space."
- FOR US: that metric is literally our skill-gap measurement (novice vs expert bot clear rates in Mossfolk level selection). Design depth = max(best player − worst player) outcome distance. Backs choosing level designs by measured skill gap; a mechanic that narrows the distance (pure luck or pure execution-trivial) adds no depth.
- Genre = core invariant rules; evolution happens in the non-core rules (create/destroy/modify) to expand or reshape possibility-space. Useful frame for "same mechanic, deeper layers" (Loop Sort lesson).
