# Game Mechanics: Advanced Game Design (Ernest Adams & Joris Dormans، 2012) — جزء 1 من 8 — نوتس مذاكرة

**المغطى:** الغلاف والـ front matter + المقدمة (xi–xiii) + **الفصل 1 كامل** (ص1–22) + **الفصل 2 لحد ص35** (الجملة الأخيرة في الجزء مقطوعة: «…he must use the boomer[ang]…» — بتكمل في جزء 2). الوحدة هنا صفحات مش دقايق.

ملحوظة: كل الكتاب تصميم مش كود، فمفيش حاجة اتجاهلت. الجداول والصور (Table 1.1، Figures 1.2–2.4) محتواها الرسومي مش ظاهر في النص، وهنذكر بس ما قيل عنها.

---

## 0. Front matter + المقدمة ★★ — الكتاب ده بيعمل إيه ولمين

- **المؤلفين:** Ernest Adams (مستشار تصميم، 23 سنة في الصناعة، 8 منهم في EA، مؤسس أول رئيس IGDA سنة 1994، مؤلف *Fundamentals of Game Design* — الكتاب المرافق). Joris Dormans (محاضر وباحث في أمستردام، PhD، بيبحث في أدوات رسمية لتصميم الميكانيكس، صاحب **Machinations**).
- **الإهداء:** لـ Mabel Addis Mergardt، المصممة الرئيسية لـ **The Sumerian Game** (بقت مشهورة بعدين باسم HAMURABI) — «أول لعبة بـ internal economy لعبتها».
- **Jesper Juul** هو صاحب التفرقة بين games of emergence وgames of progression، وهي اللي **«بتبني الكتاب كله»** ★★.
- **أصل الكتاب:** اجتماع متأخر بالليل في G-Ameland student game jam. Stéphane Bura هو اللي اقترح على Joris يعمل tool تفاعلي لما شاف الـ diagrams الثابتة الأصلية.
- **الادعاء المركزي:** «مهما كانت اللعبة حلوة المنظر، مش هتبقى fun لو الميكانيكس مملة أو unbalanced. الـ mechanics بتخلق الـ gameplay» ★★. الكتاب مش عن Unreal mods ولا استنساخ app ترند. هو عن **مبادئ timeless**.
- **الميزتان الفريدتان:**
  1. **Machinations Tool**: بتشوف الـ mechanics وهي شغالة وتجمع statistics من غير كود ولا spreadsheet. بتعمل **1,000 run في ثواني** عشان تتأكد إن الـ internal economy balanced ★★★.
  2. **Design pattern library**: بتقطّر تصميم الميكانيكس لجوهره: «الـ deep structures في الـ game economies اللي بتولّد challenge، وأنواع الـ feedback loops». الفئات: engines of growth وfriction وescalation + stability cycles وarms races وtrading.
- **الميكانيكس عند المؤلفين:** هي «القلب» اللي بينفّذ العالم الحي، وبيولّد challenges نشطة، وبيحدد أثر أفعال اللاعب. **شغل المصمم إنه يصنع mechanics بتولّد gameplay challenging وممتع ومتوازن.**
- **خريطة الفصول (بتحدد اللي جاي في الأجزاء 2–8):**
  - 1: تعريفات + مراحل التصميم + prototyping.
  - 2: emergence vs progression.
  - 3: complex systems وبنية الـ emergence.
  - 4: internal economy وإزاي بنيتها بتعمل «game shape» ومراحل لعب.
  - 5: Machinations + نموذج Pac-Man.
  - 6: common mechanisms وfeedback structures وRandomness vs Emergence.
  - 7: design patterns.
  - 8: simulation وbalancing (Monopoly وSimWar).
  - 9: building economies (Caesar III + Lunar Colony).
  - 10: دمج level design مع mechanics وتعليم اللعب.
  - 11: progression mechanisms (lock-and-key + emergent progression).
  - 12: meaningful mechanics (serious games، semiotics).
- **الجمهور:** طلبة ومحترفين. مش كتاب مبتدئين.
- **لموسفولك:** الفصول 8 و10 و11 هي الأقرب لينا بحكم التيستر-بوت وإن عندنا 3000 ليفل. هنعلّم عليها لما توصل.

---

## الفصل 1 — Designing Game Mechanics

### 1.1 Rules Define Games ★

- **التعريفات التلاتة، وكلها فيها rules:**
  - Adams: «play activity في سياق pretended reality، المشاركين بيحاولوا يحققوا **at least one arbitrary, nontrivial goal** بالتصرف حسب rules».
  - Salen & Zimmerman (*Rules of Play*): «system فيه artificial conflict، defined by rules، بينتج **quantifiable outcome**».
  - Juul (*Half-Real*): «rule-based system، outcome متغير وقابل للقياس، outcomes مختلفة بقيم مختلفة، اللاعب بيبذل جهد، متعلق عاطفيًا بالنتيجة، والعواقب negotiable».
  - **الباترن:** مش بيقارنوا بينهم، بس بيقولوا إن الـ rules هي اللي بتحدد إيه اللي اللاعب يقدر يعمله وإزاي اللعبة هترد.

### 1.2 Games as state machines ★

- **State machine:** ماكينة افتراضية ليها عدد states، وكل state ليها rules للانتقال. المثال: DVD player (play → pause بالـ pause، stop → menu، وضغط play وهو في play مش بيعمل حاجة).
- اللعبة بتبدأ في **initial state** وأفعال اللاعب (وغالبًا الـ mechanics كمان) بتودّي لـ states جديدة لحد **end state** (win / lose / quit). الـ state بتعكس موقع اللاعب والحلفاء والأعداء وتوزيع الـ resources.
- **Finite state machines** بتتستخدم عمليًا في سلوك الـ NPC البسيط (attacking/defending/patrolling). **لكن الألعاب فيها states أكتر من إنها تتوثق**، و**«state machine theory not useful»** لدراسة الـ complex mechanics اللي الكتاب عنها ★. ده تبرير ليه هيستخدموا Machinations بدل state diagrams.

### 1.3 Games Are Unpredictable ★★★

- **القاعدة:** نتيجة اللعبة ماينفعش تكون واضحة من البداية، واللعبة المتوقعة غالبًا مش ممتعة.
- **التلات مصادر لعدم التوقع:**
  1. **Chance** (نرد، spinner). الألعاب القصيرة (blackjack، Klondike) معتمدة عليه تقريبًا بالكامل.
  2. **Player choices**: rock-paper-scissors (الـ rules مش بتفضّل اختيار، فالنتيجة من قرارات اللاعبين). **Diplomacy**: الجيوش القليلة والفوز في المعركة للأكتر عددًا، لكن كل اللاعبين بيكتبوا حركاتهم سرًا وبينفذوها في نفس الوقت، فلازم **social skills** عشان تعرف فين الخصم هيضرب وتقنع حلفاءك.
  3. **Complex rules**: Chess (16 قطعة، rules بسيطة، لكن مكتبات كاملة عن الاستراتيجية). «القدرة على قراءة الـ state الحالية وفهم تعقيدها الاستراتيجي هي أهم مهارة لعب».
- **قاعدة الطول** ★★★: «لما اللاعبين يحسوا إن قراراتهم ومهارتهم مش فارقة، بيتحبطوا بسرعة. الألعاب الـ pure chance مكانها الكازينو. **كل ما اللعبة أطول، لازم المهارة تساهم أكتر في الفوز**».
- معظم الألعاب بتمزج الثلاثة. الناس بتفضل خلطات مختلفة. **الباترن:** chance أسهل في الـ implementation لكن **مش دايمًا أحسن مصدر**، والـ complex rules اللي بتدي choices كتير صعبة التصميم (ودي مهمة الكتاب). الكتاب بيعتبر الـ chance دور **supporting مش central**.
- **Stochastic vs deterministic** (NOTE): العمليات اللي فيها صدفة (التحرك بنتيجة نرد) = stochastic. اللي من غير صدفة ونتيجتها محددة من الـ initial state = deterministic.
- **لموسفولك:** الـ merge drop في Mossfolk عنده مصادر عدم التوقع التلاتة: تسلسل القطع (chance)، قرار الإسقاط (choices)، والفيزيكس (complexity). شوف مين فيهم بيشيل الجزء الأكبر في كل مرحلة ليفلات، ولاحظ إن قاعدة «الأطول = مهارة أكتر» تتطبق على الليفلات الطويلة بميزانية إسقاطات كبيرة.

### 1.4 From Rules to Mechanics ★★

- **ليه الـ video game community بتفضل «mechanics»:** الـ rules تعليمات مطبوعة اللاعب عارفها. أما mechanics الفيديو جيم فـ**مخفية** (متنفذة في سوفتوير من غير UI مباشر)، واللعبة **بتعلّم اللاعب وهو بيلعب** عكس board/card games.
- **Mechanics أدق وأكتر تفصيل من rules.** مثال Monopoly: الـ rules كام صفحة. الـ mechanics تشمل **أسعار كل الـ properties ونص كل كروت Chance وCommunity Chest**، أي «كل حاجة بتأثر على تشغيل اللعبة». **لازم تكون مفصلة كفاية إن المبرمج يحوّلها لكود من غير لبس.**
- **Core mechanics:** الأكتر تأثيرًا، بتأثر على جوانب كتير وبتتفاعل مع mechanics أقل أهمية. مثال: الجاذبية في platformer (بتأثر على كل الأجسام المتحركة وبتتفاعل مع الـ jumping والـ fall damage). **مش core:** نقل items في الـ inventory، ولا الـ AI routines للـ NPC. **الخط بينهم مش حاد** وبيختلف بين المصممين وحتى بين السياقات جوه نفس اللعبة. اللاعب الخبير بيستنتج الـ core mechanics من مشاهدة السلوك مرات كتير.
- **Mechanic vs Mechanism:** الكتاب بيستخدم **mechanism** للمفرد (مجموعة rules مرتبطة بعنصر/تفاعل واحد، ويمكن تشمل rules كتير). المثال: المنصة المتحركة في side-scroller (سرعتها، المخلوقات بتقف عليها، بتتحرك معاها، وبتنعكس سرعتها لما تخبط أو بعد مسافة معينة).

### 1.5 Mechanics Are Media-Independent ★★

- نفس الـ mechanics بتتنفذ في أكتر من medium (board = paraphernalia، video = سوفتوير). **علشان كده الباحثين مابيفرقوش بين video/board/physical games** — العلاقات بين الكيانات واحدة.
- **الفايدة:** تصمم mechanics مرة وتنفذها في وسائط متعددة (يقلل وقت التطوير) + **تجرب الـ rules كـ board/physical قبل تكلفة الكود** ★★★.
- **الألعاب الهجينة (hybrid):** board games فيها كمبيوترات بسيطة أو ألعاب physical بأجهزة متوصلة.
- **مثال بالاسم: Johann Sebastian Joust** (Copenhagen Game Collective): من غير شاشة، سماعات بس، كل لاعب ماسك **PlayStation Move controller** في مساحة مفتوحة. اللي بيحرك الكنترولر أسرع من المسموح يتشال. اللاعبين بيحاولوا يزقّوا كنترولرات بعض وهما بيحموا كنترولرهم، **بالحركة البطيئة**. **tempo الموسيقى بيسرّع أحيانًا = السرعة اللي تقدر تتحرك بيها بأمان.** (الـ UI هنا هو الصوت نفسه، والـ mechanic بسيطة والـ physical performance هي الـ gameplay.)

### 1.6 خمس أنواع Mechanics ★★★

1. **Physics**: علم الحركة والقوة في عالم اللعبة (ممكن يختلف عن الحقيقي). حساب الموقع والاتجاه والتصادم = **معظم حسابات ألعاب كتير**. من FPS واقعية لـ physics puzzles زي **Angry Birds**. **Cartoon physics** = Newtonian معدّلة (تغيير الاتجاه في الهوا). **الـ timing والـ rhythm challenges جزء من الـ physics عندهم.**
2. **Internal economy**: المعاملات على العناصر اللي بتتجمع وتتستهلك وتتبادل. موارد ملموسة (فلوس، طاقة، ذخيرة) **وتجريدات** (health، popularity، magical power). مثال: **قلوب Link في أي Zelda** + skill points في RPGs (اقتصادات معقدة جدًا).
3. **Progression mechanisms**: الـ level design بيحدد إزاي اللاعب يتحرك في العالم. الـ avatar لازم يوصل مكان معين. **Mechanisms بتحجب أو تفتح الوصول**: levers وswitches وسيوف سحرية بتدمر أبواب معينة.
4. **Tactical maneuvering**: وضع الـ units على الخريطة لميزة هجومية/دفاعية. حاسم في الـ strategy وبيظهر في RPG وsimulation. الـ rules بتحدد الميزة الاستراتيجية لكل unit في كل مكان. غالبًا بتبقى **tiles** (حتى لو متخبية ورا graphics). أمثلة: chess وGo وStarCraft وCommand & Conquer: Red Alert.
5. **Social interaction**: زمان الألعاب ما كانتش بتحكم التفاعل الاجتماعي إلا بمنع التواطؤ أو إخفاء معلومات. دلوقتي: mechanics بتكافئ **إرسال الهدايا ودعوة أصدقاء جدد**، وrules لـ role-play، وتحالفات في الاستراتيجي. **الـ board games والـ folk games عندها تاريخ أطول** في ده.

- **Mechanics وGenres** ★: الـ genre بيتحدد بنوع الـ gameplay، والـ gameplay بتولده الـ mechanics، فالـ genre بيأثر على نوع الـ rules. **Table 1.1** (أنواع الـ genres من *Fundamentals of Game Design* 2nd ed. مقابل الأنواع الخمسة، وسمك الإطار = الأهمية النسبية). جدول رسومي، مفيش محتواه في النص.
- **لموسفولك:** Mossfolk = **physics** (Unity) كـ core + **internal economy** (9 أحجام، ميزانية إسقاطات، أهداف) + **progression** (3000 ليفل) + **social interaction** (rival contests). فيه تلات أنواع من الخمسة. mossy shells/stones/rot بتضيف عناصر **economy/physics** جديدة مش tactical.

### 1.7 Discrete vs Continuous Mechanics ★★★

- **Continuous**: غالبًا الـ physics (والـ timing/rhythm). حسابات fractional عالية الدقة، مثلاً نص بيكسل يمين/شمال ممكن يغير نتيجة قفزة. بتطلع تدفق لعب ناعم.
- **Discrete**: غالبًا الـ internal economy. قيم integer، مجموعات محدودة من العناصر والأفعال، «**مفيش نص power-up**».
- **الفرق ده بيأثر على:** مدى اعتماد اللعبة على الـ medium، طبيعة تفاعل اللاعب، **وفرص الابتكار** ★★.
- **Physics:** بتحتاج حسابات سريعة كتير، فالألعاب الفيزيائية لازم تتنفذ على كمبيوتر. **Super Mario Bros.** كـ board game صعب (المهارة الجسدية بتضيع) وأنسب كـ physical course. **باترن:** قاعدة «تقفز ضعف الارتفاع بعد item» بتتنقل بسهولة بين الـ media، لكن **تنفيذ القفزة نفسه لأ**.
- **تاريخيًا:** ألعاب الأركيد القديمة كانت أكتر discrete. Donkey Kong أقل continuous من Mario. **Boulder Dash**: الجاذبية = الصخور تنزل **tile واحد كل frame** بسرعة ثابتة (فممكن تتعمل board game). الحواسيب القديمة **ما كانش عندها floating-point** فالـ physics كانت بسيطة.
- **التفاعل:** مع الـ discrete بتخطط وتنفذ استراتيجيات معقدة (تفاعل mental/strategic). مع الـ physics بعد ما تفهمها بتتنبأ بحدس لكن **بيقين أقل**، وتبقى المهارة اليدوية أهم.
- **مقارنة بالاسم** ★★★:
  - **Angry Birds**: القذف بالـ catapult على touch، المحاكاة دقيقة فاختلاف بسيط في السرعة/الزاوية = نتيجة مختلفة تمامًا في الضرر. **القذف = مهارة جسدية.** الاستراتيجية في الجزء الـ discrete (عدد وأنواع الطيور المتاحة، تحديد weak spots، خطة هجوم)، لكن التنفيذ hand-eye ومفيش تنبؤ بالتفاصيل. **فرق بيكسل واحد = critical hit أو miss كامل.**
  - **World of Goo**: بتبني من **goo balls محدودة**. المحاكاة الفيزيائية مفصلة (gravity، momentum، center of mass) واللاعب بيبني حدس منها. **لكن الأهم إنه بيتعلم يدير الـ resource الـ discrete.** **أكثر forgiving**: تسيب الكرة شمال/يمين شوية، النتيجة نفس البناء لأن **spring forces بتشدها لنفس المكان**، **واللعبة بتعرض الـ connections اللي هتتعمل قبل ما تفلت الكرة** ★★★. النتيجة: gameplay أكتر strategic، معتمدة على الـ discrete أكتر.
- **الابتكار** ★★: الـ discrete فيها فرص ابتكار أكتر. الـ physics في FPS مفيش معنى تغييرها وبقت middleware (فمجال الابتكار أضيق). **الـ FPSs بتتميز بنظام power-ups أو item economy فريد.** الـ physics تطورت أسرع من أي نوع تاني (وضوح قوانين Newton + قوة الحوسبة)، أما **قوانين الاقتصاد أصعب وأعقد**. الكتاب بيركز على الـ discrete.
- **لموسفولك:** ★★★ ده أهم كلام في الفصل بالنسبة لينا. Mossfolk أقرب لـ Angry Birds من حيث الـ drop الـ continuous، فلازم نسأل: **فين الـ forgiveness (زي spring forces في World of Goo) وفين الـ preview (زي عرض الـ connections قبل الإفلات)؟** وبما إن الابتكار في الـ discrete: mossy/stones/rot وrival contests وميزانية الإسقاطات هما مساحة الابتكار الحقيقية عندنا، مش الفيزيكس نفسها. التيستر-بوت لازم يقيس الاتنين: حساسية الإسقاط (continuous) وتوازن الـ economy (discrete).

### 1.8 Mechanics and the Game Design Process ★★★

- **Player-centric game design** (Adams): التركيز على أدوار اللاعبين والـ gameplay اللي هيعيشوه. **Gameplay = challenges اللعبة بتفرضها + actions اللعبة بتسمح بيها.** المثال: Mario بيقفز فوق canyon. الـ level design بيحدد شكل الـ canyon، **لكن الـ physics هي اللي بتحدد القفزة قد إيه والجاذبية ونجح ولا فشل**. الـ mechanics بتولّد الـ gameplay، فابدأ تصممها أول ما تعرف الـ gameplay اللي عايزه.
- **تنبيه (NOTE):** المنظور الميكانيستيك ضيق عن قصد. في ألعاب كتير الـ art والـ story والصوت والموسيقى بتساهم بقد الـ gameplay أو أكتر.
- **التلات مراحل:**
  1. **Concept stage**: فكرة عامة + target audience + دور اللاعب → vision document أو game treatment. **القرارات دي ماتتغيرش لباقي الـ design.** ممكن تعمل proof-of-concept سريع (لو مش متأكد من نوع اللعبة، أو عشان pitch، أو playtest لافتراضات)، **بس افترض إنك هترميه وتعيد من الصفر**، فاشتغل سريع من غير قلق من bugs. **متصممش الـ mechanics النهائية قبل نهاية المرحلة** (الخطط ممكن تتغير = جهد ضايع).
  2. **Elaboration stage**: غالبًا بعد التمويل. mechanics وlevels وstory draft وart assets. **لازم short iterative cycles، كل cycle بينتج حاجة playable تتختبر قبل ما نكمل** ★★. «متتوقعش تظبطها من أول مرة؛ هتعيد تصميم features كتير.» **جيب playtesters من برا الفريق ويمثلوا الجمهور**: الفريق ممكن يكون برا الـ target audience وبيعرف اللعبة أكتر من اللازم.
  3. **Tuning stage**: تبدأ بـ **feature freeze**. صعب تتنفذ (هتجيلك أفكار ذكية)، لكن في المرحلة المتأخرة حتى التغيير الصغير ممكن يكسر بشكل مش متوقع ويزوّد الـ debugging والـ tuning. **المرحلة subtractive: شيل أي حاجة مش شغالة أو قيمتها قليلة وركّز على اللي شغال.** ★★★ **الـ polish والـ tuning بياخدوا من ثلث لنص وقت التطوير كله** (الناس بتقلل من تقديرهم).
- **Documenting designs:** design docs = **living documents** (بتكبر مع اللعبة: كل mechanism وlevel بيتضاف). فوايد التوثيق: يخليك على المسار، يمنعك تعيد قرارات قديمة مرة واتنين، ويوحّد الفريق ويقلل الجهد الضايع على features متعارضة. بيبدأ بوصف مختصر للـ concept والـ audience والـ core mechanics والـ art style.
- **Designing Mechanics Early** ★★★: اسبابين:
  1. **الـ gameplay بتطلع (emerge) من الـ mechanics**: «صعب لو مش مستحيل تعرف إنها fun من قراءة الـ rules، الطريقة الوحيدة تلعبها أو أحسن حد تاني يلعبها لك».
  2. الـ mechanics دي complex systems والـ gameplay معتمد على **توازن حساس**، وبعد ما يشتغل **ممكن تهدمه بإضافة features متأخرة أو تعديل mechanisms موجودة.**
  - **بعد** ما الـ core يشتغل ومتأكد إنه balanced وfun، تبدأ levels وart.
- **Make the Toy First** (Kyle Gabler، keynote فيديو لأول Global Game Jam 2009، 7 tips لتطوير لعبة في وقت قصير، والمؤلفين شايفينها تنفع أي مشروع): **قبل أي assets ومحتوى، اتأكد إن الـ mechanics شغالة.** لازم تبقى fun للعب بيها **حتى من غير art حلو وأهداف واضحة وlevel design ذكي**. ★★★ صمّم **toy ممتع في ذاته** وابنِ اللعبة منه.
- **Getting It Right:** النظرية والأدوات مش بديل عن الحاجة الحقيقية. **لازم تبني prototypes وتكرر قد ما تقدر.**
- **لموسفولك:** Mossfolk مرحلة الـ tuning فيه **3000 ليفل** كلها، فقاعدة «ثلث لنص الوقت» ولازم نحسبها في خطة الـ content. وقاعدة feature freeze بتنطبق على إضافة mechanics جديدة (زي mossy/stones/rot): كل واحدة بتكسر توازن الـ economy اللي قبلها، فلازم تتختبر بالتيستر-بوت قبل الدخول في الليفلات. والـ playtesters لازم يكونوا من جمهور الـ hyper-casual مش من الفريق.

### 1.9 Prototyping Techniques ★★★

- **Prototype**: نموذج مبدئي غير مكتمل لاختبار الـ usability قبل المنتج الحقيقي، أسرع وأرخص.
- **مصطلحات:**
  - **High-fidelity**: بيشبه المنتج النهائي، وممكن يتحول للمنتج. تكلفته وقته أعلى.
  - **Low-fidelity**: أسرع، مش لازم يشبه، **غالبًا بتكنولوجيا مختلفة** (2D Flash لـ 3D console game، أو PowerPoint كـ interactive storyboard). بيركز على جانب واحد.
  - **Vertical slice**: كل العناصر (code، art، audio…) المطلوبة لتنفيذ feature أو اتنين. **مفيد لاختبار الـ moment-by-moment gameplay وإعطاء انطباع من غير عرض المنتج كله.**
  - **Horizontal slice**: كل أجزاء جانب واحد من اللعبة ولا حاجة من الباقي (مثلًا UI كامل من غير mechanics شغالة).
- **Software prototyping:**
  - الطريقة الأحسن لتحس بإزاي اللعبة هتبقى. استخدم open-source engines أو **GameMaker أو Unity** حتى لو الهدف مختلف.
  - **عيبه:** أبطأ من النوعين التانيين، ممكن يقرب وقت اللعبة الحقيقية. **بس بيستاهل حتى لو رميت الـ art والكود**: بيخلي المشروع على المسار، المبرمجين يعرفوا العناصر المطلوبة، الـ level designers يعرفوا الاتجاه، والمصممين عندهم بيئة للتجربة. **بيشتغل شبه design document** وبيشرح الـ interactive features أحسن من الكلام.
  - ★★★ **شرط النجاح: سهولة customization.** غيّر الجاذبية في platformer 3D أثناء اللعب. غيّر production rate في RTS بسرعة. **متضيعش وقت في UI**: خزّن القيم الأولية في text file البرنامج بيقراه عند البدء، **أو أحسن: console بسيط off-the-shelf جوه اللعبة تغير منه أثناء اللعب.**
  - **Tip:** prototypes لعبة Spore منشورة أونلاين (spore.com/comm/prototypes) — رؤية لعملية AAA حقيقية.
- **Paper prototyping:**
  - لعبة tabletop من غير كمبيوتر بتشبه لعبتك. **لو اللعبة مش معتمدة بشدة على timing/physics، اعمل board game منها. ولو معتمدة، اعمل paper prototype للأجزاء اللي مش كده** (مثلًا الـ internal economy في لعبة physics).
  - **اعرف إيه الجانب اللي عايز تستكشفه قبل ما تبدأ.**
  - **مش تافه:** تصميم board game جيد فن زي الـ video game، ومفيد تعرف ألعاب كتير («فيه mechanics أكتر بكتير من اضرب نرد وتحرك»).
  - **Kit مقترح من Corvus Elrod** (2011): **ديكين كروت شبه متطابقين بضهر بلون مختلف**، **notebook صغير** (مش كبير فيشتت) + أقلام، **tokens** (poker chips أو حجارة Go)، **كذا نرد** (مش مهم عدد الأوجه)، ولو الـ mechanics بنسب مئوية يبقى **نردين 10 أوجه** لتوليد 1–100. إضافة الكتاب: **sticky notes** + **كروت فاضية 3x5** + **card sleeves** (زي Magic: The Gathering) تدخل ورقة مكتوبة فيها = كارت سهل الخلط، **وتقدر تدخل التعديلات فوق القديم فتفضل تاريخ تصميم الكروت محفوظ** ★.
  - **المزايا:** سريع (**بالمهارة تعمل prototype كويس في ساعات**)، **وقابل للتعديل inherently حتى في وسط اللعب**: «iteration cycles مبتبقاش أقصر من كده». متضيعش وقت في art، اصرف الوقت في صياغة الـ rules واختبارها.
  - **العيوب:** (1) أصعب تدخل لاعبين تجريبيين (لازم تشرح الـ rules بنفسك لأنك هتغيرها طول الوقت، ومبتاخدش وقت لكتابتها، واللاعب قليل الخبرة ممكن مايشوفش العلاقة بين الورق والـ video game). (2) **مش كل mechanics بتترجم، خصوصًا الـ continuous.** **أنسب لاختبار الـ discrete، أي economy وprogression.**
- **Physical prototyping:** اكتب rules والعب في الواقع. ممتاز لما تكون الـ mechanics continuous physical. مثال: الجري في مبنى مكتب بمسدسات laser-tag يدي فكرة عن إحساس FPS. تحضيره أقل من paper غالبًا، سريع وقابل للتعديل، ومفيش مانع تمزج الاتنين، **لكن مش سهل برضه** (محتاج مهارة من المصممين واللاعبين). **Tip: LARP** — اللاعبين عندهم طرق للقتال الجسدي الآمن ولإدخال أشياء مش في الواقع زي magic spells، وساعات مفيد تنضم لجلسة أو تتفرج.
- **Prototype Focus** ★★★: قبل ما تبني اسأل: **عايز أتعلم إيه؟** economy balance محتاج prototype مختلف عن UI جديد. التركيز على جانب واحد يخليك أسرع **ويخلي المختبرين مايتشتتوش بـ features/bugs ملهاش علاقة.** الـ focus بيحدد التقنية: economy of power-ups في platformer ممكن paper، لكن **تجربة control scheme جديد = software prototype high-fidelity قريب من اللعبة**.
- **الأنواع الأربعة للـ focus** (مرتبة من الأبكر للأحدث):
  1. **Tech demos** ★: اتأكد إن الفريق يقدر يتعامل مع التكنولوجيا. **عالج أصعب وأجدد جانب في التكنولوجيا** وأثبت لنفسك (وللـ publisher) إنك تقدر تبني اللعبة. **ابنيها بدري** عشان متتفاجأش، **وانتبه لفرص gameplay** (حاجة بسيطة بتبنيها بسرعة ممكن تدي رؤى أعمق، خصوصًا مع تكنولوجيا جديدة).
  2. **Game economy** ★★★: بتتعمل **paper low-fidelity وبدري**. أسئلة: **هل اللعبة balanced؟ فيه dominant strategy بتكسب كل مرة؟ اللاعبين عندهم interesting choices؟ بيقدروا يتنبؤوا بنتائج اختياراتهم؟** المختبر المثالي: **power gamer خبير بيفهم الـ mechanics بسرعة وعنده خبرة في إيجاد exploits، وقوله «حاول تكسر اللعبة»**. «لو ممكن تتكسر، لازم تعرف». الفريق مختبر كويس لكن عنده handicap (يعرف الاستخدام المقصود).
  3. **Interface and control scheme** ★★: لازم **software prototype**، مش لازم محتوى كتير، «playground» يجرب فيه اللاعب أغلب العناصر. أسئلة: يقدروا ينفذوا الأفعال صح؟ فيه أفعال تانية عايزينها؟ بنديهم المعلومات اللازمة؟ التحكم بديهي؟ **ياخدوا بالهم إنهم بياخدوا damage أو إن state حيوية اتغيرت؟**
  4. **Tutorials** ★★★: لازم اللعبة تكون في **مرحلة متأخرة** (محدش عايز يبني tutorial لـ mechanics ممكن تتغير). **المختبرين لازم ما يكونوش شافوا اللعبة قبل كده**. التطوير زي tutorial طويل، **فمش هتقدر تحكم على صعوبة البداية ومنحنى التعلم بنفسك**، ومتتدخلش وهما بيلعبوا. **السؤال الأهم: هل لاعبيني فاهمين اللعبة وإزاي تتلعب؟**
- **Reference Games = prototypes مجانية** ★★: استخدم الألعاب الموجودة كنموذج، خصوصًا في **UI وcontrols وbasic physics** (اللاعبين عايزين consistency). مثال: مفيش داعي تغير WASD لـ ESDF للابتكار بس. **متسرقش تصميم** لكن اتعلم وتجنب أخطاءهم. اختر reference games بـ **scope** مشابه (لو عندك شهرين متاخدش لعبة عملها فريق كبير في سنين)، إلا لو بتدرس تفصيلة واحدة بس.
- **لموسفولك:** ★★★
  - بما إننا على Unity فـ software prototype هو الأساس. **قيم الـ physics (gravity، bounce، merge threshold، drop budget) لازم تتغير live من console أو text file** زي ما الكتاب بيقول.
  - **التيستر-بوت** هو في الأساس الـ **power gamer المثالي** للـ game economy test: يكسر ويدور على dominant strategy. ومع كده، **التيستر البشري الجديد غير قابل للاستبدال في الـ tutorial/onboarding test** (القاعدة: لاعب جديد، مفيش تدخل، السؤال «فاهم؟»).
  - فحص **Prototype Focus** قبل أي prototype جديد (rot مثلًا): الـ focus economy ولا control ولا tutorial؟
  - الـ reference games المناسبة لـ scope استوديو صغير (مش Suika بتاع فريق كبير، لو ده مش المقصود).

### 1.10 Summary + Exercises ★

- **Mechanics = rules محددة بدقة** (الكيانات والعمليات + **البيانات اللازمة لتنفيذها**). **Continuous** = real-time بحسابات floating-point كتير في الثانية، غالبًا physics. **Discrete** = ممكن مش real-time، بـ integers، لـ internal economy. **لازم تبدأ تصميم الـ mechanics بدري عشان تعمل prototypes تتلعب.**
- **التمارين الثلاثة:** (1) ترجم video game موجودة لـ paper prototype. (2) لاقي reference game مناسبة للعبة عايز تبنيها واشرح الجانب المفيد منها. (3) لاقي أمثلة discrete وcontinuous لكل نوع من الخمسة (physics، internal economy، progression، tactical maneuvering، social interaction) **من غير أمثلة الفصل**.
- **لموسفولك:** التمرين 3 تمرين حلو نعمله على Mossfolk نفسها كـ audit: لكل نوع من الخمسة عندنا إيه الـ discrete وإيه الـ continuous.

---

## الفصل 2 — Emergence and Progression (لحد ص35)

### 2.1 التقسيم الأساسي ★★★

- الـ **progression** = نوع واحد من الأنواع الخمسة → **games of progression**. الأربعة التانيين (physics، economy، tactical، social) = **mechanics of emergence** → **games of emergence**. دول طريقتين بديلتين لخلق الـ gameplay.

### 2.2 History + Games of emergence ★★

- **Juul** قدّمها في «The Open and the Closed: Games of Emergence and Games of Progression» (2002).
- **Emergence**: rules **بسيطة نسبيًا** + **variation كبير**. التحديات وتدفق الأحداث **مش مخططة مسبقًا، بتطلع أثناء اللعب**. بتنتج من التوليفات الكتير للـ rules في board وcard وstrategy وبعض الـ action games. Juul: **«Emergence is the primordial game structure»** (ص324) — أقدم الألعاب كانت emergence، ومعظم الناس بتبدأ تصميم لعبة جديدة بـ emergent design.
- **الـ states:** كل ترتيب لقطع الشطرنج = state مختلف، وإزاحة بيدق مربع واحد ممكن تفرق. توليفات القطع **ضخمة والـ rules في صفحة واحدة** ★. نفس الكلام: وضع residential zones في **SimCity**، ووضع الـ units في **StarCraft**.
- **Progression**: **كمية كبيرة من data معدّة مسبقًا** يقدر اللاعب يوصلها في **أماكن عشوائية (random access)** — مزعج في board games وسهل في video games (جيجابايتات). الـ progression الأحدث (text adventures في السبعينات). مش مقصور على الكمبيوتر: سيناريوهات **Dungeons & Dragons** المنشورة، وكتب **Choose Your Own Adventure**.
- **Board games كلها emergence** عند Juul (قطع قليلة، data معدّة مسبقًا قليلة جدًا — نص كروت Monopoly Chance وCommunity Chest **أقل من 1KB**). والألعاب اللي بتبدأ بعناصر عشوائية (كروت، دومينو) كمان emergence.
- **Progression**: تحديات كتير معدّة مسبقًا، **مرتبة تسلسليًا** بـ level design متطور. المصمم **بيفرض** أحداث بالترتيب. Juul: **أي لعبة ليها walkthrough = game of progression**. في أقصى صورها اللاعب **«railroaded»**. عدد الـ states **قليل نسبيًا** والمصمم له تحكم كامل، **فمناسبة للقصص**.
- **Tip مهم:** متخلطش المصطلح مع leveling up أو difficulty curves أو skill trees. تعريف Juul: **تحديات معدّة مسبقًا، غالبًا كل واحد ليه حل واحد بالظبط، بتسلسل ثابت (أو متغير قليلًا)**.

### 2.3 Comparing + Hybrids ★★★

- Juul في 2002 فضّل emergence («on a theoretical level, emergence is the more interesting structure»، ص328): بتوازن بين حرية اللاعب وتحكم المصمم. حتى emergent games عمليًا بتتبع **patterns منتظمة**: gun fights في **Counter-Strike** بتحصل تقريبًا دايمًا. **Risk**: الأراضي موزعة في الأول وبعدين اللاعبين بيتجمعوا في منطقة أو كذا منطقة متجاورة.
- **Chris Crawford**: **process intensity vs data intensity**. الكمبيوتر بيبرع في معالجة الأرقام وإنشاء محتوى on the fly والـ simulations المعقدة، **فالألعاب لازم تكون process-intensive مش data-intensive، والـ video games لازم تكون emergence مش progression.**
- **Juul في Half-Life (2005) أكتر دقة:** معظم الألعاب الحديثة **hybrids**.
  - **GTA: San Andreas**: عالم مفتوح ضخم + mission structure بيدخل عناصر جديدة ويفتح العالم قطعة قطعة.
  - **Deus Ex**: القصة بتحدد المكان الجاي، لكن عندك استراتيجيات وتكتيكات كتير. ممكن تكتب walkthrough لكن **walkthroughs كتير ممكنة** (زي ما نظريًا ممكن walkthrough لخريطة SimCity، لكن متابعته صعبة).
- **Emergence مش أحسن من progression، هما مختلفين** ★★. **Spectrum** بين قطبين:
  - Pure emergence: كتير من الـ casual زي **Bejeweled**.
  - Pure progression: نادرة، مثال **The Longest Journey** (adventure games — مش النوع المهيمن زي زمان).
  - الأغلب: **emergent behavior جوه الـ level + levels بتسلسل صارم** (Half-Life وZelda). الـ action-adventures أكتر من الـ adventures التقليدية لإنها فيها emergent action. **بين الألعاب الكبيرة الـ hybrids هي الأشهر.**
- **لموسفولك:** ★★★ **Mossfolk = hybrid بالتعريف**: جوه كل ليفل emergent (فيزيكس + merge chains + RNG القطع)، وبين الليفلات progression صارم (3000 ليفل بتسلسل، أهداف، ميزانية). والـ **تحدي الجوهري:** كل ليفل بهدف وميزانية محددين = «challenge معدّ مسبقًا». نسأل: هل بنقدم الـ **Juul walkthrough test** (ليفل ليه حل واحد = progression) ولا الـ emergent (حلول كتير)؟ **التيستر-بوت اللي بيقيس bot_difficulty** بيجاوب عمليًا: لو الـ bots بتكسب بحلول متنوعة = emergent، ولو بحل واحد = أقرب لـ puzzle ثابت. وكمان **مولد الليفلات** بيحط جزء من الـ data-intensity في **process-intensity** (Crawford).

### 2.4 Games of Emergence — البنية ★★★

- **الأصل:** المصطلح من **complexity theory**: سلوك system **ما ينفعش يتشتق مباشرةً من أجزائه**. **Juul بيحذر: ماتخلطش emergent behavior مع سلوك المصمم بس ما توقعوش** ★. «الكل أكبر من مجموع الأجزاء». **Go وChess** (عمق ضخم من عناصر وقواعد بسيطة) + Tetris وBoulder Dash وWorld of Goo (استراتيجيات ضخمة، **مفيش play-through بيحس زي التاني**). **الباترن:** الـ emergent quality **جاية من تعقيد التفاعلات بين الأجزاء مش من تعقيد الأجزاء نفسها.**
- **Simple parts in complex systems:** العلماء بيحاكوا agents بنماذج بسيطة (مثال: تدفق المشاة بقواعد قليلة وأهداف — Ball 2004، ص131–147). الكتاب بيتبنى نفس النهج. **الميزة:** الألعاب دي **efficient to build** حتى لو أصعب في الفهم الأولي ★★.
- **Probability space** ★★:
  - الألعاب كـ state machines بتتفرع بسرعة، **لكن مش كل state ممكنة** (مفيش بيادق بلونك في الصف الأقرب ليك، ولا فيلين على مربعات نفس اللون).
  - **Probability space** = كل الـ states المحتملة من الـ state الحالية. **Wide** = states كتير من الحالية (اللاعب عنده options كتير). **Deep** = states كتير بعد اختيارات متتالية.
  - **Shannon** (1950): states الشطرنج وGo **أكتر من ذرات الأرض**. الـ rules بتحدد عدد الـ states لكن **rules أكتر ≠ states أكتر بالضرورة**. **لعبة تنتج states كتير بـ rules قليلة = أسهل في الوصول للاعبين** ★★.
- **Trajectory** = مسار اللاعب خلال الـ probability space. الـ states والـ trajectories خصائص emergent. **ألعاب فيها trajectories كتير ومثيرة = gameplay أكتر.** **لكن صعب جدًا تحكم على نوع وجودة الـ gameplay من قراءة الـ rules** ★★★.
- **Tic-tac-toe vs Connect Four** (الدليل بالأرقام):
  - Tic-tac-toe: 3×3، تبادل أدوار، المربع يتشغل مرة واحدة، أول من يحتل **3** في صف يكسب.
  - Connect Four: **7×6**، نفس القواعد + **rule 4: بس أسفل مربع فاضي في العمود** + **4** في صف.
  - الفرق في الـ rules قليل لكن **الفرق في الـ gameplay هائل، أكبر بكتير من الجهد الذهني لفهم الـ rules.** القاعدة الأعقد (4) **بتتنفذ بالجاذبية** (التوكن بينزل لأسفل مربع فاضي) فاللاعب بيركز على **آثار** القاعدة مش تنفيذها. Tic-tac-toe للأطفال الصغار بس، وConnect Four ممتعة للكبار: استراتيجيات كتير وإتقانها أطول. بين خبيرين = مباراة مثيرة بدل **draw مضمون**.
- **لموسفولك:** ★★★ درس Connect Four هو بالظبط نفس حالة Mossfolk: **قاعدة الدمج (اتنين نفس الحجم = أكبر) بسيطة، والفيزيكس بتنفذ القاعدة الأعقد (تراكم وتدحرج)**، فاللاعب بيفكر في الآثار. ولأن الـ gameplay quality مش ظاهرة من الـ rules، مفيش بديل عن التيستر-بوت وـ playtests. وكمان: ما نضيفش rules (shells/stones/rot) من غير ما نتأكد إن الـ probability space بتتسع فعلًا مش بس بتتعقد.

### 2.5 مثال Civilization ★★★

- **Sid Meier's Civilization**: تقود حضارة ~**6 آلاف سنة**؛ بتبني مدن وطرق ومزارع ومناجم ووحدات عسكرية؛ upgrades (temples، barracks، courthouses، stock markets)؛ فلوس للبحث أو تحويلها لـ luxuries للسكان أو تسريع الإنتاج. **Turn-based على tile-based map**، كل turn = سنين. حضارات AI بتنافس على المساحة والموارد.
- **كل العناصر بسيطة بشكل مفاجئ:**
  - معبد: **1 gold في الـ turn** ويقلل غير السعداء في المدينة بـ **2**.
  - Units: قيم integer للحركة والهجوم والدفاع.
  - **Settlers** تبني مدن، **artillery** تقصف من بعيد.
  - **جبال**: تكلف حركة زيادة وتضاعف الدفاع (**×2**) والطرق تلغي تكلفة الحركة.
- **الـ mechanics كلها discrete** (turn-based، tiles، أرقام صحيحة) = **سهلة الفهم فرديًا** (تحسب في دماغك) **لكن الـ probability space ضخم** ★★★. الوصف الكامل بياخد كتاب والـ game جاي بـ encyclopedia.
- **ليه معقدة:** **كل حاجة متصلة بكل حاجة**: الوحدات بتتنتج في المدن وتستهلك موارد كان ممكن تروح لحاجة تانية، وبعدين upkeep بالذهب كل turn؛ الطرق استثمار وقت وموارد لكن بتنشر القوات بكفاءة فتقلل الجيش المطلوب؛ البحث بيخلي وحداتك أقوى. جيش قوي بدري = توسع أكبر لكن على حساب تطورات تانية = تأخر طويل المدى. **وقرارات الحضارات التانية بتأثر على فعالية استراتيجيتك.**
- **استراتيجيات ومراحل بتظهر طبيعيًا:** توسع مبكر (امسك الأرض، تكنولوجيا بسرعة لتحديد الموارد) → قابل الحضارات: هجوم أو صداقة (الغزو الكامل أسهل بدري وأصعب بعدين) → لو غني وجارك لأ: **cultural offensive** → مراحل: **early expansion، investing in economy، violent conflict، technology & production race to space**. **الـ setup بيطلّع كل ده من الـ mechanics.**
- **Historical periods vs gameplay phases** ★★: الفترات (classical → medieval → renaissance → modern) بتحدد الـ graphics والتمثيل، **triggers اعتباطية** ومش بتنبثق من الـ mechanics (إضافة سطحية للون بصري). **Golden age**: 20 turn من إنتاج مرتفع، محفزاتها شبه اعتباطية، **لكن اللاعب عنده تحكم أكتر ويستطيع يستهدفها**، فهي **بين المنزلتين**: مش emergent لكن بتأثر على gameplay phase.
- **كمصمم Civilization-like:** تعمل iterations وprototypes كتير، **حافظ على كل عنصر بسيط لكن اعمل علاقات كتير بينهم**. ده يضمن التعقيد **لكن مش** gameplay مثير. **لازم تعرف structure الـ mechanics: بعض البنى بتطلع emergent behavior أكتر.** ★★★ **Feedback loops في الـ mechanics طريقة قوية خصوصًا لو بتشتغل على مقاييس وسرعات مختلفة** (هتتفصل في الفصول الجاية). **«Structures»** = الطرق اللي المصمم بيربط بيها mechanics ببعضها (feedback loop وtrigger اللي بيشغل event لما شرط يتحقق).
- **لموسفولك:** ★★★ الباترن ورا Civilization: **عناصر بسيطة × علاقات كتيرة × feedback على مقاييس مختلفة = مراحل لعب طبيعية من غير scripting**. عندنا: مراحل الـ jar (فاضي → متراكم → ضغط) بتطلع من الفيزيكس والميزانية، **مش من أرقام الليفلات**. وعشان كده «mossy shell» لازم يكون له علاقة بباقي العناصر (مش بس عقبة منفصلة). وتحذير الـ Golden age: أي bonus أو event حفزناه بشكل اعتباطي بيأثر على اللعب لكن مش مصدره الـ mechanics، فيبقى يتصنف كـ progression/dressing مش emergence.

### 2.6 Games of Progression ★★★

- **مصمم محترف لازم يعرف progression**: ألعاب كتير فيها story على مدى ليفلات. كل ليفل **mission واضحة** بتحدد الأهداف وتبني المهام. المصمم لازم يخطط اللعبة والليفلات لـ **تجربة متماسكة**، وبيستخدم mechanics تتحكم في إزاي اللاعب يتحرك. **مفتاح لتصميم levels كويسة وinteractive stories.**
- **المعركة الأكاديمية** (NOTE): **Narratologists** (الألعاب في تقليد وسائل السرد) vs **Ludologists** (ابدأ بالـ mechanics والـ gameplay أولًا). **Angry Birds**: ليها story لكن بتتحكى بين الليفلات بس، **والأحداث جوه الليفل ما بتشاركش فيها** — الـ ludologists محقين هنا. لكن فيه ألعاب بتدمج gameplay مع story (RPG وadventures خصوصًا). «لما نقول storytelling نقصد القصص المدمجة مش السياق السطحي».
- **Progression mechanics = أداة المصمم** لتحديد: مين العناصر اللي اللاعب يقابلها الأول، يبدأ بإيه من موارد، وإيه المهام لازم يعملها. **القدرات + layout الليفل + مكان الـ locks والـ keys والـ power-ups الحيوية** → اللاعب بيتدرج في اللعبة، وبيستكشف ويكتسب قدرات ومهارة، **وفي الآخر بتتكون تجربة شبه قصة** (أحداث الليفل، أدلة، cut-scenes عند أماكن معينة).
- **Tutorials** ★★★: بنستخدم progression mechanics لعمل tutorials وlevel design تدرب اللاعب. **عدد الـ rules والـ UI والخيارات في أي retail game أكبر من إن اللاعب يستوعبه مرة واحدة**، حتى الألعاب الصغيرة على الإنترنت. **التعرض للكل مرة واحدة = تجربة ساحقة ويسيب اللعبة بسرعة.** **الحل: صمم الليفلات لتعليم الـ rules في chunks سهلة، وفي الـ tutorial levels المبكرة اللاعب يجرب في بيئة آمنة ومتحكم فيها، والأخطاء عواقبها قليلة.**
- **Narrative architecture** (Henry Jenkins 2004، «Game Design as Narrative Architecture»): الألعاب بتتفوق في تصوير **المساحة** (عكس الأدب والسينما اللي بتفوق في الزمن). **«spatial stories»**: زي الأساطير ورحلات الأبطال وTolkien. **مجرد السفر في فضاء اللعبة بيحكي قصة.** وبيعني تدريب اللاعب بالـ tutorials والـ level design هو من نقاط قوة الـ video games.
- **Half-Life** ★★: FPS بيعبر عالم يبدو واسع بس في الحقيقة **مسار ضيق**. القصة كلها جوه اللعبة: **مفيش cut-scenes** تاخد اللاعب برا، الحوارات من شخصيات داخل اللعبة، واللاعب يقدر يسمع أو يتجاهل. **Railroading**: مش صدفة إن اللاعب بيوصل بـ**قطر** في Half-Life وHalf-Life 2. **العيب:** حرية اللاعب **وهم**، ولما اللاعب يروح اتجاه مش مقصود **الوهم بينكسر بسرعة**، ويحتاج مهارة تصميم عالية لمنع اللاعب من ملاحظة الحدود الخفية.
- **صعوبة الـ interactive stories:** **Branching story trees** غير فعالة (محتوى كتير مش هيعيشه اللاعب في play-through واحد). **Open worlds** (زي Elder Scrolls) حرية كبيرة لكن **اللاعب بيضيع القصة الرئيسية**. المطلوب **توازن دقيق** بين الحرية والتقييد بالـ level design.
- **لموسفولك:** ★★★ الـ tutorial عندنا (أول ليفلات) لازم تتصمم كـ progression chunks: كل عنصر جديد (shell/stone/rot) في بيئة آمنة وعواقب قليلة وبالتدريج، وده بيتفق مع Extra Credits (المعلومة وقت الحاجة). والـ side quests وrival contests هي «الـ open world» عندنا، والتحذير: خطر ضياع الخط الرئيسي (زي Elder Scrolls). الـ **narrative architecture** ممكن تتطبق على ترتيب الليفلات والـ garden/world map كحكي مكاني.

### 2.7 مثال Zelda: Forest Temple (Twilight Princess) ★★★

- **الليفل:** Link ينقذ **8 قرود** من وجود شرير في معبد الغابة. المهمة: تحرير 8 قرود + هزيمة **mini-boss** (ملك القرود **Ook**) + إيجاد وإتقان **gale boomerang** + هزيمة **level boss** (**Twilit Parasite Diababa**). Figure 2.3 = خريطة، Figure 2.4 = **graph المهام وعلاقاتها**.
- **سلسلة الاعتماد (dependency chain):** للوصول لمعركة الـ boss النهائية → لازم مفتاح وإنقاذ **4 قرود** → ده محتاج الـ gale boomerang → ده محتاج هزيمة ملك القرود … وهكذا. **بعض المهام ترتيبها مش مهم** (تحرير القرود)، **وبعضها اختياري لكن بمكافآت مفيدة**.
- **السمات اللافتة:**
  - **Bottleneck** في نص الـ mission = معركة الـ mini-boss + الحصول على الـ boomerang.
  - **قسمين parallel options قبل وبعد الـ bottleneck.**
  - الفضاء مبني بـ **hub-and-spoke** بيدعم المهام الموازية: من **القاعة المركزية (حيث بتحارب العنكبوت الكبير)** تروح 3 اتجاهات. الطريق اليمين يتفرع بسرعة لـ 3 طرق: **3 لقرود محتجزة وواحد للـ mini-boss**. الأخير **مفتوح بعد تحرير أول 4 قرود**. بعد الـ boomerang تقدر توصل أماكن إضافية في الـ hub الأول و**hub جديد**.
- **Hub-and-spoke (NOTE):** غرفة مركزية = hub، الأجزاء = spokes، اللاعب يرجع للـ hub بعد كل مهمة. **المزايا:** اللاعب **يختار أي مهمة الأول (ويغير لو صعبة)**، الـ hubs أماكن حلوة لـ **save points ومداخل الـ dungeon**، **ويقلل backtracking** في أماكن شافها اللاعب بالفعل. تفاصيل أكتر: فصل 12 في *Fundamentals of Game Design*.
- **Zelda مش pure progression:** كل ألعابها بتدمج progression مع **emergent gameplay**. القتال مثلًا emergent (يتعلم تقنيات كتير ويكتشف الاستراتيجية الأنسب لكل عدو). **لكن فيها levels ذكية وstory line طويلة، فهي مثال رئيسي للـ progression.**
- **Lock-and-key:** الـ gale boomerang مثال نموذجي للـ lock-and-key mechanisms المعتادة في سلسلة Zelda (Ashmore & Nietsche 2007، «The Quest in a Generated World»). **الـ lock-and-key = طريقة لترجمة prerequisites قوية في mission لبنية مكانية تفرض العلاقات بين المهام.** الـ boomerang **سلاح ومفتاح**: بينشط **wind switches** بتتحكم في **كام جسر دوّار** يفتح مناطق جديدة. وللوصول لـ **master key** اللي بيفتح باب غرفة الـ boss النهائية لازم تنشط **4 switches بالترتيب الصحيح**، و[الجملة مقطوعة هنا — بتكمل في الجزء 2].
- **الباترن ورا Zelda:** المهام = **graph مش خط**، فيه bottleneck للـ gating وparallel sections للاختيار، والـ lock-and-key بيحول الاعتماديات لمكان، وبكده الـ level design هو الـ progression mechanism.
- **لموسفولك:** ★★ الـ 3000 ليفل خط مش graph، لكن **الـ side quests hub** و**الـ garden/world map** ممكن تتبني hub-and-spoke (اللاعب يغير المهمة لو صعبت، ومفيش backtracking زايد). وتحدي 2501+ (mossy shells/stones/rot) ممكن يتصمم كـ lock-and-key خفيف: كل عقبة «تتفتح» بأداة/ميزة اتعلمها قبلها. ولتسلسل الـ boss/الذروة، Forest Temple نموذج لـ **bottleneck في النص**.

---

**ملخص الجزء 1 (للربط لما نكمل):** المؤلفين بيأسسوا إن الـ mechanics (خصوصًا discrete) هي اللي بتولد الـ gameplay، وإن **المصمم لازم يبني prototypes بدري** (paper للـ economy، software للـ control، tutorial test بلاعبين جدد)، وإن الألعاب على spectrum بين **emergence** (قواعد بسيطة × تفاعلات كتير = probability space ضخم) و**progression** (تسلسل مخطط بـ locks/keys وhub-and-spoke)، وإن أغلب الألعاب الكبيرة hybrids. **الجزء 2 هيكمل من منتصف لـ Zelda lock-and-key في الفصل 2** (Structural Differences وIntegration)، وبعده الفصل 3.

# Game Mechanics: Advanced Game Design (Adams & Dormans) — جزء 2/8 — نوتس مذاكرة

**الجزء ده:** من منتصف Ch.2 (الـ gale boomerang في Forest Temple، ص51) لحد Ch.5 لحد شكل الـ random flow rates (ص84 تقريبًا). الكتاب مش برمجة، فمفيش حاجة متجاهلة. الجزء بينتهي في نص Fig 5.5 (تدريجات الـ random rates)، وبقية Ch.5 في الجزء 3.

---

## الفصل 2 (تكملة): Emergence and Progression — ص51–57 ★★★

### Zelda: Forest Temple (Twilight Princess) — الـ progression المتصمم كـ hero's journey

1. **Gale boomerang = مفتاح + سلاح + أداة تجميع**: بيجيب حاجات بعيدة (عنده power يلقط items صغيرة ومخلوقات) وبيتستخدم كسلاح. **التاكتيك**: المصمم يحط عناصر النص التاني من المهمة (بعد الـ mini-boss) في **نفس المساحة** بتاعة النص الأول ★★. اللاعب بيقابل عوائق مش قادر يعديها لحد ما يلاقي «المفتاح الصح» (الـ boomerang).
   - **الباترن ورا التاكتيك**: ده space reuse. الأكبر من الـ level بيتحول من «مساحة جديدة» لـ «نفس المساحة بقدرات جديدة»، فتكلفة المحتوى بتقل والـ backtracking بيبقى مكافأة.
2. **Discrete mechanics جوه Zelda**: Zelda بتخلط **continuous** (الفراغ وأغلب التحديات الفيزيائية) مع **discrete**.
   - الـ discrete: قلوب الـ health bar، والـ damage (عدو معين دايمًا بيعمل نفس الضرر، وبتقتله بعدد ثابت من ضربات السيف)، وكل mechanics التقدم (small key لباب، **عدد معين من القرود** عشان تعدي فجوة).
   - **الباترن**: الـ progression بيعتمد على حالات بسيطة ومحسوبة (discrete) عشان المصمم يقدر يتحكم فيها.
3. **هيكل Forest Temple = حكاية بطولية** ★★ (الأرقام والتسلسل بالنص):
   - يدخل Link → **challenge to adventure**: أول قرد من **8 قرود** لازم يحررهم.
   - بعدها بشوية: عنكبوت كبير بيحرس أول **hub**. هزيمته بتفتح أماكن كتير في الجزء الأول.
   - اختبارات وعوائق، وأصدقاء وأعداء جدد.
   - **منتصف الـ level**: مواجهة monkey king، وفيه **plot twist**: مش هو الخصم الحقيقي.
   - الهروب بـ magic item (gale boomerang) بيفتح الجزء التاني ويساعد في هزيمة الخصم الحقيقي في **climactic battle** أخير.
   - **الباترن**: نفس الهيكل (hero's journey) مبيبايتش في الحواديت وأفلام المغامرات، وبيتكرر في مغامرات Link وألعاب تانية كتير.
4. **Takeaway التصميمي** ★★★: كل عدو/trigger/lock = «آلية بسيطة» بتتحكم في الوصول للجزء التاني من القصة. أهم أدواتك للتحكم في التقدم هما **الـ layout الفيزيائي للـ level ومكان الـ key items**. القواعد التلاتة:
   - تجربة smooth ومتماسكة.
   - اللاعب لازم يكون اتعلم ومارس المهارات المطلوبة قبل الـ level.
   - **الأهم**: اللاعب يستمتع بتقدمه نفسه، بإنه يتغلب على عقبات كان **عاجز** عنها في الأول.
5. معلومة جانبية: Christopher Vogler — *The Writer's Journey: Mythic Structure for Writers* (1998) هو أشهر مرجع عن hero's journey.

### الفروق البنيوية: Emergence vs Progression ★★★

- **Emergence**: قواعد **قليلة**، والتعقيد جاي من **التفاعلات والاتصالات بين القواعد** مش من عدد القواعد.
  - فيه **complexity barrier** (Fig 2.5): بعد نقطة معينة في تعقيد القواعد، تعقيد الـ gameplay **بيقفز**. التفاعلات بتعمل **explosion of the probability space**.
  - المكانيزمات دي بتضيف **حالات (states) كتير** للعبة → replayability عالية، وكل بلاي مختلف.
- **Progression**: قواعد **كتير** وتفاعلات **قليلة** بينها. أغلب المكانيزمات بتخدم غرض واحد: تمنع اللاعب يوصل مكان لحد ما يخلص مهمة تانية. حالتها **اتنين بس** (باب مفتوح/مقفول، مفتاح اتلقى/لأ). نادرًا بتضيف states، **بس المصمم بيتحكم فيها بسهولة**.
  - **المميزات**: المصمم يملي **ترتيب** التحديات والمهارات، ويدمج تحديات متصاعدة جوه قصة كبيرة. التجربة الكلية أسهل في التصميم بكتير من emergence.
- **شكل الـ probability space**:
  - Emergence: **large and wide** (خيارات كتير + عوامل خارج تحكم اللاعب زي النرد).
  - Progression: **small but deep** (تسلسل طويل من اختيارات، وكل نقطة قرار فيها خيارات قليلة، فالمصمم عارف النتايج ومتحكم فيها).
  - **ده سبب** إن ألعاب الـ progression أطول وبتقدر تحكي قصة متماسكة، وألعاب الـ emergence (زي checkers) أقصر.
- ★★ **فخ الـ emergence الطويلة**: لو اللعبة طويلة والـ emergence عالية، غلطة صغيرة بدري ممكن تخلي اللعبة **مش قابلة للكسب بعد ساعات**. ده **design flaw**، ومثاله **X-COM: UFO Defense** (لعبة ممتازة بس فيها ده).
- الـ progression بتقيّد الـ probability space (اللاعب مش بيكمل قبل ما يحل المشكلة)، وبتخلّيك تتحكم في الصعوبة فلا يقابل تحدي مش جاهز له.
- **Table 2.1** (حرفيًا):

| البند | Emergence | Progression |
|---|---|---|
| عدد القواعد | Low | High |
| عدد عناصر اللعبة | High | Low–High |
| التفاعلات بين العناصر | High | Low |
| Probability space | Large, wide | Small, deep |
| Replay value | High | Low |
| تحكم المصمم في التسلسل | Low | High |
| طول اللعبة | قصيرة (Civilization استثناء نادر) | طويلة |
| Learning curve | Steep | Gentle |

### دمج Emergence + Progression ★★★

- الهدف: **حرية ومفتوحية الـ emergence** + **تجربة منظمة شبه القصة من الـ progression**. الـ progression هو أداة الحكي، لكن صعب تعمل plot متماسك مع حرية فعل كبيرة.
- **الممارسة الفعلية: التناوب**. level/mission emergent بيفتح حتة صغيرة من القصة بين الـ levels، وبعدين emergent level تاني. مثال: **GTA**: تكسب المهمة بطرق متنوعة جدًا لكن اختياراتك **مش بتأثر على القصة**، القصة بتحصل بين المهام.
- قليل جدًا من الألعاب نجح يدمجهم **في نفس اللحظة**. الأسباب التلاتة:
  1. الـ video games وسيط صغير لسه.
  2. **فجوة Wardrip-Fruin** (*Expressive Processing*, 2009): mechanics الـ simulation (حركة، قتال، فيزيا) متطورة جدًا، أما تتبع تقدم القصة فمجرد **bottlenecks/gates** كـ milestones. لما اللاعب يخلص مهمة المحطة، القصة تتقدم. شكل mechanics القصة أقل إثارة من باقي اللعبة.
  3. مفيش نظرية formal قوية عن إيه الـ mechanics. وده هدف الكتاب (منهج منظم).

### StarCraft → StarCraft 2 (مثال التكامل) ★★★

- **SC1 = emergence صرفة**: ساعدت تعرّف genre الـ RTS. عناصر بسيطة وعلاقات كتير. الـ campaign: **30 mission**، أغلبها تبني base، تدير موارد، تبني/ترقي قوة هجوم، تدمر الأعداء. **التقدم جوه الـ mission تقريبًا ثابت وبالتالي متوقع → مش حاسسه قصة**.
  - القصة بتتحكى **حوالين** الـ levels (على بنية tragedy كلاسيكية، نادرة في الألعاب)، لكنها **framing device**: أداء اللاعب واختياراته **صفر تأثير** على الـ plot غير إنه يخلص المهام.
- **SC2 (بعد أكتر من عقد)**: التغيير الأكبر = القصة وتكاملها. الـ core mechanics اتغيرت قليل (تبني base، موارد، ترقي القوة)، لكن **المهام متنوعة** جدًا:
  - **"The Devil's Playground"**: الأجزاء السفلية من الماب **بتغرق بالحمم دوريًا** وتدمر كل حاجة فيها. الهدف **مش تدمر base عدو** بل تعيش وتحصد كمية موارد. إيقاع وتقدم مختلف.
  - **"The Evacuation"**: تحمي **مستعمرين مدنيين** هربانين من كوكب اجتاحه الأليينز. تؤمّن **4 caravans** عشان توصل لميناء فضائي. بتبني base وقوة هجوم **لكن لحماية المسار والمدنيين**.
  - نادر تلاقي مهمة بتمشي في مراحل SC1 المعتادة. **اللاعب بيتضغط بأحداث وسيناريوهات متصممة مسبقًا = classic progression mechanic**، فالمهام متنوعة، وبتجبر اللاعب يكيّف استراتيجيته وأنماطه، ومش مكررة → **أكتر شبه بالقصة**.
  - تحكم أكبر في القصة الكبيرة: ترتيب المهام جزئيًا، وأحيانًا اختيار بين اتنين. لكن ده **أقل تطورًا** من التكامل على مستوى المهمة الواحدة.
- **الباترن**: أحسن دمج بيحصل على **مستوى الـ mission**: نفس نظام emergence تحته، وفوقه أحداث/قيود progression مصممة بتغيّر الهدف والإيقاع.

### الملخص والتمرين

- فيه ميل في game studies عند مصممين معينين لتفضيل emergence، سببه بنية mechanics أكتر إثارة وحجم possibility space.
- **تمرين**: الشطرنج ليه 3 مراحل (opening / middle / endgame) والقواعد ما بتتغيرش، فالظاهرة **emergent property** مش مصنوعة بـ progression. المطلوب: (1) لعبة تانية (طاولة أو video) بمراحل لعب مختلفة، (2) إيه السبب، (3) المراحل emergent فعلًا ولا نتيجة سيناريو متصمم/triggers عشوائية؟

**لموسفولك:** ★★★ Mossfolk في الأساس لعبة emergence (physics merge)، وطبقة الـ 3000 level (goals + drop budget) هي الـ progression فوقها. الـ SC2 lesson ينطبق مباشرة: تحديات 2501+ (mossy shells / stones / rot) هي بالظبط «أحداث متصممة بتضغط على اللاعب» بتكسر تكرار الليفل، والتنويع بيجي من **تغيير الهدف والإيقاع** مش بس من زيادة الأرقام. أسئلة للمراجعة: (1) كل challenge كائن بيغيّر الهدف ولا بس بيصعّب؟ (2) فخ X-COM عندنا هو **dead state**: ممكن إسقاطة بدري في جرة تخلي الليفل مستحيل بعد ما الـ budget يخلص؟ التيستر-بوت يقيس نسبة الـ runs اللي بتدخل dead state بدري. (3) الـ side quests (rival contests) و minigames هي طبقة progression تانية، فنسأل: بتتكامل مع الـ core ولا إطار حواليه (زي قصة SC1)؟

---

## الفصل 3: Complex Systems and the Structure of Emergence — ص43–58 ★★★

### Gameplay كـ emergent property

- **تعريف Gameplay**: التحديات اللي اللعبة بتحطها قدام اللاعب + الأفعال اللي اللاعب يقدر يعملها. أغلب الأفعال بتتخطى تحديات، وقليل مش مرتبط بتحديات (تغيير لون عربية، شات). الأفعال بتحكمها الـ mechanics (الأفاتار ما يقفزش إلا لو في jumping mechanic).
- طريقتين لتوليد التحديات:
  1. **تحدي ↔ فعل فريد** (text adventures: كل puzzle فريد وله حل فريد) = progression.
  2. **Tetris** ★: محدش برمج كل تتابعات القطع. اللعبة بترمي tetrominoes عشوائيًا، والتحدي = **تتابع عشوائي × أفعال اللاعب السابقة**، مختلف كل مرة، واللاعب عنده تحكم. **أفعال قليلة تتعامل مع تنوع لانهائي من التحديات** (Solitaire card games كمان).
- ★★★ **Harvey Smith — "The Future of Game Design" (2001)**: ابني الأنظمة بحيث اللاعب يتصرف بطرق تعبيرية (expressive) واسعة. **ابعد عن الحلول الخاصة لتحديات فردية متصممة، وروح لـ mechanics بسيطة ومتسقة تتركب بطرق مثيرة، حتى لو طلعت نتايج غريبة**.
  - مثال: **Rocket jumping**: الصاروخ المتفجر بيدي قوة للأجسام القريبة في أغلب الـ FPS، فلاعبين أذكياء استخدموها يقفزوا أعلى وأبعد. Smith شايف ده **فرصة مش مشكلة**.
- **Sidebar: Consistency over Realism** ★★: Steven Poole — *Trigger Happy* (2000): في الألعاب **الاتساق أهم من الواقعية**.
  - Formula 1 واقعية = سنين تدريب = مش ممتعة.
  - لاعبين متوقعين blasters Star Wars مش ليزر حقيقي (سرعة الضوء ومخفي).
  - الناس عايزة تعمل حاجات مستحيلة/خطيرة، والـ rocket jump جزء من المتعة. **لكن بيتحبطوا لو الـ mechanics بدت اعتباطية**: صاروخ بيقتل عدو جامد ومش بيكسر باب خشب خفيف.
- **عدد القواعد ≠ تعقيد السلوك**: العلاقة مش خطية (tic-tac-toe و Connect Four من Ch.2). **مفيش إنك تضيف قواعد = لعبة أحسن**، وأحيانًا **تقليل** القواعد بينتج emergence أحسن.
- ★★ **الصعوبة**: صعب تتنبأ من القواعد وبس إذا هتطلع gameplay مثيرة.

### بين النظام والفوضى ★★

- **أنظمة معقدة (Complex systems)** مش «صعبة الفهم» بل **فيها أجزاء كتير**، كل جزء بسيط. لما يتجمعوا بيظهر سلوك مفاجئ. الألعاب مثال كلاسيكي في أدبيات التعقيد.
- **تصنيف من 4 درجات** (Fig 3.1): **Ordered** (سهل التنبؤ) ← **Periodic** ← **Emergent** ← **Chaotic** (مستحيل التنبؤ حتى لو فاهم الأجزاء). الـ emergence **بين النظام والفوضى**.
  - **Periodic**: بيمشي في عدد مراحل محدد بتتابع متوقع (الفصول الأربعة. بعض المناطق بإيقاع صارم، والأحوال العامة متوازنة).
  - **Emergent**: أنماط مستقرة لكن ممكن **يتحول من نمط لنمط فجأة**. الطقس: دورة الفصول معروفة لكن الطقس لسنة معينة (أول صقيع، كمية الثلج) شبه مستحيل التنبؤ بدقة. قواعد الإبهام (مثل «plant peas on Good Friday») مش موثوقة كل سنة.
- **تجربة الحنفية** (الـ 4 فئات بإيدك):
  1. حنفية مقفولة = ordered.
  2. فتح خفيف = نقط منتظمة = periodic.
  3. فتح أكتر = نقط أسرع، وقبل التيار الكامل بقليل ينقلب غير منتظم = ناحية chaos.
  4. بين الاتنين ممكن أنماط periodic أعقد (نقطتين سريعتين وبعدها وقفة)، أو تتناوب بين نقط سريعة وتنقيط بطيء غير منتظم = **emergent**.
  5. فتح أكتر = رجوع سريع لتدفق ثابت منظم.
- **داخل الألعاب** ★★: كذا نمط مع بعض:
  - ألعاب progression = **ordered** (كل تتابعات التحديات والأفعال متصممة مسبقًا).
  - ألعاب الطاولة بالأدوار = **periodic**. والـ ticks في الـ MMORPGs بتأثر على استراتيجيات اللاعبين.
  - مراحل Civilization (expansion, consolidation, war, colonization, race to space) = **emergent**.
  - النرد والـ RNG واللاعبين التانيين = عنصر **chaotic**.
  - **المصمم لازم يوازن كل ده** بحيث السلوك العام يقع في فئة emergence.

### هل الـ emergence ممكن تتصمم؟

- الـ emergence بتحصل **بعد تشغيل النظام**. ده سبب اعتماد الـ game design على الـ **prototypes والـ playtests**: النظام المعقد مفيش طريقة تعرف إنه ممتع/متوازن إلا بإن ناس تلعبه.
- **باراكس**: المصمم ممكن ميعرفش الحالة النهائية بالظبط، بل بيصمم **تجربة الوصول**. لكن بنى معينة بتنتج نتايج معينة، وفهمها بيساعد حتى مع الاحتياج لتست كتير.

### الصفات البنيوية للأنظمة المعقدة ★★★ (أهم جزء في الفصل)

- **Butterfly effect**: تغيير صغير = تأثير كبير بعدين (فراشة تحرك هواء → إعصار على الجانب الآخر). أمثلة تانية: البورصة، المرور، حركة المشاة، طيران الطيور، حركة الأجرام.
- **Cellular automata** (المجال بين الرياضيات وعلوم الكمبيوتر والألعاب): خلايا في خط/شبكة (أبيض/أسود). قواعد بتحدد تغيّر اللون حسب لون الخلية وجيرانها (**8 جيران في 2D، جارين في الخط**). بتتحدث كلها **في آن واحد** (بتتعلّم، وبعدين تتغيّر كلها قبل الـ iteration الجاي). كل iteration = **generation**.
- **Wolfram's automaton** (*A New Kind of Science*, 2002): خط خلايا، حالة كل خلية = حالتها السابقة + جارين → **8 تركيبات** ممكنة. تبدأ بخلية سودا واحدة. مثال القواعد: «سودا محاطة بسودا من الجانبين → تبقى بيضا»، و«بيضا فيها سودا على الشمال فقط → تبقى سودا». **مفيش عشوائية في القواعد**، ومع ذلك الناتج شكله عشوائي ومعقد.
- **التلات صفات الحرجة للسلوك الديناميكي** (Wolfram):
  1. **خلايا بسيطة بقواعد محلية** (أجزاء توصف بسهولة منفصلة).
  2. **Long-range communication**: تغيير في جزء يقدر يأثر في أجزاء بعيدة في المكان/الزمان. في الأتوماتون: كل خلية بتأثر على جيرانها، والجيران ليهم جيران → كل خلية متصلة بكل خلية بشكل غير مباشر.
  3. **مستوى النشاط (activity)** مؤشر جيد لتعقيد السلوك. قليل جدًا من الخلايا النشطة = مفيش سلوك معقد. «نشطة» = اتغيّر حالتها.
- ★★ **تقدر «تقرا» الصفات من القواعد**: كل خلية بتاخد input من نفسها + جارين = اتصال محتمل. **4 من 8 قواعد** بتغيّر اللون = نشاط كبير متوقع.
- **عتبة التعقيد منخفضة بشكل مفاجئ**: قواعد بسيطة + كفاية أجزاء + نشاط + اتصالات = سلوك معقد. ومفيش لازم لاعب بشري، الـ emergence ممكن تحصل من غير input بشري.
- ★★★ **Tower Defense كمثال لعبة تشبه الـ cellular automata**:
  - أعداء بمسار متصمم، وكل عدو سرعة وhit points وبعض السمات. أبراج تطلق على أعداء في مدى وبمعدل معين، وبعضها يبطئ، وبعضها **يعزز أبراج مجاورة**.
  - فيه عناصر **محلية** (أعداء وأبراج) **نشطة** (الأعداء بيتحركوا، والأبراج بتستجيب) و**مترابطة** (الأبراج بتضرب الأعداء، وبتعزز بعض).
- ★★★ **الفرق بين ألعاب emergence و progression من حيث النشاط والاتصال**: في الـ progression، كل العناصر (puzzles، شخصيات) بتتفاعل **مع الأفاتار بس** مش مع بعض، وبتنشط **بس وهي على الشاشة** (اللي برا الشاشة خامل). التفاعلات قليلة ومحددة مسبقًا → تحكم للمصمم لكن **ألعاب متوقعة وبتبطل تبقى ممتعة لما كل الخيارات المتصممة تتستكشف**.

### الـ Feedback loops: تثبّت أو تزعزع النظام ★★★

- **Ecosystem / predator–prey**: فريسة كتير → مفترسين يلاقوا أكل → عددهم يزيد → الفريسة تقل → مفترسين مش لاقيين أكل → عددهم يقل → الفريسة تزيد… **Feedback loop** = تأثير تغيير في جزء بيرجع يأثر على نفس الجزء لاحقًا.
- **Negative feedback loop** (يحافظ على التوازن): thermostat (حرارة منخفضة → سخان → ترتفع → يقفل)، **speed governor** (آلة تسرع → يقلل مصدر القدرة، تبطأ → يزيده؛ بيخلي الآلة تشتغل بأكفأ سرعة ومتجريش بخطورة لو الحمل اتشال فجأة). في الألعاب: **Civilization**: سكان المدينة بيطلبوا أكل أكتر فتوقف النمو عند حجم مستقر يتحمله التضاريس ومستوى التقنية (Fig 3.4: مدينة Thebes).
- **Positive feedback loop** (يعزز اللي سبّبه): **audio feedback** (ميكروفون ← مكبّر ← سماعات ← ميكروفون… صرخة حادة، توقفها بإبعاد الميكروفون). في الألعاب: الشطرنج، لما تاخد قطعة عندك قطع أكتر فأسهل تاخد تانية. **يخلق أنظمة volatile بتتغير بسرعة**.
- **الباترن**: negative feedback = استقرار، positive feedback = زعزعة. أغلب ألعاب emergence فيها **كذا loop بيشتغلوا مع بعض**.

### أنماط سلوك مختلفة على مقاييس مختلفة (Different Scales) ★★★

- **Conway's Game of Life**: شبكة 2D (نظريًا لا نهائية)، كل خلية 8 جيران، حية/ميتة. قواعد الـ iteration الأربع (بالنص):
  1. حية بأقل من **2** جيران أحياء → تموت (وحدة).
  2. حية بأكتر من **3** جيران أحياء → تموت (زحمة).
  3. حية بـ **2 أو 3** جيران → تعيش.
  4. ميتة بـ **3 بالظبط** جيران أحياء → تحيا.
  - عند التشغيل: غالبًا نتايج فوضوية ونشاط ينفجر من الخلايا الأولى، وبعد iterations بتستقر غالبًا مع مجموعات بتتأرجح بين حالتين. (Tip: Golly open-source — golly.sourceforge.net، وWikipedia "Conway's Game of Life".)
- **Glider**: مجموعة **5 خلايا حية** بتكرر نفسها **خلية واحدة بعيد بعد 4 iterations** (شكلها مخلوق صغير بيتحرك). **Glider gun**: نمط ثابت بيطلع gliders جدد **كل 30 iteration**.
- ★★★ **الدرس**: في الأنظمة المعقدة، **أمتع سلوك على مقياس مجموعات الأجزاء مش الجزء الواحد**.
  - **Flocking** الطيور: القطيع بيتحرك كوحدة وليه شكل واتجاه وهدف. قواعد المحاكاة: الطير بيوازن بين **التحرك ناحية مركز المجموعة**، و**مطابقة سرعة واتجاه الجيران**، و**تجنب الاقتراب الزائد**.
- ★★★ **Pac-Man ghosts** (أفضل مثال في الألعاب):
  - اللاعبين افتكروا الأشباح بتتعاون وتنصب فخاخ، وهي **مش بتتعاون**. كل شبح آلة بسيطة.
  - اللعبة بتتبدل بين **scatter** (كل شبح يروح لزاوية مختلفة) و**chase** (أغلب الوقت، بيطاردوا).
  - في chase: القرار عند كل تقاطع، اختار اتجاه **يقرّب من اللاعب** ويتجاهل الحيطان.
  - اختلاف بسيط لكل شبح: **Blinky (أحمر)** ← مكان اللاعب الحالي. **Pinky (وردي)** ← **4 خانات قدام** اللاعب. **Inky (أزرق)** ← يجمع موقع اللاعب وBlinky. **Clyde (برتقالي)** ← يطارد لما بعيد، ويروح للزاوية السفلية الشمال لما يقرب.
  - الأثر الكلي ذكي: Blinky يتتبع، Pinky وInky يسبقوك، وClyde يضيف noise. **انطباع تعاون بينما هي مجرد استراتيجيات متكاملة (complementary strategies) من غير معرفة بمكان بعض**.
  - (مرجع Tip: gameinternals.com "Understanding Pac-Man ghost behavior").

### تصنيف Fromm للـ emergence ★★ (*Types and Forms of Emergence*, 2005)

1. **Nominal / Intentional**: مفيش feedback أو feedback بين عناصر على **نفس المستوى** فقط. أغلب الآلات المصنوعة. سلوك deterministic ومتوقع لكن **بدون مرونة/تكيف** (speed governor، thermostat).
2. **Weak emergence**: **top-down feedback** بين مستويات. Flocking: الطير بيتفاعل مع جيرانه (agent-to-agent) **وبيدرك القطيع كمجموعة (group-to-agent)**. نفس الكلام لأسراب السمك، وأي وحدة بتدرك محيطها وحالة المجموعة.
3. **Multiple emergence**: feedback متعدد يعبر مستويات التنظيم. مثال: **short-range positive + long-range negative**. **البورصة**: الأسهم بتطلع → ناس تشتري → تطلع أكتر (positive قصير المدى). والناس عارفة إنها هتوصل قمة وبتخطط تبيع → تنزل (negative طويل المدى). وبالعكس. **Game of Life** برضه: positive (قاعدة الولادة) + negative (قواعد الموت)، ومستويات تنظيم (الخلية ← gliders وglider guns).
4. **Strong emergence**: أمثلتها: **الحياة من النظام الجيني**، و**الثقافة من اللغة والكتابة**. فرق كبير بين المقاييس ومقاييس وسيطة، ونتيجة أعلى مستوى **ممكن تنفصل** عن الوكلاء على أدنى مستوى. مثال: شبكة خلايا Game of Life تتظبط بحيث تشتغل كـ **كمبيوتر** على مستوى أعلى (تبني منه أنظمة جديدة، حتى ألعاب)، والاعتماد السببي بين سلوك الكمبيوتر وGoL نفسه **ضئيل**.
- **Takeaway**: في الألعاب في مستويات emergence مختلفة، وأحيانًا في نفس الوقت. والخصائص البنيوية (**feedback loops** و**المقاييس المختلفة**) دورها حيوي.

### الخلاصة والتمارين

- التلات صفات البنيوية: **أجزاء نشطة ومترابطة، feedback loops، تفاعل على مقاييس مختلفة**. دول بداية إطار **Machinations**. الفصول الجاية: اقتصاد داخلي (Machinations ورؤية البنى)، وبعدها **Ch.10 "Integrating Level Design and Mechanics"** و**Ch.11 "Progression Mechanisms"** للتوسع للـ levels.
- **تمارين**: (1) غيّر بعض قواعد Wolfram من الـ 8 على ورق مربعات وابدأ بخلية واحدة وقارن. (2) اكتب قواعد شبيهة بـ GoL على **شبكة سداسية (6 جيران)** أو **مثلثية (3 جيران)**.

**لموسفولك:** ★★★ (1) **سلاسل الدمج (chain merges)** هي الـ long-range communication عندنا (دمجة تدفع/تفتح مكان لدمجة تانية بعيدة)، والنشاط = عدد الدمجات في الثانية. نقدر نقيسهم من البوت بدل التخمين (طول أطول chain، متوسط النشاط لكل ليفل). (2) **ملاحظة تحقق**: الجرة المزدحمة بتخلي الدمج أصعب فتزحم أكتر: هل ده positive feedback destructive (downward spiral) فعلًا عندنا؟ يتأكد بالبوت قبل ما نبني عليه قرارات. (3) **Pac-Man**: rival contests ممكن تتصمم بقواعد بسيطة متكاملة ومختلفة لكل rival (شخصية لكل واحد بقاعدة سطر واحد) بتبان ذكية، وده أرخص من AI معقد. (4) **Consistency over Realism**: قواعد الـ mossy shells / stones / rot لازم تكون متسقة (مثال الباب الخشب: لو حاجة بتكسر قشرة تقيلة، متفشلش في خفيفة) والاتساق أهم من الفيزيا الواقعية. (5) **Rocket jumping**: نسيب مساحة لتكتيكات اللاعبين اللي مش متصممة (ارتدادات الفيزيا) ونعتبرها فرصة مش bug، ونراقبها من الـ analytics.

---

## الفصل 4: Internal Economy — ص59–78 ★★★

### ليه الاقتصاد الداخلي مهم ★★

- الاقتصاد = نظام فيه موارد بتتنتج وتتستهلك وتتبادل بكميات قابلة للقياس. **في الألعاب بيشمل حاجات مش اقتصاد حقيقي**: health، experience، skill. أمثلة: **Doom** (أسلحة، ذخيرة، health، armor)، **Risk** (جيوش بتخاطر بيها)، **Mario Galaxy** (نجوم وpower-ups تدي حيوات إضافية). **كل genres تقريبًا** فيها اقتصاد.
- ★★ **ده شغل المصمم وحده**: الفيزيا مع المبرمجين، والـ level مع الكتّاب ومصممي الـ levels، لكن **الاقتصاد لازم تصممه لوحدك**. ده «جوهر حرفة المصمم»: تصنع mechanics لنظام ممتع وتحدّي.
- مرجع: Ernest Adams — *Fundamentals of Game Design*, Ch.10 "Core Mechanics". واستخدام الكلمة **واسع**: information economy، political economy، market economies، والمعنى المجرد = أي نظام فيه موارد من أي نوع تتنتج وتتبادل وتتستهلك.

### عناصر الاقتصاد الداخلي ★★★

- **Resources**: أي مفهوم **قابل للقياس رقميًا**: فلوس، طاقة، وقت، وحدات، items، power-ups، حتى **أعداء**. أي حاجة اللاعب بينتجها/يجمعها/يدمرها غالبًا resource. **مش كل resource تحت تحكم اللاعب** (الوقت بيختفي لوحده). السرعة resource لكنها غالبًا جزء من الـ physics engine. **مش resources**: منصات، حيطان، أي ميزات ثابتة.
  - **Tangible**: ليها خصائص فيزيائية في العالم، موجودة في مكان وبتتنقل (items في inventory، أشجار Warcraft، وحدات strategy).
  - **Intangible**: مش بتحتل مكان. الشجر لما يتحصد يتحول لـ **lumber** (مجرد رقم). المهم تبقى عندك الكمية عشان تبني. **Warcraft** مثال على التبديل بين tangible/intangible؛ كذلك medical kits (tangible) وhealth points (intangible) في الـ shooters.
  - **Abstract vs Concrete**: abstract = **محسوبة من حالة اللعبة ومش موجودة فعلًا** (strategic advantage في الشطرنج، ارتفاع الأفاتار)، واللعبة عادة مش بتقول للاعب عنها. بعض الـ resources الشكلها abstract هي concrete فعلًا: **XP** في الـ RPG (intangible لكن حقيقية بتتكسب وبتتصرف)، **happiness وreputation**.
  - **طريقة العمل** ★: ابدأ بتحديد الـ **main resources**، وبعدين صِف الـ mechanisms.
- **Entities**: بتخزن **كمية محددة** من resource (= variable بلغة البرمجة). مثال: entity اسمها «Timer» بتخزن الوقت المتبقي؛ في **Monopoly** كل لاعب entity للـ cash.
  - **Simple entity** = قيمة واحدة. **Compound entity** = مجموعة simple entities (وحدة strategy: health، damage، max speed…) وكل واحدة attribute.
- ★★★ **4 وظائف اقتصادية**:
  1. **Sources**: بتخلق resources من العدم (تلقائية بمعدل، أو بحدث، أو تتشغل/تتقفل). مثال: فلوس في sim games تتولد بفترات **متناسبة مع السكان**؛ **health regen** بمرور الوقت.
  2. **Drains**: عكس الـ source، بتشيل resources **نهائيًا** من اللعبة. مثال: الأكل بيتصرف بمعدل متناسب مع السكان؛ الذخيرة بتتصرف بالإطلاق.
  3. **Converters**: بتحول resource لنوع تاني. **Warcraft**: الشجر ← lumber بمعدل معين. ترقيات التقنية بتحسّن كفاءة الـ converters.
  4. **Traders**: بتنقل resource من entity لـ entity وتنقل resource تاني في الاتجاه المعاكس حسب قاعدة تبادل (شراء درع بـ **3 قطع ذهب**). **مش converter**: مفيش حاجة بتتخلق أو بتتدمر، بس تبادل.

### الشكل الاقتصادي (Economic Shapes) ★★★

- الرسوم البيانية في الواقع: **على المقياس الصغير فوضوية، وعلى الكبير بتظهر أنماط** (صاعد/نازل، فترات كويسة ووحشة). Fig 4.1: انهيار وول ستريت 1929 على Dow Jones (أكتوبر 1929 – أكتوبر 1930 تقريبًا، المحور 100–400)، حركة فوضوية والانهيار واضح.
- ★★ **مفيش شكل واحد = جودة gameplay**: الجودة حسب أهدافك وسياقك. مثال: لعبة طويلة فيها يكافح اللاعب كتير قبل ما يكسب (Fig 4.2) أو لعبة قصيرة بانقلابات سريعة (Fig 4.3).

### شكل لعبة الشطرنج ★★★

- الموارد: القطع. تقييم نقاط في نظام معين: **pawn = 1، rook = 5، queen = 9**. المجموع = **material**. **Strategic advantage** = resource abstract.
- **الأنماط**:
  - **اتجاه material لتحت** للاتنين: بتخسر وتضحي بقطع. **المكسب صعب جدًا**: الطريقة الوحيدة هي ترقية pawn (حدث نادر وبيبدأ تغيير درامي). فالشطرنج «معركة استنزاف» من ناحية material (اللي يخلّي material يعيش أطول غالبًا يكسب).
  - **Strategic advantage ديناميكي**: بيتكسب ويتخسر. اللاعب بيصرف material لكسب advantage أو لتقليله عند الخصم. علاقة **غير مباشرة**: material أكتر → أسهل تاخد advantage، والـ advantage → تاخد قطع الخصم → تقلل material. وأحيانًا تضحي بقطعة لكسب advantage أو تستدرج الخصم يخسره.
  - **التلات مراحل** تظهر في الرسم: **Opening** (تحركات محضرة، material ينقص ببطء والاتنين بيبنوا advantage)، **Middle game** (استغلال advantage لأخذ قطع → انحدار حاد في material)، **Endgame** (قطع قليلة، الملك آمن للمشاركة، material بيستقر والمحاولة الأخيرة لتحويل advantage لفوز). الحدود غير واضحة.
  - ملحوظة الكتاب: التحليل ده تجريد عالي لتوضيح مبدأ؛ الشطرنج عن كش الملك مش عن أخذ قطع، لكن بيوضح إن **أي لعبة نقدر نفهمها اقتصاديًا حتى لو مش عن الاقتصاد**.

### من الـ Mechanics للـ Shapes ★★★

1. **Negative feedback = equilibrium**: بيخلّي النظام مقاوم للتغيير (ثلاجة ثابتة الحرارة رغم برا). أبسط شكل = خط أفقي. ممكن equilibrium **يتغير تدريجيًا** أو **دوريًا** (Fig 4.6)، وده بيحتاج **عامل ديناميكي** مستقل عن الـ negative feedback (مثال: درجة الحرارة الخارجية على مدار السنة).
2. **Positive feedback = arms race (منحنى أسّي)**: الفايدة على حساب التوفير. في **StarCraft**: تصرف **50 mineral** على SCV (Space Construction Vehicle) يجمع minerals جديدة. لو رجّعت جزء ثابت من الدخل لبناء SCVs تاخد نفس منحنى الفايدة.
   - اللاعبين مش بيصرفوا على SCVs بس (وحدات عسكرية، توسع، تقنية). لكن **إمكانية النمو الاقتصادي للـ base حيوية**. كتير بيبنوا دفاعات ويحصدوا موارد كتير قبل الهجوم بقدرة إنتاج أعلى.
   - **Sidebar: Deadlocks and mutual dependencies** ★★: minerals ← SCVs ← minerals (اعتماد متبادل). لو معندكش minerals ولا SCVs → **deadlock** (مش هتقدر تبدأ إنتاج). كمان محتاج minerals كفاية وSCV واحد على الأقل لبناء **headquarters** (مورد تالت بيفعّل الـ loop). **تهديد حقيقي**: عدو يدمر كل SCVs وانت صرفت كل minerals على جيش. **وكمان أساس لـ level design**: تبدأ mission بوحدات عسكرية وبعض minerals **من غير SCVs وHQ**، فاللاعب لازم **يلاقي وينقذ** SCVs.
   - ★★ **استخدام مهم**: positive feedback **بيضخّم الفروق الصغيرة** (حسابين بنفس الفايدة وإيداع أولي مختلف: الفرق بس يزيد)، فبيدفع اللعبة لـ **conclusion** بعد ما فرق حاسم يتكون. «محدش بيحب يكمل لعب لما يتضح مين هيكسب».
3. **Positive feedback على آلية تدميرية = downward spiral**: خسارة قطع في الشطرنج تضعف موقفك وتزود احتمال خسارة قطع أكتر. ★ **مش نفس الـ negative feedback** (ده بيخمد ويعمل توازن). وممكن negative feedback على destructive mechanism: **Half-Life** بيطلّع health packs أكتر لما hit points قليلة.
4. **Long-term investments vs short-term gains** ★★★: لو StarCraft مجرد سباق جمع minerals: هل تبني SCV كل ما تجمع كفاية؟ **لأ**: لو صرفت كل الدخل على SCVs مش هتدّخر (وده اللي بتحتاجه). في لحظة لازم **توقف إنتاج SCVs وتبدأ تكدّس**.
   - الوقت الأمثل حسب **الهدف** (أكبر كومة في وقت محدود، أو رقم معين بأسرع وقت)، وحسب باقي اللاعبين. فيه عدد SCVs مثالي.
   - **Fig 4.8 "a race of accumulation"**: وانت بتستثمر minerals مش بتتراكم؛ أول ما توقف تزيد بخطوة ثابتة حسب عدد SCVs. **كل ما استثمرت أطول، تبدأ تتراكم أبعد، لكن في النهاية تلحق وتعدي اللي بدأ قبلك**. حسب الهدف، واحد من الخطوط هو الأكفأ.
   - **Balance**: لو صرفت كل minerals على SCVs هتتهاجم. لازم توازن الطويل مع الاحتياجات القصيرة (حماية الـ base). فيه **tank rush** (شهرته من **Command & Conquer: Red Alert**): بناء هجوم سريع قبل دفاعات الخصم. وفي خرايط الوصول الأولي للموارد محدود، فلازم تتحرك بسرعة تثبّت الوصول. الاستثمار في SCVs جيد على المدى الطويل لكن **بياخد مخاطرة في البداية** (التخلي عن مكاسب عسكرية سريعة).
   - **الباترن**: مفاضلة الاستثمار/الاستهلاك هي اللي بتخلّي الاقتصاد = استراتيجية.
5. **Sidebar: Variation from player performance and resource distribution** ★: مش بس عدد SCVs. الـ minerals في **crystal deposits** بمواقع محددة. إيجاد أحسن موقع للـ base، وإدارة SCVs يحصدوا بكفاءة (**micromanagement**) مهارة بحد ذاتها. = **مهارة اللاعب وتضاريس العالم** تعمل input variation. ★★ **القاعدة**: inputs اللاعب لازم تأثر الاقتصاد، لكن الأفضل **تحصل كتير ولا واحد منها يكون ضخم التأثير**.

### Feedback على الـ relative scores ★★★

- **Marc LeBlanc، GDC 1999** (نسختين من كرة السلة):
  - **Negative feedback basketball**: لكل **5 نقاط** الفريق المتقدم، الفريق المتأخر **يلعب بلاعب زيادة**.
  - **Positive feedback basketball**: العكس: المتقدم بيلاعب زيادة لكل 5 نقاط.
- **الفرق عن الـ feedback المبني على قيم مطلقة**: التأثير على **الفرق بين اللاعبين** مش على الموارد المطلقة، وده بينتج تأثيرات **غير بديهية**. في negative basketball: تقدم الفريق الأقوى **يستقر عند مسافة ثابتة** يعوّض فيها نقص مهارة المتأخر باللاعبين الزيادة (Fig 4.9).
- **Positive basketball**: بيضخّم فروق المهارة. فريق أقوى = مباراة **أحادية الجانب**. لكن لو الفريقين **متقاربين**: المباراة تفضل قريبة لحد ما فريق ياخد تقدم حاسم، وبعدها تبقى أحادية. **فرق مهارة صغير أو مجهود زيادة أو حظ ممكن يكون العامل الحاسم**. (التفاصيل Ch.6.)
- **Sidebar: Dynamic equilibrium** ★★: الـ equilibrium اللي بينتجه negative feedback مغذّى بفرق الموارد بين لاعبين **مش قيمة ثابتة** بل بيعتمد على عوامل متغيرة. **أغلب التطبيقات المثيرة للـ negative feedback ديناميكية** كده. لجعله ديناميكي (حسب الحظ النسبي أو عوامل أخرى) = **ابعد عن التوازن الثابت المتوقع**. بخبرة تركّب عوامل لـ equilibria دورية أو تقدمية أو أي شكل مطلوب.
- **Sidebar: Rubberbanding** ★★★ = negative feedback على الموقف النسبي في سباقات: **العربيات كأنها متربطة بشريط مطاط**، متبعدش ولا تتأخر قوي. تنفيذ:
  - بسيط: **إبطاء المتصدرين وتسريع المتأخرين**.
  - أدق (**Mario Kart**): power-up عشوائي، **المتأخرين فرصتهم أكبر لأقوى power-up**. وكمان أغلب أسلحة Mario Kart بتتستخدم على **اللي قدامك**، فـ **المتصدر هدف أكتر** من آخر واحد → **الصدارة بتتبدل** وحماس أكتر وفرصة لـ **last-minute surge**.
  - **الباترن**: التقارب الاصطناعي بيبقى بالعدل/الحظ مش بالغش الصريح.

### استخدامات الاقتصاد الداخلي حسب الـ genre ★★★

#### أ) يكمل الفيزيا (action games) ★★
- الفيزيا بتختبر البراعة والتوقيت والدقة؛ الاقتصاد بيضيف نظام مكافآت أو power-ups. **مجرد scoring system = اقتصاد**: كام هتستثمر في قتل عدو؟ (مخاطرة بالأفاتار؟ ذخيرة/طاقة مش بسهولة تتعوض؟).
- **Super Mario Bros**: coins → حيوات إضافية. لازم تجمع **كتير**، فالمصمم يحطها بسخاء ويضيف/يشيل منها خلال الـ playtest **من غير تأثير ملحوظ**. **تُستخدم لتوجيه اللاعب = breadcrumbs**. **افتراض آمن إن كل coin ممكن توصلها**، فمكافأة اللاعب المتمكن في أماكن صعبة. وفيه feedback loop: coins أكتر ← حيوات ← مخاطرة أكتر ← coins أكتر.
- ★★ **توازن المخاطرة والمكافأة**: **coin واحدة في فخ مميت = ظلم** (اللاعب هيحس إنه اتخدع). **مكافأة يشوفها اللاعب وما يوصلهاش أسوأ** (يخاطر على مكافأة مستحيلة). المصمم مسؤول عن مطابقة risk/reward خصوصًا **قريبًا من مسار المبتدئين**.
- **Power-ups والذخيرة في FPS**: ممكن مكافآت بذاتها. التوازن: مقبول أحيانًا إن قتل الأعداء يكلف رصاص أكتر مما يطلعه اللوت، **لكن لو اللاعب ينتهي بنقص ذخيرة قبل مواجهة الـ boss = بتعاقبه على إنه بذل مجهود**. في **survival FPS**: اقتصاد أسلحة شحيح = توتر ودراما (توازن صعب). في الـ action: **ذخيرة كتير وكافئ قتل الأعداء الزيادة**.

#### ب) يأثر على الـ progression ★★★
- power-ups وأسلحة فريدة تفتح أماكن (double-jump = منصات أعلى). اقتصاديًا: موارد جديدة بتنتج المورد abstract **access** (للمكافآت أو مطلوب للتقدم).
- ★★★ **خطر الـ deadlock** (مثال الكتاب): عدو خاص يحرس مخرج الـ level، وسلاح فريد في نفس الـ level مطلوب لقتله بطلقة واحدة، السلاح بيتحمل بـ **10 رصاصات** ومفيش تاني لحد الـ level الجاي، لكن اللاعب (أول مرة) مش عارف. يجرب شوية، يستعمله على أعداء تانيين، ويوصل المخرج بـ **رصاصة واحدة** ويخطئ. **deadlock**: محتاج رصاص عشان يعدّي، ومحتاج يعدّي عشان رصاص.
- ★★★ **Sidebar: Deadlock resolution in Zelda**: كتير من ألعاب Zelda لازم تستهلك items (**arrows أو bombs**) للوصول لمناطق جديدة. المصممين يمنعوا الـ no-win بـ **مصادر متجددة كفاية**: **الجرار (pots)** في الـ dungeons بتدي الموارد المطلوبة لما تكسرها، و**بتتجدد** لما تتنقل من غرفة لغرفة (source بيتعوّض من وقت لوقت). **الجرة ممكن تحتوي أي حاجة** فالمصمم يقدر يدي أي resource مطلوب. **وكمان وسيلة تلميح gameplay**: لو اللاعب بيلاقي arrows كتير، غالبًا هيحتاج bow قريب.

#### ج) يضيف gameplay استراتيجي ★★★
- كتير من التحديات الاستراتيجية في RTS **اقتصادية**: في StarCraft غالبًا بتقضي وقت في إدارة الاقتصاد أكتر من المعركة. الاقتصاد = بعد استراتيجي على مدى زمني أطول من الأكشن/التاكتيك.
- **ليه RTS اقتصادها معقد**: عشان تكافئ **التخطيط والاستثمار طويل المدى**. لعبة عسكرية من غير تخطيط واستثمار = لعبة **tactics** مش strategy. الاقتصاد الاستراتيجي = **موارد متعددة، feedback loops كتير، علاقات متداخلة**. تأسيسه صعب والتوازن أصعب: **تعديلات كتير على اقتصاد StarCraft حتى بعد النشر** بعد ما اللاعبين طوروا استراتيجيات جديدة.
- حتى من غير إنتاج، الاقتصاد يضيف عمق: الشطرنج = «أقصى استفادة من القطع» (material وstrategic advantage).
- ★★ **Prince of Persia: The Sands of Time**: خنجر سحري بيتحكم في الوقت: **rewind** لو حصل خطأ (حتى في القتال بعد ضربة كبيرة)، و**freeze time** مفيد ضد أعداء كتير. **الرمل محدود** (rewind مرات محدودة)، **وهزيمة الأعداء بتدي رمل جديد**. اللاعب لازم **يدير resource حيوي ويقرر إمتى يستثمره**. لاعبين مختلفين: بعضهم في القتال وبعضهم يحتفظ بيه للـ jumping puzzles. **versatile resource**: يعزز الأداء حيث ما يحتاج.

#### د) يخلق probability spaces كبيرة ★★★
- اقتصاد معقد = probability space بيكبر بسرعة = replay value وتجربة شخصية (أداء واختيارات اللاعب بتحدد أي أجزاء تنفتح). الاقتصاد للتطوير (character development، تقنية، نمو، ترقية مركبات) بيستخدم **عملة داخلية** لتدي خيارات: RPGs (فلوس للعتاد، XP للمهارات)، سباقات بتسمح بـ tune/upgrade بين السباقات أو أثناءها. **شرط**: خيارات كتير وبتمثل حلول **مختلفة فعلًا**.
- ★★★ **3 تحذيرات**:
  1. **توليفة أكفأ يكتشفها اللاعبون وينشروها (online RPG)** → الاقتصاد يختل: يختاروا الخيار ده بس (يقلل الـ probability space ويبقى ممل) أو يشتكوا من إنهم مش قادرين يلحقوا. **العلاج: negative feedback** على الـ customization. مثال: في الـ RPG كل ما ترتقي level تحتاج **XP أكتر** للـ level الجاي → تقلل الفروق وتطلب استثمار أكبر لكل level.
  2. **الـ probability space لازم يكون أكبر من إنك تستكشفه كله في session واحدة**. مثال: RPG فيه rating **1–5** لـ strength وdexterity وwisdom وتزود كل مرة، **غلط تتطلب ترقية الكل للأقصى لإنهاء اللعبة**. وكمان لو ترتيب الترقيات محدود، نتايج الاختيار تقل. ★★ **أفضل طريقة لخيارات ذات عواقب: خيارات متنافية (mutually exclusive)**: class واحد في RPG، وكل class مهارات فريدة. **Deus Ex**: تختار بين module يخلّي الشخصية **غير مرئية لفترات قصيرة** أو **subdermal armor** أمتن ضد الضرر.
  3. **صمم levels بحيث تنفع استراتيجيات مختلفة**. **Deus Ex**: combat أو stealth أو hacking. فأغلب levels بحلول متعددة. **صعب التوازن**: لو تقدّر إن اللاعب رقّى 3 خيارات قبل level معين، ممكن 3 مرات combat، أو 3 stealth، أو 3 hacking، أو كلهم مرة. وفي Deus Ex المشكلة أكبر لأن **مصادر XP غير متجددة** (بتكسبها بالتقدم وبعض side quests، ورجوع لمنطقة سابقة لحصد XP مش خيار). **الـ levels لازم تكون أكتر مرونة وعمومية** لأنك مش عارف قدرات الأفاتار. ★★★ **Deus Ex: Human Revolution flaw**: طرق لعب متعددة **لكن طريقة واحدة بس لهزيمة الـ bosses**، فبتهدم فايدة الـ customization.

#### هـ) نصايح ألعاب بناء الاقتصاد (SimCity، construction/management) ★★★
- المصمم يعمل **toolbox** من mechanics تتركب بطرق كتير. **أصعب من تصميم اقتصاد كامل وظيفي ومتوازن بنفسك**، لأنك لازم تدرك كل طرق تركيب اللبنات. لما ينجح، الاقتصاد اللي اللاعب بناه يعكس اختياراته (**مفيش مدينتين SimCity متشابهتين**).
- **3 استراتيجيات للتحكم في التعقيد**:
  1. **متقدّمش كل لبنات اللاعب مرة واحدة**: قدّمها شوية شوية. بتتحكم في الـ probability space في الأول، وبتصمم سيناريوهات وتحديات خاصة. لو مفيش levels واضحة، **متفتحش كل خيارات البناء من الأول**: خلّي اللاعب يجمع موارد قبل ما يفتح اللبنات المتقدمة. **Civilization** مثال ممتاز: أغلب اللبنات مقفولة في الأول وتتفتح واحدة واحدة.
  2. **انتبه للـ meta-economic structure**: في الاقتصاد المثالي طرق تركيب اللبنات لانهائية، لكن بعضها أفضل (وفي ألعاب بشرط فوز، بعضها غير قابل للكسب). في **SimCity** مزيج معين من zones صناعية وسكنية وتجارية فعّال جدًا، واللاعبين هيكتشفوه بسرعة. ★★★ **طريقة صعبة لكن فعالة لتجنب هيمنة نمط**: **الأنماط الفعالة بدري تبطل تكون فعالة بعدين**. مثال: layout للـ zones فعال للنمو السكاني الأول لكن يسبب **تلوث** على المدى الطويل. **آلية = slow-working destructive positive feedback**.
  3. **استخدم الخرايط لإنتاج التنوع وتقييد الـ possibility space**: SimCity وCivilization مش هتبقى ممتعة لو تبني على أرض مثالية. جزء من التحدي هو التعامل مع الحالة الأولية للبيئة. فلو فيه **dominant meta-economic structure**، الماب ممكن يمنع تنفيذه، فيضطر اللاعب يرتجل (يكافئ المرنين). كمان **SimCity disaster scenarios** (كوارث طبيعية) واختبار الارتجال، وSimCity بتولّد كوارث عشوائية بتأخّر تقدم اللاعب.

### الملخص والتمارين

- عناصر: resources، entities، sources/drains/converters/traders. Shapes من graphs. **Negative feedback = equilibrium، Positive = arms race، وعلى destructive = downward spiral**. Feedback مبني على علاقات بين لاعبين يخلي اللعبة قريبة أو يخلي المتقدم يفضل متقدم.
- **تمارين**: (1) حدد resources والوظائف الاقتصادية في لعبة منشورة. (2) لعبة (غير اللي في الفصل) فيها: negative feedback بـ periodic equilibrium، أو downward spiral، أو short vs long-term trade-off، أو feedback على relative scores، أو rubberbanding، واشرح الـ resources والـ mechanics. (3) لعبة (غير Zelda) فيها deadlock محتمل، وهل بتكسره؟

**لموسفولك:** ★★★ (1) **ارسم اقتصاد Mossfolk بالـ 4 وظائف**: الـ **merge = converter** (2 من حجم n ← 1 من n+1)، **drop budget = drain**، التسجيل/الأهداف = resources مقاسة. حدد الـ sources الفعلية (مكافأة نهاية ليفل؟ إعلان rewarded؟) ولو مفيش source للـ budget داخل الليفل يبقى الـ drain الوحيد. (2) **Deadlock عندنا**: budget = 0 والجرة مليانة مخلوقات مش هتندمج = deadlock (زي رصاصة Zelda الأخيرة). **البوت يقيس** نسبته في كل ليفل، وأي dead state بدري = تصميم خطأ (مش غلطة لاعب). (3) **Zelda pots**: لو فيه resource بيخلص (إسقاطات إضافية؟ booster؟)، لازم مصدر متجدد أو fallback قبل الـ deadlock. وكمان تلميح gameplay: ما نغذّي اللاعب بنوع مخلوق عشان يلمّح للي جاي. (4) ★★★ **rot = نموذج الكتاب بالظبط لـ slow-working destructive positive feedback**: وده المفروض يقتل «dominant meta-economic structure» (مثل أحسن طريقة تكديس ثابتة) لما يصير dominant. نراجع: الاستراتيجية الأكفأ بدري في ليفلات 2501+ بتبطل تشتغل بعدين؟ ولو لأ، نضيف. (5) **Don't introduce all building blocks**: mossy shells وstones وrot اتقدموا واحد واحد بتدرج (Civilization-style)، ولا مرة واحدة؟ (6) **Super Mario coins**: أي مكافآت (نجوم/عملات) داخل الليفل = breadcrumbs وخطر/مكافأة: مكافأة صغيرة في مكان خطر = ظلم، ومكافأة مرئية ومستحيلة أسوأ. (7) **Prince of Persia sand**: مورد مكتسب بالأداء ومستخدم عند الحاجة (undo/تجميد الجرة؟)، وده أفضل قالب لـ booster مربوط بالمكافأة (حتى rewarded ad) من الـ booster المدفوع الصرف. (8) **Rubberbanding** للـ rival contests: negative feedback على الموقف النسبي (مثل Mario Kart: المتأخر فرصة أكبر لقطعة قوية، والمتصدر هدف أكتر)، ولازم يكون **ديناميكي** (متعلق بفرق النتيجة) مش ثابت. و**ما نستخدمش positive feedback** في contest قصير إلا لو عايزين نهاية سريعة بعد فرق حاسم. (9) **Deus Ex HR flaw**: لو الـ levels فيها حلول متعددة لكن الـ boss/المحتوى الذروي بحل واحد، فبننسف الحرية. نراجع الليفلات الذروية/المنافسين. (10) **Probability space**: مش نطلب من اللاعب يستخدم كل الأدوات/الخيارات عشان يخلص، وخيارات متنافية للعواقب الحقيقية. (11) **Sidebar variation**: مهارة اللاعب في كل drop لازم تأثر لكن مفيش drop واحد يكون ضخم التأثير.

---

## الفصل 5: Machinations (البداية — ص79–84) ★★★

### الإطار والفكرة

- **Machinations** (Joris Dormans) = visual language/framework لـ **إنشاء وتوثيق ومحاكاة واختبار** الاقتصاد الداخلي. **Syntax واضح** = توثيق وتواصل بشكل ثابت. هنستخدمه كل الكتاب. ★ تحذير: إطار كبير ومفاهيمه متداخلة ومفيش نقطة بداية طبيعية، فمتستغربش لو رجعت لمفاهيم سابقة.
- **أداة أونلاين**: jorisdormans.nl/machinations (رسم + محاكاة real-time). **Appendix C** (peachpit.com/gamemechanics) فيه tutorial للأداة، و**Appendix A** مرجع سريع (الكتاب نفسه بيذكر Appendix A كمان كـ tutorial في ملحوظة تانية، فيه تضارب في النص).
- **ليه موجود؟** الـ mechanics مخفية في الكود. النماذج الموجودة (**كود، finite state diagrams، Petri nets**) معقدة وغير مناسبة للمصممين، وعلى مستوى تجريد غير مناسب لإظهار **feedback loops** بوضوح. Machinations = **سهل الوصول مع الحفاظ على الخصائص البنيوية والسلوك الديناميكي**.
- ★★★ **الرؤية النظرية**: الـ gameplay بيتحدد في النهاية بـ **تدفق الموارد (tangible, intangible, abstract)** عبر نظام ا

