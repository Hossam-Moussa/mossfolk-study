---
name: rules-of-play
description: >
  عدسات وقواعد تشغيلية من Rules of Play لـ Salen & Zimmerman (MIT Press 2004)، مدموجة من 3 دفعات digest في مستند واحد.
  بتستعمله في: تقييم فكرة لعبة واختيارها، كتابة ورقة قواعد لبروتوتايب، تشخيص بروتوتايب «مش ممتع»،
  ضبط الصعوبة وقراءة bot_difficulty، صيد الـ degenerate strategies بالتيستر-بوت، تصميم rival contests
  وside quests وminigames، الـ simulation والـ replay والـ share، الـ social play والـ metagame،
  مراجعة creative قبل CPI، المراجعة الثقافية (أسماء، شخصيات، شروط فوز)، ومراجعة أي feature بعدسة RULES / PLAY / CULTURE.
version: merged-1 (دمج الدفعات 1/3 و2/3 و3/3)
source_parts: نوتس الأجزاء 1–15 و17 من 17. الجزء 16 مش موجود في أي دفعة. كان فيه تكرار في نسخ الأجزاء 5 و6 و7 و10 و11 واتدمج.
use_when:
  - اختيار أو فلترة فكرة لعبة جديدة
  - كتابة scope أو ورقة قواعد لبروتوتايب
  - تشخيص «اللعبة مش ممتعة» أو «اللاعب تايه»
  - معايرة bot_difficulty أو اكتشاف degenerate strategies
  - تصميم rival contest أو side quest أو share أو social
  - مراجعة creative إعلاني قبل اختبار CPI
  - مراجعة ثقافية أو تمثيلية
---

# SKILL: rules-of-play — المستند التشغيلي الموحّد

## §0. إزاي تستخدم المستند

**ترتيب الاستخدام**
- مستعجل؟ ابدأ من §9 (Cheatsheet).
- هتاخد قرار؟ روح §5 (جداول القرار).
- هتفحص بروتوتايب أو ليفل؟ استخدم §6 (Checklists).
- عايز التفاصيل؟ القواعد المرقّمة في §4، من R001 لحد R222. كل قاعدة جنبها مصدرها والمثال اللي اتبنت عليه.

**العلامات**

| العلامة | المعنى |
|---|---|
| ★★★ | بتخدم خط «لعبة جديدة كل يوم/أسبوع» مباشرة: اختيار أفكار، بروتوتايب، CPI، تيستر، إعلانات |
| ★★ | مهمة للتصميم العام ولـ Mossfolk |
| ★ | خلفية أو مرجع |
| 🟢 MF | تطبيق على Mossfolk: 9 أحجام، drop budget، تحديات mossy shells/stones/rot من ليفل 2501، 3000 ليفل، bot_difficulty، side quests hub، rival contests، minigames |
| [رأي النوتس] | اقتراح أو رقم من كاتب النوتس، مش من الكتاب |
| [مكمَّل] | البند ده اتحال عليه في الـ digests ومحتواه مجاش، فاتكمّل من نص الكتاب. لازم يتراجع على الأصل |
| [فجوة] | محتوى مقطوع في المصدر ومش موجود في أي دفعة |

---

## §1. النطاق والفجوات

### 1.1 التغطية

| الجزء من الكتاب | التغطية |
|---|---|
| Foreword، Preface، Ch.1–11 | كاملين |
| Ch.12 Rules | لحد «Specificity of Rules». الباقي [فجوة]: بقية Specificity وDesigning Elegant Rules |
| Ch.13 | من النص للآخر. أوله لحد «What kind of contex…» [فجوة] |
| Ch.14–19 | كاملين. ذيل Ch.19 (من Rational player) جه من الدفعة 2 |
| Ch.20 Conflict | كامل (Level Playing Field + LOOP + Pig Redux) |
| Ch.21 Breaking the Rules | كامل |
| Commissioned Game 2: Ironclad | كامل. نسخة من النوتس كانت قاطعة قواعد الروبوتات، والمعتمد هنا النسخة الكاملة |
| Unit 3 + Ch.22 Defining Play | كامل تقريبًا. الجزء بين «Games ⊂ Play» و«Being Playful» [فجوة] |
| Ch.23 Experience، Ch.24 Pleasure | كاملين |
| Ch.25 Meaning | لحد Caucus Race (Alice). الباقي [فجوة] |
| Ch.26 Narrative | كامل، بما فيه Retelling/Replay/Recam اللي جه من الدفعة 3. LEGO Drome مقطوع عند «race analysis» |
| Ch.27 Simulation | كامل ما عدا قسم Wargames اللي مقطوع بعد Dunnigan، وPilotwings اتذكرت بس كمثال |
| Ch.28 Social Play | كامل |
| Commissioned Game 3: Sneak | قواعد التصميم والأرقام بس. نص القواعد الكامل مش موجود |
| مقدمة Unit 4 + Ch.29–30 | كاملين |
| Ch.31 Open Culture | البداية بس (Eno). الباقي [فجوة] |
| Ch.32 Cultural Resistance | لحد Alteration strategies حسب نطاق الدفعة 3، بس محتواه مجاش في الـ digest [فجوة] |
| Ch.33 Cultural Environment، Commissioned Game 4 «Caribbean Star» | [فجوة] |
| Back matter (Bibliography، List of Games، Index) | جه منه بس اللي استُخدم في جدول التعارضات |

**مراجع اتحال عليها جوه الـ digests ومحتواها مجاش:**
- الدفعة 1: §4.5 و§4.7 و§4.10 و§4.11 و§8 و§9.
- الدفعة 2: §2 و§3 و§5 و§7، والقواعد من بعد R84.
- الدفعة 3: §3 (الجداول T1–T7)، §4-G، §5، §9، والقواعد من بعد R50.

اللي بقدر أكمّله من الكتاب بثقة متعلّم [مكمَّل]، والباقي متعلّم [فجوة].

### 1.2 هيكل الكتاب وخريطة الـ Schemas

**الهيكل:** 33 فصل، و4 Commissioned Games، وBibliography، وList of Games Cited، وIndex، وقوائم Figures/Tables/Sidebars. الـ TOC بيكرر «Further Readings/Further Reading».

| الوحدة | الفصول | الـ Commissioned Game |
|---|---|---|
| Unit 1 Core Concepts | Ch.3–10 | CG1 (Garfield) |
| Unit 2 Rules | Ch.11–21 | CG2 «Ironclad» (Frank Lantz) |
| Unit 3 Play | Ch.22–28 | CG3 «Sneak» (Kira Snyder) |
| Unit 4 Culture | Ch.29–33 | CG4 «Caribbean Star» |

**الـ Primary Schemas (Ch.10):** RULES / PLAY / CULTURE.

| الـ Schema | الفصول اللي تحتها |
|---|---|
| RULES | Emergent (14)، Uncertainty (15)، Information Theory (16)، Information Systems (17)، Cybernetic (18)، Game Theory (19)، Conflict (20)، Breaking the Rules (21) |
| PLAY | Defining Play (22)، Experience (23)، Pleasure (24)، Meaning (25)، Narrative (26)، Simulation (27)، Social Play (28) |
| CULTURE | Cultural Rhetoric (30)، Open Culture (31)، Cultural Resistance (32)، Cultural Environment (33) |

---

## §2. تعارضات المصادر وتنبيهات الأمانة (اقراها الأول)

| # | النقطة | الطرف أ | الطرف ب | القرار التشغيلي |
|---|---|---|---|---|
| 1 | هل الـ Puzzle لعبة؟ | Scott Kim: الـ puzzle ليه إجابة صح والـ game لأ (Poker) | الكتاب: كل الـ puzzles ألعاب، بس subset خاص | استخدمها كأداة تشخيص (R016) |
| 2 | Roulette | النوتس (الدفعة 1) بتنقل عن الكتاب: 31 رقم، 15 أحمر، 15 أسود، وصفر. الأحمر = 15/31 = 48.39% | تنبيه من برّه النوتس: الروليت الحقيقي 37 خانة في الأوروبي (الأحمر 18/37 ≈ 48.65%) أو 38 في الأمريكي | الرقم محفوظ زي ما هو كمثال Risk. لو هتحسب حاجة حقيقية، راجع الأصل |
| 3 | الـ pure chance | Caillois: الحظ الخالص مالوش علاقة بقرار اللاعب | الكتاب: حتى الـ pure chance فيها لحظات اختيار (Chutes، اللوتري) | صمّم لحظات اختيار (R049) |
| 4 | القواعد كـ information | Pearce: القواعد «Known to all» information | المؤلفين: القواعد مش information | صنّف المعلومة بس، مش القواعد (R062) |
| 5 | حل Prisoner's Dilemma | — | حلها لسه مختلف عليه | ما تبنيش ميكانيك على «حل» PD |
| 6 | الثيم والـ structure | Lantz (Ironclad): مش بينفصلوا بسهولة | Breakout × 3: نفس الـ structure بثلاث ثيمات (سجن، تنس، force field) | اختبر الثيمات على مستوى الإعلان، بس ما تفترضش إن الـ mechanic شغال تحت أي ثيم (R123 + R192) |
| 7 | الدفع عشان تكمّل | Gauntlet: الـ quarters والصعوبة المتصاعدة بتضمن إنهم يدفعوا | خط حسام ضد الابتزاز وتعقيد الطاقة | الـ continue بإعلان rewarded مقبول بشرط يبقى اختياري ومن غير حجب (R100) |
| 8 | الحد الأدنى للاعبين في Sneak | مقدمة القواعد: «3 or more» | Setting up: «4 or more» | تناقض جوه نفس المصدر. صمّم لـ 4+ واعتبر 3 حالة حدية |
| 9 | عقوبة النداء الغلط في Sneak | Playtest 2: −5 | الدفتر: «خفّضنا بنقطة»، والنهائي −2 إضافي (−3 إجمالي) | الأرقام مش متسقة حسابيًا. اعتمد النهائي: الصح +3 (يبقى +8)، والغلط −2 (يبقى −3). تعدادات المحتوى (زي 65) فئاتها متداخلة ومش بتتجمع |
| 10 | اسم دراسة Linda Hughes | النوتس: «Rooie Rules» | Further Reading: «Rookie Rules» | نفس الدراسة (Foursquare، ideal vs real rules). استخدم Rooie Rules زي الـ Index |
| 11 | كتاب Gary Alan Fine | «Shared Fantasies» (1983، ص186) | «Shared Fantasy» (Further Reading) | نفس الكتاب |
| 12 | تاريخ Chaturanga | Ch.30: الهند، القرن الخامس | List of Games: c.650 | اذكر الاتنين |
| 13 | لعبة Icehouse الشبيهة بالشطرنج | Ch.31: Martian Chess | List of Games: Martian Backgammon | غالبًا لعبتين مختلفتين أو خطأ نقل |
| 14 | لعبة الكروت السردية | Ch.31: Once Upon a Tale | List of Games: Once Upon a Time | غالبًا خطأ نقل. الاسم التجاري المعروف Once Upon a Time |
| 15 | سباق «الوقود» ولا «العاطفة» | Harvey Smith: بيفضّل محاكاة الوقود والـ wind shear | الكتاب: الاتنين مثيرين، بس ما ينفعوش في نفس اللعبة | اتجاه واحد لكل لعبة |
| 16 | معنى «simulation» | LeBlanc: simulation = generalized بس، وemulation = case-based | الكتاب: simulation أوسع وبتشمل الاتنين | لما تقرا LeBlanc ترجمها generalized |
| 17 | Lara Croft | Toby Gard: «empowered woman… gun-toting bitch بعيدة المنال» | المؤلفين: «action slut، digital pin-up» مع ازدواجية تحدي/تكريس | مفيش حسم. المطلوب وعي بالـ rhetoric |
| 18 | الـ Immersion | Laramée وSpector (الـ holodeck حتمي)، ومدير تنفيذي: «الألعاب هتنضج لما الوشوش تعبّر عن مشاعر» | Gorfinkel والمؤلفين: الـ immersion أثر بين اللعبة واللاعب، وممكن تنغمس في Tetris | اعتمد موقف الكتاب (R185) |
| 19 | Little Max: إمتى تتحدّى | Knizia نظريًا: تحدّى لو اللي قبلك محتاج يتخطى 6-1 أو أحسن (50%) | Knizia عمليًا: الناس بتـ duck، و«Ducking among ducks is the best strategy» | صمّم للسلوك مش للحساب |
| 20 | Ms. Pac-Man | أيقونة نسوية أو خليفة أفضل | marked case (روج + فيونكة = أنوثة)، رمز استهلاك، لحظة البوب الياباني | النص الثقافي ليه قراءات متعددة |
| 21 | Mad Magazine Game | بتقوّض الرأسمالية بالسخرية | يمكن بتعززها | الكتاب نفسه بيقول «غير واضح» |
| 22 | أصل أدوار اللاعبين | Sutton-Smith: أدوار internally derived من ألعاب أطفال | Bartle: أدوار externally derived وmacro من MUDs نصية | مش تعارض، تمييز. Sutton-Smith لميكانيكا التفاعل، وBartle لتقسيم الجمهور |
| 23 | تسمية rhetoric الخيال | Ch.30: Play as the Imaginary | الـ Index: imagination | نفس المفهوم |
| 24 | إملاء «Constituative» | الكتاب كاتبها كده | الإملاء المعتاد Constitutive | المستند ماشي على إملاء الكتاب |

**تنبيه أمانة:** البند «sabotage خفيف كـ forbidden play في rival contests» مكتوب في النوتس صراحة إنه «فكرة تصميمية مني، مش من المصدر».

---

## §3. القاموس الموحّد ★★★

> **ليه قاموس؟** Jenkins (مؤتمر MIT، 10–11 فبراير 2000) قال إن الـ vocabulary المشترك ليه 4 فوايد:
> 1. **Training**
> 2. **Generational Transfer**: بدل ما كل واحد يحل نفس المشكلة من الأول
> 3. **Audience-building**
> 4. **Buffer Against Criticism**: ضد الـ censorship والـ regulation
>
> Warren Spector (RE:PLAY 2000) وصف بناء الـ vocabulary بإنه «absolutely vital».
> 🟢 MF: أي حاجة البوت بيتعلمها تتسجل بالمصطلحات دي (merge، drop budget، bot_difficulty…).

| المصطلح | التعريف التشغيلي |
|---|---|
| **Meaningful play (descriptive)** | المعنى بيطلع من العلاقة بين action اللاعب وoutcome النظام. بيوصف كل لعبة |
| **Meaningful play (evaluative)** ★★★ | بيحصل لما علاقة action→outcome تبقى discernable وintegrated في سياق اللعبة الأكبر. ده هدف التصميم الناجح |
| **Discernable** | نتيجة الفعل بتوصل للاعب بشكل محسوس: «إيه اللي حصل» |
| **Integrated** | الفعل ليه أثر فوري وبيأثر على اللعب بعدين: «ده هيأثر على الباقي إزاي» |
| **Design** | «the process by which a designer creates a context to be encountered by a participant, from which meaning emerges» |
| **Game** ★★★ | «a system in which players engage in an artificial conflict, defined by rules, that results in a quantifiable outcome» |
| **Game design** | خلق لعبة يقابلها لاعب ويطلع منها meaningful play. وكمان «Game design هو play design» (Hans) |
| **Play** | «free movement within a more rigid structure» |
| **System** (Littlejohn) | Objects، Attributes، Internal relationships، Environment |
| **Space of possibility** ★★★ | كل الأفعال والمعاني الممكنة. المصمم بيبنيها بشكل غير مباشر من خلال القواعد. وهي كمان space of possible conflict |
| **Magic circle** | حدود اللعبة في الزمان والمكان، والقواعد ليها سلطة جوّاها. finite space with infinite possibility |
| **Lusory attitude** (Suits) ★★★ | قبول قواعد بتطلب وسائل أقل كفاءة عشان النشاط يبقى ممكن: «voluntary effort to overcome unnecessary obstacles» |
| **Autotelic** | auto = self وtelos = goal. اللعب غاية في حد ذاته |
| **Schema** | عدسة تحليل أو صنع. فيها variables وembed ومستويات تجريد كتير، وknowledge مش definitions |
| **RULES / PLAY / CULTURE** | Formal / Experiential / Contextual |
| **Operational rules** | قواعد اللعب المكتوبة، بتتعامل مع الخامات والـ input/output |
| **Constituative rules** | البنية المنطقية والرياضية تحت السطح |
| **Implicit rules** | etiquette وsportsmanship. لا نهائية وبتتغير حسب السياق |
| **Emergence** | أنماط مش متخططة بتطلع من قواعد بسيطة على عناصر محدودة: «coupled, context-dependent interactions» |
| **Engine** (Lantz & Zimmerman) | تركيبة عناصر متشابكة بتنتج أثر أكبر. بتتكتشف ومش بتتصمم مباشرة |
| **Second-order design** ★★★ | المصمم بيصمم القواعد اللي بتولّد الـ play، مش الـ play نفسه |
| **Information** (Shannon) | مقياس عدم اليقين وحرية الاختيار، مش المعنى |
| **Information** (كمعرفة) | المحتوى اللي اللعبة بتخبيه وتكشفه وتعمله random وتنقله |
| **Feedback loop** | sensor → comparator → activator. الـ Positive بيضخّم والـ Negative بيثبّت |
| **Saddle point / Degenerate strategy** ★★★ | قرار أمثل ثابت مهما كان الخصم أو الحالة. بيقتل الـ uncertainty، فتجنّبه |
| **Utility** | مقياس رقمي لرضا اللاعب عن النتيجة |
| **Strategy** (game theory) | خطة كاملة من أول اللعبة لآخرها ضد أي خصم. ≠ heuristic |
| **Core mechanic** | النشاط الجوهري اللي بيتكرر. ممكن يبقى فعل واحد أو compound |
| **Flow** (Csikszentmihalyi) | شريط قطري ضيق بين anxiety وboredom |
| **Entrainment** (Moriarty) | اللعبة «entrainment engine» بتقوّي الأنماط وبتهدّي الـ dissonance |
| **Metagame** | «the game beyond the game»: اللي اللاعب بيجيبه وبياخده، وبين الجلسات وأثناءها |
| **Simulation** | «a procedural representation of aspects of "reality."» |
| **Immersive fallacy** | الاعتقاد إن المتعة في نقل المشارك حسيًا لواقع وهمي واختفاء الـ frame |
| **Metacommunication** (Bateson) | رسالة «إحنا بنلعب» اللي بتغلّف الفعل |
| **Play community** (DeKoven) | أي مجموعة بتتجمع تلعب. «مجتمع مؤقت بكود بنألفه وإحنا ماشيين» |

---

## §4. القواعد التشغيلية المرقّمة

### A. العدسة الأم: RULES / PLAY / CULTURE

**R001 ★★★ أي feature أو فكرة تعدّي على التلات عدسات قبل ما تتعمد.**
- **RULES:** البنية المنطقية والرياضية. ينفع تتقاس بالبوت؟
- **PLAY:** التجربة والاجتماع والتمثيل. اللاعب هيحس بإيه؟
- **CULTURE:** توقعات جمهور hyper/hybrid-casual، عُرف ألعاب الـ merge، الإعلانات، الـ store.
- مثال الكتاب (typeface): RULES = أوزان الحروف بالنسبة لبعض، PLAY = تجربة القراءة، CULTURE = المراجع التاريخية.
- العدسات مش taxonomy ومش متنافية. مفيش حاجة اسمها «ده RULES مش PLAY». دي أدوات تركيز.
- 🟢 MF:
  - RULES = الدمج، الـ 9 أحجام، drop budget، الأهداف.
  - PLAY = إحساس الإسقاط، الـ rival contests، الـ side quests.
  - CULTURE = عُرف الجمهور.

**R002 ★★★ التأطير متداخل: formal rules ⊂ system of play ⊂ cultural framing.**
- أي قرار في طبقة ليه صدى في الطبقتين التانيين.
- Per Bak: «لا يوجد unit على أي مستوى له حق الأولوية».
- مثال: «إيه معنى إن الأبيض دايمًا بيتحرك الأول؟»
- 🟢 MF: قبل أي تغيير اسأل «أثره على التلات مستويات إيه؟». «الرياضيات شغالة» لوحدها مش كفاية.

**R003 ★★★ `bot_difficulty` أداة RULES-schema، يعني closed system.**
- البوت مش شايف PLAY ولا CULTURE.
- اللاعب عايش open experiential system فيه إعلانات ومقاطعات وسمعة.
- أي قرار مبني على رقم البوت لوحده لازم يتعاير ببيانات لاعبين حقيقيين. شوف R180.
- جدول Open/Closed في §5-T01.

### B. Meaningful Play وتشريح الاختيار

**R004 ★★★ كل نتيجة لازم تبقى discernable.**
- من غير كده اللاعب «بيضغط أزرار عشوائي».
- Rouse ضرب مثالين:
  - strategy game فيها وحدات بتتهاجم برّه الشاشة واللعبة ما بتعرّفش.
  - RPG فيه جوع مش واضح لحد ما عضو يموت فجأة: «Why should the player have to guess at such game-critical information?»
- **Asteroid:** لو ضربته وما اتغيرش مش هتعرف. الحل صوت أو اهتزاز أو انفجار أو التلاتة.
- 🟢 MF:
  - الـ 9 أحجام = 9 درجات feedback.
  - في الـ chain-merges الفوضوية لازم يبان «إيه اللي حصل وليه».
  - ممنوع rot ينتشر أو mossy يتقشّر «برّه الشاشة».
  - فحص سريع: «أي نتيجة مش مقروءة في أول ثانيتين؟»

**R005 ★★★ كل فعل لازم يبقى integrated (اختبار Decathlon).**
- لو السباق الأول ما لوش علاقة بالباقي، اللاعبين هيمشوا فيه بالراحة.
- لو النقط بتتجمع في سكور تراكمي، يبقى integrated.
- Chess عميقة لأن الافتتاح بيودّي للـ middle game والـ middle game بيودّي للـ end game.
- 🟢 MF:
  - نتايج الـ side quests والـ rival contests والـ minigames لازم تتحول لحاجة في الـ progression، وإلا هتتجاهل.
  - كل إسقاط بيأثر على اللي بعده.
  - مكافأة الـ rewarded ad لازم تبقى discernable فورًا وintegrated.

**R006 مفيش صيغة واحدة للـ meaningful play.**
- asteroid محتاج feedback فوري حسّي.
- لعبة story ممكن نتيجة فعل من أولها تتفهم في آخرها بشكل درامي.
- طبقات الـ meaningful play:
  - formal: حركة Chess.
  - اجتماعي: اللعبة منتدى تواصل.
  - ثقافي: Chess كدعاية في الـ Cold War، وجدل AI ضد العقل البشري.

**R007 ★★★ شخّص أي بروتوتايب «مش ممتع» بـ Anatomy of a Choice.**
- الأسئلة الخمسة في §5-T02، والـ failure states في §5-T03.
- الخطوة 5 بترجع للخطوة 1.
- Juul: اللعبة state machine.
  - في Chess الحالة الداخلية والخارجية متطابقين.
  - في Asteroids الشاشة امتداد للـ state الداخلي.

**R008 ★★ صمّم على مستويين micro وmacro، وكل فعل يشتغل على الاتنين (Go).**
- Go: tactics (معارك قطاعات) وstrategy (شكل الرقعة كلها).
- Blackjack: الـ micro = hit أو لأ، والـ macro = الفلوس عبر الجولات، والـ card counting بيربط الإيدين ببعض.
- Football: اختيار الـ play جماعي (staff + QB) ضد النتيجة والساعة والـ down، وبعد الـ snap تنفيذ لحظي.
- الاختيار مش لازم يبقى عقلاني: twitch زي مسدس Time Crisis، أو رمية نرد.
- فشل الـ parse في text adventure («grab rock» بدل «get rock») ليه معنى، لأنه بيرسم حدود اللعب.
- 🟢 MF: الإسقاطة micro، والـ budget والهدف macro. كل إسقاطة تدمج **و**تقرّب من الهدف.

**R009 ★★★ الاتساق بيولّد planning-intention.**
- المصدر: Doug Church، «Formal Abstract Design Tools»، Gamasutra، 16 يوليو 1999. نفس المقال مصدر الـ short-term goals في R144.
- Tekken: لما Eddy Gordo يعمل cartwheel kick إنت عارف هتاخد إيه.
- **الخسارة اللي ليها معنى بترجّع اللاعب:**
  - لو عرفت ليه خصمك أحسن منك، بتقيّم نفسك وبتلعب تاني.
  - لو مش عارف ليه خسرت، غالبًا مش هترجع.
- الـ macro بيشمل قرار «ألعب أصلًا ولا لأ ومع مين».
- 🟢 MF: الفيزياء الفوضوية بتهدد الـ consistency. لازم خط توقع أو مسار تقريبي قبل الإسقاط.

**R010 Crawford: interactivity = listen / think / speak، وجودتها = جودة كل مرحلة (مثال Joe وFred).**
- 🟢 MF:
  - listen = input سريع.
  - think = الفيزياء.
  - speak = feedback واضح.
- Sudnow (Breakout): توقيعك في 2 و3/7 بوصة، ومفيش «heft» في الزرار.
- غياب الـ tactile marker بيتعوّض بـ haptics وتأثير بصري يضخّم الدمج.

**R011 ★★ التفاعل بيتجرّب مش بيتراقب.**
- ده نقد للـ over-the-shoulder journalism.
- مفاهيم Sudnow: directed choice، player control، amplification of input، system representation، direct visible feedback.

**R012 Multivalent Model: 4 أنماط بتتداخل في كل لحظة.**
- الجدول في §5-T04.
- Poker (fold ولا لأ): حجم الكروت functional، والـ face cards cognitive، وفكرة «الـ card shark الأنيق» cultural.

**R013 ★★ القاعدة هي اللي بتحوّل الفعل لتفاعل مصمم.**
- تفاحة بتقع مش تصميم.
- رمية Craps تصميم، لأن فيه قاعدة «عُد النقط اللي فوق» وسياق.
- التفاحة بتبقى لعبة لو قلت «عِدّوا كام مسكة ورا بعض قبل ما تقع».
- «حتى في أبسط السياقات التصميم بيخلق معنى».

### C. التعريف والحدود

**R014 ★★★ فحص «هل دي لعبة؟» بالعناصر الستة:**
1. System
2. Players
3. Artificial
4. Conflict (تعاون أو منافسة، ضد النظام أو multiplayer)
5. Rules
6. **Quantifiable outcome**، وده غالبًا اللي بيفرّق game عن play

- 🟢 MF: system (jar + physics + merges)، conflict (الـ budget ضد الأهداف)، rules، outcome (هدف ونجوم).

**R015 ★★★ العائق هو المتعة.**
- الـ drop budget هو الـ unnecessary obstacle بتاع Suits.
- أي تعديل بيكسره، زي إسقاطات إضافية بإعلان، لازم ما يبقاش «شراء تجاوز العائق».
- **خط سياسي يتقرر مع حسام.**

**R016 ★★★ الـ Puzzle أداة تشخيص (التعارض #1).**
- Solitaire (Kevin Maroney): أي deck يا ليه حل محدد يا مالوش، والـ shuffle مولّد puzzle عشوائي.
- جدول التشخيص puzzle/toy في §5-T05.
- 🟢 MF: البوت يقيس:
  - حل واحد بيتكرر في كل الرانات = puzzle زيادة.
  - مفيش اتجاه = toy زيادة.

**R017 Limit cases.**
- **RPG** (D&D، Ultima، EverQuest):
  - Gygax (AD&D Player's Handbook 1978، ص7): «open-ended. There is no winner».
  - لكن مهام الـ session ومستويات القوة outcomes متراكمة.
  - Costikyan: «No victory conditions… but goals; lots of them, you get to pick».
  - الأكتر لعبية = tournaments في المؤتمرات. الأقل لعبية = storytelling.
- **SimCity** (Will Wright): أقرب للـ toy، واللاعبين بيحولوه لعبة بأهدافهم.
- الحدود fuzzy، وده أرض خصبة للأفكار.
- 🟢 MF: sandbox من غير أهداف = toy. والـ side quests والـ rivals بتضيف outcome للـ meta.

**R018 ★★ «Uncertain» عند Caillois هو `bot_difficulty` الحقيقي.**
- السؤال: النتيجة مش محسومة **لنوع اللاعب ده بالذات**؟ (Chess master ضد مبتدئ.)
- ده مش مجرد سهل/صعب.

**R019 ★★ Safety (Crawford): نتايج اللعبة أخف من اللي بتنمذجه.**
- 🟢 MF: الخسارة أخف من أي عقاب حقيقي، وده متماشي مع خط حسام ضد تعقيد الطاقة.

### D. الـ Magic Circle والـ Lusory Attitude

**R020 ★★★ الدايرة هشة ومحتاجة maintenance مستمر.**
- Sniderman: صفارة «Play Ball» مش هي بداية اللعبة الحقيقية. المشاركين بيراقبوا طول الوقت إن شروط اللعب لسه متحققة.
- Apter: الـ protective frame ممكن يبقى proscenium arch، أو سور حديقة، أو خط الكريكيت، أو القواعد نفسها.
- 🟢 MF ★★★:
  - interstitial أو popup في نص ليفل بيخرّم الـ frame.
  - نقطة الخروج المشروعة الوحيدة بين الليفلات.
  - لكل نقطة إعلان أو شراء اسأل: دي «pause رسمي» (زي ماتش تنس واقف عشان المية) ولا اقتحام؟

**R021 الـ Pause = تعليق رسمي.**
- لاعب Tetris بيوقف ويكمل زي لاعب التنس.
- ده غير screensaver لعبي مالوش بداية ولا وسط ولا نهاية.
- 🟢 MF: شاشة الـ pause عندنا تعليق رسمي؟

**R022 ★★★ متعة اللعب بتطلع من الفجوة بين الفعل والنتيجة.**
- Missile Command: الصاروخ بيطلع ببطء من تحت.
- البولينج: بتقف بعيد وتسيب الكورة تتدحرج.
- الملاكم بالقفازات مش بالمسدس.
- الجولف: 300–400 يارد بدل ما تحط الكورة بإيدك.
- 🟢 MF: الفجوة بين الإسقاط والاندماج (المخلوق بيقع ويرتد) هي مصدر المتعة. أي «تحسين» زي snap أو auto-merge بيشيلها.

**R023 ★★ اختبار الدايرة في الـ playtest: اللاعب بيلوم نفسه ولا بيلوم اللعبة؟**
- لو الـ budget بقى «ظلم» بدل «قيد ممتع»، الدايرة اتكسرت.

**R024 ★★ الـ rival contests عقد اجتماعي (دايرة البلي).**
- محتاجة لحظة دخول صريحة: دايرة بالطباشير، وكل واحد يحط بلية، و«for keeps».
- الـ lusory attitude معناها تقبل القواعد لأن اللعب غاية في حد ذاته.
- اللعبة من غير لاعيبة زي نوتة موسيقى مستنية حد يعزفها.
- كمّلها بـ Bateson والـ frames في R187.

### E. القواعد (Ch.11–13)

**R025 ★★★ ورقة قواعد من صفحة واحدة قبل أي بروتوتايب.**
- الصيغة: قاعدة = فعل + نتيجة.
- «لو مش قادر تحدد الـ core rules، إنت فاقد الاتصال بتصميمك».
- الورقة دي قريبة من specs الـ programmable prototype.
- 🟢 MF، Rules of Mossfolk:
  - الجرة.
  - موضع الإسقاط.
  - الدمج: اتنين من نفس الحجم يبقوا الحجم اللي أكبر.
  - 9 أحجام.
  - drop budget.
  - شرط الهدف.
  - شرط الخسارة/overflow.
  - قواعد mossy shells/stones/rot.
- [فجوة]: قايمة قواعد Tetris اللي كانت في §8 الأصلي مجاتش.

**R026 ★★★ اختبار الاستبدال.**
- بدّل القاعدة بـ 3 بدائل. لو اللعب اتغير، دي قاعدة حقيقية ورافعة تصميم.
- مثال: الـ randomizer في Tetris. بدائله (دورة ثابتة، شكل واحد، اللاعب يختار) بتغيّر البنية.
- 🟢 MF: **الـ drop queue قاعدة رسمية**، وهي أكبر متغير بيأثر في `bot_difficulty`:
  - عشوائي، ولا bag، ولا ترتيب ثابت، ولا اللاعب يختار.
  - وعدد الـ preview.

**R027 ★★★ افصل الـ skin عن الـ system.**
- الجرافيك والصوت عادةً مش قواعد:
  - Game & Watch Gallery: Classic وModern بنفس القواعد.
  - أسامي الـ suits لو بقت Death/Love/War/Sex نفس اللعبة.
  - أعواد Popsicle متعلّمة 4×13 نفس اللعبة.
- **الاستثناء:** الشكل بيبقى قاعدة لما بيغيّر المعلومة المتاحة للقرار أو الأداء:
  - حجم sprite في Berzerk قاعدة. اللون مش قاعدة إلا لو بقى invisible.
  - الانعكاس في البِركة قاعدة لو هو الدليل الوحيد إنها سحرية.
  - ظلال Thief قاعدة (private مقابل public info).
  - قطعة Chess لازم تشغل مربع واحد وتتميز عن غيرها.
- 🟢 MF:
  - حجم وcollider المخلوق قاعدة.
  - الشكل واللون قاعدة **لو** هما اللي بيفرّقوا الـ 9 أحجام. لو 6 و7 اتلخبطوا، دي قاعدة وظيفية اتكسرت.
  - شكل mossy وrot قاعدة لو هو الإشارة الوحيدة، فيتعدّى على playtest قبل التلميع.
- ★★★ Pipeline:
  - placeholder graphics في البروتوتايب والبوت.
  - reskin لاختبار CPI بنفس النظام بيفصل أثر القاعدة عن الغلاف.
  - البوت شغال على طبقة القواعد بس.

**R028 ★★ قواعد الاستراتيجية مش قواعد اللعبة.**
- «لو خصمك هيكسب، اقفل عليه» دي strategic rule للـ AI.
- 🟢 MF: لو البوت لقى استراتيجية بتكسر ليفل، ده كشف strategy مش bug. القرار عندك تحميها ولا تقفلها (R043).

**R029 ★★★ الخصايص الست للقواعد، audit لكل قاعدة جديدة (§6-C05).**
- الغموض يتحل قبل اللعب.
- القاعدة غير الملزمة بتجيب غش.

**R030 ★★ تلات مستويات قواعد. هوية اللعبة = operational + constituative.**
- Parlett: «كل لعبة **هي** قواعدها».
- الـ implicit مستبعدة من الهوية لأنها مشتركة.
- نفس الـ constituative بـ operational تانية (Die & Scoresheet / Cards & Chips / Spinner & Pegs) بتتحس «مش Chutes and Ladders».
- المادة اللي بيعيش بيها اللاعب المنطق مهمة قد المنطق نفسه.
- 🟢 MF:
  - iOS وAndroid وWeb = نفس الـ formal identity، زي مثال Go.
  - أي تعديل في الـ budget أو أحجام الدمج = لعبة جديدة، مش «تحسين».

**R031 الـ implicit rules ممكن تتكتب حسب الجمهور.**
- Chutes كاتبة setup صريح للأطفال: «حط اللوحة بحيث الكل يحرّك بسهولة»، والقطع الزيادة out of play جنب المربع #1.
- شجرة الـ baseball ممكن تبقى ضمنية للأطفال وoperational للاعب جديد.
- «القواعد والتعليمات نفسها لازم تتصمم وتتختبر وتتنقح». شوف Cold read في R214.

**R032 ★★★ كسر الـ implicit rules مصدر أفكار.**
- أمثلة: مؤشر مش مطابق للماوس، أو نص شات بيوصل مختلف عن اللي اتكتب.
- الـ implicit في الديجيتال:
  - المؤشر بيتبع الماوس.
  - البرنامج بيتشغل ويتنسخ ويتمسح ويتسمى.
  - اللعب ما بيأثرش على الجهاز بشكل دائم.
- **مخاطرة في hyper-casual:** اختبره كـ hook إعلاني أو side quest الأول، وما تخليهوش إحباط في الـ core.

**R033 ★★★ موضع الخط هو الصعوبة (Suits).**
- خطوط فضفاضة = ملل، ومع «utter laxity» اللعبة بتنهار.
- خطوط مشدودة = اللعبة «بتتعصر لحد ما تخرج من الوجود».
- «رسم الخطوط بمهارة جوهر صنعة الـ gamewright».
- 🟢 MF: الـ target مش نسبة فوز ثابتة. تيوتوريال فضفاض، وذروة مشدودة.

**R034 الوضوح الاصطناعي نقطة بيع.**
- الحياة غامضة واللعبة واضحة بشكل اصطناعي.
- Candyland: محدش يهمه مين وصل أول غير اللي دخلوا الدايرة.
- 🟢 MF: حافظ على الوضوح ده حتى مع الـ modifiers.

**R035 ★★ الـ modifiers اللي بتتغير وسط الليفل لازم تمشي على قاعدة أعمق ثابتة.**
- مثال Flux، وتغيير القواعد في الرياضة بيعدّي على legislative process.

### F. الـ Emergence (Ch.14)

**R036 ★★★ مفيش complexity يبقى مفيش meaningful play.**
- الـ complexity شرط مسبق، مش هي الـ meaningful play.
- Meaningful play = علاقة قرار↔نتيجة. Complexity = علاقة الأجزاء ببعض.
- أنواعها: intricacy استراتيجي، علاقات اجتماعية، سرد غني، ونفسية الرهان بفلوس حقيقية.

**R037 ★★★ صنّف كل ليفل أو بروتوتايب على مقياس Langton (§5-T06).**
- Per Bak: المنتظم بالكامل مش معقد، والعشوائي بالكامل مش معقد.
- 🟢 MF: المقياس الأساسي هو الارتباط بين موضع الإسقاط والنتيجة عبر آلاف الرانات.

**R038 ★★★ التعقيد في الترابط مش في العدد.**
- Three-Body Problem (Casti): جسمين ليهم حل مغلق، والتالت ملوش حل. التعقيد زاد order of magnitude مش تلت.
- **Chess مقابل Go:**
  - Chess فيها 6 أنواع قطع وقواعد خاصة: حركة البيدق الأولى، queening، castling.
  - Go فيها نوع واحد ما بيتحركش بعد ما يتحط، وهي أعقد رياضيًا (Holland).
  - «قواعد أعقد ≠ تعقيد أكبر».
- 🟢 MF: في تحديات 2501+ اسأل «كام coupling جديدة مع الموجود؟» عنصر من غير coupling = تعقيد مفتعل.
- ★★★ فلتر الفكرة:
  - القواعد بتتكتب في صفحة والـ space كبير؟
  - فيه coupling؟
  - لو فيه عنصر معزول، الـ emergence لازم ييجي من الفيزياء أو الفراغ.

**R039 ★★ coupled + context-dependent = emergence.**
- الـ coupled بيتردد عبر المساحة. الـ context-dependent بيتموّج عبر الزمن.
- Game of Life: سياق الخلية جيرانها الـ 8.
- Holland: النظام nonlinear، و«مش هتفهم استراتيجيات لعبة بورد بتجميع إحصائيات حركات القطع».
- النحو ما بيفسّرش Huckleberry Finn ولا الدستور الأمريكي ولا «Oops! I Did It Again».
- 🟢 MF: الدمج بيحرك الجيران فتطلع chain، وترتيب الجرة بيغيّر النتيجة.
- [رأي النوتس]: rot بينتشر من الجيران بقواعد محلية = أرخص نمط مفاجئ ومقروء.

**R040 ★★★ دقة الـ attributes هي اللي بتولّد الميزة (Populous: The Beginning).**
- المصدر: Peter Molyneux، عن Rollings & Morris.
- القاعدتين: preacher بيحوّل المحاربين اللي بيسمعوه، واللي بيقاتل مش ممكن يتحوّل.
- الناتج: الموجة التانية بتقابل attack radius المحاربين المحوَّلين، فلازم تتجول وتحرّكهم ورا الـ preachers.
- الميزة طالعة من: conversion radius، ووقت التحويل، ومدى الملاحظة، وسرعة المحاربين، وإمتى هما immune. أي تغيير واحد بيخفيها.
- 🟢 MF: ورقة attributes دقيقة لكل تحدي:
  - نطاق انتشار الـ rot وسرعته.
  - كام دمج لقشر الـ mossy.
  - كثافة الحجر.
  - إمتى القطعة immune.

**R041 ★★★ لوحة tuning شغالة live جوه البروتوتايب.**
- Gearheads (أداة Marc LeBlanc): pull-down menus بجداول stats، والتعديل بيتطبق فورًا في نص اللعب.
- Gearheads خدت 18 شهر playtesting. Conway قعد سنتين يضبط Life.
- ★★★ Reusable: قالب بروتوتايب موحد فيه لوحة live.

**R042 ★★★ صمّم أنواع عناصر تشتغل مع بعض، والـ space هيكبر أُسّيًا.**
- Gearheads فيها 12 لعبة. اللاعب بيختار 4 أو 5 قبل الماتش، والخبير بيحط engine أو اتنين.
- Magic: The Gathering «hothouse للـ emergence».
- Engines:
  - **Punching Roaches:** Ziggy + Kanga.
  - **Bomb Shield:** Disasteroid + Walking Time Bomb، والقنبلة ما بتأثرش على Disasteroid.
  - **Perpetual Motion:** Crush Kringle + Handy + Crush Kringle في نفس الصف.
- 🟢 MF: لكل زوج من mossy/stones/rot: فيه engine؟ stone بيحمي من rot؟ الدمج جنب shell بيقشّرها؟

**R043 ★★★ لو البوت لقى engine، ده مش bug بالضرورة.**
- قرّر: تحميه (Disasteroid محصّن عشان الـ engine يبقى ممكن) ولا تضبطه.
- AI بتاع Gearheads استعمل engine-based heuristics واللاعبين اتعلموا منه.
- 🟢 MF:
  - الـ engines تتسجل وتتعرض كريبلاي أو tip.
  - ★★★ وهي مخزون إعلانات: chain مفاجئة كبيرة لقطة «اكتشاف».

**R044 ★★★ Second-order design: مش هتقدر تختبر كل تعديل.**
- بتبني «sixth sense» بنيوي، ومع كده مش هتتوقع كل حاجة.
- **عشان كده الـ CPI والتيستر-بوت مش رفاهية.**
- 🟢 MF: مولد الـ 3000 ليفل = sixth sense مدعوم برانات البوت.

**R045 ★★★ «إصلاح لعبة تافهة» بمتغيرات Heads & Tails.**
- [فجوة]: قايمة المتغيرات اللي كانت في §4.7 الأصلي مجاتش.
- المبدأ المتاح: لعبة تافهة بتتصلح بإضافة coupling واختيار وuncertainty، شوف R036–R039 وR047.

**R046 ★★★ الـ stickiness جاية من الـ emergence.**
- حلقة مسلسل ويب بتتشاف 2–3 مرات. اللعبة بتتلعب عشرات أو مئات أو آلاف المرات.
- variety وnovelty وsurprise = استراتيجية repeat play.

### G. عدم اليقين (Ch.15)

**R047 ★★★ كل لعبة لازم فيها uncertainty.**
- الـ macro (النتيجة الكلية) لازم في كل لعبة. الـ micro (آليات الحظ) مش لازم.
- الاختبار: «لو عارف مين هيكسب، هتلعب؟»
- الرياضة بتتذاع لايف لنفس السبب. Halo بين متكافئين.
- DeKoven: تخيل إنهم أعلنوك فايز قبل ما تبدأ.
- جدول Epstein في §5-T07.

**R048 ★★★ إحساس العشوائية أهم من العشوائية نفسها.**
- Chinese Checkers (4–6 لاعيبة) شكلها «مخلوطة» وهي منطق خالص، والقفز المتعدد بيبرز ده.
- SiSSYFiGHT 2000 مفيهاش random وuncertain.
- الترتيب: Chess < Chinese Checkers < Pick-Up Sticks بكتير.
- قليل = جافة وتنافسية بحدة. كتير = فوضى وعجز.

**R049 ★★★ حتى الـ pure chance لازم فيها لحظات اختيار (التعارض #3).**
- **Chutes and Ladders** ليها 3 متع formal: ميكانيكية، وuncertainty، وقفزات بتجيب reversals of fortune. من غيرهم «flat»: 1–6 كل دور واللي قدام فاضل قدام.
- **اللوتري:** نوع اللعبة، الأرقام، عدد مرات الدخول، النمط، خانات الـ scratch-off. واللاعبين عندهم أنظمة: أرقام فايزة قديمة، أعياد ميلاد، numerology.
- 🟢 MF:
  - ليفل بيتحسم بدري (نضيف أو مخنوق بعد أول 30% من الـ budget) = flatness.
  - محتاج «ladders» (chain merges) و«chutes» (rot) في الليفلات الذروية.
  - البوت يقيس **نقطة الحسم** في الـ budget.
  - الـ side quests العشوائية محتاجة اختيارات صغيرة، مش spin وانتظار.

**R050 ★★ حجم البورد × توزيع النرد = pacing.**
- Monopoly فيها 40 خانة ومتوسط الرمية 7، يعني حوالي 6 رميات للفة، والتصادم بيبدأ حوالي الدور 7.
- 🟢 MF: البوت يحسب متوسط الإسقاطات لأول merge لحجم N ولأول موقف ضغط، ويقارنه بالـ pacing المستهدف.

**R051 ★★★ Thunderstorm: جودة الحظ بتتغير مع مورد داخلي، والدورات المتراكبة بتعمل قوس درامي من غير قرار واحد.**
- المتاح من النوتس:
  - النرد بيتحكم في البناء والعاصفة مع بعض.
  - رسم البيت personification وسجل مقارن مرئي. العدّ لـ 6 أو الكروت أو البنسات كانوا أضعف.
  - public information، وخرافة غرور وقدر.
  - مقارنة بـ Hangman.
  - الخجول بيكسب.
- [فجوة]: أرقام القواعد التفصيلية اللي كانت في §8.
- 🟢 MF:
  - الـ budget المتناقص هو «عدد الزهرات». هل احتمال merge مفيد بيتغير فعلًا؟
  - لازم سجل مقارن مرئي للتقدم.
  - الدورات: كل drop، ودورة الـ chain، والتقدم للهدف، والـ endgame.
  - في الـ rivals التمني المزدوج قابل للنسخ: تفرح بفشل الخصم وتتمنى نجاح اللي قبلك.

**R052 ★★★ Pig: قرار واحد بسيط واقف على تقاطع كذا اتجاه.**
- القواعد: هدف 100 نقطة، والـ 1 بيضيّع نقط الدور.
- Knizia: قف عند 20+.
- راعي موقف الباقيين: لو متأخر اضغط، ولو متقدم العب محافظ.
- ★★★ «إيه القرار البسيط اللي بيقلب اللعبة؟» لو مفيش، مفيش ماتش.
- **rewarded ad double-or-nothing = Pig جاهز** وقالب بيتكرر بين الألعاب.
- 🟢 MF: push-your-luck في الـ minigames والـ rivals. البوت يبني جدول نجاة (احتمال تفادي الـ overflow مع كل drop زيادة)، مع إظهار سكور الخصم.
- مشكلة العدالة في Pig: شوف R098.

**R053 ★★★ افحص الـ RNG إحصائيًا.**
- الكمبيوتر بيولّد pseudo-random. logistic rule عند Casti: ×4 وبعدين اطرح 4×المربع، شكلها عشوائي وهي محددة.
- قصة ميكروبات Eric:
  - 16 اتجاه، والركن الأيسر العلوي اتعد مرتين فاحتماله الضعف.
  - الميكروبات كلها راحت عليه، واتفسّر غلط كـ emergence.
  - «تحيز صغير × نظام معقد = أثر emergent كبير».
- 🟢 MF:
  - البوت يعمل histogram لموضع الـ spawn وتوزيع الأحجام وترتيب الـ queue. دوّر على off-by-one وتحيز جانبي.
  - seeds deterministic.
- ★★★ اختبار توزيع الـ RNG خطوة ثابتة في كل بروتوتايب.

**R054 ★★★ اللاعبين هيحوّلوا أي حظ لاستراتيجية.**
- المصدر: Goldstein، Counting Out، فيلادلفيا 1967، أطفال 4–14 سنة. 6 طرق:
  1. Specific Rhyme Repertory
  2. Extension of Rhyme
  3. Skipping Regular Counts: الأشهر والأكتر ازدراء
  4. Stopping or Continuing
  5. Changing Positions
  6. Respite by Calling Out: الجروب بيقيّدها بواحد لكل جولة
- ورا كده فكرة ideal rules مقابل actual rules (R101).
- 🟢 MF:
  - قرّر صراحة: الـ seed ثابت ولا بيتجدد مع كل retry؟ ومين المستفيد؟
  - في الـ rivals دوّر على «Skipping Regular Counts».

**R055 ★★★ صمّم على مغالطات الاحتمال (§5-T08).**
- أفكار لعب من الكسور:
  - عشوائية مختلّة عمدًا: كود سري، أماكن الحظ فيها بيميل.
  - لاعيبة بيعدّلوا الـ random قانونيًا: فلوس بتغيّر الرمية، رصّ الكروت.
  - لعبة حوالين أرقام محظوظة ومنحوسة.
- «أي قاعدة تصميم ممكن تتكسر».
- ★★ تقاطع مع Portnow's Postulate، يعني إحباط الـ RNG.

### H. المعلومات (Ch.16–17)

**R056 ★★★ Information = مقياس عدم اليقين = حرية الاختيار = space of possibility.**
- Weaver: «بتخص اللي **تقدر** تقوله مش اللي قلته».
- مثال J.L.:
  - فطار yes/no = قليل.
  - لون مفضل = أكتر.
  - كلمة مفضلة من كل الإنجليزي = أعلى.
  - لو عارف كل حاجة عنه = صفر.
- Littlejohn: الموقف المتوقع بالكامل مافيهوش information.
- التلغراف: «Only infrmatn esentil to understandn mst b tranmitd».
- 🟢 MF: عدد مواضع الإسقاط اللي نتايجها مختلفة فعلًا. لو كلها نفس النتيجة، يبقى قرار وهمي.
- ★★★ مقياس موحّد: entropy نتايج البوت (win/fail/near-miss). لو 0% أو 100% يبقى الليفل مالوش معلومة. مفيش لعبة تتنشر وتوزيعها ثابت.

**R057 ★★ الـ preview بيقلّل uncertainty.**
- Mastermind: كل تخمين بيضيّق المساحة. لو الحل بيتعاد ترتيبه يبقى زي الروليت.
- Twenty Questions: بتضيّق في أقل من 20.
- 🟢 MF: عدد قطع الـ preview = ضبط مباشر للـ information. وminigame Mastermind سهل تتبني.

**R058 ★★★ الـ Noise ممكن يبقى المحتوى أو العقبة الممتعة.**
- Telephone: الـ noise هو المتعة.
- Charades: بتحارب الـ noise، ولحظة اكتمال الدايرة إشباع عميق، ودي lusory attitude.
- نموذج Shannon & Weaver (1949): source → signal → channel → receiver، ومعاهم noise.
- 🟢 MF: فيزياء الجرة noise. سيبه في اللعب، **بس مش في الـ UI ولا التيوتوريال**.

**R059 ★★★ الـ Redundancy بيوازن الـ noise.**
- الإنجليزي فيه حوالي 50% redundancy.
- الكلمات المتقاطعة محتاجة ≥50% حرية:
  - لو 100%، أي مصفوفة تمشي وملهاش طعم.
  - لو 20%، مستحيل تتبني.
- مثال: «GET OUT OF THE ROOM RIGHT ___».
- 🟢 MF:
  - (أ) مسارات متداخلة لنفس الهدف، وده الفرق بين «مكسور من غلطة واحدة» و«متسامح». في 2501+ اسأل: بتقفل مسارات ولا بتزود؟
  - (ب) التيوتوريال والتحديات الجديدة: نفس المعلومة في أكتر من قناة (شكل + لون + صوت + اسم).
- ★★★ قاعدة الـ 50% لألعاب الألغاز: الحل الجزئي يفتح الباقي، والحل يفضل مش تافه.

**R060 ★★★ Balancing act.**
- بنية كتير = overdetermined. بنية قليلة = chaotic.
- الـ sweet spot هو «المشكلة الأساسية في تصميم الألعاب».
- 🟢 MF: ده الإطار النظري لـ `bot_difficulty`. ينطبق كمان على الـ side quests hub، وفيه تقاطع مع Choice Paralysis.

**R061 ★★★ اختار محورَي المعلومة والحظ بوعي، وهما مستقلين عن بعض (§5-T09).**
- 🟢 MF:
  - Mossfolk تقريبًا perfect info، والـ chance في الـ queue.
  - أي تحدي بيخبّي معلومة لازم ليه لحظة كشف مصممة.
  - لكل rival mode قرار: حالة الخصم مكشوفة ولا مخفية؟

**R062 ★★ صنّف كل معلومة بفئات Pearce (The Interactive Book) وتابع حركتها.**
1. Known to all: قواعد Chess ولوحتها.
2. Known to one: كروت Gin في إيدك.
3. Known to game only: ديك Gin، ومسارات Space Invaders.
4. Randomly generated: نرد Backgammon.

- الاعتراض في التعارض #4.
- الفرق بين game-only وrandom: تركيبة الديك الباقي معروفة للكل؟
- الحركة بين الفئات هي الدراما، زي Battleship.
- 🟢 MF:
  - الجرة للكل.
  - الـ queue يا game-only يا random.
  - الـ mossy shell بتخبّي الحجم.
  - الـ rivals فرصة لمعلومة private.

**R063 ★★★ الـ Perceived information هي اللي بتفرق، مش الـ objective.**
- Euchre: الـ trumps اللي اتلعبت مهمة بس لو اللاعب متابعها.
- Scrabble: نسب الحروف مطبوعة على اللوحة. هل الـ Z الوحيد اتلعب؟
- Enchanted Forest: خلط الديك أنجح متأخر.
- المعنى علائقي، زي كلمة «bird».
- 🟢 MF:
  - شارت الـ 9 أحجام والسلسلة يفضلوا ظاهرين.
  - الفجوة بين البوت (عارف الـ objective) واللاعب بتفسّر فشل لاعب في ليفل البوت بيعديه بسهولة، وده مكان الـ hints.
  - ★★★ «المعلومة وقت الحاجة» (Tutorials 101).

**R064 ★★ معلومة خاصة محفوظة في الذاكرة = مخاطرة طبيعية (Enchanted Forest).**
- سلوك الخصم قناة معلومات تانية: بيجري للقلعة لأنه شاف الكنز ولا بيـ bluff؟

**R065 ★★★ اختار نوع النظام المعلوماتي لكل لعبة واكتبه في أول صفحة (§5-T10).**
- **تحذير:** ما تعتمدش على المحتوى المخفي عشان تولّد اهتمام. مفيش كارت مخفي هتكتشفه في Poker بعد 30 ساعة.
- 🟢 MF:
  - معسكر Tetris/Go.
  - التنوّع بتحديات بتتكشف تدريجيًا، مش بإخفاء القواعد.
  - المقفول يتعرض في الـ hub للتصفح.

### I. الـ Feedback Loops وضبط الصعوبة (Ch.18)

**R066 ★★★ اكتب كل loop بصيغة LeBlanc.**
- المصدر: GDC 1999، «Feedback Systems and the Dramatic Structure of Competition».
- السلسلة: Game State (الحالة الرسمية، مش مهارة ولا مشاعر) ← Scoring function (sensor) ← Controller (comparator) ← Game mechanical bias (activator).
- 🟢 MF:
  - الجرة اللي بتتملي = positive ضد اللاعب (death spiral).
  - الـ merge = negative.
  - الـ combos = positive في السكور.
  - مصفوفة loops لكل ليفل.

**R067 ★★★ اختار اتجاه الـ feedback بوعي (Positive / Negative Basketball).**
- كل N نقطة فرق (مثلًا N=5) بيتضاف لاعب:
  - للخسران = negative، ماتشات قريبة.
  - للكسبان = positive، runaway.
- الحذف بيدّي نفس النتيجة بالعكس.
- de Rosnay:
  - Positive = كرة تلج، تفاعل متسلسل، فائدة مركبة، تضخم، أو إفلاس وكساد.
  - Negative = goal-seeking، بيتذبذب حوالين توازن من غير ما يوصله (ثرموستات، عوامة).
- 🟢 MF: لكل rival contest: rubber-band ولا snowball؟
  - توزيع فروق النتايج قريب = negative.
  - مبعثر = positive.
- مكان الـ feedback في §5-T11.

**R068 ★★★ كل positive loop لازم يبقى جواه damper.**
- 🟢 MF:
  - الـ chains ليها حد أو خطوة بتفك السلسلة.
  - البوت يدوّر على loops اتعملت بالصدفة من الفيزياء.

**R069 ★★★ قواعد LeBlanc الثمانية (§6-C10). أهمها: الإحساس بالتحكم أهم من التحكم نفسه.**
- لو العربية التانية على ضهرك طول الوقت، أداؤك مش فارق.
- حط سقف للحاق.

**R070 ★★★ قرار مفتوح في Mossfolk: DDA خفي ولا opt-in واضح (مساعدة بـ rewarded ad)؟**
- أسئلة الكتاب: «بتلعب اللعبة ولا هي بتلعبك؟» ده غش؟ ينفع في multiplayer؟
- ★★★ لحظة «بعد N فشل» أنسب مكان لـ rewarded ad كمساعدة.
- ★★★ Reusable DDA module: sensor (فشل أو قرب من الهدف) ← comparator (عتبة) ← activator (مساعدة)، مع config للعتبة والحجم والسقف.

**R071 ★ الـ exact landing في Chutes مش cybernetic حقيقي.**
- مفيش فيه sensor ولا comparator ولا activator.
- لو القاعدة «الأول يطرح 1 من رميته» يبقى loop.
- ممكن تتصاغ «لو باقيلك أقل من 6، أي رمية أكبر من N ملهاش أثر».
- قيمة الـ schema في حل مشاكل التصميم، مش في إرضاء منظّري الأنظمة.

### J. Game Theory (Ch.19)

**مرجع مضغوط**
- **Rational player** (Poundstone):
  - ما بيفوّتش قفزة في checkers ولا بيقع في فخ Chess.
  - اتنين عقلانيين في TTT = تعادل دايمًا.
  - «زي Mr. Spock»: خرافة مفيدة للتحليل المعزول.
- **Simultaneity:** قرار في نفس الوقت (RPS). العقلانيين «متوقعين نفسيًا»: مش حاقدين ولا ناسيين ولا مدمّرين لنفسهم ولا كسالى.
- Game theory مدرسة اقتصاد مش تصميم. أمثلتها: تبيع سهم Disney؟ لتر لبن ولا اتنين؟ ضرائب الاستيراد؟
- **Utility:**
  - Davis: برتقانة وتفاحة وكمترى.
  - بيت الشاطئ: على البحر +10، على بعد أمتار +5 أو +2، مش شايف المحيط سالب، وبتعظّم المجموع.
  - تشبيه الحرارة: كانت إحساس غامض قبل القياس.
  - كل لعبة ليها نتيجة قابلة للقياس: kills، وقت تأهل، مين كسب.
- النظرية محصورة في لاعبين اتنين. مع 3+ بتتعقد زي مشكلة الأجرام التلاتة.
- **Zero-sum:**
  - Poker بـ pot مشترك.
  - Roulette بين اللاعيبة مش zero-sum، وضد الكازينو zero-sum.
  - Checkers +1/−1.
  - Lord of the Rings Board Game التعاونية مش zero-sum.
- **النظرية:** أي لعبة zero-sum وfinite بلاعبين اتنين ليها حل.
- **Saddle point** (تشبيه الممر الجبلي) = Minimax theorem، Von Neumann سنة 1928 قبل كتاب 1944.
- **Prisoner's Dilemma:**
  - شهدت والتاني سكت: إنت حر وهو 3 سنين.
  - الاتنين شهدوا: سنتين لكل واحد.
  - الاتنين سكتوا: سنة لكل واحد.
  - مش zero-sum، وحلها مختلف عليه (التعارض #5).
- **Further Reading:**
  - Holland، *Emergence*: ف2 Games and Numbers، ف3 Maps, Game Theory, and Computer-Based Modeling.
  - Poundstone، *Prisoner's Dilemma*: ف3، ف6، ف12. «أوضح كتاب غير تقني»، وفيه سيرة Von Neumann والحرب الباردة.

**R072 ★★★ تجنّب الـ saddle points «زي الطاعون».**
- هي short-circuit في الـ space of possibility.
- أمثلة:
  - لعبة قتال بتتكسب بتكرار هجوم قوي واحد.
  - ثغرة RTS AI مش بيعرف يدافع ضد نوع وحدة.

**R073 ★★★ الطريقة الحقيقية الوحيدة لكشف الـ degenerate strategy هي playtesting صارم.**
- لو اللاعيبة بينجذبوا لنفس الاستراتيجيات مرة ورا مرة، غالبًا فيه ثغرة.
- **عندنا ده البوت.**

**R074 ★★★ Dominant-strategy probe إجباري قبل الـ CPI.**
- شغّل سياسات ثابتة غبية على البروتوتايب.
- 🟢 MF:
  - «دايمًا المنتصف».
  - «دايمًا الركن».
  - «دايمًا نفس العمود».
  - «دايمًا الحجم الأصغر».
- لو سياسة ثابتة كسبت ≥ العتبة ([رأي النوتس]: 40–50%)، يبقى فيه saddle point والليفل فشل في الـ meaningful play.
- أي CPI عليه هيضلّل، لأن اللاعب هيزهق بسرعة.

**R075 ★★ ارسم payoff matrix بسيطة لأي mechanic جديدة في الكونسبت قبل الكود.**
- السؤال الوحيد: فيه خيار أحسن دايمًا؟

**R076 ★★★ الـ leaderboard بيزوّد ضغط الاستغلال.**
- الناس بتستغل من غير تردد لما الإنجاز معروض برّه اللعبة (online high score list).
- أي leaderboard أو rival لازم يسبقه probe.

**R077 ★★ Mixed strategy للـ rival AI (Matching Pennies).**
- متطابقين: اللاعب 1 ياخد العملتين. مختلفين: اللاعب 2.
- مفيش saddle point، فالحل 50/50 ومتوسط الـ utility صفر.
- أي pattern ثابت هيتستغل.
- في القرارات المتزامنة حافظ على الغموض (مبدأ RPS).

**R078 ★★ Cake Division: عدالة بالمصلحة الذاتية.**
- واحد يقسم والتاني يختار. «الطمع بيضمن القسمة العادلة».
- Poundstone: فرق «فتاتة» (crumb)، فالقيم −1/+1، والحل في الخلية فوق-يسار.
- 🟢 MF: واحد يحدد الـ seed أو التقسيم والتاني يختار الجانب.

**R079 ★★ Decision tree على مستوى الميتا.**
- الأشجار الكاملة نظرية. شجرة Chess مرسومة بحجم مقروء تغطي المجموعة الشمسية (Poundstone).
- شروط الشجرة: زمن discrete، وقرارات محدودة نتايجها knowable، ولعبة finite.
  - American Football مش بتنفع حتى على مستوى الـ play calls.
  - Chess finite بقاعدة التعادل.
  - Chutes تنفع: 6 فروع، وشجرة لكل عدد لاعبين.
- الـ Hypertext روابطه ثابتة، لكن اللعبة اللي تقدر تعملها دلوقتي معتمدة على اللي حصل (الـ rooks في الأول).
- 🟢 MF:
  - ارسم شجرة الـ side quests hub وتحديات 2501: نجاح أو فشل، وبعدها أنهي مهمة؟
  - كام مسار؟ فيه loops بتكرر المحتوى؟
  - متوسط كام مهمة هيلعبها اللاعب؟

**R080 ★ «Strategy» في الاستوديو = heuristic (زي Zerglings بدري)، مش بالمعنى الـ game-theoretic.**
- ما تخلطش المعنيين في النوتس والتيوتوريال.

**R081 ★ قواعد بسيطة جدًا ممكن تطلّع سياقات قرار معقدة (PD).**
- وبتثير أسئلة أخلاق ومجتمع، مش رياضة بس.

### K. الصراع والأهداف والعدل (Ch.20)

**مرجع مضغوط**
- Crawford: الصراع طبيعي وموجود دايمًا: مباشر أو غير مباشر، عنيف أو لأ.
- في اللعبة الصراع staged، والأهداف ليها قيمة جوه الدايرة بس.
- أشكال الصراع السبعة في §5-T12.
- **المختلط:**
  - مصارعة فردية بنقاط فريق.
  - Double Dragon: لاعب أو اتنين متعاونين.
  - Survivor: فريقين، بعدين مجموعة، بعدين فايز واحد.
- مباشر/غير مباشر: Arm wrestling مباشر، Figure skating غير مباشر، Starcraft multiplayer مختلط.
- **Centipede:**
  - score مستمر، وأهداف تانية: مدة، مستوى، تدمير كل نوع.
  - التناوب بيخلي السكور zero-sum وbinary.
  - ممكن تخسر قدام خصمك وتكسب personal best.
  - الـ high score list بتعرض أعلى 8 بس. الهدف ممكن يبقى «ادخل القائمة» أو تنافس ودّي.
- **Joust:**
  - simultaneous، وقوائم high score يومية وall-time منفصلة، وسكورين ظاهرين.
  - اللعب بيتحول قتال zero-sum أو تعاون أو الاتنين.
  - **اللي في موضع أعلى في التصادم بيقتل**، فبيحصل قتل بالغلط.
- **Gauntlet:**
  - لحد 4: Warrior، Valkyrie، Thief، Wizard. ما يقدروش يهاجموا بعض.
  - اللعبة بتقف بين المستويات وتعرض إحصائيات (أكبر كنز).
  - التنافس على food وkeys وpotions بيجيب اتهامات «ظالم» و«جشع».
  - الـ quarters بتزوّد الصحة أو تحيي، والصعوبة المتصاعدة بتضمن الدفع، فبتبقى conspicuous consumption. أو بالعكس: مين يلعب أطول قبل ما يدفع.
  - اختبار عكسي: لو قدروا يضروا بعض التعاون يضيع، ولو مقدروش يدفعوا التنافس على الموارد يبقى أشرس.
- SimCity: اللاعيبة بيخترعوا أهداف. «space of possibility = space of possible conflict».
- **Competition/Cooperation:**
  - DeKoven (*The Well-Played Game*، ص11): «اللعب للفوز» بيفرّق.
  - المؤلفين: من غير هدف مفيش قياس، ومن غير قياس مفيش feedback. مثال: لعبة The Grid «الفظيعة».
  - «compete» = con petire يعني «نسعى معًا» (Csikszentmihalyi).
  - Systemic cooperation في كل لعبة، وplayer cooperation في بعضها. الصراع زي duel بين ممثلين.
- **New Games Movement:**
  - Stewart Brand (*Whole Earth Catalog*)، أواخر الستينات، tournaments عامة في Bay Area.
  - أثّروا على الجيم المدرسي: parachute وEarth Ball.
  - كتبهم: *The New Games Book* و*More New Games*.
  - DeKoven (ص87–88): «خصمك هو شريكك في اللعبة».
- **Catch the Dragon's Tail** (8–10 أشخاص):
  - آخر واحد حاطط منديل في حزامه، والراس بتحاول تخطفه، واللي في النص مش متأكدين يروحوا فين.
  - «مين الفايز؟ كلنا!»
  - الراس تبقى الديل، والتاني من قدام يبقى الراس.
- **Caillois** (*Man, Play, and Games*، ص14): الصراع «under ideal conditions» عشان قيمة الانتصار تبقى دقيقة.
  - العدل الكامل مستحيل: أولوية الحركة (dame/شطرنج)، آخر مزايد في bridge، الأخير في croquet، الشمس والريح والحارة.
  - العلاج: قرعة، وبعدها تناوب صارم.
- الرقمي: تحكم أدق، بس الشك في lag أو AI «بيغش» أو stutter بيدمّر اللعبة، سواء الشك حقيقي أو لأ.
- **Further Reading:** Homo Ludens (ف1)، New Games Book: «Creating the Play Community» (DeKoven)، و«Theory of Game Change» (Brand).

**R082 ★★★ الهدف الواضح القابل للقياس هو العمود اللي شايل الخيمة.**
- من غيره اللاعب مش قادر يحكم أفعاله، واللعبة «بتنهار في كومة غموض».
- الهدف «موت اللعب» كمان.
- التزلج leisure، ولما تسابق صاحبك لتحت الجبل يبقى لعبة.
- الرحلة لازم تبقى **taut and efficient**.
- Space Invaders: أطول لعب أو أعلى سكور، و«عايش على وقت مستعار».

**R083 ★★★ الأسئلة التسعة بتحدد بنية الصراع في 10 دقايق قبل البروتوتايب (§6-C11).**
- 🟢 MF: تتطبق على كل side quest وrival mode.

**R084 ★★★ طبقات أهداف على نفس الـ core (درس Centipede).**
- personal best ← ترتيب بين أصحاب ← دخول top-N (binary) ← rival.
- ★★★ module واحد قابل لإعادة الاستخدام: score → rank → binary goal.

**R085 ★★ Rival مباشر ولا غير مباشر؟**
- غير المباشر (كل واحد في برطمانه، زي figure skating) أرخص وأأمن.
- المباشر (تبعت عقبات) بيضيف قرارات بس فيه قتل بالغلط زي Joust.
- القرار بوعي.

**R086 ★★ «كل الألعاب تنافسية وكل الألعاب تعاونية».**
- «تعاوني» مش معناه «من غير هدف».

**R087 ★★★ Catch the Dragon's Tail كمولّد أفكار.**
- اكسر افتراض (هدف لكل لاعب، خطوط تنافس حادة) هتطلع فكرة مختلفة.
- «تصميم الألعاب هو اللعب بالأفكار».

**R088 ★★★ (درس LOOP) الـ core الأول، وبعدين جرّب 2–3 تركيبات فوز/خسارة واختار بـ playtest أو بوت.**
- LOOP: single-player أونلاين، بتصطاد فراشات بلفّ خطوط، ونفس اللون بيدّي بونص.
- الـ core اتعمل قبل الشروط.
- 3 سيناريوهات فوز: عدد معين، تنضيف الشاشة، اصطياد للأبد.
- مخططين للخسارة: وقت محدد، شاشة بتتملي.
- **اختاروا الوقت** لأن التقدم فيه أوضح. في Tetris واضح إنك بتقرّب من فوق، وفي LOOP مكانش واضح إمتى الفراشات «بقت كتير».
- اتشال meter لعدد الفراشات لأنه بيعقّد الـ interface.
- الليفلات منفصلة بـ quota.
- القرارات اتاخدت بالـ playtest مش بالحدس.
- ★★★ خانة «win/loss variants tested» في قالب البروتوتايب. المعيار: «حاسس بالتقدم؟ مقروء؟».

**R089 ★★★ شرط الخسارة لازم يبقى legible قبل ما يحصل، وده مهم قد شرط الفوز.**
- 🟢 MF:
  - خط overflow واضح زي Tetris + عدّاد budget.
  - اتأكد إن قرب الخسارة باين في ليفلات mossy/stones/rot، لأن ده بالظبط عيب LOOP.

**R090 ★★ ما تصممش هدف بيفضّي الساحة لو هيطلّع حل أمثل واحد.**
- LOOP: عدد الفراشات ثابت، وكل مجموعة بتتصاد نفس العدد بيدخل من الجنب.
- 🟢 MF:
  - الـ drop queue يمنع حل محسوب مسبقًا.
  - البوت يقيس عدد الحلول الناجحة المختلفة لكل ليفل.
  - أهداف «عدد كامل من X» ولا «تنضيف»؟ لو تنضيف: إيه اللي يحصل لو فضلت قطعة واحدة؟

**R091 ★★ Overshoot reward.**
- LOOP: تزحف لحد ما يفضل واحد على الـ quota، وبعدين تضرب مجموعة كبيرة، والزيادة bonus كبير.
- 🟢 MF: مكافأة على أقل إسقاطات أو chain كبيرة في الآخر.

**R092 ★★★ قالب goal/loss قابل للتبديل فوق نفس الـ core.**
- الخيارات: timer / budget / عدد أخطاء / حد ارتفاع. أرخص «لعبة مختلفة».
- جرّب أفكار LOOP المفتوحة: أكتر من شرط فوز، أو لعبة هدفها تخسر بأسرع ما يمكن.

**R093 ★★★ الإحساس بالعدل أهم من العدل الرياضي.**
- 🟢 MF، الـ rival contests:
  - نفس الـ seed ونفس تسلسل المخلوقات للاتنين. دي قرعة Caillois.
  - مفيش rubber-banding ظاهر، لأنه هيتقري «cheating AI».

**R094 ★★ الخسارة لازم تتقري خطأ لاعب، مش stutter فيزيكس أو حظ.**
- مرتبط بـ Portnow.
- ورّي معلومات (next piece) بدل ما تسيب اللاعب يشك.

**R095–R097 دمج: Pig Redux (مشكلة ميزة الأول).**
- مثال: 5 لاعيبة، والأول وصل 100 في الدور العاشر.
- الحلول وعيوبها:

| الحل | العيب |
|---|---|
| الفايز اللي فات يبدأ | positive loop، ومش بيحل أول لعبة |
| الأقل يبدأ | مش عادل للكل |
| رمية عشوائية للترتيب | مش بتتحس عادلة، والأول لسه ليه ميزة |
| ألعاب بعدد اللاعيبة مع تدوير البداية (10 لاعيبة = 10 ألعاب) | بتتحول tournament |
| **Knizia** (*Dice Games Properly Explained*، ص128–30): لما حد يوصل 100 الباقي يرموا مرة أخيرة | الأحسن، بس أول واحد يوصل 100 في عيب صغير لأن الباقيين عارفين الرقم وبيلعبوا push-your-luck |

**R098 ★★★ الحل الصح هو اللي «بيتحس صح».**
- اختبر الإحساس بالعدل مع اللاعيبة، مش الرياضة بس.

**R099 ★★ ميزة الحركة الأولى موجودة دايمًا. عالجها بالقرعة + التناوب الصارم، أو بفرصة رد أخيرة (Knizia).**

**R100 ★★★ الدفع للاستمرار (Gauntlet) بيحوّل الصراع لـ «تحمّل إنفاق».**
- الـ continue بـ rewarded ad مقبول بشرط يكون اختياري ومن غير حجب.
- الصعوبة المتصاعدة اللي «بتضمن إنهم يدفعوا» = ابتزاز، وحسام ضده (التعارض #7).

### L. Breaking the Rules (Ch.21)

**مرجع مضغوط**
- Goldstein («Strategies in Counting Out»): مجموعتين قواعد، ideal وactual. الأطفال بيزوّدوا «eenie-meenie-minee-moe» عشان ما يبقوش «It».
- DeKoven: «القواعد زي بعضها، بس طريقة اللعب مختلفة تمامًا».
- المحاور: الالتزام بالقواعد، والاهتمام بالفوز، ودرجة الـ lusory attitude. الأنواع في §5-T13.
- الفئات سياقية ومش مانعة لبعض. البولينج: «جاد زيادة» عشان مصمم على الـ tenth frame.
- فيه slippery slope: حماس ← unsportsmanlike ← غش.
- Huizinga: الـ spoil-sport بيحطّم عالم اللعب. Prensky: العدمي هو اللي بيفسد.
- الجمهور:
  - Scrabble بتجذب الاتنين.
  - Myst مقابل Myth: The Fallen Lords.
  - Pictionary مقابل wargames وRPGs.
- **Degenerate strategies:**
  - RTS بـ pathfinding ضعيف: تقود العدو لمناطق عوائق.
  - MtG الطبعات الأولى: قتل في الدور الأول. Wizards of the Coast منعت كروت أشهرها Black Lotus، بس فضل في الدِّكات الكاجوال سنين.
  - Pac-Man: حفظ الأنماط عمل معسكرين.
  - لعبة قتال: unsportsmanlike أو «حل بازل» (transformative).
  - ضد الكمبيوتر ممكن يتشاف أنيق، وضد البشر ممل وبيضيّق الـ space.
- **Ecosystem:**
  - C&C tank rush ولّد دفاعات ووسّع الـ space.
  - Basketball (سيطرة الطوال في الستينات والسبعينات): 3-point line، و3-second rule في الـ paint. قبلهم dribbling أول القرن، وبعدين shot clock، وجدل zone defense.
  - Dave Hickey («The Heresy of Zone Defense»): illegal-defense طلّعت «fluid complexity» و«match-up game» بالـ switch، والكوليدج فضل «parcels of real estate».
- **Sanctioned violations:**
  - double-dribbling، icing، اليد.
  - fouls out بعد 6 personal fouls. الحكم امتداد للنظام.
  - كوع = foul، لكم = سوء رياضية.
  - «draw fouls» ممكن يرتد charging.
  - منع مدى الحياة لتلاعب المباريات.
  - ليه؟ الواقع «بلا حبيبات» (ملّي-ثانية، ملّيمتر، false starts) + رأس مال ضخم.
- **Illuminati** (Steve Jackson Games، 4th ed. 1991، ص9–10، مبنية على Robert Anton Wilson): variant غش.
  - ممنوع: تقلب الطاولة أو تبعثر الـ power structures، فلوس مزيفة أو من نسخ تانية، تغش في البنك وقت setup أو income phase.
  - «أي حاجة غير كده مسموحة». اللي يتمسك يرجّع غشه بس.
  - أساليب: قراءة نرد غلط، سرقة من البنك، كذب في power/resistance، ترتيب الدك.
  - «لو حد ساب الطاولة، كل حاجة مسموحة».
  - «العبها مع أصدقاء كويسين جدًا أو ناس مش هتشوفهم تاني».