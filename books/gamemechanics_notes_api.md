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

# Game Mechanics: Advanced Game Design (Adams & Dormans) — الجزء 3 من 8 — نوتس مذاكرة

**النطاق:** تكملة الفصل 5 «Machinations» (من Random flow rates لحد الـ Exercises، كتاب ص 84–106) + الفصل 6 «Common Mechanisms» كامل (ص 107–145).
**ملحوظة تقنية:** الاستخراج فقد كل الأشكال (Figures) وجدولين: Table 6.1 (الخصائص السبعة) وTable 6.2 (رموز الـ determinability). اعتمدت على النص المحيط وملخص الفصل لتغطيتهم. تمارين الفصل 5 (4 مجموعات) رسوماتها ضاعت، فاتسجلت كوصف بس.
**قاعدة الاستثناء:** الكتاب ده مش برمجة، فنصايح الـ Machinations Tool اتسجلت باختصار لأنها بتخدم تصميم الـ simulation عندنا.

---

# الفصل 5 (تكملة): Machinations

## 5.1 نصايح الـ Tool اللي اتقالت قبل Activation Modes ★

- **Quick run mode**: تحت تاب run في الـ side panel. بيشغّل الدياجرام أسرع من غير ما تتفرج على الموارد وهي ماشية في الـ connections.
- الـ pool نوع واحد بس من 8 أنواع nodes. الـ 7 التانيين متخصصين وبيتشرحوا في «Advanced Node Types».
- **Fixed flow rate**: اختار الـ resource connection واكتب رقم أو كلمة `all` في الـ Label box.

## 5.2 Activation Modes ★★★ — إمتى الـ node يطلق

الـ node بيعمل fire (بيدفع أو بيسحب موارد) حسب الـ activation mode. في 4 أنماط:

1. **Automatic**: بيطلق كل iteration. كل الـ automatic nodes بتطلق **في نفس الوقت**. علامته `*`.
2. **Interactive**: بيمثل **player action** وبيطلق بعد ما اللاعب يدوس عليه. علامته double outline.
3. **Starting action**: بيطلق مرة واحدة بس **قبل أول iteration** (في الـ Tool: فورًا بعد الضغط على run). علامته `s`.
4. **Passive**: مبيطلقش إلا ردًا على **trigger** من عنصر تاني. من غير علامة.

**الباترن ورا التاكتيك:** الأنماط الأربعة هي تصنيف «مين بيحرك الحدث»: النظام (automatic) / اللاعب (interactive) / الإعداد (starting) / نظام تاني (passive). أي ميكانيكا في أي لعبة تتحط في واحدة من الأربعة.

## 5.3 Pulling & Pushing ★★

- الـ pool لما يطلق **بيسحب** (pull) عن طريق الـ inputs. العدد = flow rate للـ resource connection (الرقم جنب الخط).
- **Push mode**: بيدفع على الـ outputs بدل ما يسحب. علامته `p`. الـ pool اللي له outputs بس دايمًا push، فالـ `p` بتتشال.
- **لو الموارد أقل من المطلوب:**
  - **الافتراضي**: بيسحب اللي موجود لحد حد الـ flow rate.
  - **All-or-none mode**: لو مش كله متاح، مفيش حاجة بتتسحب. علامته `&`. ينطبق على الـ push كمان، فممكن node يبقى `p` و`&` مع بعض.
- **مثال Fig 5.8:** node A (interactive) عايز 3 من الـ input اللي فوق و2 من اللي تحت والـ pools مش كفاية، فبيسحب المتاح بس. node B بيحاول يسحب رقم عشوائي 1–6، ولو الرقم 4 أو 5 أو 6 بيسحب الـ 3 الموجودين.

**الباترن:** الـ `&` هو نمط «ادفع التمن كامل أو مفيش صفقة». مناسب للـ costs، والافتراضي مناسب لـ harvesting.

## 5.4 مثال الـ Hourglass ★

pool A (passive، فيه 5) وpool B (automatic، فاضي) متوصلين بـ connection واحد. كل iteration بيسحب B واحد من A لحد ما الخمسة ينتقلوا، وبعدها الدياجرام يثبت ومفيش تغيير.

**الباترن:** أبسط نظام بـ timer: automatic puller + مخزن محدود = عدّاد تنازلي.

## 5.5 Time Modes ★★★ — الوقت في الـ simulation

| Mode | القاعدة |
|---|---|
| **Synchronous** | كل الـ automatic بتطلق على interval منتظم (للنظام كله). الـ interactive اللي اتداس عليها بتطلق في الـ step الجاي مع الـ automatic. كل الأفعال في الـ step متزامنة. اللاعب ينشّط أكتر من interactive node في الـ step، **بس كل واحدة مرة واحدة بس**. |
| **Asynchronous** (الافتراضي في الـ Tool) | الـ automatic على intervals بطول اختياري. اللاعب ينشّط الـ interactive **في أي وقت** والتنفيذ فوري. الـ interactive ممكن تتنشط **أكتر من مرة** في الـ step. |
| **Turn-based** | الـ steps مش على intervals منتظمة. الـ step الجديد بييجي بعد ما اللاعب ينفذ عدد محدد من الأفعال. كل interactive node ليها **action points**، واللاعب معاه **ميزانية ثابتة كل turn**. لما تخلص تطلق الـ automatic nodes وتبدأ turn جديدة. |

**نصايح الـ Tool:**
- الـ Time mode من pull-down في الـ side panel (لما مفيش عنصر متحدد).
- الـ interval بالثواني، وبيقبل كسور (2.5 = كل step 2.5 ثانية).
- في turn-based بيظهر Actions/Turn بدل الـ interval. تكلفة كل interactive node بالـ action points (ممكن صفر).
- ★ **حيلة «End Turn»**: خلي كل الـ interactive nodes تكلفتها صفر ما عدا node واحدة اسمها "end turn" بلا تأثير تاني. كده اللاعب يعمل أي عدد أفعال لحد ما يقول خلصت.

## 5.6 Resolving Pulling Conflicts ★★

مشكلة: pools اتنين بيسحبوا من نفس المصدر في نفس الوقت ومفيش كفاية.

**مثال Fig 5.10:** A فيه 9. كل step بيسحب B واحد من A، وC وD كل واحد بيحاول يسحب واحد من B.
- **Synchronous:** في الـ step الأول B معاه واحد، فمفيش C ولا D بيسحب. بعد step تاني B معاه اتنين، فالاتنين يسحبوا واحد واحد. بيتكرر كل step اتنين **في نفس الوقت**. بعد 9 steps: C وD معاهم 4 كل واحد، والواحد الباقي على B، والحالة تثبت.
- **Asynchronous أو turn-based:** واحد بس منهم بياخد. الأولوية **عشوائية في الأول** وبعدين **بتتبادل كل step**. النتيجة النهائية: 4 على واحد و5 على التاني.

**الباترن:** الـ time mode بيحدد فلسفة العدالة. في الـ sync الطلب المتعارض بيفشل للكل (ندرة = لا أحد يكسب)، وفي الـ async/turn بيتحل بأولوية متبادلة. ده نفس الفرق بين لعبة simultaneous وturn-based.

## 5.7 State Changes ★★★ — الـ State Connections

- **State** = توزيع الموارد الحالي على الـ nodes.
- **State connections** = أسهم **منقطة** من الـ **origin** (الـ node المتحكم) لـ **target** (node، أو resource connection، أو نادرًا state connection تانية). الـ label بيحدد التأثير.
- 4 أنواع: label modifiers / node modifiers / triggers / activators.

### Label Modifiers ★★★
- بيعدلوا **الـ label** بتاع resource connection (يعني الـ flow rate).
- المعادلة: **Lt+1 = Lt + M × ΔS** (التأثير في الـ step الجاي). لأكتر من modifier: **Lt+1 = Lt + Σ(M×ΔS)**.
- الـ label بيبدأ دايمًا بـ + أو −.
- **مثال:** modifier +3 والـ origin زاد 2 يبقى الـ target +6. لو الـ origin نقص 2 يبقى −6.
- **Fig 5.11:** كل resource بيضاف لـ pool A بيزوّد 2 على الـ flow بين B وC (الـ flow = 3 + 2×عدد A). أول تفعيل: 1 لـ A و3 لـ C. التاني: 1 لـ A و5 لـ C.
- **Tip لتجنب اللخبطة:** label موجب = الـ target **يتبع** الـ origin (يطلع لما يطلع، ينزل لما ينزل). label سالب = **يعكسه**. لو الـ origin بينزل والـ modifier موجب، الـ target هينزل.
- **مثال Monopoly (Fig 5.12):** كل ما property اللاعب زادت، زاد الاحتمال إن فلوس اللاعبين التانيين تيجي له. القيمة الدقيقة مش محددة (مش للتشغيل)، وأخد الـ property نفسه مش موجود في الرسمة (مفصّل في ف6 وف8).
- ملحوظة: ده أول استخدام للون، وهنا للوضوح بس.

### Node Modifiers ★★
- بيوصلوا node بـ node. تغير الـ origin بيعدل **عدد الموارد** في الـ target في الـ step الجاي: **Nt+1 = Nt + Σ(M×ΔS)**.
- ★ **Shortages:** المعدلات السالبة أو إعادة التوزيع ممكن تخلي العدد **سالب = shortage**. مفيش سحب من node فيه shortage، والموارد الداخلة تعوّض العجز الأول.
- ⚠ **تحذير:** الـ node modifiers بتخلق وتدمر موارد لو الـ target pool. ده كويس لمورد **مجرد** زي "threat level"، لكن **تجنبه** مع الموارد الملموسة أو غير الملموسة زي "keys" أو "health". استخدم sources/drains للتوليد والتدمير.
- **Fig 5.13:** C = 3×A − 2×B.
- **Fractions** (+1/3، −2/4): البسط يتطبق كل ما الـ origin يتغير بمقدار **المقام** (بالقسمة والتقريب لتحت). لما الـ origin يروح من 7 لـ 8: الـ modifier −2/4 ينقص الـ target بـ 2، والـ +1/3 مفيش تغيير.
- ★ **مثال The Settlers of Catan:** نقطة لكل village ونقطتين لكل city. node الـ villages ونode الـ cities origins، والـ target هو points اللاعب.

### Triggers ★★★
- state connection بـ label `*`. **مبتغيرش أرقام**، بتطلق الـ target.
- الـ trigger بيطلق لما **كل inputs الـ origin تتحقق** (كل input جاب الكمية بتاعته حسب الـ flow rate). لو الـ target resource connection بيسحب حسب الـ flow rate بتاعه.
- الـ node اللي من غير inputs بيطلق triggers كل ما يطلق (automatic، أو بفعل لاعب، أو بتريجر).
- **Tip:** الـ triggers غالبًا بتطلق **passive nodes**. يعني تعمل node ما بيعملش حاجة إلا لما تحصل ظروف معينة.
- **مثال Monopoly (Fig 5.14):** دفع فلوس للبنك بيطلق نقل property من البنك للاعب.

### Activators ★★★
- بيوصلوا nodes اتنين. **بينشّطوا أو يكبتوا** الـ target حسب حالة الـ origin وشرط.
- الشرط في الـ label: تعبير حسابي (`==0`, `<3`, `>=4`, `!=2`) أو range (`3-6`).
- متحقق = الـ target **activated** (ينفع يطلق). غير متحقق = **inhibited** (ميطلقش).
- **مثال Caylus (Fig 5.15):** اللاعب بيحط laborers في مبنى (مثلًا gold mine) عشان يعمل الأكشن بتاعه. ومع كل تعدين بيرجع العامل لـ pool الـ Workers عن طريق trigger.

**الباترن عبر النوعين:** modifiers = «الكمية تأثر في الكمية»، triggers = «الحدث يطلق حدث»، activators = «الحالة تفتح أو تقفل فعل». ده كل أنواع الارتباط في أي نظام لعبة (resource → rate، resource → resource، event → event، state → permission).

## 5.8 Advanced Node Types ★★★

**ليه موجودين:** Dormans عملهم عشان الدياجرامات تتقري بسهولة. بعضهم ممكن يتبني من pools وconnections بس، لكن الدياجرام هتتزحم.

### Gates ★★★
- شكل **معين (diamond)**. **مبيجمعش موارد، بيوزعها فورًا**. مفيهوش flow rate، كل output عليه **probability** أو **condition**.
- **Probable outputs** و**conditional outputs**، ولازم كل outputs الـ gate يبقوا من نوع واحد.
- **الاحتمالات:**
  - نسب مئوية (20%): مجموعها **ميزيدش عن 100%**. لو أقل فيه احتمال إن المورد **يتدمر** (مبيروحش لأي output).
  - **أوزان** (1 أو 3): الاحتمال = وزن الـ output ÷ مجموع الأوزان. مثال وزن 1 ووزن 3: 1/4 و3/4.
  - استخدامها: **chances and risks**. مثال Risk: اللاعب بيعرّض armies للخطر عشان يكسب territories = gate بـ probable outputs للنجاح والفشل.
- **Conditional outputs** (`>3`, `==0`, `3-5`): كل الشروط بتتفحص لكل مورد داخل، ومورد واحد بيتبعت على **كل output شرطه اتحقق**. الشروط ممكن تتداخل فتحصل **duplication**، ولو مفيش شرط اتحقق المورد بيتدمر.
- **4 activation modes** زي الـ pools. الـ gate من غير inputs بيطلق trigger كل ما يطلق، فتقدر تعمل triggers automatic أو بفعل لاعب.
- **Distribution modes:**
  - **Deterministic** (diamond مفتوح صغير): بيوزع بالتساوي حسب النسب أو الأوزان. مع conditional outputs بيعد الموارد اللي عدّت في الـ step ويفحص الشروط على العدد ده، ففكر فيه كـ **counting gate**.
  - **Random** (علامة نرد): بيولد قيمة عشوائية. مع probable: قيمة 0–100% أو رقم تحت مجموع الأوزان. مع conditional: **1–6 زي نرد عادي** (ممكن يتغير بعدين).
- **Tip:** نوع الـ gate من أيقونات Type في الـ side panel (المفتوح = deterministic الافتراضي، النرد = random).
- **Gate بـ output واحد** (الصف الأوسط في Fig 5.16، من الشمال لليمين): بيعدّي 30% عشوائيًا / بيمرر المورد فورًا بغض النظر عن الـ flow rate / بيعدّي أول موردين بس.
- **كل output state connection من gate = trigger.** الـ modifiers والـ activators من gate **ملهاش لازمة** لأنه مبيخزنش. والـ triggers دي ممكن تكون conditional أو probabilistic.
- **Fig 5.17:** gate عشوائي automatic بين pool A وB (passive): فيه 30% احتمال إن 3 موارد يتحركوا كل step.

### Sources ★★
- مثلث لفوق، **بيخلق موارد**. ممكن automatic (الافتراضي) أو interactive أو passive أو starting. معدل الإنتاج = flow rate للـ outputs.
- **أمثلة:** تجدد shields المقاتلة في **Star Wars: X-Wing Alliance** = automatic source. بناء armies في **Risk** = interactive source. المرور على **Go** في Monopoly = passive source بيطلق بحدث لعبة.
- الـ source = pool من غير inputs بمخزون كبير جدًا أو لانهائي. لـ **limited sources** استخدم pool بعدد محدد (من الفصل 4: Four Economic Functions).

### Drains ★★
- مثلث لتحت. المورد اللي يدخله **بيختفي للأبد**. المعدل من الـ input flow rate. ممكن مستقر أو عشوائي أو بفترات.
- الـ label `all` بيخليه يستهلك كل اللي في الـ input (مثال: **السيفون** بيفرّغ الخزان كله).
- ممكن تمثله بـ pool من غير outputs، لكن الـ drain بيوضح إن الموارد دي «خلصت ملهاش تأثير تاني».
- **الاستخدام:** إزالة موارد من الاقتصاد نهائيًا: التآكل والاحتكاك في نظام فيزيائي، واستهلاك الذخيرة في shooter.

### Converters ★★
- مثلث لليمين بخط رأسي. بيحوّل مورد لمورد تاني: مطحنة (قمح → دقيق)، مصنع (خام → منتج).
- **converter = drain بيطلق source**: بيستهلك مورد وينتج التاني. أنواع المعدلات نفس الـ sources/drains. مثال: sawmill بيحول شجرة لـ 50 لوح خشب.
- **Limited converter** = drain + limited source (Fig 5.21: طريقتين متكافئتين).

### Traders ★★
- خط رأسي فوق مثلثين (يمين وشمال). بيخلي الموارد **تغير مالكها** عند الإطلاق، يعني **تبادل مش تحويل**.
- استخدمه لما عدد من نوع يتبادل بعدد من نوع تاني: **التسوق** (التاجر ياخد فلوس، الزبون ياخد بضاعة بنسبة = السعر). لو أي طرف مش معاه الموارد المطلوبة، الصفقة **متحصلش**.
- **Fallout 3:** كل تجارها بمخزون محدود.
- ممكن يتبني من gates اتنين موصلين بـ trigger: لما مورد يوصل التاني يرجع بدله.
- ★★ **Converter vs Trader (Sidebar):** من منظور اللاعب شبه بعض (تدي حاجة وتاخد حاجة). من منظور المصمم مختلفين تمامًا:
  - **Converter** (drain + source): الموارد فعليًا تستهلك وتنتج، فإجمالي الموارد في اللعبة **ممكن يتغير**.
  - **Trader:** تبادل بس، **إجمالي الموارد ثابت دايمًا**.
- Fig 5.22 (color-coded): الأحمر فلوس والأزرق بضاعة، ولما تدوس على الـ trader 3 فلوس تتبادل بـ 2 بضاعة.

### End Conditions ★★
- مربع بمربع أصغر مليان جواه (رمز الـ stop). الـ Tool بيفحصهم كل step وبيقف **فورًا** لما أي شرط يتحقق.
- لازم يتفعل بـ **activator** بيحدد حالة النهاية.
- **Fig 5.23:** الشمال بيقف بعد ما 25 مورد يتفرغوا automatic. اليمين: **بتكسب** لما تزرع أكتر من 3 تفاح وبرتقال.

## 5.9 Modeling Pac-Man ★★★ — دراسة حالة كاملة

**تحذير المؤلفين:** النموذج **تقريب** مش محاكاة حرفية. مثلًا الأشباح بتطلع كل 5 steps بانتظام، واللعبة الحقيقية بخوارزمية أعقد. الهدف تعليم الـ framework. ومثال آخر عن التبسيط: الدياجرام مش بيمثل شكل المتاهة (Machinations مبتقدرش)، بيمثل تدفق الموارد وحالات اللعبة بس.

**الموارد (7):**
1. **Dots:** منتشرة في المتاهة، ملموسة، لازم تتدمر كلها عشان تكسب. عدد ثابت ومبيتنتجوش أثناء اللعب (إلا مع الليفل الجاي). اللعبة الحقيقية **240 dot** كل ليفل، والنموذج **50** عشان يقصر.
2. **Power Pills:** 4 في كل ليفل، تخليك تاكل الأشباح. **نادرة** وملموسة، تتستهلك بس ومبتتنتجش.
3. **Fruits:** بتظهر أحيانًا، تاكلها لنقاط زيادة.
4. **Ghosts:** 4 بيطاردوك. مكانهم: **ghost house** أو المتاهة. ★ مورد ملموس. وملحوظة: **الموارد مش دايمًا حاجة إيجابية للاعب**.
5. **Lives:** 3، غير ملموسة. لو خلصوا تنتهي اللعبة.
6. **Threat:** مورد **مجرد اخترعوه** عشان يحاكي أثر المطاردة. لما يعدي حد معين يتمسك باك-مان ويخسر life. قرارات نمذجته **ذاتية** مش من اللعبة الأصلية.
7. **Points:** من أكل dot أو fruit أو ghost. هدف اللعبة أكبر عدد نقاط. غير ملموسة.

**الميكانيكات (واحدة واحدة):**

- **Dots (Fig 5.24):** pool بـ 50 dot + pool نقاط فاضي + converter للأكل (interactive) + end condition (كل الـ dots اتاكلوا = خلصت الليفل). ★ الـ input للـ converter **random flow rate**: احتمال نجاح الأكل يبدأ **100%** وينقص **1%** لكل dot اتاكل (state connection +1% × ΔS = −1%). **المعنى:** بتتحرك في المتاهة وتاكل كل dot واحدة، وكل ما قلت الـ dots بقى أصعب تلاقي اللي لسه ما اتاكلش. في اللعبة الحقيقية 100% لحد ما ترجع مكان زرته وبعدها 0%، فده تقريب. لو الرقم 0.25% بدل 1% يبقى لاعب ماهر مبيضيعش وقت في أماكن زارها.
  - ★ **درس:** عملية التقريب دي أصعب جزء في النمذجة، ولازم تفكر في معنى كل قرار. **أسهل تنمذج لعبة جديدة من لعبة موجودة**، لأنك تعمل أي حاجة وتجرب وتعدل.
- **Fruit (Fig 5.25):** source معدله 1/20 (فاكهة كل 20 iterations) + drain معدله 1/5 (تختفي بعد 5 لو متاكلتش). Eat Fruit بـ **50%** نجاح (تقريب صعوبة اصطيادها)، لكن بـ **5 نقاط** بدل 1. في الأصل بتظهر مرتين بس في الليفل ونقاطها تتصاعد، فاتبسطت وزادت تكرارها عشان تتشاف.
- **Ghosts Produce Threat (Fig 5.26):** pool المتاهة بيسحب شبح كل 5 iterations. كل شبح في المتاهة بيزود إنتاج الـ threat من automatic source (مورد أسود). اللاعب يقلل الـ threat بـ **Evade** (interactive random gate): **50%** احتمال يطلق drain يشيل **9** threat. لو فشل مفيش حاجة وممكن يحاول تاني. لاعب أمهر = نسبة أعلى.
- **Capture & Loss of Life (Fig 5.27):** لما الـ Threat **>100** (activator أوتوماتيك) يتمسك ويخسر life. يطلق **Reset gate** في 3 اتجاهات: drain life، ورجوع الأشباح للبيت، وتفريغ كل الـ threat. لو آخر life تنتهي اللعبة. الـ 100 اعتباطي.
- **Power Pills (Fig 5.28):** مخزون محدود. **Eat Power Pill** converter يحول pill لـ **power-up time** (مورد مجرد بيتصرّف automatic). طول ما فيه power-up time: الأشباح **توقف إنتاج threat**، ويتفعّل drain على الـ threat، وبيبقى متاح فعل جديد **Eat Ghost** (يرجع شبح للبيت + 5 نقاط). المدة والنقاط في الأصل تتغير بالليفل فاتبسطوا.

**الاستنتاجات التصميمية من الدياجرام المبسط ★★★:**
- لاعب Pac-Man لازم **يوازن بين مهام**: أكل dots، وتفادي الأشباح، وأكل الفاكهة.
- ★ الفاكهة **معزولة** عن باقي اللعبة: تدي نقاط بونص ومبتساعدش في حاجة تانية، فالمبتدئ الغرقان في الأكل والتفادي **يقدر يتجاهلها بأمان**.
- الـ power pills مورد لازم **يتصرف بحكمة**.
- في استراتيجيات ظاهرة من التشغيل: تاكل الأشباح للبونص، **أو** تستخدم الـ pill عشان تروح للـ dots الأخيرة بأمان وتخلص أسرع.

**الباترن:** اللعبة كلها = اقتصاد موارد (dots = هدف، pills = مورد نادر، threat = ضغط، lives = ميزانية أخطاء)، والمتعة جاية من الموازنة بين مهام متنافسة مع مهمة جانبية آمنة للمبتدئ (الفاكهة) وقرار استراتيجي حقيقي (استخدام الـ pill).

## 5.10 Summary + Exercises
- الملخص: الـ pool يخزن، والـ resource connections بتحكم أين ومتى وكام، والـ state connections (منقطة) تغير سلوك الـ connections وعدد العناصر وتطلق أو تكبت الأحداث. الـ sources تخلق، والـ drains تدمر، والـ converters تحول، والـ gates توزع وتنتج triggers. نمذجة Pac-Man أثبتت إنها تنفع حتى **لألعاب الأكشن**.
- **Exercises (رسوماتها ضاعت):** 1) 8 دياجرامات: كام مورد في pool A بعد كليك واحدة. 2) و3) 6 دياجرامات في كل واحد: أقل عدد كليكات لنقل كل الموارد لـ A. 4) 6 دياجرامات: أقل كليكات للفوز (بعضها فيها أكتر من interactive element).

### **لموسفولك (الفصل 5):** ★★★
1. **نموذج Machinations لـ Mossfolk بيتعمل بنفس خطوات Pac-Man:**
   - **ميزانية الإسقاطات** = pool محدود (مش source) فيه عدد الـ drops. وكل drop = **interactive node**. وهي بالظبط **action points** في turn-based mode.
   - **الدمج** = **converter** 2:1 (اتنين نفس الحجم → واحد أكبر). والإجمالي بيتغير فعلًا (مش trader).
   - **الـ chain merges** = **triggers** (دمج بيطلق دمج).
   - **ملء البرطمان** = مورد مجرد زي threat، مع **end condition** للخسارة عن طريق activator (>حد).
   - **توزيع المخلوق الجاي** = **random gate بـ weights** (مش نسب).
   - **الهدف** = end condition للفوز.
   - **«الميزانية خلصت والهدف لسه»** = **reverse trigger** على الـ end condition.
2. **الـ mossy shells والـ rot (من 2501):** ممكن تتنمذج كـ **activators** (قفل لحد شرط دمج معين) أو **threat** بيتولد automatic. وتتصنف بالخصائص السبعة: rot = positive destructive (spiral).
3. **درس الـ Pac-Man للتيستر-بوت:** النمذجة **التقريبية** مقبولة طالما بتحفظ البنية، واحنا لازم نكتب كل تقريب (زي الـ 0.25% vs 1%) كـ **افتراض مسمّى**. ولو البوت بيعمل نفس دور اللاعب «الماهر مقابل المبتدئ» نغير نسبه زي ما غيروا نسبة الأكل.
4. **الفاكهة المعزولة = side quests:** مهمة جانبية آمنة بنقاط إضافية من غير ما تخلي المبتدئ يغرق. فنفحص الـ side quests: هل هي معزولة فعلًا ولا بتضغط على الـ core؟
5. **حيلة End Turn:** لو عملنا مود فيه «اسقط أي عدد قبل ما تضغط خلصت» تتنمذج بتكلفة 0 + node نهاية.
6. **Converter vs Trader:** أي تبادل في متجر الـ in-app (عملات ↔ boosters) هو **trader** (إجمالي ثابت)، لكن الـ merge **converter**، فاحسب الاقتصاد الكلي بعد الفرق ده.

---

# الفصل 6: Common Mechanisms

**المقدمة:** الفصل بيقدم ميزات متقدمة في Machinations، وبيشرح قراءة **feedback structures** من الدياجرام (**7 خصائص**)، وبيتكلم عن استخدام **randomness** لإضافة عدم توقع، وبيختم بنماذج لأنواع ألعاب. الهدف: الدياجرامات (الثابتة والرقمية) أداة أساسية لفهم **النظام الديناميكي** اللي بيحرك الـ gameplay.

## 6.1 More Machinations Concepts

### Registers ★★
- مربع ممتلئ برقم بيعرض قيمته الحالية. للحسابات البسيطة أو أرقام جاية من اللاعب. ممكن تتعمل بـ pools وsources/drains لكن الدياجرام يبقى مش مقروء.
- كأنه **pool بيعرض قيمته كرقم**. ممكن passive أو interactive.
  - **Passive:** قيمته من input state connections، ومعروض `x` لما الدياجرام واقف.
  - **Interactive:** قيمة ابتدائية + زرين يعدلوها أثناء التشغيل = pool + interactive source + interactive drain.
- مبتوصلش له resource connections. node modifiers تنفع.
- **حسابات:** كل state connection داخلة بتاخد حرف تلقائيًا، وتكتب formula بالحروف. وفيه `max` و`min` لأعلى أو أدنى input.

### Intervals ★★★
- باستخدام `/` في الـ flow rate: **1/5** = مورد كل 5 steps. شبه 0.2 لكن الـ interval بيدي تحكم ويسمح بـ **bursts**: **5/10** = 5 موارد مرة واحدة كل 10 steps.
- **عشوائي:** **D6/3** = من 1 لـ 6 كل 3 steps. **1/(D4+2)** = مورد واحد كل 3–6 steps. **D6/D6** = من 1–6 موارد كل 1–6 steps.
- ★★★ **Sidebar: Random Intervals in Games (John Hopson، "Behavioral Game Design" 2001):** تجارب علم النفس السلوكي بتقول إن سلوك اللاعب بيتأثر بالصدفة والـ interval اللي بيتكافأ عليه:
  - مكافأة على **intervals منتظمة** → انتباه ونشاط اللاعب **يرتفع عند الـ intervals** دي.
  - **intervals عشوائية الطول** → اللاعب **نشط معظم الوقت** لأنه مش عارف إمتى فعله الجاي هيجيب مكافأة.
  - «استخدم المعرفة القوية دي **بحذر**».
- **Dynamic intervals:** label modifier بوحدة `i` (+1i, −3i) بيغير الـ interval للـ target. Fig 6.4: interval output الـ source A بيزيد مع وصول موارد لـ pool B.

### Multipliers ★★
- `n*` قبل الـ flow rate: `3*50%`, `2*10%`, `3*D3`. بيجمع فرص متعددة في قيمة واحدة. مثلًا source بفرصتين في الـ step = outputs اتنين بـ probable flow rate، لكن الـ multiplier أنظف. **لو الاحتمالات مختلفة لازم الـ construction الطويل.**
- **Dynamic:** modifier بوحدة `m` (+2m, −1m) بيغير الـ multiplier. **Fig 6.6:** multiplier input الـ drain A بتتحكم فيه register B: بتضغط A فيحاول يفرّغ عنصرين بـ 50% لكل واحد، وبتغير B فتغير العدد. والـ modifier +2m هينقل **ضعف** تغيير B.

### Delays and Queues ★★★
- **Delay:** دايرة صغيرة بساعة رملية. الـ label على الـ output = **عدد الـ time steps للتأخير** (مش flow rate زي باقي الـ labels). ديناميكي بـ label modifiers، وممكن عشوائي بـ dice notation. **بيعالج موارد متعددة في نفس الوقت**: كل مورد داخل بيتأخر المدة المحددة بغض النظر عن عدد الموجود.
- **Queue:** ساعتين رمل. **مورد واحد في المرة**. مثال Fig 6.8: مورد كل 5 steps. أوامر البناء بتتطابور وتتنفذ واحد واحد.
- **Fig 6.7:** إنتاج الجنود بياخد وقت وموارد.
- **State connections من delay/queue** بتنقل عدد الموارد اللي بيعالجها (شاملة المنتظرة في الـ queue)، فبتعمل **timed effects**. **Fig 6.9:** تفعيل delay A بيشغّل source B لمدة **10 steps**، وممكن تفعّله طول ما فيه موارد في pool C. ده بيحسن نمذجة الـ power pills في Pac-Man.

### Reverse Triggers ★★
- label `!`. لو الـ source node حاول يسحب ومقدرش يسحب **كل** المطلوب من inputs، الـ reverse trigger يطلق الـ target.
- **مثال Civilization (Fig 6.10):** لما اللاعب يخلص ذهب ومش قادر يدفع **upkeep** لتحسينات المدن، اللعبة **تبيع** بعضها أوتوماتيك.
- كمان لإطلاق **end conditions** (Fig 6.11): اللعبة تنتهي لما اللاعب ياخد damage بعد ما hit points تخلص.

**الباترن:** reverse trigger = «عقاب العجز»: النظام يعاقب أو يعوض تلقائيًا لما اللاعب مش قادر يدفع.

### Color-Coded Diagrams ★★★
- Option Color-Coded في إعدادات الدياجرام. اللون بقى **ذا معنى**.
- connection لونه مختلف عن الـ source **بيسحب موارد لونه بس**. state connection لونها مختلف **بتستجيب لموارد اللون ده فقط**.
- فتقدر **تخزن موارد مختلفة في نفس الـ pool**. source أو converter واحد ينتج ألوان مختلفة لو outputs ألوانها مختلفة. الـ gates **تفرز بالألوان**.
- **Fig 6.12:** source A ينتج عدد عشوائي من البرتقالي والأزرق، والاتنين في pool B. عدد البرتقالي في B بيزود الأزرق المنتج في A والعكس. وdrain C ينفع بس لما يكون في B على الأقل **20 برتقالي و20 أزرق**.
- **Gate بيغير لون الموارد:** لو اللون الداخل مش مطابق لأي output، بيختار output (عشوائيًا للـ random gate، أو حسب الأوزان للـ deterministic) **ويغير اللون**. **Fig 6.13:** إنتاج أحمر وأزرق عشوائي بنسبة متوسطها **7/2**.
- **Delays/Queues ملونة:** outputs بألوان مختلفة بتأخر الموارد حسب كل لون. **Fig 6.14:** بناء knights (أحمر) وsoldiers (أزرق) بـ queue واحدة: الـ knights **تكلفهم ذهب أكتر ووقت أكتر**.
- Tip: لو مش مفعّل الـ option تقدر تلون للتوضيح، لكن المحاكاة بتتصرف كأن كله لون واحد.

## 6.2 Feedback Structures in Games ★★★

- **مثال كلاسيكي، Monopoly (Fig 6.15):** الفلوس المصروفة على property بترجع بربح لأن property أكتر = دخل أكتر. الـ loop يتقرا من **الدائرة المغلقة** من resource وstate connections بين pools الـ Money والـ Property.

### Closed Circuits Create Feedback
- الـ feedback = دائرة connections مغلقة. تغير الحالة بيأثر لحد ما يرجع للعنصر الأصلي.
- **دائرة resource connections بس** (Fig 6.16): نظام دوري بسيط، المورد بيلف ومفيش حاجة أكتر تفاعلًا.
- **الأهم: دوائر مختلطة** (resource + state) فيها **label modifier أو activator** على الأقل.
- **Fig 6.17 (heater بـ activator):** بيحافظ على المورد حوالي **20**، زي تدفئة غرفة: تشغّل سخان بـ output ثابت لما الحرارة تنزل تحت 20. والرسم البياني بيعرض الحرارة مع الوقت.
- **Sidebar Charts:** الـ Tool بيعمل charts تتبع عدد الموارد في pool عبر الوقت. وصّل pool بالـ chart بـ state connection (بتظهر كسهمين صغيرين لما مش متحددة).
- **Fig 6.18 (heater بـ label modifier):** output السخان بيتعدل بالحرارة الفعلية، فمنحنى **أنعم** (سخان بينتج حرارة متغيرة مش ثابتة).

### Feedback by Affecting Outputs
- **Fig 6.19 (air conditioner):** كل ما الحرارة زادت، تتفرّغ أسرع.
- أي حاجة بتأثر على output node ممكن تقفل loop: label modifier مباشر، أو trigger/activator على عنصر في نهاية الـ connection (drain أو converter أو gate، Fig 6.20).

### Positive and Negative Feedback Basketball ★★★ (تفصيل مفهوم Marc LeBlanc من الفصل 4)

**Positive feedback basketball:** سلة عادية بقاعدة زيادة: «لكل **N نقطة فرق**، الفريق المتقدم **يضيف لاعب** في الملعب».
- **النموذج (Fig 6.21):** كل لاعب له احتمال يسجل كل step. الفرق 5 لاعبين، فمعدل الـ source = 5 (المبسط: السلة نقطة، بلا ثلاثيات). gate بنسبة = نسبة نجاح المحاولات. **الأزرق 40% والأحمر 20%** (الأزرق أمهر). pool اسمه **Difference**: كل تسجيل أزرق يضيف نقطة وأحمر يخصم. **كل 5 نقاط فرق = لاعب زيادة** (فرق 5 = +1، فرق 10 = +2...). حجم الفريق **لا يقل عن 5**.
- **النتيجة:** الفريق الأفضل ينطلق لفوق بسرعة (**spiral**) لأن الفرق بيزود لاعبيه.

**Negative feedback basketball:** القاعدة معكوسة: الفريق **الخاسر** يضيف لاعب لكل N فرق (بعكس إشارات state connections).
- ★★ **النتيجة المفاجئة (Fig 6.22):** كنا نتوقع الأضعف يتخطى الأقوى، لكنه **مبيعديش**. الـ negative feedback **يثبّت الفرق**. عند نقطة معينة يبقى الفريق الأضعف متأخر جدًا فمهارته القليلة **تتعوض بحجم الفريق**، وبعدها الفرق مبيتغيرش كتير.

**فريقين متكافئين في positive feedback (Fig 6.23):** بيسجلوا بمعدل متساوي تقريبًا، لكن لما فريق ياخد lead **بالصدفة** يبدأ الـ positive feedback ويتسارع. في الرسم ميل مميز في خط الفرق بعد حوالي **30 step**.

**الباترن:** positive feedback يضخم الفروق الصغيرة (بما فيها الصدفة)، وnegative feedback يضغط الفروق ويثبتها بس مبيقلبش الترتيب.

### Multiple Feedback Loops ★★★
- **Jochen Fromm** (typology الـ emergence من الفصل 3): أنظمة بـ loops متعددة تبين emergence أكتر من واحد. ينطبق على الألعاب. **Risk** فيها **4 feedback loops** متفاعلين.
- ★ **Sidebar: Ideal Number:**
  - **2 لـ 4 major feedback loops** كافي لأغلب الأنواع.
  - **major** = بيتضمن ميكانيكات مهمة متعددة وتأثيره كبير. **minor** = محلي وتأثيره قليل.
  - ممكن تزيد على 4 minor من غير تعقيد، لكن **أكتر من 4 major = لعبة صعبة الإتقان**.
  - ⚠ **المصمم فاهم الـ loops، لكن اللاعبين لأ.**

**الـ 4 loops في Risk:**
1. **الأساسي: armies ↔ territories (Fig 6.24).** تصرف armies لتكسب territories (Attack gate interactive)، الـ armies الناجحة تروح converter يحولها territories. والـ Build source: الـ label **+1/3** = output يزيد 1 لكل 3 territories.
2. **Cards (Fig 6.25):** كسب territory = كارت. تجمع sets وتبدلها بـ armies. **كارت واحد في الـ turn** بس (limiter gate). **Trade Cards** converter يبدل 3 كروت بـ **عدد عشوائي** من الـ armies (تبسيط: مش كل ثلاثي بيدي armies، وبعضه بيدي أكتر).
3. **Continents (Fig 6.26):** السيطرة على continent كاملة = **bonus armies كل turn**. التمثيل: pool موصل بـ pool بـ node modifier، و**5 territories = continent** تنشّط الـ bonus source (**مكافأة 2 armies كل turn** كما في الـ Level of Detail sidebar).
4. **Loss of territories (Fig 6.27):** خسارة territories بسبب لاعبين تانيين. مين يهاجم مين يعتمد على الموقع والاستراتيجية والتفضيلات: أحيانًا تضرب الضعيف، وأحيانًا تقاوم القوي. ★ **عدد الـ continents اللي معاك بيأثر جامد**: لأنها بتدي bonus، اللاعبين بيهاجموا بعدوانية لمنع حد من الاحتفاظ بـ continent.
   - **الباترن:** دي **friction** من اللاعبين، وهي **negative feedback** موجود تقريبًا دايمًا في الـ multiplayer اللي فيه أفعال ضد بعض، خاصة لو **collusion** ضد المتصدر.
   - في الدياجرام بتتمثل بأيقونة **multiplayer dynamic** (بيدقين) على الـ flow للـ Opposition drain.

★ **Sidebar: Level of Detail:** في Fig 6.28 بعض التفاصيل **محددة** (build واحد لكل 3 territories، continent = 2 armies/turn) وبعضها **محذوف** (كام armies من الكروت، وكام territory اتخسروا) واتمثل برموز عشوائية، وتأثير الـ continent على drain المعارضة غير محدد بدقة. **وده مقبول في الدياجرام الثابت**: إحنا بنهتم بالبنية. تحذف تفاصيل = بنية أوضح. **لكن لتشغيله في الـ Tool لازم تحدد كل حاجة.**

### Feedback Profiles ★★★
أول 3 loops في Risk كلهم **positive** لكن **profiles مختلفة**:
- **Territories:** مباشر، بطيء نسبيًا، **استثمار كبير** (غالبًا بتخسر armies في الغزو أكتر ما بتكسب من build واحد → استراتيجية الـ build على turns متتالية).
- **Cards:** **أبطأ** بكتير (كارت واحد/turn ومحتاج 3 على الأقل لـ set) لكن **أقوى** (بين **4 و10 armies** حسب الـ set).
- **Continents:** **أسرع وأقوى** لأنه يولد bonus كل turn. قوي وواضح لدرجة إنه يستدعي **countermeasures شرسة** من اللاعبين.

**أثرها على السلوك ★★:**
- اللاعبين **أكتر استعدادًا للمخاطرة بهجوم** لما الكارت الجاي هيكمل set قيّم. ده **مبيحسنش فرصة كسب المعركة، لكنه يزود المكافأة لو كسبت**.
- فرصة capture continent بتخلي اللاعب **يخاطر أكتر مما ينبغي**.
- في Risk المخاطر والمكافآت بتتحول باستمرار، و**قراءة اللعبة** مهارة حاسمة.
- **التصنيف «positive» وحده مش كفاية. لازم تفهم سرعتها وقوتها.**

### Seven Feedback Characteristics ★★★
**الخصائص السبع:** **type، effect، investment، return، speed، range، durability**. (+ الـ determinability بعدين). [Table 6.1 ضاع في الاستخراج.]

- **التمييز المهم:** positive ≠ constructive، وnegative ≠ destructive. مثال **positive destructive:** خسارة قطع في الشطرنج تزود فرصة خسارة قطع أكتر وخسارة اللعبة. ومثال **negative على constructive effect:** في **Civilization** نمو المدينة بيتبطأ بسبب **corruption** من المدن الكبيرة.
- **Strength** = مؤشر غير رسمي على التأثير، ومبتتنسبش لخاصية واحدة بل لتفاعل عدة خصائص. مثال: feedback **دائم** بـ **return صغير** ممكن يبقى تأثيره قوي.
- ⚠ **تغيير الخصائص يغير اللعبة جامد.** feedback **غير مباشر وبطيء** بـ return كبير وغير durable = **تأثير مزعزع للاستقرار** (destabilizing) قوي. حتى الـ negative feedback ممكن يزعزع النظام لو اتطبق بشكل **متقطع** أو لو تأثيراته **قوية لكن بطيئة وغير مباشرة**: بعد وقت طويل يحصل حاجة كبيرة صعب تتوقعها أو تمنعها.
- **feedback التفاعل المباشر في multiplayer** (زي استهداف لاعب في Risk): غالبًا **negative destructive** (تهاجم المتصدر أو تتآمر عليه)، لكن ممكن يبقى **positive destructive** لو حد بدأ يفترس الضعاف.

**إرشادات قراءتها من الدياجرام:**
- **Effect:** شوف اتوصل بأنهي end condition: مباشرة بشرط فوز = غالبًا constructive، وبشرط خسارة = غالبًا destructive.
- **Investment:** كام مورد بيستهلك لتفعيله، وكتر الـ elements اللي لازم اللاعب يفعلها = investment عالي (وقت أو turns أكتر).
- **Return:** كام مورد بيتنتج. **لازم تقارنه بالـ investment**.
- **Speed:** عدد الأفعال والعناصر للتفعيل. **delays وqueues = أبطأ**. **automatic nodes = أسرع** من الـ interactive. **state connections = أسرع** غالبًا من resource connections.
- **Range:** عدد العناصر في الـ loop. كتير = range عالي.
- **Durability:** أغلب الـ loops أساس اقتصاد اللعبة فـ durability ممتدة أو دائمة. لتحديد المحدودة: شوف هل جزء منها معتمد على موارد محدودة **مبتتعوضش** أو بتتعوض بفترات طويلة.
- **Type:** **أصعب** خاصية. label modifiers موجبة على flow إنتاج = positive، لكن موجبة على flow ناحية drain أو converter = غالبًا **negative**. مع الـ activators أصعب، ولازم تدرس الآلية كلها بتفاصيلها.

### Determinability ★★ (Table 6.2 ضاع)
- عوامل زي الصدفة ومهارة اللاعب وأفعال لاعبين تانيين بتأثر على قوة loop. الدياجرامات بتمثلها برموز **nondeterministic**: **نرد** (random)، **بيدقين** (multiplayer)، **joystick** (player skill)، و**strategy**. بتتحط على connections وgates. loop واحد ممكن يتأثر بأنواع متعددة (مثال: loop الكروت في Risk = random gate + random flow؛ خسارة الـ territories = multiplayer dynamic).
- **Tetris (Fig 6.29):** بتصعب كل ما البلوكات تتراكم، ومعدل التخلص منها = **مهارة اللاعب** (interactive gate بيتحكم في converter). اللاعب الماهر بيجاري لفترة أطول. **المهارة هنا tactical/operational**. وفي ألعاب الصدفة والتكتيك أو deterministic feedback **المهارات الاستراتيجية** ممكن تحسم. وفي Tetris كمان **شكل البلوك عشوائي**، فاللاعب ممكن «يحظ» برضه رغم إن المهارة أحسم.
- ★ **Sidebar استخدام الرموز في الـ Tool:** label `D` = نرد، `M` = multiplayer، `S` = skill (joystick)، `ST` = strategy. **كلها وظيفيًا بتولد قيمة عشوائية 1–6** في الـ Tool (قابلة للتغيير في الإعدادات)، لأنه مبيقدرش يحاكي مهارة أو لاعبين فعليين. الرموز دي للقراءة بس.

## 6.3 Randomness vs. Emergence ★★★

- ألعاب بعوامل عشوائية كتير **مبتتوقعش**، واللاعبين بيحسوا إن أفعالهم **قليلة التأثير**. قوة الـ emergence إن أغلب السلوك الديناميكي بيجي من **تعقيد الأنظمة، مش من عدد النرد اللي بيترمى**.
- ★ **موقف المؤلفين:** اللعبة الجيدة **بتعتمد على الصدفة المحضة باقتصاد**. لعبة بـ **كام deterministic feedback loop** ممكن تبين سلوك ديناميكي مفاجئ. ولما تستخدم emergence مش العشوائية، **كل قرار اللاعب مهم**، فيتشجع على الانتباه والانخراط.

### Frequency and Impact of Randomness ★★★ (Sidebar)
- التأثير غالبًا بيتعلق بمدى وتوزيع الأرقام. **نرد واحد**: احتمال متساوي (1–6 خطوات). **اتنين**: مدى أوسع (2–12) لكن **التوزيع غير متساوي**، فـ **7 أكتر احتمالًا** من أي رقم.
- ★★★ **القاعدة:** لألعاب الـ emergence غالبًا الأفضل **ميكانيكات عشوائية تشتغل بتكرار عالي لكن بتأثير منخفض نسبيًا**. **زيادة تكرار** ميكانيزم عشوائي طريقة كويسة **لتقليل تأثيره**: على المدى الطويل الاحتمالات **بتتعادل**.
- **موقفين مفيد فيهم العشوائية:** (1) إجبار اللاعبين على الارتجال، (2) مواجهة الاستراتيجيات المسيطرة.

### Use Randomness to Force Improvisation ★★
- **أمثلة:** الخرائط العشوائية في **Civilization** و**SimCity** بتعمل تحديات جديدة كل مرة. في **Magic: The Gathering** اللاعب يبني دك بحوالي **40 كارت**، لكن في كل لعبة **بيخلط**: تتحكم في الكروت لكن بتتعامل معاها بترتيب عشوائي. **التخطيط وبناء الدك مهارة، والارتجال واكتشاف الفرص أثناء اللعب مهارة تانية.**
- الارتجال بيشتغل كويس في لعبة بـ **ملعب عشوائي لكنه متساوي** للكل. لو الأحداث العشوائية تأثر على كل اللاعبين بالتساوي، العامل الحاسم **رد فعل اللاعب واستعداده**. ألعاب الـ **European-style** الحديثة كتير بتستخدم العشوائية كده.
- ★★ **Sidebar: Power Grid** (Fig 6.30): لاعبين يشتروا وقود لتوليد طاقة ويبيعوها لشبكة مدن. **عاملين عشوائيين بس**: ترتيب اللاعبين الأولي، وكروت خلطت تحدد محطات الطاقة المتاحة. **فيه ميكانيزمات تعادل العشوائية دي:**
  - ترتيب اللاعبين **بيتغير كل turn بشكل في صالح المتأخرين** (negative feedback).
  - أغلب الوقت المحطات **الرخيصة بس متاحة** والغالية بتتحط في الدك تاني **لتيجي في النهاية**.
  - **مفيش قرار لاعب بيعتمد على نرد**. الشراء = مزايدة (multiplayer dynamic مش random).
  - ألعاب تانية بنفس الفلسفة تستاهل التحليل: **Puerto Rico وCaylus وAgricola**.

### Use Randomness to Counter Dominant Strategies ★★★
- **Dominant strategy** = مسار عمل **الأفضل دايمًا** في كل الظروف (مش بيضمن الفوز، لكنه أفضل اختيار). ⚠ **لازم يتجنبه المصمم**: اللعبة بـ dominant strategy **مش ممتعة** لأن اللاعبين بيعملوا نفس الحاجة كل مرة. العلاج الأصلي: **balance** أحسن (ف8). لو ده صعب أو طويل، **زيادة العشوائية حل سهل**.
- ★★★ **مثال لعبة الـ Harvester:** لاعبين، كل واحد يبدأ بـ harvester بيجمع **0.1 طاقة/turn**. تشتري harvester إضافي بـ **3 طاقة**. الهدف **30 طاقة** والأول يكسب.
  - **الأحمر:** يصرف كل الطاقة على **7 harvesters** قبل ما يبدأ يجمع. **الأزرق:** **2 فقط**.
  - لعبة deterministic: **الأحمر دايمًا يكسب**: **119 turn** مقابل **146** للأزرق.
  - **Table 6.3 (عدد harvesters إضافية → turns):** 0→**300**، 1→**181**، 2→**146**، 3→**133**، 4→**125**، 5→**121**، 6→**120**، **7→119**، 8→120، 9→120، 10→121، 11→121، 12→122. فـ **7 هي الـ dominant strategy**.
  - ملحوظة: نفس نمط «Long-term investments vs. short-term gains» في ف4.
  - **النسخة العشوائية (Fig 6.32):** كل harvester يزود **احتمال** الحصاد بـ 10% بدل 0.1 ثابتة. **بعد 1000 تشغيل: الأزرق عنده حوالي 15% احتمال فوز**. النتائج اتغيرت تمامًا.

**الباترن:** العشوائية بتكسر نمط «الحل الأمثل المحسوب» لأنها بتخلي النتيجة الأمثل غير مضمونة، فاللاعب يبقى محتاج يتكيف.

## 6.4 Example Mechanics ★★★

**ليه بيتنمذجوا لوحدهم:** نماذج الألعاب الكاملة تتعقد بسرعة والدياجرامات المطبوعة ثابتة. وفي كتير من الحالات مش لازم كل ميكانيكا. الألعاب بتتبني من **مكونات ديناميكية**، وفهمها كل واحد لوحده **أول وأهم خطوة** لفهم الكل (الكل أكبر من مجموع أجزائه في ألعاب الـ emergence). فيه نسخ رقمية أونلاين.

### Power-Ups and Collectibles in Action Games ★★★
- الـ gameplay من **الفيزياء وتفاعل اللاعب**. ليفلات خطية: لازم تنفذ مهام كل واحدة بفرصة فشل، والهدف توصل للنهاية قبل ما تخلص lives.
- **Fig 6.33:** ليفل صغير بـ 3 مهام (A, B, C)، كل واحدة **skill gate** بيولد رقم 1–100. اللاعب = مورد بيتنقل بين pools. الفشل: **يموت** (A وC) أو **يرجع لمكان سابق** (B).
- **اقتصاد داخلي:** power-ups وcollectibles. **Super Mario Bros**: coins = نقاط وlives إضافية، وpower-ups قوى خاصة بعضها محدود المدة. بتتمثل كـ **موارد ملونة** بتتحصد من أماكن معينة.
- **Fig 6.34:** اللاعب لازم يكون **موجود في مكان** عشان يجمع الـ power-up. **خيارات استراتيجية:** تتقدم بسرعة وسهولة بالمواقع **I ← II ← V** بسرعة، أو تاخد **الطريق الخطر III وIV** وتجمع **أحمر واحد وأصفر اثنين زيادة**.
- **Required vs. helpful:** power-up لازم لإكمال الليفل (الأزرق مطلوب للمهمة الأخيرة = **lock-and-key**)، وآخر مفيد بس (الأحمر بيسهل المهمة الأخيرة شوية) فاللاعب يقرر **كام مخاطرة ياخد مقابل المكسب**.
- ★ **Tip: Lock-and-Key** هي **أهم ميكانيزمات ألعاب الـ progression** للتحكم في تقدم اللاعب. **نادرًا فيها feedback loops، فنادرًا بتظهر emergence.** (ف10).
- **Limited-Duration Power-ups (Fig 6.35):** delays للـ power-up المؤقت، وبيعمل **respawn** ويبقى متاح تاني بعد الاستهلاك.
- **Collectibles = خيار استراتيجي (Fig 6.36):** لو لازم تخاطر بـ lives لتجمع coins ولازم coins لتكسب lives، فـ **التوازن بين الجهد والمخاطرة وعدد الـ coins** حاسم. ★ لو جمعت **تقريبًا كفاية** لحياة زيادة، **المخاطرة بالزيادة تبقى استراتيجية مقبولة**. ده loop **positive**، لكن **مهارة اللاعب** هي اللي تحدد هل العائد كافي لموازنة المخاطرة.

### Racing Games and Rubber Banding ★★★
- سباقات = لعبة **«إنتاج مسافة»**: الأول يجمع مسافة كفاية يكسب (Fig 6.37). الإنتاج ممكن يتأثر بالصدفة أو المهارة أو الاستراتيجية أو جودة العربية.
  - **Game of Goose:** صدفة بالكامل. **أركيد الفيديو:** مهارة. **ألعاب فيها tuning:** استراتيجية طويلة كمان.
- ⚠ **عيب كبير:** لو المهارة أو الاستراتيجية حاسمة **النتيجة نفسها تقريبًا دايمًا** (Fig 6.38: مهارة مختلفة = احتمالات إنتاج مختلفة، والأزرق **يكسب تقريبًا دايمًا**).
- **Rubber banding** = تطبيق **negative constructive feedback** على أساس **المسافة** بين اللاعب والخصوم الاصطناعيين لإبقائهم قريبين. (شفناه في negative feedback basketball.) **لكنه** بالشكل ده يبقي اللاعبين قريبين **من غير ما يخلي الأضعف يكسب أكتر**.
- ★★★ **التعديل:** لو الـ negative feedback **أقوى ويستمر لفترة** تأثيره يتغير. **Fig 6.39:** مهارة الأزرق **60%** والأحمر **40%**. register يحسب فرق المسافة ويشير لـ **Boost** source للاعب المتأخر. **الـ boost يستمر 20 steps** وكل boost يحسن الأداء **5%**. النتيجة: **الأزرق والأحمر يتبادلوا الصدارة**.
- ملحوظة: نفذوه بشكل **متطرف عمدًا** للوضوح. الألعاب الحقيقية بتستخدم boosting **أخف**.

### RPG Elements ★★★
- مهارات وسمات الشخصيات = موارد بتأثر في القدرة على المهام. **الهيكل الأهم: positive feedback loop**: لازم تنجح في مهام لتزود قدراتك، فتزيد فرصة نجاحك في مهام أكتر.
- **XP وLevels كموارد منفصلة (Fig 6.40):** 3 أفعال: **combat وmagic وstealth**. النجاح يولد XP. **10 XP = level up**: تتحول لـ **level أعلى** و**2 upgrades** يزودوا القدرات. (لو XP ما بيتستهلكش وبيطلق upgrades عند عتبات: source بيولد upgrades + activator.) **صعوبة المهام** بتزيد أحيانًا باستخدام color-coding، وكل مهمة تتقدم بشكل مختلف. في الأصل **dungeon master** أو النظام يضمن مهام مناسبة.
- ★★★ **Negative feedback جزئي:** XP المطلوب للـ level التالي **بيزيد مع كل level**. ده شائع في RPGs. **أثره:** بيفضّل **التخصص** (specialization): كل ما XP المطلوب زاد، اللاعبين هيفضلوا المهمة اللي هم أحسن فيها لأن فرصة تنتج XP أكبر.
- **العلاج:** negative feedback على **تكلفة أو تأثير الـ upgrade لكل قدرة لوحدها** (Fig 6.41)، بدل أو مع زيادة XP

# Game Mechanics: Advanced Game Design (Adams & Dormans) — جزء 4/8 — نوتس مذاكرة

الجزء ده بيغطي صفحات الكتاب ~145–207 (PDF 160–222): ذيل **الفصل 6** (الملخص والتمارين)، **الفصل 7** كامل (Design Patterns)، **الفصل 8** كامل (Simulating and Balancing)، وأول **الفصل 9** (Building Economies).

ملحوظات على المصدر:
- النص **مقطوع في نص الفصل 9** عند قواعد Lunar Colony (setup الماب). الباقي في الجزء 5.
- رسومات تمارين الفصل 6 (البنود 6-8) اتبوّظت في الاستخراج (صور diagrams)، فمش هتتسجل.
- شرح syntax الـ scripting بتاع Machinations (الأوامر والـ operators) = tool/برمجة. اتسجل منه بس اللي ليه قيمة تصميمية، والباقي متجاهل.

---

## الفصل 6 (الذيل) — ملخص + تمارين ★

- الخلاصة: Machinations بتحاكي economies الأساسية في action وRPG وFPS وRTS. الفصل الجاي = **design patterns**: «تراكيب مألوفة تبني وتختبر بيها mechanics بسرعة».
- **التمارين (8):**
  1. ضيف negative feedback loop زيادة في Monopoly.
  2. اعمل لعبة كل الـ random effects فيها بتأثر على كل اللاعبين بالتساوي.
  3. صمم mechanics لعبة سباق فيها positive, constructive feedback وتفضل عادلة (fair).
  4. ارسم diagram لأهم feedback loops في لعبة منشورة.
  5. ★★ **منهج مهم:** اعمل prototype + playtest للعبة فيها loop واحد، وكمّل ضيف loops بـ signatures مختلفة لحد ما تبقى اللعبة ممتعة ومتوازنة وفيها emergent behavior. **اعمل prototype وplaytest في كل خطوة.** السؤال: محتاج كام loop؟
  6. diagrams: معدل إنتاج الـ automatic source بعد ضغطة واحدة على interactive node A (4 diagrams) — *الصور مفقودة*.
  7. 5 turn-based diagrams: كام turn لحد ما تجمع 10 resources في pool A — *مفقودة*.
  8. diagrams ملونة: أقل عدد ضغطات للفوز (2 diagram) — *مفقودة*.
- **الباترن ورا التمرين 5:** الـ feedback loops بتتضاف **واحد واحد** وبتتختبر في كل خطوة. مش بتتصمم كلها مرة واحدة.
- **لموسفولك:** التمرين 5 هو منهج إضافة التحديات الجديدة (mossy shells / stones / rot): تضيف loop واحد، تشغّل التيستر-بوت، تقيس `bot_difficulty`، وبعدين اللي بعده. والتمرين 2 مرتبط بالـ rival contests: لو الـ RNG بتاع تسلسل القطع هو نفسه للاعب والـ rival، العدالة بتتضمن بالتصميم.

---

## الفصل 7 — Design Patterns ★★★ (مفيد جدًا كمفردات ومنهج)

### 7.1 الفكرة الأساسية: Monopoly = Harvester
- Figure 7.1 (Monopoly) وFigure 7.2 (Harvester game، نسخة لاعب واحد من الفصل 6): لو تجاهلت Pass Go source وPay Rent drain وقلبت 90° عكس عقارب الساعة، الـ loop **واحد**.
- التركيب: **source بيغذي pool بمعدل إنتاج، وresources من الـ pool بتتحول لنوع جديد بيزوّد معدل إنتاج الـ source.**
- Risk فيها loop مشابه كمان.
- ★★ **الباترن ورا الملاحظة:** ده مش صدفة ومش سرقة. «الباترن ده في الـ mechanics بيشتغل لألعاب كتير»، فهو بنية متكررة.
- **التعريف: Design patterns = recurrent patterns في structure الـ game mechanics.**
- الأصل: المعماري **Christopher Alexander** (*A Pattern Language*, 1979) → اتنقل لهندسة البرمجيات → وهنا للألعاب بنفس الخط.

### 7.2 تاريخ مختصر
- **Alexander:** حاول يوثق معايير جودة موضوعية في العمارة. اقتباس: «في quality مركزية هي المعيار الجذري للحياة والروح في الإنسان والمدينة والمبنى والبرية — موضوعية ودقيقة لكن ملهاش اسم» (p. ix).
- **Pattern language** عنده: مكتبة كاملة، وكل pattern:
  - حل لمشكلة تصميم شائعة، موصوف **بأكبر قدر من العمومية** عشان يتستخدم في ظروف مختلفة.
  - بنفس الفورمات.
  - وليه روابط بـ patterns أكبر وأصغر، والأصغر بيكمّل الأكبر.
  - أكتر من **100 pattern** عبر مجالات (من urban planning لمبنى واحد).
- **Gang of Four** (Gamma, Helm, Johnson, Vlissides — *Design Patterns*, 1995): مبادئ OOP حلّت محل الـ quality اللي ملهاش اسم عند Alexander.
  - الفايدة: **مفردات مشتركة** (common vocabulary) لحاجات المبرمجين كلهم عارفينها ومالهاش أسماء → تعاون أسهل وكود أحسن.
  - المجموعة الأصلية ~**20 pattern**، اتضاف شوية واتشال شوية، والـ core لسه صغير.
- **الباترن ورا نجاح الـ patterns:** لغة مشتركة + حلول عامة مجرّبة + مفيش pattern منعزل (فيه علاقات).

### 7.3 Sidebar: «Good Design»
- «Good» بتتفهم كحكم شخصي. لكن نقاد الألعاب والأفلام والكتب والعمارة شايفين إن بعض المنتجات **موضوعيًا أحسن**.
- الافتراض اللي الكتاب شغال بيه: **بعض جوانب اللعبة قابلة للتقييم الموضوعي**. الآراء مش مقبولة عالميًا لكنها أكتر من ذوق شخصي («ولو مش شايفين كده يراجعوا اختيار المهنة»).
- تعلم الـ patterns بيساعدك تفهم خصائص الألعاب الكويسة.

### 7.4 مفردات التصميم (Design Vocabularies) في الألعاب
- مفيش مفردات متفق عليها تخلي المصممين يتشاركوا الأفكار بكفاءة.
- **Doug Church (1999)، Gamasutra، «Formal Abstract Design Tools»:**
  - *Formal* = دقيق.
  - *Abstract* = يتخطى تفاصيل لعبة واحدة.
  - أدوات مناسبة لمهام مختلفة، ومش كلها تنفع لكل لعبة.
  - **التلات أدوات:**
    1. **Intention:** اللاعب يقدر يعمل **plan قابل للتنفيذ** من تأليفه ردًا على الوضع الحالي وفهمه لخيارات اللعب.
    2. **Perceivable Consequence:** العالم يرد **بوضوح** على أفعال اللاعب، والنتيجة تبان.
    3. **Story:** خيط سردي (من المصمم أو اللاعب) بيربط الأحداث ويدفع للإكمال.
  - منتدى Gamasutra (1999–2002): المصطلح اتغيّر من design **tool** لـ design **lexicon**، لأنها نجحت كأداة **تحليل** أكتر من أداة تصميم. Bernd Kreimeier (2003): **25 مصطلح على الأقل** من تقريبًا نفس عدد المساهمين. المشروع اتهجر، لكن Church بيتنسب له أول محاولة جادة.
- **Sidebar: Patterns vs Vocabularies:**
  - الاتنين بيحاولوا يلقطوا الخصائص الجوهرية للألعاب.
  - الـ **patterns** هدفها تساعد الناس **يصنعوا** ألعاب (أو كود أو مباني) كويسة، فهي prescriptive.
  - الـ **vocabularies** أكتر حيادية (خصوصًا أكاديميًا).
  - الكتاب اختار patterns لأنها أنفع للمصمم.
  - النقد المحتمل: الـ prescriptive أضيق (بيترد عليه في sidebar النقدين تحت).
- **مفردات أونلاين (بعضها متهجر):**
  - **The 400 Project:** Hal Barwood وNoah Falstein، هدفه 400 قاعدة تصميم. اتسجل **112** بس، وآخر إضافة 2006.
  - **Game Ontology Project:** يرتب حكمة التصميم في ontology واحدة. أداة تحليل لفهم الألعاب مش بنائها، لكن فيها «design lore» قيّم.
  - **Game Innovation Database:** يتتبع ابتكارات التصميم لمصادرها الأصلية (منظور تاريخي).

### 7.5 Design Patterns في الألعاب (المحاولات)
- محاولات pattern language أقل من vocabulary.
- **Kreimeier** (2002، «The Case for Game Design Patterns»): اقترح framework ومبناهوش.
- **Björk & Holopainen** (*Game Design Patterns*, 2005): مئات الـ patterns + موقع. تعريفهم: «semiformal interdependent descriptions of commonly reoccurring parts of the design of a game that concern gameplay» (p. 34).
  - ده أقرب لـ vocabulary.
  - ملهمش رؤية نظرية لمعنى الجودة في الألعاب ومصدرها.
  - مجموعة معرفة قيّمة، لكن **مبتقولش إزاي تستعملها عشان تبني ألعاب أحسن.**
- ★★★ **موقف المؤلفين:** أي محاولة لازم تبدأ **برؤية نظرية واضحة** لـ «إيه اللي بيخلّي اللعبة جيدة موضوعيًا — الجودة الجوهرية جاية منين»، وبعدين تحدد المشاكل الشائعة وتديها حلول عامة. كده الـ patterns تبقى أداة **تصميم** مش تحليل بس.

### 7.6 Machinations Design Pattern Language
- رؤية الجودة هنا: **العلاقة بين structure الـ internal economy والـ emergent gameplay**، وأهمها feedback loops. وMachinations diagrams هي لغة التعبير.
- **فورمات وصف الـ pattern** (مأخوذ من Gang of Four، والوصف الكامل في Appendix B):
  1. **Name** (+ Also Known As).
  2. **Intent:** جملة قصيرة تقول إيه اللي بيعمله.
  3. **Motivation:** استخدام أوسع + سيناريوهات.
  4. **Applicability:** إمتى يتستخدم وأي مشاكل بيحل.
  5. **Structure:** تمثيل graphical بـ Machinations.
  6. **Participants:** العناصر والـ mechanisms والـ compound structures المسماة.
  7. **Collaborations:** أهم العلاقات الهيكلية بين الـ participants.
  8. **Consequences:** المتوقع لو طبقته، بما فيه الـ trade-offs والمخاطر.
  9. **Implementation:** طرق تنفيذ بديلة + **تأثير الـ randomness**.
  10. **Examples:** **مثالين على الأقل** من ألعاب منشورة.
  11. **Related Patterns:** بعضها بيضاد بعض وبعضها بيكمّل.
- الـ diagrams عامة عن قصد: الأرقام مش محددة، والـ resource connections مكتوب عليها `n`، والـ state connections `+` أو `-`. عشان تشغّلها لازم تضيف تفاصيل.

### 7.7 مكتبة الـ patterns (11 في 3 categories + 5 متفرقة = 16)

**Category 1: Engines** (بتولّد resources تحتاجها mechanics تانية)

| Pattern | التعريف | استخدمه لما... |
|---|---|---|
| **Static Engine** | تدفق ثابت من resources عبر الوقت يستهلكه اللاعب أو يجمعه | عايز **تحدّد أفعال اللاعب من غير تعقيد**. بيخلّي اللاعب يفكر يصرف إزاي من غير تخطيط طويل المدى |
| **Dynamic Engine** | source بتدفق قابل للتعديل، واللاعب يستثمر resources يحسّنه | عايز **trade-off بين استثمار طويل المدى ومكسب قصير المدى**، وتحكم أكبر للاعب في معدل الإنتاج من static |
| **Converter Engine** | converterين في loop بيعملوا فائض resources يتصرف في حتة تانية | عايز آلية أعقد تدّي موارد أكتر من static/dynamic (المثال فيه عنصرين interactive مقابل واحد في dynamic). **بيزوّد الصعوبة** لأن قوة الـ loop والاستثمار المطلوب أصعب في التقدير. وعايز خيارات كتير لضبط **profile** الـ loop |
| **Engine Building** | جزء **كبير** من اللعب مخصص لبناء engine وضبطه عشان تدفق ثابت | تركيز قوي على building/construction وعلى استراتيجية وتخطيط طويلي المدى |

- **Profile** الـ feedback loop = مجموعة خصائصه (effect, investment, speed...) من Table 6.1.

**Category 2: Friction** (بتسحب resources من الـ economy أو تقلل إنتاجيتها، للتعبير عن الفقد والـ inefficiency)

| Pattern | التعريف | استخدمه لما... |
|---|---|---|
| **Static Friction** | drain بيستهلك تلقائيًا من اللي ينتجه اللاعب | عايز آلية تقاوم الإنتاج لكن اللاعب **يقدر يتغلب عليها** في الآخر، وعايز تبالغ في فايدة ترقيات الـ dynamic engine طويلة المدى |
| **Dynamic Friction** | نفس الـ drain لكن معدل الاستهلاك **متأثر بحالة عناصر تانية** | تعالج ألعاب فيها resources بتتنتج **بسرعة زيادة**، وتقاوم الإنتاج وتتسكيل **أوتوماتيك** مع تقدم اللاعب وقوته، وتقلل فعالية الاستراتيجيات طويلة المدى لصالح قصيرة المدى |
| **Stopping Mechanism** | بتقلل فعالية mechanism **كل مرة** بتتفعّل | تمنع إساءة استخدام أفعال معينة، وتقاوم dominant strategies، وتقلل فعالية positive feedback |
| **Attrition** | اللاعبين بيسرقوا أو يدمروا resources بعض (اللي محتاجينها لأفعال تانية) | تسمح بتفاعل مباشر واستراتيجي بين اللاعبين، وتدخل feedback في نظام طبيعته بتحدده تفضيلات اللاعبين ونزواتهم |

- **Stopping mechanism = قانون العائد المتناقص** (diminishing returns). المثال: السماد بعد حد معين بيقلل المحصول لأنه سام بكميات كبيرة.

**Category 3: Escalation** (ضغط على اللاعب بتحديات بتكبر)

| Pattern | التعريف | استخدمه لما... |
|---|---|---|
| **Escalating Challenge** | التقدم نحو الهدف **بيزوّد صعوبة** التقدم الزيادة | لعبة سريعة مبنية على مهارة (غالبًا جسدية) واللعبة بتصعب كل ما تتقدم وقدرتك بتتعطل. وعايز emergent mechanics **تحل جزئيًا** محل level progression مصمم مسبقًا |
| **Escalating Complexity** | اللاعب بيقاوم تعقيدًا بيكبر ويحاول يسيطر لحد ما الـ positive feedback يقوى والتعقيد المتراكم يخسّره | لعبة high-pressure قائمة على مهارة، ونفس هدف استبدال level progression |
| **Arms Race** | اللاعب يستثمر resources يحسّن قدراته الهجومية والدفاعية ضد لاعبين | تدّي خيارات استراتيجية أكتر للعبة بتستخدم attrition، وتطوّل زمن اللعب |

**متفرقة (Miscellaneous):**
- **Playing Style Reinforcement:** feedback بطيء، positive، constructive على أفعال اللاعب → اللعبة تتكيف تدريجيًا مع أسلوبه المفضل. استخدمه لما تريد استثمارًا طويل المدى **عبر جلسات متعددة**، وتكافئ البناء والتخطيط المسبق والاستراتيجيات الشخصية، وتخلي اللاعب «يكبر» في دور أو استراتيجية.
- **Multiple Feedback:** mechanism واحد بيغذي عدة feedback mechanisms، كل واحد بـ profile مختلف. استخدمه لـ **تزويد الصعوبة** و**مكافأة قدرة اللاعب على قراءة حالة اللعبة**.
- **Trade:** تجارة بين اللاعبين = multiplayer dynamics + **negative, constructive feedback** + social mechanic عن طريق التجارة (بدل القتال).
- **Worker Placement:** اللاعب يتحكم في resource محدودة لازم **يلتزم بها** عشان يفعّل أو يحسّن mechanisms. استخدمه لإدخال micromanagement مستمر، وتشجيع التكيف مع الظروف المتغيرة، وجعل **التوقيت (timing)** عامل حاسم، وبناء صراع غير مباشر خفي.
- **Slow Cycle:** mechanism بيدور بين حالات **ببطء**، فبيعمل تغييرات دورية في mechanics. استخدمه لـ:
  - تنويع عن طريق phases دورية.
  - مقاومة سيطرة استراتيجية معينة.
  - إجبار اللاعب يعدّل استراتيجيته دوريًا.
  - ★ **إطالة فترة التعلم قبل الإتقان:** اللاعب بيشوف الـ slow cycle أقل، فعنده فرص أقل يتعلم منه.
  - تفاعل استراتيجي غير مباشر خفي بالتأثير على **period/amplitude** الدورة.

### 7.8 دمج الـ patterns
- الألعاب نادرًا بتطبق pattern واحد.
- **Tetris** = escalating complexity (المكعبات بتتراكم والفجوات تكتر في القاع) + escalating challenge (المكعبات بتنزل أسرع كل ما تمسح خطوط).
- **أنواع (genres) بتتشكل من تركيبات:**
  - **RTS** = dynamic engine (بناء القاعدة للإنتاج) + attrition (حرب استنزاف). الـ RTS الكبيرة بتضيف arms race أو (أقل شيوعًا) engine building لخيارات أكتر ولعب أطول.
  - **RPG** = playing style reinforcement (character building) + escalating challenge.
- التجريب بتركيبات غير متوقعة ممكن يطلّع نتايج مثيرة.

### 7.9 Elaboration & Nesting
- **Elaboration:** pattern هو تنفيذ أكثر تفصيلًا لـ pattern تاني.
  - Dynamic engine حالة خاصة من engine building (لو حطيت dynamic engine فعندك engine building ضمنًا).
  - **Attrition** حالة خاصة من dynamic friction مطبقة **بشكل متماثل** (symmetric).
  - **سلسلة الـ engines:** worker placement ⊃ engine building ⊃ dynamic engine ⊃ static engine.
  - كل engine pattern هو elaboration لـ source عادي، وكل friction pattern لـ drain عادي → تقدر تستبدل أي source بـ engine والعكس.
  - Appendix B بيسرد في Related Patterns مين بيعمل elaboration لمين.
- ★★★ **أداة تصميمية (الباترن):**
  - اللعبة **بسيطة زيادة** → استبدل pattern بـ pattern بيعمله elaboration → تعقيد أكتر.
  - اللعبة **معقدة زيادة** → استبدل pattern معقد بالأبسط اللي هو بيعمله elaboration → تبسيط.
- **مثال Harvester:**
  - ترقية الـ pattern كله لـ engine building أو worker placement (Fig 7.3).
  - أو استبدال الـ source بـ converter engine (Fig 7.4).
  - والـ converter نفسه = drain بيفعّل source، فتقدر تستبدل أي واحد فيهم بـ engine أو friction.
- **Sidebar: عكس الـ elaboration = Simplification:**
  - تشيل تعقيد من التصميم، أو تعمل diagrams **أكثر تجريدًا** من اللعبة لكن محتفظة بجزء من سلوكها الديناميكي.
  - استخدموها في **Pac-Man (ch5)** و**Risk (ch6)**: معارضة اللاعبين الآخرين اتمثلت كـ **dynamic friction** (Fig 6.27). ولو multiplayer diagram كان هيستخدم **attrition**.
  - باستبدال attrition بـ dynamic friction شالوا اللاعبين الباقيين من الـ diagram وركّزوا على الـ internal economy من منظور لاعب واحد.
  - الـ elaboration مش للـ patterns بس، لأي عنصر (Fig 7.5: طرق مختلفة لـ elaboration لـ converter = أي mechanism يستهلك resource ويطلّع تانية). دي مش patterns لأنها مش حل عام لمشكلة شائعة، لكن بناء **repertoire** منها (مع معرفة أصلها) بيسهّل التجريب.
- **Sidebar: Elaboration & Design Focus:**
  - طابق تعقيد الـ mechanics مع **design focus** (الـ gameplay المقصود).
  - لو اللعبة عن القتال: mechanisms معقدة للقتال، وبسيطة للأجزاء اللي اللاعب بيقضي فيها وقت أقل ومبيهتمش (construction أو inventory مثلًا).
  - لو الـ mechanisms الثانوية معقدة زيادة: استبدلها بـ patterns أبسط أو حتى **عنصر واحد**، وأحيانًا الأحسن **source بسيط بمعدل تدفق عشوائي** بدل آلية إنتاج معقدة.
  - ★★ «elaborate اللي بيولّد أهم gameplay وبسّط الباقي».

### 7.10 توسيع اللغة
- المكتبة مش مكتملة، وبيشجعوا تلاحظ patterns جديدة من تصاميمك أو تحليل ألعاب غيرك.
- القاعدة: وصف الـ pattern الجديد **بمصطلحات عامة**. مثال: لقيت pattern في لعبة sci-fi عن تجارة بين المجرات، ما تسميش الـ pattern وparticipants باسماء اللعبة دي.
- التزم بالفورمات، سمِّ أهم participants، فكّر في **طرق تنفيذ متعددة**، والأهم **حدد المشكلة التصميمية الشائعة** اللي بيحلها.

### 7.11 Sidebar: نقدين للـ formal methods (ومعها الرد)
- **السياق:** Raph Koster، GDC 2005، «A Grammar of Gameplay: Game Atoms — Can Games Be Diagrammed?» اقترح طريقة diagramming، وردّ فعل الجمهور كان **متباين** (Sheffield 2007). المؤلفين لاحظوا نفس الانقسام في الصناعة.
- **النقد 1:** المنهجيات «لُعب أكاديمية» قليلة الصلة بالتصميم التطبيقي.
  - الرد: السجل الحالي للـ formal methods في الصناعة **ضعيف** فعلًا. معظمها اتصمم على أيدي أكاديميين قليلي الخبرة العملية، وبتحتاج استثمار كبير في التعلم بعائد قليل، خصوصًا أدوات **التحليل** (التحليل الرسمي بيحصل في الجامعات أكتر من الصناعة).
  - ★★ **معيار التقييم:** الأداة لازم تساعد المصمم **يبتكر ويفهم ويعدّل تصميماته**، مش يحلل ألعاب الناس بس. Machinations بتسمح بتجريب mechanics **بدري** في التطوير (case study في Ch9).
- **النقد 2:** مفيش منهجية تحل محل **العبقرية الإبداعية** (Guttenberg 2006)، وبيخافوا الأدوات تحصر نظر المصمم.
  - الرد: تصور ساذج للفن. الفن = **موهبة + تقنية متمرّن عليها + شغل كتير جدًا**.
  - الموهبة الخالصة نادرًا بتعوّض الاتنين التانيين.
  - الصناعة اللي فيها فلوس كتير على كل مشروع مش قادرة تقامر بالموهبة كل مرة.
  - أمثلة تاريخية: **المنظور الهندسي** (geometric perspective) ثورة في رسم النهضة، ومعدود علمي مش جمالي. **الفن التجريدي** (القرن 19 وأول 20) كان عملية فكرية تدريجية ومقصودة.
  - الطرق **تدعم** العبقرية ولا تستبدلها، وأقصى فايدتها تخفف العبء وتصقل التقنيات. وهي كمان بتسهّل **teamwork**: بدل الجدال عن سلوك mechanics بعد الكود، الفريق يعمل diagram ويحاكي **قبل سطر كود واحد**.

### 7.12 استخدام الـ patterns في التصميم
- المكتبة guidelines للاستكشاف مش قواعد إجبارية.
- ★★ **نصيحة:** **التزم بالـ patterns في الأول** (النسخ من تراكيب مجرّبة = أسرع تعلم)، وبعد ما تكتسب خبرة اكسر منها. الاستكشاف الجديد مهم لكن بعد الخبرة.
- **تحسين تصميمك (مثال تشخيصي):**
  - اللعبة بتطلّع **نتايج عشوائية/اعتباطية** لأن positive, constructive feedback قوي بيضخّم فرق صغير في الحظ بدري.
  - الحلول من المكتبة: لو فيه resources متعددة → **Trade** (يدخل negative feedback). أو **dynamic friction** يقاوم الـ positive feedback.
  - ادرس المكتبة لتعرف أشكال تنفيذ الـ pattern ومشاكلها (design lore مركّزة تطورت عبر زمن طويل).
- **Brainstorming:**
  - اسحب 2-3 patterns عشوائيًا وصمم game economy حواليهم. ممكن تنفّذ واحد في diagram وتضيف الجاي، وتكرر لحد 3-4، ومع paper prototype لكل خطوة.
  - لو الـ pattern اتكرر، طبّقه على resource أو جزء تاني.
  - أو اختار patterns قبل ما تبدأ وصمم economy بيطبقها كلها من الأول.
  - المؤلفين بيكتبوا أسماء الـ patterns على كروت بيضا ويخلطوها (تمرين 3 تحت).
- **على لعبتك الحالية:**
  - الـ patterns بتوحي بمصطلحات عامة لموارد اللعبة حسب **وظيفتها** في الـ economy.
  - حدد أي resource هو «الطاقة» الأساسية اللي بتشغّل أفعال اللاعب الجوهرية.
  - اسحب pattern عشوائي كـ **lens**: موجود في التصميم؟ شغال زي ما عايز؟ لو لأ، هل إضافته تعالج مشكلة؟
- **على ألعاب موجودة:** إيه الـ stopping mechanism في StarCraft؟ لو غيرنا الـ dynamic engine لـ converter engine؟ إيه patterns تتضاف؟

### 7.13 Sidebar: Player-Centric Design (Ernest Adams)
- من *Fundamentals of Game Design*: تتخيل **لاعب نموذجي** وتحكم كل قرارات التصميم على توقعاته وآماله.
- ★★ **مش بيتعارض مع الـ formal methods:** الـ player-centric في قلب تصميم الـ mechanics حتى لو مجرّدة.
- **مثال Power Grid:** أنظمة معقدة متشابكة وعشوائية قليلة → بيجذب **mathematical strategists** (بيحبوا فك النظام وتحسينه). لعبة أقصر وعشوائية أكتر → كاجوال ولاعبين صغار.
- «الناس بتختار اللعبة حسب نوع الـ gameplay، والـ mechanics بتصنع الـ gameplay.» ولازم تفضل تسأل **«مين بيحب النوع ده من الألعاب؟»**

### 7.14 الملخص + التمارين
- الخلاصة: 16 pattern، 3 categories (engines, friction, escalation) + متفرقة. بتستخدم للدمج والـ brainstorming وتحليل الألعاب اللي في التطوير، وللـ **common vocabulary** مع الفريق.
- الفصل الجاي: الـ **scripted artificial player** + تحليل Monopoly وSimWar.
- **التمارين:**
  1. إيه patterns استخدمتها في مشاريعك الأخيرة؟ وإيه اللي كان ممكن تستخدمه وماستخدمتوش؟ هل كان هيحسّن اللعبة؟
  2. لعبة تعرفها كويس (أي genre ما عدا pure adventure لأنها من غير internal economy): إيه patterns فيها؟ ارسمها.
  3. اختار pattern-ين عشوائيًا (كروت)، هل في لعبة بتحتوي الاتنين؟ أو صمم concept لعبة بيهم وارسم diagram.

**لموسفولك:**
- **جرد patterns:**
  - الـ jar بيمتلي = **escalating complexity** (زي Tetris: تراكم + حفر).
  - **Drop budget** = pool بيتستهلك.
  - الـ merge = **converter** (2 → 1 أكبر).
  - Mossy shells / stones / rot (2501+) محتاجين يتصنفوا: static friction ولا dynamic friction ولا stopping mechanism؟ اسأل: **هل بتتسكيل أوتوماتيك مع تقدم اللاعب؟** (ده سؤال الـ dynamic friction).
  - الـ rival contests: attrition (تأثير مباشر على موارد الخصم) ولا race متوازي؟ اتحقق.
- **أداة تشخيص:** لو ليفلات كتير بتنتهي بنتيجة «اعتباطية» من حظ أول القطع، شوف قائمة الحلول: friction أو negative feedback بدل ما تعدّل البوت.
- **Elaboration & design focus:** الـ core (drop + merge + physics) هو اللي يتعمل له elaboration. الـ side quests/minigames/garden يتبسطوا لـ source بمعدل عشوائي لو الميزانية ضيقة (ده بالظبط نصيحة hybrid-casual scoping).
- **مكتبة patterns داخلية:** نكتب كل تحدي جديد بنفس الفورمات (Name/Intent/Applicability/Consequences/Implementation/Related) وبأسماء **عامة** مش «Mossfolk-specific». دي مفرداتنا المشتركة مع الـ tester-bot ومولد الليفلات.
- **Brainstorm بكروت:** سحب 2 patterns عشوائي لتصميم side quest أو rival contest جديد.
- **Power Grid vs casual:** بنقرر نمط اللاعب الأول قبل ما نختار تعقيد pattern (hyper/hybrid → بسيط).

---

## الفصل 8 — Simulating and Balancing Games ★★★ (أنفع فصل للتيستر-بوت)

### 8.1 المقدمة: ليه المحاكاة
- ألعاب بسيطة (blackjack, roulette) تحسب احتمال الفوز **بدون لعب**. الألعاب المعقدة اللي فيها عشوائية لازم تتلعب **مرات كتير** عشان تعرف لو متوازنة.
- الأرقام في الفصول السابقة جاية من **آلاف simulated play tests** بـ **artificial players (AP)** بتجري أوتوماتيك.

### 8.2 الـ Artificial Player في Machinations
- مربع صغير فيه **AP**، **مش متوصل بأي حاجة**. بيشغّل **script** بيتحكم في nodes تانية («virtual click»). مش بس interactive nodes، يقدر يفعّل أي named node.
- **منطق الـ script** (تصميمي مهم ★★):
  - سطور بتتقيّم من فوق لتحت.
  - **أول command بيتنفّذ بيوقّف الـ script** (الـ fire الجاية بتبدأ من فوق تاني).
  - مفيش else: الـ if بتتفحص بالترتيب لحد ما شرط يصح. **= قائمة أولويات (priority list) first-match-wins.**
  - مينفعش command مباشر ورا command مباشر (التاني مش هيتنفذ).
  - الأوامر الأساسية:
    - `fire(node)`: يفعّل node.
    - `fireAll(...)`: كلهم مع بعض.
    - `fireSequence(...)`: واحد واحد بالترتيب ويدور (مثال: Produce, Produce, Upgrade, Produce, Consume).
    - `fireRandom(...)`: يختار واحد عشوائيًا، **وتكرار الاسم بيزوّد احتماله** (مثال: Produce, Produce, Consume, Upgrade = **50% / 25% / 25%**).
    - `if(condition)command`: الشرط على pools/registers.
  - أوامر إضافية: `stopDiagram(message)`، `endTurn()`، `activate/deactivate`.
  - ★★ **`stopDiagram(message)`:** رسالة نص. في الـ multiple runs الأداة **بتعدّ كل رسالة** وبتطلّع إحصاءات **إيه اللي أوقف الـ diagram** (مين اللاعب اللي أنهاه مثلًا).
  - في turn-based: الـ AP عنده عدد actions في الدور، ولو أكتر من واحد بتتنفذ على فاصل **ثانية**.
  - في diagrams الملونة: الـ AP بيفعّل بس nodes **بنفس لونه**.
  - **قيم خاصة:**
    - `random` (0-1، يتغير).
    - `pregen0…pregen9` (10 قيم عشوائية بتتولّد **مرة واحدة** عند بدء الـ run وبتثبت فيه).
    - `actions`، `steps`، `actionsOfCommand`، `actionsPerStep`.
  - مثال: `if(random < 0.25) fire(A)` = 25%. و`if(random*100 > Resources) fire(Produce)` = احتمال عكسي لعدد الموارد (AP بيشغّل Produce بس لما «يحس» إنه محتاج).
  - جدول الـ operators (==, !=, <, >, +, −, *, /, %, &&, ||) = syntax. **متجاهل.**

### 8.3 جمع الداتا من runs متعددة
- **Quick Run:** تشغيل سريع من غير تفاعل. **لازم الـ diagram يكون فيه end condition قادر يوصله**، وإلا توقفه يدويًا.
- **Multiple Runs:** الافتراضي **100 run** (تتغير). لو run ماوصلش end condition بعد **10,000 time step** بيوقف تلقائيًا.
  - بيعدّ كام مرة اتوصل لكل end condition (لو كل لاعب له win condition → تعرف مين بيكسب أكتر). الأرقام اللي في الكتاب جاية من الميزة دي.
  - بيحسب **متوسط الزمن** لكل run → مفيد لمقارنة AP scripts: أي script بيوصل للنصر (غالبًا) **أسرع**.
- **Charts:** بتخزن داتا كل run. بتعرض آخر **25 run** افتراضيًا (لكن بتخزن أكتر وتتصفح بـ `<<` `>>`)، الـ run الحالي ساطع والباقي باهت (Fig 8.3 بيعرض run رقم 97)، تنضّفها بـ `clear`، وتصدّرها **CSV** (`export`) لـ spreadsheet أو برنامج إحصاء.

### 8.4 تصميم استراتيجيات الـ AP
- ★★★ **الـ AP مش بديل للاعبين حقيقيين ومش AI ذكي.** الهدف اختبار **استراتيجيات بسيطة** لنشوف الـ mechanics بتتصرف إزاي.
- **اصنع caricatures:** AP يمشي استراتيجية واحدة **بإصرار مهما كانت العواقب**. مثال RTS: كذا AP بيبنوا mixes مختلفة من الوحدات ويلعبوا ضد بعض.
- تقدر تبدّل بين APs (automatic/passive) أثناء الـ run.
- مفروض تلاقي **استراتيجيات صالحة كتير** للـ APs. لو لقيت AP **بيغلب باقي الـ APs (أو إنت) باستمرار → dominant strategy → غيّر الـ mechanics** عشان تقلل فعاليتها.
- ده بياخد محاولات كتير، وده طبيعي.
- ★★★ **تحذير ختامي:** لو بتصرف وقت كبير عشان تعمل AP يتحكم في الـ economy بنجاح → **الـ economy فيها مشكلة.** الـ AP مش مفروض يبقى ذكي كفاية يغلب لعبة ظالمة أو ضعيفة، وهدفه **يكشف** المشاكل مش يخبيها. ★★★ **«Tune your mechanics, not your artificial players.»**
- **Sidebar: Removing All Randomness** (لتحديد dominant strategy):
  - العشوائية تغطي على الـ pattern المسبب لـ dominant strategy، فشيلها.
  - احتمال بنسبة % → كسر ثابت (**20% → معدل 0.2 = واحد كل 5 steps، يعني اتنين كل 10**).
  - نطاق من نرد متعدد (مثل 3D6): توزيعه مش منتظم، فاستخدم **المتوسط**: **Average = (عدد أوجه النردة + 1) × عدد النردات ÷ 2**. مثال 3D6 = (6+1)×3÷2 = **10.5**.
  - في scripts الـ AP: استبدل `fireRandom` بـ sequential، واستبدل شروط `random` بـ `steps` والـ modulo (مثال: `if(random<0.3)` → `if(steps%10<3)`).
  - لو شيلت كل العشوائية (labels + scripts) هتاخد **نفس النتيجة كل run** = طريقة لمعرفة لو استراتيجية **متفوقة فعلًا** على أخرى.
- **Linking APs:** تقسيم script طويل على كذا AP يفعّل بعضهم (AP «builder» يحدد أحسن فعل بناء، AP «attacker» لأحسن فعل هجوم، وAP تالت `fireRandom(builder, attacker)` يختار بينهم).

### 8.5 مثال Monopoly (نموذج لاعبين اتنين)
- **اختلافات النموذج:**
  - لاعبين اتنين، ومكان source/drain للإيجار بقى **gates** بتنقل فلوس بين اللاعبين: كل عقار = **4% احتمال** كل step إن اللاعب التاني يدفع **وحدة فلوس واحدة**.
  - **20 عقار** فقط في pool Available، ولما تخلص مفيش شراء.
- **AP script (للاثنين):** كل step فيه **10% احتمال** يشتري، بس لو فلوسه > **4 + steps×0.04**.
  - **الباترن ورا الشرط:** الـ reserve بيكبر مع الوقت لأن كل ما اللاعب يمتلك عقارات أكتر، تزيد احتمالية إنه يدفع إيجارات متتالية، فيحتاج احتياطي أكبر. وده بيمنع الـ AP يفلس بدري.
- **التحليل:**
  - لاعبين متطابقين: الفلوس مستقرة ~**أول 90 step** وبعدين بتزيد تدريجيًا = أثر الـ positive feedback = **dynamic engine** (Fig 8.5/8.6).
  - **النسخة الـ deterministic:** الشراء كل 10 steps (`steps%10<1`). التريند واضح، واللاعبين متطابقين فخط واحد ظاهر (Fig 8.8).
- **تأثير الحظ:**
  - الأحمر يشتري كل **20 step** بدل 10، والـ reserve عنده 4+steps×0.02 → **نص فرص الشراء**.
  - الفلوس مش مختلفة أوي في الأول، **لكن العقارات هي المؤشر الحقيقي للقوة**.
  - **تأثير عشوائية كل mechanic على حدة:**
    - **زمن المرور على Go** (معدل 2/(3+D5) أي اتنين كل 4-8 turns): تأثير **صغير**، ومبيغيرش التريند. المرور على Go مش بيأثر في اللعبة بشكل كبير.
    - **عشوائية الإيجار:** تأثير **أكبر** لكن مبيكسرش التريند، وأحيانًا الأحمر بيبقى فلوسه أقل بكتير فيشتري أقل.
    - ★★ **عشوائية فرصة شراء العقار:** تأثير **أكبر بكتير**. بتغير **توزيع العقارات** بين اللاعبين، وده بيأثر على توزيع الفلوس. (الأزرق: random×10<1، والأحمر: random×20<1.)
  - كلها عشوائية مع بعض (Fig 8.13): الأرقام ضد الأحمر (نص الفرص)، والأحمر **نادرًا يفوز**.
- **توازن الإيجار والدخل:**
  - المشكلة: معظم الـ runs **اللعبة ماتنتهيش** لأن مفيش **rent inflation**. لاعب غني بالإيجار، لكن التاني يعوّض بالمرور على Go، فاللعبة تكمّل للأبد.
  - الحل: **بيوت وفنادق** (Fig 8.14) = استثمار يزوّد الإيجار.
  - AP الجديد: السطر التاني `if(Property > Houses/5 && Money > 6+steps×0.04) fire(Invest)`. الكتاب بيوصفه «لو عنده أكتر من 5 أضعاف العقارات مقارنة بالبيوت» (الصياغة الحرفية للشرط ممكن تتقرا عكس الوصف، لكن مش مؤثر على الدرس).
  - تجربة deterministic وزيادة دخل Go: **لاعب بيستثمر في بيوت (أزرق) بيكسب على اللي ما بيستثمرش (أحمر)**. وبدون خيار البيوت، الاتنين بيعملوا زيادة ثابتة متطابقة (الخط البنفسجي).
  - الـ balance اتغير بين **دخل Go** و**تكلفة الإيجار**: مبقاش ممكن تمر على Go كفاية تغطي الإيجار المتصاعد.
  - **1,000 run غير deterministic**، الاتنين بيستثمروا:
    - دخل Go = **5/(3+D5)**: حد بيكسب **~75%** من المرات (فرصة متساوية للاتنين)، و**25%** بتجر لحد ما الأداة توقفها.
    - دخل = **2/(3+D5)**: احتمال اللعبة تجر للأبد **صفر**.
    - دخل عالي + rent inflation **مضاعف**: احتمال الدخول في equilibrium **2%**.
- **إضافة Dynamic Friction (ضريبة عقارات):**
  - المشكلة: بعد rent inflation، **قوة العقارات زيادة**. أكتر مؤشر لمين هيكسب = مين عنده عقارات أكتر → الـ dynamic engine مسيطر زيادة.
  - الحل (من Appendix B): **dynamic friction**. ضريبة عقارات: كل **6 steps** بيخصم من فلوس اللاعب حسب عدد العقارات/البيوت، وبيبدأ بصفر، وبيزيد مع التجميع. (التمثيل: **6% لكل بيت و30% لكل عقار** في الـ diagram.)
  - **Table 8.2** (1000 run؛ الأزرق مبرمج يشتري **14** عقار، الأحمر **6**):

| معدل الضريبة (عقار/بيوت) | أزرق يفوز | أحمر يفوز | مفيش فائز |
|---|---|---|---|
| بدون ضرايب | 632 | 152 | 216 |
| 0.1/0.02 | 557 | 314 | 129 |
| 0.2/0.04 | 472 | 503 | 25 |
| 0.3/0.06 | 456 | 542 | 2 |

  - ★★ **الدروس:**
    1. ميزة الأزرق بتقل مع زيادة الضريبة.
    2. فوق حد معين الضرايب بتخلّي العقارات **عيب** والأزرق بيخسر أكتر مما يكسب (= dynamic friction بيكبح الـ positive feedback).
    3. ★ **الـ friction بيقلل «no winner»** (216 → 2) أي بيمنع **الجمود/stalemate**، وده خاصية مرغوبة.
  - الـ APs بيشتروا بأقرب فرصة، وده مش أحسن استراتيجية مع الضرايب (ممكن يلعبوا أحافظ).

### 8.6 مثال SimWar (Will Wright، GDC 2003)
- **لعبة نظرية minimal** (محدش بناها، بس معروفة): 3 وحدات فقط:
  - **factories** (تنتج الـ resource).
  - **defensive units** (ثابتة).
  - **offensive units** (الوحيدة المتحركة).
- الوحدات بتتبني بـ resource غير محدد من الـ factories. كل ما factories أكتر، resources أكتر.
- لما offensive unit تقابل defensive unit للعدو: **50% احتمال** إن واحد يدمر التاني، والعكس.
- **رهان Wright:** حتى الـ R

# Game Mechanics: Advanced Game Design (Adams & Dormans) — الجزء 5 من 8 — نوتس مذاكرة

**النطاق:** ص207–262. الجزء بيبدأ في نص الفصل 9 (قواعد setup بتاعة Lunar Colony)، وبيغطي الفصل 10 كله، وبيقف في الفصل 11 **في نص sidebar** «Storytelling: When progress as a journey still makes sense» (الجملة مقطوعة عند «even if they appreciate the context that the story pr…»). الباقي في الجزء 6.
**ملحوظات تقنية:**
- ص263 وص264 فيهم نفس محتوى Figures 11.1–11.3 مكرر (غالبًا خطأ extraction)، فاتسجل مرة واحدة.
- أشكال Machinations (9.10، 10.3–10.7، 11.13–11.15) اتسجلت بمعناها التصميمي.

---

## الفصل 9 (تكملة): Building Economies — Lunar Colony ★★★

### 9.أ. Setup وقواعد اللعبة (ص207–210)

**Setup:**
- كل لاعب بيرمي النرد ويحط tokens ice/ore على الترابيزة، واللاعبين بيتبادلوا لحد ما الكومتين يخلصوا.
- لو النرد أعلى من الباقي، بيتحط الباقي كله.
- مسموح تحط lodes جنب بعض.

**Starting colony:**
- كل لاعب بياخد 3 tokens بلونه، كل token بيمثل station.
- **واحد لازم يلمس ice lode واحد بالظبط، وواحد يلمس ore lode واحد بالظبط.** ده بيـ«claim» الـ lodes دي، ومحدش تاني يقدر يحط station لاصق فيها.
- التالت في أي مكان، حتى يـclaim lode تاني.
- لو مش لامس lode يبقى **way station**، وبيُستخدم لنقل ice/ore.
- النقل في الأول ما يزيدش عن **الضلع القصير لكارت لعب**، فالأحسن تفضل المحطات قريبة، والـ way stations بتقفل الفجوات الكبيرة.
- اللاعبين بيعملوا الـ setup بالدور.

**أنواع الـ stations** (stack من tokens بلون اللاعب، بيخزن ice وore):
- Ice mine: لامس ice lode.
- Ore mine: لامس ore lode.
- Way station: مش لامس أي lode.
- أي mine بيخلص الـ lode بتاعها بتتحول أوتوماتيك لـ way station.

**الأكشنات:**
- عدد الأكشنات في الدور = (عدد الـ stations ÷ 2) مقرّب لفوق. كل لاعب يبدأ بـ 3 stations يعني أكشنين في أول دور.
- الأكشنات المتاحة:
  1. Mine ice.
  2. Mine ore.
  3. Transport: token واحد بين محطتين في حدود الضلع القصير.
  4. Build new station: تشيل ore مخزنة وتتخلص منها، وتحط station جديدة جنب المحطة اللي جت منها، في حدود الضلع القصير.
  5. Expand: تشيل ice + ore (لازم من الاتنين) وتزود token للـ stack. الحجم = عدد الـ tokens.
  6. Produce energy: تشيل أي عدد ice من محطة، وكل ice بيدي energy بعدد = **حجم المحطة**. المثال: محطة حجمها 2 وشايل 3 ice = 6 energy. الـ energy مع اللاعب مش على الترابيزة.
  7. Research: تصرف energy تشتري technology.
- **كل station تتستخدم مرة واحدة بس في الدور** (mine/build/expand/produce energy). الـ transport والـ research مش بيستهلكوا station، وأي عدد موارد ممكن يتحرك من/إلى محطة وتفضل متاحة لأكشن تاني.

**Technology** (3 energy لكل واحدة، أكشن واحد، وبتتكتب على ورقة كـ public record):
- Fast Ice Mining: تاخد token ice اتنين بدل واحد.
- Efficient Ore Mining: مع كل ore بتمينها تاخد واحدة إضافية من unused tokens برّه الماب.
- Transportation Capacity: تنقل اتنين بدل واحد.
- Long Range Shuttles: تستخدم الضلع الطويل للنقل وللبناء.
- Luxurious Habitats: بتأثر في الـ score بس.

**الفوز:**
- اللعبة بتخلص لما أي لاعب يمين آخر ore أو آخر ice، بعد ما يكمل دوره.
- من غير Luxurious: نقطة لكل station حجمها ≥2.
- مع Luxurious: نقطة لكل expansion فوق 2 (حجم 3 = 2 نقطة، حجم 4 = 3 نقط).
- الأكتر نقط يكسب.

### 9.ب. Basic Economic Structure (ص211–212) ★★★

- **Mine Ice = gate** (Fast Ice Mining بتخليه يسحب 2). **Mine Ore = converter** (Efficient Ore Mining بتحوّل ore داخلة لاتنين، وده مش ممكن بـ gate).
- الموارد بتروح pool مشترك «Resources»: ore يبني stations، ice يعمل energy، الاتنين للـ expand.
- **توزيع الموارد على الترابيزة** اتحاكى بـ pools «Accessible Ice/Ore»: بناء station زيادة = **50%** فرصة تفتح ore أكتر و**25%** ice أكتر. النسب دي مأخوذة من كثافة الموارد في الـ setup.
- الـ register «Actions» في turn-based diagram بيغيّر عدد الأكشنات/دور، وهنا بيزيد مع عدد الـ stations.
- **الدياجرام ناقص عمدًا:** النقل، Transportation Capacity، Long-Range Shuttles. Luxurious Habitats مش محددة لأنها معتمدة على أحجام المحطات، وإنتاج الـ energy معتمد على الـ positioning وقرارات اللاعبين.
- **الباترنات:**
  1. **Dynamic engine**: ore/ice → stations + energy، والـ energy → تحسين إنتاج ore/ice (أسهل ما يتشاف في loop الـ ice).
  2. Dynamic engine تاني: ore → stations → أكشنات أكتر في الدور.
  3. **Engine-building**: اللاعب بيتحكم يحسّن أنهي جزء (أكشنات/دور ولا معدلات إنتاج).
- ★★ **ملاحظتين مهمين:**
  - **Positive feedback بس** وتفاعل مباشر قليل (مفيش هجوم أو سرقة).
  - الـ friction الأساسي = بناء way stations لو الموارد بعيدة، وده **static friction** (محدد بالـ setup مش بحالة الـ engine) وممكن يزيد كل ما الموارد الأخيرة تبعد.
- اللعبة متوازنة نسبيًا بين اللاعبين، **لكن اختيار starting position بيفرق جدًا**. اللي يختار أحسن مكان غالبًا يكسب، ودي نتيجة طبيعية لغياب negative feedback.
- **Design challenges:**
  - غيّر الـ end condition (تخلص لما كل الموارد تتشال أو تتستهلك؟ أول واحد يجمع 4–5 نقط؟ رقم أنسب؟ نوع تاني؟).
  - ضيف negative feedback (ابدأ من Appendix B).

### 9.ج. Building Blocks (ص213–216) ★★★

- النسخة الأولى فيها **building block واحد بس (stations)**. كل المحطات بتشتغل تقريبًا بنفس الطريقة، والقرارات الوحيدة: فين تحط، وأنهي تعمل expand (الأفضل القريبة من ice ثم ore). **بلوك واحد = تنوع بنية اقتصاد قليل = اختيارات مش مثيرة.**
- **النسخة 2:**
  - لونين tokens جداد (ice/ore متنقّى).
  - قاعدة الأكشنات اتغيّرت: كل لاعب يبدأ بـ **أكشنين**، وبيزيدوا بالـ transporters بدل عدد المحطات.
- **الأنواع الجديدة** (بتتحول من station حجمها 1 بس، وماتنفعش تتبني من الصفر أو في الأول):
  - **Purifier:**
    - محتاج ice واحد مخزن + **2 energy**، والـ ice بيتحط تحت المحطة كعلامة.
    - مبقاش يمين ولا يعمل energy ولا expand.
    - بأكشن واحد بيحوّل كل الـ ice المخزنة (أو اللي تحب) بـ **1 energy لكل ice**، ويستبدل كل ice باتنين purified من الاحتياطي برّه.
    - ما ينفعش تتنقّى تاني، ولا يفرق عن ice عادي في الاستخدام. **وظيفته بس تضاعف كمية الـ ice بصرف energy.**
  - **Refinery:** نفس الـ purifier على ore، لكن **2 energy لكل ore** عند التكرير (وبناؤه برضه 2 energy).
  - **Transporter:**
    - 2 energy، وبيتحط energy token تحته.
    - بيدي **+1 أكشن/دور لكل transporter**.
    - بيشحن أي أو كل tokens فيه لمحطة واحدة **في أي مكان على السطح** بـ 1 energy.
    - برضه مبقاش يمين ولا يعمل energy ولا expand.
- ★★ **Sidebar: ليه التكرير أغلى من التنقية؟** الـ Efficient Ore Mining بتضاعف الـ ore أصلًا، ومكن تمين **40 ore** في لعبة لاعبين، بينما ice الحد الأقصى **20** حتى مع Fast Ice Mining. فعشان **resource balance** أحسن تحفّز مضاعفة الـ ice مش الـ ore. **الباترن:** سعّر الـ converter عكس وفرة المورد وطاقة تضاعفه الموجودة أصلًا.
- نوتة prototype: الأحسن tokens بألوان قريبة (أبيض ice / رمادي purified)، وفي الـ playtests استخدموا **Post-its** على الـ tokens لأن مفيش ألوان تانية.
- **Challenges:**
  - أنسب عدد ice/ore ابتدائي لتجربة أطول (الـ purifier والـ refinery أصلًا بيطولوا اللعب).
  - Purifier وRefinery متشابهين جدًا، و**«في الألعاب الأفضل نفرّق وظائف العناصر»**. الخطر إن ice وore يحسّوا بنفس الإحساس، فاقترح قواعد بديلة متوازنة.
- ★★★ **تأثير التغييرات على البنية:**
  - اتشال الـ dynamic engine (أكشن لكل 2 محطة). النظام القديم كان فيه feedback كتير و**static friction** كتير (لازم تصرف ore على way stations)، والجديد (transporters) بيقلل الاتنين.
  - **دور الـ energy كبر:** converter engine (Fig 9.14): energy → ice أكتر (purify)، وice → energy أكتر. الـ purifier مجدي **بس لو الـ ice الواحد بيتحول لـ ≥2 energy**. وطلب الـ energy زاد كتير فيُنصح تزود توافره.
- ★ **Sidebar: More features, more upkeep:** الإضافات بتخلي اللعبة أبطأ وأتقل في bookkeeping. في prototype ما تقلقش، لأن الكمبيوتر بيحسبها في الفيديو جيم والـ board design بيساعد في البورد جيم.

### 9.د. Obstacles & Events (ص216–218) ★★

مرجع: Caesar III (مهمات بتجارب مختلفة بـ obstacles + scripted events).

**Obstacles:**
- أجزاء من السطح غير متاحة (كتب/أكواب/علب قبل الـ setup)، والموارد والمحطات على الترابيزة بس. ما يكفي من العوائق = تجربة مختلفة تمامًا.
- ورق فاضي = rough terrain: الموارد كلها لازم تتحط عليها، والمحطات فوقها ما تكبرش (أو ما تتحولش لـ purifier/refinery/transporter).
- المحطات نفسها كعائق (زي ألعاب بناء الاقتصاد): ما ينفعش refinery/purifier قريب من mines، لازم على بعد ضلع قصير على الأقل.

**Events** (كلها بتأثر على **كل اللاعبين** ولو مش بالتساوي، عشان الحظ ما يبقاش عامل كبير):
- **نرد في آخر الدور:** 5 = تحط 3 ice جداد من اللي برّه، كل واحد على lode مختلفة. 6 = كل اللاعبين ممكن يدفعوا 3 energy لنقطة إضافية في الآخر.
- **كروت مصنوعة:** تسحب في آخر الدور وتتخلص منها، وبعد ما الدك يخلص تخلط المتخلص. **التحكم في التوزيع أدق:** في 12 كارت، لو اتنين ice يبقى مضمون مرتين كل 12 دور.
- **كروت كسيناريو مكتوب:** ترتيب محدد يتحكم في إمتى إيه يحصل. مثلًا لو عرفوا إن بعد 10 أدوار في نقط على بيع ore يستعدوا لها. وده بيسمح بـ solitaire version لكن محتاج مصمم يجهّز البداية والترتيب.
- **Secret objectives** (مثلًا نقط لو خلصت بـ 5 energy أو بنيت station حجم 4): بتنوّر اللعبة وأحسن لما فيها تفاعل مباشر أكتر بين اللاعبين.
- **Challenges:** 3 طرق مختلفة للـ obstacles/events مع playtest لواحدة، وكمان نسخة single-player بسيناريو.

### 9.هـ. Additional Economic Strategies — Raiding (ص218–219) ★★★

- **المبدأ:** في ألعاب بناء الاقتصاد لازم يكون فيه **أكتر من استراتيجية اقتصادية viable**.
- Raiding بيتنفذ بـ **attrition pattern** لكن بالسرقة بدل التدمير.
- **خطر التوازن:** لو قوي زيادة يبقى **dominant strategy** (الكل يغير بس والباقي يبقى obsolete)، ولو ضعيف ما حدش هيستخدمه فملوش لازمة.
- **طريقتين للتوازن:**
  1. **فرّق الاستراتيجيتين في المخاطر والمكافآت** (زي SimWar في الفصل اللي قبله). هنا نزوّد مخاطرة الـ raiding.
  2. ★★ **ما تحاولش توازن اتنين، اعمل 3 استراتيجيات في rock-paper-scissors.** ده أثبت من توازن اتنين، لأن لو واحدة بانت أحسن أغلب الوقت اللاعبين يبدأوا يختاروا اللي بتغلبها، فالـ RPS **أقل تأثرًا بالاختلالات الصغيرة**.
- الكتاب اختار الطريقة الأولى، وخلّى الـ raiding **أكثر فعالية للي متأخر** (negative feedback loop إضافي بيخلّي اللعبة tight وممتعة).
- **الأكشنات الجديدة:**
  - **Build Raider:** 1 energy في أي station، والـ energy token بيتحط فوق المحطة كـ raider.
  - **Raid:**
    - الهدف أي station عدو في حدود الضلع الطويل.
    - ترمي نرد: لو **≤ عدد الموارد (ice+ore) المخزنة في محطة الهدف** يبقى نجاح، وتاخد token واحدة لمحطة الـ raider.
    - بعدين ترمي تاني: لو **≤ عدد الموارد في محطتك** الـ raider بيتدمّر.
    - الـ raider مرة واحدة في الدور، وممكن raids متعددة من نفس المحطة في أدوار متتالية.
  - **الباترن ورا القاعدة** (قراءتي للقاعدة): الرمية الأولى بتزيد احتمال نجاح الغارة على **المخزن الغني** (المتقدم بيبقى هدف أسهل)، والتانية بتزيد خطر الـ raider لو **محطتك أنت غنية**. فالاتنين بيدفعوا ناحية تقليل الفجوة، وده معنى «بيساعد اللي متأخر».
- **Challenges:** اختبر إن قواعد الـ raiders بتشتغل بالأثر المقصود، واعمل mechanics للدفاع ضد الغارات.

### 9.و. Summary وExercises

- الـ economy-building games بتديك building blocks (مباني/طرق) والاقتصاد بيتصمم بتاع اللاعب. Lunar Colony بتعمل «land rush» بـ blocks بسيطة.
- التقدم بيتبني بـ scripted events.
- **تمارين:**
  1. اعمل كل الـ design challenges.
  2. اعمل **automated model لنسخة single-player** تجمع إحصائيات وتظبط التوازن.
  3. اعمل paper prototype لـ economy game من عندك، وموديل Machinations ليه، وسيمولايت، وبلايتست مع ناس، وسجّل كل تغيير وليه.
- الفصل الجاي = progression مع level design وstorytelling.

**لموسفولك:**
- **Rival contests:**
  - مبدأ «الإيفنتس بتأثر على الكل» يتحول عندنا لـ **نفس seeded drop sequence للمتنافسين**، فالحظ ما يحسمش.
  - والـ raiding pattern (احتمال النجاح بيزيد مع تخزين الهدف، وخطر الفاعل بيزيد مع تخزينه هو) نموذج جاهز لـ **negative feedback** في أي مسابقة بين لاعبين.
  - وفي لعبة بتضم 3 استراتيجيات للـ contest حاول تبنيها كـ RPS بدل ما توازن اتنين.
- **المولد والتيستر:** درس 40 ore / 20 ice يتحول لسؤال: «كم أقصى عدد merges/نقاط ممكن في الليفل؟» وعلى أساسه نحدد الـ budget والـ goal. وكمان نشغل البوت لمعرفة هل الليفل فيه **positive feedback بس** (اللي بدأ كويس يكسب غالبًا). المفروض بوت-رانز تقيس الأثر ده.
- **Obstacles من 2501:** (mossy/stone/rot) = بالظبط obstacles/events بنوع «بتأثر على الكل». فكرة الكروت والـ distribution المتحكم فيها = **scripted drop decks** (12 كارت منها 2 فقط تدي X).
- **Secret objectives** = star goals اختيارية.
- **بروتوتايب ورقي بـ Post-its:** رخيص لتجربة side quests قبل الـ Unity.

---

## الفصل 10: Integrating Level Design and Mechanics ★★★

الفصل ده ومعاه الـ 11 بينقلوا التركيز من emergent mechanics لـ **mechanics كأداة progression design**: إزاي الليفلات بتنظّم التحديات في missions وتربط الـ story بتقدم اللاعب. ★ **«level design مش بس مساحات أو أدوات، الـ mechanics بتحدد إزاي الليفل بيقدّم التحدي».**

### 10.أ. From Toys to Playgrounds / Structuring Play

- بحسب Kyle Gabbler (ch.1 sidebar «Make the Toy First»): لحد دلوقتي بنينا toy، دلوقتي نبني **playground**.
- **Toy = play حر**، واللعبة = goal محدد (**victory condition**). ممكن بسيط (دمر كل السفن/اجمع نقط).
- **Space Invaders:** الهدف عمليًا مش قابل للتحقيق، موجات جديدة لحد ما تخسر آخر حياة. فالهدف الحقيقي = **تنجو وتجيب أعلى سكور**، والـ high-score table (تكتب initials) هي المكافأة المساندة للهدف ده.
- **Sidebar: Learning from real play spaces:**
  - المتنزهات بتغمرك في عالم خيالي وما بتضيّعكش. ★ **قلعة ديزني لاند** عالية ومرئية من كل مكان للـ orientation.
  - ★ ملاعب **mini golf**: 18 حفرة بصعوبة متزايدة (ركن بيرجّع الكورة، منحدر، نفق) وبعضها مبتكر. **تصميم حفر mini golf تمرين ممتاز لأي مصمم**.
- **ألعاب emergence:** أهداف بسيطة (اجمع نقط/اهزم وحدات)، والمهارة والاستراتيجية والخبرة هي اللي توصّل لحالة الفوز. مناسبة لـ **جلسات قصيرة متعددة** تتطور فيها مهارة اللاعب. والتعريف الدقيق للهدف بيفرق جدًا.
- ★★ **Sidebar Goals in Machinations Diagrams (مثال الـ harvester game):** هدف = عدد energy points بيحدد العدد المثالي للـ harvesters. لو غيّرت الهدف لـ «عدد harvesters» يتولد dynamic تاني: كل اللاعبين يبنوا harvesters بأسرع ما يمكن (**مش بالضرورة gameplay أحسن**). **الباترن: نوع الـ end condition بيعيد تشكيل الاستراتيجية المثلى.**
- ★ **Sidebar Playing vs Gaming: Paidia vs Ludus** (Roger Caillois، Man, Play, and Games 1958):
  - **Paidia** = اللعب الحر غير المنظّم (مرتبط بلعب الأطفال).
  - **Ludus** = السلوك المنظّم الموجه بهدف (مرتبط بالألعاب/الرياضة الأدلت).
  - الألعاب تقليديًا على طرف ludus، لكن بعضها (**RPGs**) بيقدم فرص paidia كتير في نفس الوقت.
  - الـ ludus مش بالضرورة أحسن، والتحدي التصميمي الكبير = **تقدم الشكلين في لعبة واحدة بنتيجة متناغمة**.
- **ألعاب progression:** أهداف بسيطة (لاقي الكنز، أنقذ Princess Peach «تاني»، اهزم الساحر)، لكن لازم تحقق **subgoals** كتير قبل المحاولة الأخيرة. الفعل الفاصل نفسه مش بالضرورة صعب.
- emergence وprogression مش حصريين (ch.2). ★ **الألعاب الطويلة محتاجة progression عشان تدي purpose وتنوع للـ gameplay.**

### 10.ب. Structuring Progress — أربع أنواع تقدم ★★★

**1. Progress through completing tasks:**
- مقاس بنسبة («خلصت 75% من اللعبة»)، لازم victory condition قابل للتحقق.
- فيه tasks اختيارية: النسبة نسبية لإجمالي المهام، والـ victory condition أقل من 100% أو معرّف بمهام محددة.
- أمثلة:
  - **Grand Theft Auto III** بتقيس التقدم بـ stunts وتحديات اختيارية كتير، وتخليك تكمل بعد «الفوز الاسمي».
  - ألعاب adventure الكلاسيكية (**Kings Quest، Leisure Suit Larry**) بتقيس بنقط تتجمع بأفعال معينة، وممكن تنتهي من غير كل النقط، واللاعبين بيعيدوها لهدف «كل النقط».
- القاعدة: **لازم تنويع كفاية، ما تصفش مهام متطابقة**، ومعدل pacing + difficulty curve مناسب.
- ★ **Sidebar: The aesthetics of shifting perspectives:** الناس بتحس بجمال في تحولات المنظور المفاجئة، زي تسلق جبل: غابة ومنظور محدود وبعدين فجأة القمة تنفتح وترى أميال. تغيّرات gameplay وبيئة موزونة تعمل نفس الأثر. **ولذلك الأحسن يكون فيه أنواع landscapes/backgrounds مختلفة في أقسام اللعبة.**

**2. Progress as distance to target:**
- الألعاب emergent ما فيهاش subgoals منفصلة، لكن victory condition رقمي. فنقيس القرب (مثال **Caesar III**: ابنِ مدينة لعدد سكان معين).
- ★★ **النسبة مش بتضمن إنك توصل في وقت ثابت:** ممكن تكون عند 90% من السكان المستهدفين لكن خلص مكان البناء أو مفيش food يكبّر المدينة، فتفضل بعيد عن الـ 10% الباقية.
- ★★★ **الفرق الجوهري: اللاعب ممكن يعاني setbacks.** في Caesar III البرابرة بيقتلوا سكان ومباني فيزيد البُعد عن الهدف. أما في adventure، لما المهمة تخلص ما تتلغيش أبدًا.
- مسار tasks = **predesigned** ولا بياخد في الحسبان مهارة اللاعب (ألعاب puzzle-adventure عادة من غير difficulty settings).
- التقدم في الأنظمة الـ emergent **بيتكيف مع الأداء طبيعيًا** لو الميكانيكس مظبوطة: استخدم **escalating challenge وescalating complexity patterns** (ch.7 وApp. B) عشان تتأقلم بسرعة.
- التنوع في الـ emergent بييجي من **phases** بتمر بها اللعبة من الميكانيكس نفسها (مثال The Shape of a Game of Chess، ch.4). وتستخدم **slow cycle pattern** تخلّي الـ phases تطلع.

**3. Progress as character growth:**
- RPGs (خصوصًا tabletop وMMORPGs من غير هدف نهائي): مقاسة بـ **character levels** من XP، وعادة **open-ended**.
- ممكن مسارات نمو متفرعة لو الاختيارات **mutually exclusive**.
- ★ **مثال Deus Ex:** augmentation canisters بتزود القدرات، كل canister بتديك اختيار بين عدة cybernetic enhancements، **كل اختيار بيتعرض مرة واحدة بس**، واللاعب بيقرر بين خيارات تدعم **أنماط لعب مختلفة**.
- بيتستخدم لهيكلة اللعب (مثلًا strength معين قبل منطقة).
- **لكن المصمم ما يتحكمش مباشر** في طريقة نمو اللاعب، فاللعبة لازم تدعم **طرق كتير توصل لنفس النقطة**. وأحيانًا نهايات مختلفة حسب نمو الشخصية.

**4. Progress as player growth (مهارة اللاعب):**
- **Zelda، Super Mario Bros.، Metroid Prime**: الـ avatar بيتقدم قليل (قدرات جديدة وحياة زيادة، من غير granularity الـ RPG). اللعبة **بتدرّب اللاعب** على استخدام القدرات بتحديات أصعب وأعقد.
- ★★ في كتير من الألعاب القدرات بتفتح مناطق، لكن **مهارة اللاعب هي اللي بتحدد هو يوصل ولا لأ**. **استخدم البيئة لقياس مهارة اللاعب.** الأطفال في الواقع بيمشوا على حيطان قصيرة ويقفزوا فوق أسوار ويتحدّوا نفسهم ما يدوسوش على شقوق الرصيف. ★ لما اللاعب يشوف **كوينة في مكان غريب** في لعبة platform، أغلب الناس هتفترض إن المصمم قصد إنها تتوصل وتحاول تعرف إزاي بقدرات الأفاتار ومهارتها. **غريزة استكشاف اللعب دي أداة تصميم.**

### 10.ج. Focusing on Different Structures in Your Mechanics ★★★

- اللعب الكبير بيقسم نفسه لـ **levels** لأن الميكانيكس معقدة أوي تترمي دفعة واحدة، خصوصًا مع لاعب مش عارف اللعبة، وده كمان بيدي تنوع ويجبر اللاعب يجرب استراتيجيات مختلفة.
- في بعض الألعاب **كل ليفل بيركز على جانب مختلف**، ودي محتاجة core ميكانيكس كبير كفاية فيه أكتر من structure بتولّد gameplay كفاية لحمل ليفل. الليفلات الأولى بتبرز **subsets** من الميكانيكس، والأخيرة ممكن تضم كلها.
- **Fig 10.1:** subsets مختلفة من اقتصاد Lunar Colony الأساسي بتعمل ليفلات مختلفة. ولأن الـ core صغير كل نسخة هتحس كمقدمة جديدة للاعب.
- ★★★ **StarCraft II:**
  - الاقتصاد واسع (حصاد موارد، بناء قاعدة، بحث تكنولوجي).
  - **الليفل 1: من غير بناء أصلًا**، بس إدارة وحدات القتال (حركة وقتال).
  - **الليفل 2:** مقدمة القاعدة والحصاد، وفيه مباني قليلة جدًا.
  - مباني وترقيات جديدة بتتفتح **بعد ليفلات معينة**.
  - **بعد أول 3 ليفلات اللاعب يختار الليفل الجاي** (يسعى لأهداف محددة).
- ★★★ **فرق StarCraft II عن الأصلي: مهمات كتير بتقدم mechanics خاصة بالمهمة** (اتذكرت في ch.2):
  - **«The Devil's Playground»:** المعادن بتتحصد بس من مناطق منخفضة بتتغمر دوريًا بلافا ساخنة، فلازم تنقل وحداتك لمكان آمن من وقت للتاني. ده بيضيف **slow cycle pattern** قوي لاقتصاد اللعبة الداخلي.
  - **«Outbreak»:** slow cycle تاني، الليل هجوم mutants جماعي على القاعدة، والنهار تروح تدمر المباني المصابة.
  - ليفلات تانية بتجبرك تحرك قاعدتك عبر الماب عشان تحمي/تهاجم قوافل دورية، أو تستولي بسرعة على أهداف.
- ★★★ **الخلاصة:** بتجيب **gameplay كتير من نفس الـ core** بـ: تغيير الأهداف، تعطيل mechanisms معينة، أو إضافة mechanism جديدة تشتغل في ليفل واحد بس. التغييرات دي بتجبر اللاعب على استكشاف استراتيجيات متنوعة (ما يقدرش يستخدم نفس الطريقة في كل ليفل).

### 10.د. Storytelling

- الستوري بتساعد في هيكلة الليفلات وتوجيه اللاعب، وبتدي **motive** لأهداف تانية مجردة. قتل الـ orcs بياخد دلالة عاطفية لما الستوري تقوله انتقام أو دفاع عن النفس.
- ★★ الستوري بتشتغل أحسن لما **الميكانيكس + هيكل الليفل + dramatic arc يترابطوا بسلاسة**. **مثال هيكل dungeon في Zelda:**
  - Link تقريبًا دايمًا بيحارب **mini-boss في منتصف الليفل** عشان يجيب **سلاح خاص** محتاجه لهزيمة الـ end boss.
  - **الفوائد:** فرصة كبيرة لاستكشاف ميكانيكس السلاح الجديد + تنويع بتقديم ميكانيكس في نص الـ dungeon + تقدم بفتح مناطق كانت مقفولة + **dramatic arc** مألوف (البطل يقاتل في سلسلة تحديات عشان ياخد الحافة).
- **أنواع الستوري:** linear (نفس الحاجة كل مرة)، branching (قرارات تأثر في اتجاه الحبكة بشكل كبير)، **emergent storytelling** = الستوري تطلع من الميكانيكس وأفعال اللاعب بس («الكأس المقدسة» للمصممين).
- ★ الـ emergent storytelling **intractable**: لأنه بيطلب توصيف المواقف الدرامية والسلوك البشري رقميًا/خوارزميًا، وده **أصعب من اقتصاد Civilization المعقد**. لسه بحث أكاديمي ونادرًا في ألعاب تجارية.

### 10.هـ. Missions and Game Spaces ★★★

**منظورين:**
1. **Challenges:** التحديات/المهام اللازمة لإكمال الليفل. وبحسب **Ernest Adams (Fundamentals of Game Design، ch.9)** التحديات **هرمية**: مجموعات قصيرة بتكوّن أكبر. أصغرها **atomic challenges** (لا تتجزأ)، مثال: توصيل لكمة في لعبة ملاكمة = atomic، وكسب مباراة = mission من كتير منها، وإنهاء اللعبة ممكن يطلب كسب عدة مباريات.
2. **Layout:** معمار الليفل ذاته (Adams ch.12). أمثلة: side-scrolling وHalf-Life شبه خطية، سباقات السيارات على مسار حلقي، وفضاءات FPS مالتي بلاير معقدة (مناطق مفتوحة ومحمية، أبواب تتحرس، نقط مراقبة عالية).

- **قوة كل منظور:** pacing وdifficulty curve أسهل تحت منظور المهام، و**storytelling والأجواء** أفهم من الـ spatial layout (لو الستوري رحلة).
- الكتاب هيستخدم **mission** (تسلسل المهام) و**game space** (التخطيط المكاني) منفصلين، ولو إن في المنتج النهائي لازم يتناغموا. ★ الفصل بينهم يوضح علاقتهم بالـ emergent gameplay.
- ★★★ **ممكن تعيد استخدام نفس المساحة لمهمات مختلفة** (مثال **GTA**): بيوفر وقت وفلوس لأنك مش بتعمل مساحة جديدة لكل ليفل، وفيه **فائدة gameplay**: اللاعب بيستفيد من معرفته المسبقة بالمساحة فبيزيد إحساس **السيطرة** مع كل مهمة بتعيد استخدامها.
- ★ **Sidebar: What if the dungeon is the mission?** في hack-and-slash tabletop:
  - الـ dungeon طريقة سريعة لعمل ليفل (الـ DM بيرسم متاهة على ورق graph ويرمي وحوش وكنز في الآخر وlandmarks عشوائية).
  - خريطة الـ dungeon تقريبًا flowchart للمهمة، فهيكل المساحة بيهيمن.
  - مناسب لنمط لعب معين (**Diablo** بتثبت إن فيه niche قابل للحياة).
  - **لكن:** تحكمك في الـ pacing قليل، والأكشن بيتكرر بسرعة. فلو عايز gameplay arc أعقد، **صمم الـ mission منفصل عن الـ space** واعمل بنية جيدة لكل واحد.
- المساحة لازم تستوعب المهمة، والمهمة المفروض توجه اللاعب في استكشاف المساحة.
- **ابدأ بتصميم الـ mission غالبًا** (أسهل في الكتابة والتنظيم وهيكلها بسيط)، لكن مش قاعدة مطلقة:
  - **الخطر:** ممكن تعمل مساحة خطية جدًا عشان تناسب المهمة وتشيل أي فرصة للاستكشاف لذاته.
  - في بعض الليفلات الأحسن تبدأ بمساحة جذابة (قلعة/محطة فضاء/موقع حقيقي مشهور) وتصمم مهمة تناسبها.

### 10.و. Mapping Mechanics to Missions ★★★

الميكانيكس بتحدد الأكشنز المتاحة، والأكشنز بتقترح tasks (لو ممكن تجمع ورد، المهمة: اجمع 10 ورود).

**إضافة تحديات (Fig 10.3–10.5):**
- **Fig 10.3:** مهمة «10 ورود» = **trivial وrepetitive**: اضغط الـ source 10 مرات، من غير اختيار ولا مهارة.
- **Fig 10.4 (إضافة أعداء):** اللاعب لازم يختار يركّز على تجنب الأعداء ولا جمع الورد. (في Machinations: synchronous mode وكل عنصر يتفعل مرة كل ثانية.) **تجنب الأعداء بيشيل 1–3 threat tokens عشوائيًا** (العشوائية بتمثل **تفاوت مهارة اللاعب**). صعوبته في **سرعته** (الـ pace العالي) مش في التفكير.
- **Fig 10.5 (تفاعل بين الميكانيكين):** كل وردة بتجمعها بتزود **معدل إنتاج التهديد**، فاللاعب لازم يصرف وقت أكتر في التجنب وهو بيتقدم للهدف. ده **منحنى صعوبة جيد: يبدأ سهل ويصعب بسرعة**.
- ★★ **Sidebar Speed vs Cognitive Effort (Chris Crawford، The Art of Computer Game Design 1984):** المهام (جمع/تجنب) بسيطة، لكن السرعة العالية بتخلّي إيجاد التوازن **تحدي فعلي**. **القاعدة: السرعة والجهد المعرفي لازم يتوازنوا:**
  - **ألعاب فيها جهد معرفي كبير → بطيئة (أو turn-based).**
  - **ألعاب جهدها المعرفي قليل → سريعة عشان تبقى مثيرة.**
  - جرّب تغيّر سرعة الدياجرام أو تحوله turn-based وتحس بالتوازن.
- **Design challenge:** Fig 10.5 بيطبق escalating challenge وقريب جدًا من escalating complexity. غيّره ليطبق الثانية وفكر إزاي تدخل الميكانيكس الجديدة في الـ fiction (عالم الورد والأعداء).

**إضافة subtasks (Fig 10.6):**
- نفس الهدف (10 ورود) لكن لازم تعمل **3 subtasks** تفتح كل الورد. كل subtask في الدياجرام مجرد gate، لكن ممكن يتحول لـ mechanism أعقد (مثلًا enemy-avoiding نفسه).
- ★ **للتنويع: اعمل subtasks بتقدم تجارب gameplay مختلفة**، يا لأنها بميكانيكس فريدة أو بتبرز structures مختلفة من الميكانيكس العامة.
- ★★★ **Sidebar: Avoid creating too many individual mechanisms:**
  - كل mechanism جديدة محتاجة تصميم واختبار، **وكلها لازم تكون ممتعة**.
  - ★★ **اللاعبين بيدركوا الليفل ممتع بقد أضعف mechanism فيه** (الناس بتتذكر التجارب السلبية أقوى من الإيجابية).
  - **الحل:** ابني core ميكانيكس متين الأول، وبعدين **zoom in على أجزاء من الهيكل ده كل task** (نفس نصيحة «ركّز على structure مختلف كل ليفل»).

**Dependencies (Fig 10.7):**
- معظم الألعاب ما بتتيحش كل tasks مرة واحدة، وبتخلق **dependencies**. **الميزة:** تتحكم في الـ pacing وتعمل difficulty curve (المهام الأصعب معتمدة على الأسهل).
- ممكن تنتج missions خطية تمامًا، لكن **اللاعبين بيقدروا حرية الفعل**. ولو التسلسل ثابت لازم على الأقل الأكشنز في كل subtask تسمح بخيارات، وإلا يبقى **gameplay = تعليم «✓» على خانات**.
- ★★★ **سؤال تقييم دايم: «كام خيار متاح للاعب في اللحظة؟»** الأكتر أحسن، بشرط ما تغرقوش بخيارات من غير data إزاي يختار.
- ★ **Sidebar: Linear missions in open game spaces:** مهمة خطية مش لازم مساحتها خطية، لكن لو كتير بتجبر اللاعب يجري رايح جاي في القلعة ده **backtracking** (محبط لو اتكرر). **مجرد فتح المساحة لإعطاء تنوع لمهمة خطية استراتيجية ضعيفة**، الأحسن تعيد تصميم المهمة لتجربة أقل خطية وتدي اللاعب أسباب حقيقية لاستكشاف القلعة.

**تقنيات متقدمة (أصعب في التصميم): optional وmutually exclusive tasks:**
- **Optional task:** فكر في **المكافأة**: بتأثر على الميكانيكس (سلاح أقوى) ولا مجرد eye-candy أو badge of honor؟ مكافأة بتأثر على gameplay بتغني اللعبة، **لكن حذار إن يكبر أثرها لدرجة إنها تبقى فعليًا شرط لإنهاء اللعبة**.
- **Mutually exclusive tasks:** مثال الحارس: تتسلل وتسرق المفتاح، أو تقاتل أو ترشي. لو حاولت ترشيه التسلل يبقى مستحيل (عرف إنك هناك)، ولو تسللت الرشوة تتلغي (شكوكه اتثارت).
  - ★★ **خطر:** ما تعملش وضع اللعبة فيه unsolvable، فهنا **القتال = backup strategy متاحة دايمًا**.

### 10.ز. Mapping Mechanics to Game Spaces

- Machinations ممكن تمثل المساحات: **pools = أماكن**، ومورد واحد = اللاعب بيتحرك بين الأماكن بالنقر (الـ pools بتسحب افتراضيًا، فلتحريك اللاعب تنقر على pool فاضية فتسحبه).
- Fig 10.8: لعبة خطية بسيطة بحركة في اتجاه واحد.
- **Fig 10.9 (مساحة لعبة جمع الورد):** اللاعب مورد أزرق والورد أحمر. وجود اللاعب في مكان معين بيتيح نقل الوردة لمخزونه بالنقر على gate مجاور. جمع **5 ورود** بيفتح المكان اللي لازم يوصله ليفوز.
- ★★ **وجود اللاعب في مكان بيفتح أكشنز** (استخدام شائع للمساحة)، وبيشتغل مع مورد واحد (شخصية) أو **عدة موارد (وحدات في RTS)**.
- **Fig 10.10:** حصاد المعادن في «The Devil's Playground» (StarCraft II) متضمن التدمير الدوري لكل الـ SCVs في المناطق المنخفضة. المسافات بين الـ pools في الدياجرام مش المسافات الفعلية، وتأثير SCV الأقل على معدل إنتاج الموارد على اليمين = **البعد الفعلي عن القاعدة**.
- **العكس كمان:** حالة الميكانيكس بتتحكم في إتاحة أماكن. الـ **lock-and-key** الأبسط = حالة binary (معاك المفتاح ولا لأ). Fig 10.11: مفتاح (أخضر) بيفتح وصول لورود زيادة.
- **Sidebar: Can you use Machinations as a level design tool?** مش اتصمم لتفاصيل الـ level design. بيشتغل أحسن مع تمثيلات بسيطة (حفنة pools)، مناسب جدًا لألعاب **point-and-click adventure**. مع تفصيل أكتر هتكرر ميكانيكس كتير، وتحريك وحدات حول الماب ضعيف. **لكن** مفيد لتجارب هياكل الليفل بسرعة (بيجبرك تركّز على البنية المجردة) وبيخلّي التفاعلات بين space/mission/mechanics مرئية.

### 10.ح. Learning to Play ★★★

- اللاعبين النهاردة **مش بيقروا manuals**، خصوصًا الـ **casual وmobile**. فلازم الليفلات تقدم الميكانيكس **بشكل تدريجي مفهوم** (approaches متوافقة اتنين).

**1) Skill Atoms (Daniel Cook، «The Chemistry of Game Design»، Gamasutra 2007):** كل ذرة = خطوة تعلم من 4 أحداث:
1. **Action:** ضغط زرار/حركة ماوس.
2. **Simulation:** اللعبة تطبق الميكانيكس وتغيّر حالتها.
3. **Feedback:** إزاي بتوصّل التغيير عبر الـ output (مش positive/negative feedback جوّا الميكانيكس).
4. **Modeling:** اللاعب يحدّث الـ mental model.

- **مثال Mario jump:** ضغط A → اللعبة تطبق قوة قفز وجاذبية → الشخصية تتحرك والأنيميشن يتغير وصوت قفز → اللاعب يتعلم إن A = يقفز.
- ★ الذرات **تعتمد على مهارات قبلها** (القفز قبل القفز على المنصات أو ضرب بلوك يكشف حاجات). بتكوّن **chains وtrees** (Fig 10.12 شجرة جزئية لـ Mario).
- ★★★ **عرض وعمق الشجرة:** wide = لازم يتعلم مهارات كتير مستقلة، deep = سلاسل طويلة معتمدة. **الأحسن deep مش wide على الأقل للمهارات المبكرة**، لأن:
  - **الـ secondary skills** (بتبني على مهارات تانية) بتتلقط بسهولة كإضافة على اللي عارفه.
  - **الـ primary skills** (بداية السلسلة) لازم تتعلم صراحة من غير خبرة سابقة (تعليمات داخل اللعبة أو تجريب أزرار عشوائي).
  - لو فات اللاعب primary skill (**ما دسش زرار الضرب أبدًا**) ممكن ما يعرفش إن الضرب خيار ويفوّت **فرع كامل من الشجرة**.
- الـ skill atoms مناسبة لأكشن مهاراتي وللاستراتيجي كمان (مثال turn-based: الفارس فعال ضد الرماة: أمر الفرسان بالهجوم → اللعبة تحسب فعالية الهجوم → أنيميشن وتأثيرات → اللاعب يحدّث الموديل).
- ★★ **Sidebar «Easy to learn but a lifetime to master»:** بنعلّم بعض المهارات صراحة (tutorials) وبعضها اللاعب بيتعلمها ضمنيًا. الشطرنج: عدد المهارات الصريحة **قليل جدًا** (حركات + castling + en passant + pawn promotion)، لكن المهارات الضمنية **ضخمة**. الألعاب ذات الخاصية دي عندها **skill trees deep مش wide**: مهارات أولية قليلة فمش محتاجة تعليم كتير، وسلاسل مهارات طويلة بتتعلم بالخبرة طول العمر.
- ★★ **Sidebar Hidden information in games:** لازم تفرّق بين وضوح **الحالة الكلية** ووضوح **لحظة تغيّر الحالة**. اللاعب محتاج يعرف **إمتى** بتحصل تغييرات عشان يتعلم الميكانيكس، واللعبة ممكن تخفي **الحالة الدقيقة**. ألعاب الكروت: بتشوف كام كارت اللاعبين بيسحبوا أو بيرموا، فتستنتج حاجة عن الحالة (توزيع الكروت وهل إيدك أحسن).

**2) Martial Arts Learning Principles (karate، belts/dan):** 4 مراحل متراكمة لكل «ليفل»:
- **Kihon (fundamentals):** يتعلم تكنيك واحد، والتركيز على إنه يطلع صح.
- **Kihon-kata:** تكرار لا نهائي لحد ما يتنفذ من غير تفكير (**Karate Kid: «wax on, wax off»**).
- **Kata (form):** يدمج تكنيكات في تسلسل choreographed ثابت.
- **Kumite (sparring):** يثبت إتقانه بقتال حر مع الأستاذ. في أول ليفلات الأستاذ يستخدم **subset بسيط ومتوقع**، ومع التقدم يستخدم هجمات أوسع **بشكل أقل توقعًا**.

**التطبيق على Super Mario Bros. وCrash Bandicoot:**
- **Kihon:** يتمرن على حركة جديدة (القفز) في بيئة آمنة نسبيًا، ولما يتعلمها يكمل.
- **Kihon-kata:** تتكرر في سلسلة قفزات بصعوبة متزايدة غالبًا، وبعد شوية اللاعب بيقفز من غير تفكير.
- **Kata:** تحديات بتحتاج **تركيبات حركات** (يقفز ويضرب في نفس الوقت)، وأنماط حركة الأعداء **deterministic ومتوقعة**: لما تلاقي التركيبة الصح هتنفع كل مرة (في المرحلة دي).
- **Kumite:** **boss encounter** = قتال حر بتركيبات الحركات، وسلوك الـ boss بيصعب التنبؤ بيه في آخر اللعبة وبيطلب إتقان أكبر.

**ربط التعلم بالـ mission structure:**
- كل مرحلة تعلم بتبقى **subtask (أو سلسلة)** لازم تخلصها عشان تكمل، فاللعبة بتركز على **اختبار قدرات اللاعب**. عشان تعدي kihon لازم تثبت إنك تقدر تقفز.
- الاختبار سهل التصميم: **تحدي لا يمكن تفاديه ويتطلب المهارة الصح.**
- المراحل الأولى: **بسيطة وآمنة لبناء ثقة اللاعب**، والمراحل المتأخرة تزود المخاطرة.
- **أفضل مع missions خطية** (أو على الأقل ما يقدرش اللاعب يواجه مهام المراحل المتأخرة قبل ما يخلص المبكرة).

★★★ **أمثلة Twilight Princess:**
- **Forest Temple** (Fig 10.13: مربعات = tasks وأسهم = dependencies):
  - في أول الليفل **bomblings** (مخلوقات صغيرة بتنفجر بعد ثواني من ما Link يلتقطها): أول task (kihon) استخدامها لتدمير نبتة آكلة لحوم كبيرة بتسد الغرفة الجاية.
  - يكرر حركات مشابهة كام مرة لتفجير الحيطان (kihon-kata).
  - لما ياخد **Gale Boomerang** يتعلم يستخدمه لقلب مفاتيح خاصة وجلب أشياء بعيدة في سلسلة اختبارات بسيطة (kihon وkihon-kata)، ويثبت إنه يقدر يوجّهه لتسلسل أهداف.
  - قرب النهاية: يستخدم البوميرانج لجلب bomblings بعيدة وإيصالها لنبتة تانية (**kata**).
  - ده يجهّزه لنفس التكنيك في هزيمة الـ level boss (**kumite**).
- **Goron Mines (الـ dungeon التاني):**
  - يجيب **Iron Boots** (حذاء بيخليه تقيل) ويبين طريقة استخدامه (**kihon**).
  - الـ dungeon يدرّبه على استخدامات: يغرق لقاع المياه، يمشي على صخور مغناطيسية رأسية أو مقلوبة، ويقاتل مخلوقات تقيلة وقوية (**kihon-kata**).
  - في نص الـ dungeon ياخد **hero's bow** ويستخدمه لفتح مسارات بإطلاق النار على أهداف (kihon وkihon-kata).
  - بعدها قتالات تتطلب **تبديل الحذاء بسرعة** ودمجه مع الرماية والسيف (**kata**).
  - الـ boss يتطلب دمج المهارات التلاتة (**kumite**).
- **البنية دي بتتكرر في كل dungeons Twilight Princess.** Fig 10.14 chart بيورّي الـ mechanisms المقدمة في كل dungeon وبين كل اتنين، واللعبة بتقدم mechanisms جديدة ببطء على مداها كله وتركز على **تركيبة مختلفة لكل ليفل**. ★ **chart زي ده يُستخدم للتخطيط لمراحل التعلم في لعبتك ولتحليل ألعاب منشورة.**

### 10.ط. Summary وExercises

- 4 قياسات للتقدم (مهام مكتملة، تقدم لهدف رقمي، نمو الشخصية، نمو مهارة اللاعب). استخدام subset من الميكانيكس لعمل ليفل. التفريق بين mission وlayout. Machinations لتصميم الاتنين. التعلم، وTwilight Princess كمثال.
- **تمارين:**
  1. خد دياجرام قديم، واعمل **3 ليفلات على الأقل بصعوبة تصاعدية** بحذف أجزاء وتغيير end conditions.
  2. حلل **Knytt Stories** أو **Robot Wants Kitty**: هيكل الليفلات، التدريب، الفرق بين mission وgame space، المهارات المتعلمة وإزاي بتترابط.

**لموسفولك:**
- ★★★ **الـ jar = game space ثابت، والـ goal + drop budget = mission.** (نفس منطق GTA في إعادة استخدام المساحة.) فكل فايدة من «اللاعب يعرف المساحة ويحس بالسيطرة» بتشتغل عندنا بالفطرة. وحاجة نلاحظها: بما إن المساحة ثابتة، تنويع الإحساس لازم ييجي من **الـ mission + الـ mechanic subset**.
- ★★★ **الـ obstacles من 2501** (mossy shells/stones/rot) **تتقدم بسلسلة kihon → kihon-kata → kata → kumite:**
  - ليفل «آمن» يعرّف العائق (kihon).
  - كام ليفل تكرار بصعوبة تصاعدية (kihon-kata).
  - ليفل بتركيبة عائقين أو عائق + goal معين، بمصادر عشوائية قليلة (kata).
  - ليفل ذروة (kumite).
  - نقيس كل خطوة بـ `bot_difficulty` ونتأكد إن المنحنى بيصعد وما فيهوش قفزة. بالإضافة لعمل **chart زي Fig 10.14** يوزّع إدخال العناصر الجديدة على الـ 3000 ليفل.
- **Skill atoms لكل عنصر جديد:** action (إسقاط) → simulation (فيزياء/merge) → feedback (صوت/أنيميشن/اهتزاز) → modeling (فهم القاعدة). ولو الـ feedback غامض يبقى الـ atom فاشل. وعندنا skill tree **deep مش wide** (primary skills: drop وmerge، والباقي secondary) وده الشكل المثالي حسب الكتاب، فخلي أي عائق جديد **secondary يبني على اللي معروف** مش primary جديد.
- ★★ **Crawford:** الميكانيكس عندنا لعب فيزيائي سريع/جهد معرفي قليل، فالـ pace السريع مناسب، لكن **ليفلات فيها تخطيط ثقيل (budget ضيق)** محتاجة وقت/pacing أبطأ (مفيش timer).
- ★★ **قاعدة «ممتع بقد أضعف mechanism»:** تتطبق على الـ **minigames في الـ side quests**. كل minigame ضعيفة بتضرب تصور الـ quest كله، فنكتفي بـ **core متين ونعمل minigames كـ zoom على أجزائه** مش mechanics جديدة كل مرة.
- **Optional/mutually exclusive:** أي optional task في الـ side quests مكافأته تأثر على الـ gameplay **لكن مش شرط** للنهاية. وأي خيار حصري لازم يبقى فيه **backup strategy** (مفيش unsolvable).
- **تعريف الـ goal بيحدد الاستراتيجية** (harvester sidebar): كل ما نغيّر نوع هدف ليفل (نقاط ولا عدد merges ولا إخلاء) نختبر بالبوت إن الاستراتيجية المثلى لسه ممتعة.
- ★ **Progress as distance to target مع setbacks:** goal مع **نكسات** (البرطمان بيمتلئ) = progress نوعه 2. فنقيس «% الهدف» **ونفتكر إن 90% مش معناها قريب** (مفيش مساحة). ده مهم لأي progress bar أو إعلان «انتبه، إنت قريب» (مثلًا كان ممكن تتعرض rewarded ad عند «قريب» لما الحقيقة بعيد).
- **Backtracking/shifting perspectives:** تنوّع خلفيات/بيئات البرطمان بين الأقسام (Landscape sidebar) بتدي نفس الأثر.

---

## الفصل 11: Progression Mechanisms ★★★ (جزء — الفصل مقطوع عند sidebar الستوري)

**الهدف:** إيجاد mechanisms تقدم **أكتر emergent** من اللي بتستخدمه الألعاب التجارية، بمدخلين:
1. نص أول: lock-

# Game Mechanics: Advanced Game Design (Adams & Dormans) — الجزء 6 من 8 — نوتس مذاكرة

**الحدود:** الجزء ده بيبدأ في نص Chapter 11 «Progression Mechanisms» (من آخر قسم الـ emergent storytelling، ص 262 تقريبًا). بعده Chapter 12 «Meaningful Mechanics» كاملًا (ص 271–299). بعده Appendix A (Machinations Quick Reference) وبداية Appendix B (Design Pattern Library: Static Engine وDynamic Engine وأول Converter Engine). **القطع في الآخر** جاي في نص Converter Engine عند «It increases the difficulty of the g…»، وباقيه في الجزء 7.

ترقيم الفصول مكمّل من السياق: ده فصل 11 (آخره) + فصل 12 (الأخير في الكتاب) + الملحقين.

ملحوظة: ما فيش «شرح برمجة» في الجزء ده. أقسام الـ implementation في Appendix B تصميمية (تنويع معدلات الإنتاج) فاتسجلت كاملة.

---

## الفصل 11 (آخره): Progression Mechanisms

### 11.أ Emergent Storytelling (آخر القسم) ★

- **التعريف:** مجال بحثي بيحاول يحل التناقض بين تجربة الـ gameplay التقليدية وتجربة الـ story التقليدية. اللعبة الافتراضية تستخدم emergent mechanics للـ gameplay، وemergent progression system يولّد أحداث بلوت مثيرة درامية من غير مؤلف.
- **الشرط الصعب:** تضمن إن التجربة تحس «storylike» فعلًا، من غير 4 حاجات: **تكرار، عشوائية، رجوع في الزمن (reversals in time)، شخصيات غير مقنعة**.
- **المحاولات:** بتستخدم AI يبحث في الأحداث المستقبلية المحتملة للبلوت زي برنامج الشطرنج ما بيبحث في النقلات. بدل ما يدوّر على كش مات، بيدوّر على بلوت ممتع.
- **الحقيقة:** لحد دلوقتي **محدش نجح يبني emergent storytelling بحجم لعبة كاملة**. كل المحاولات prototypes صغيرة.
- **لموسفولك:** القصة والـ side quests نفضل نكتبها authored. ما نبنيش عليها نظام مولّد. الأولى نستعمل الـ emergence في الـ gameplay نفسه (physics merge) ونسيب البلوت للكتابة اليدوية.

### 11.ب Producing Progress Indirectly ★★★

- **التعريف:** خطوة زيادة على «progress as resource». اللاعب بيولّد التقدم **بشكل غير مباشر** والتقدم بيتقاس على **أكتر من resource**. مفيش action واحد بينتج progress، العملية فيها خطوات متعددة وresources متعددة. الباترن شائع في **open-ended simulation games**.
- **Elite (space trading classic):**
  - اللاعب بيسافر بالسفن ويتاجر في مجرة كبيرة. ألهم Privateer series وMMO **Eve Online**.
  - أغلب الفلوس بتتستثمر تاني في السفينة. سفينة أحسن توصّلك لأماكن أبعد وأخطر وأربح.
  - **التقدم = جودة وسعة السفينة** (مجموعة resources ملموسة).
  - اللعبة open-ended، لكن أغلب اللاعبين بيختاروا نفس الهدف: سفينة قوية وثروة.
  - ★ **ممكن تخسر progress:** السفينة تتدمر، تضرب صواريخ غالية ضد القراصنة، أو تستخدم intergalactic hyperdrive بيتصرف مرة واحدة. ده نادر في games اللي progress فيها رحلة (journey) لكن عادي في الـ simulation.
- **The Settlers of Catan:**
  - الهدف **10 نقاط**. النقاط من: بناء villages، ترقية village لـ city، أطول road، أكتر knights، حظ في شراء development cards.
  - كل الـ point-scoring mechanics **مترابطة**: مش تقدر تبني village وتاخد نقطة وقت ما تحب. لازم roads لمواقع مناسبة وresources صح.
  - بناء الـ village مش نهاية العملية: بيزوّد فرصة الحصول على resources، والـ city بتضاعف الـ output.
  - الـ economy (Figure 11.20): turn-based، 5 resources بألوان. كل village وcity بتدّي فرصة إنتاج resource كل turn، وكل city بتزوّد فرصة إن الإنتاج يتضاعف.
  - **التركيبة:** dynamic engine + engine building pattern + trade pattern.
  - ★★ **إزاي تهرب من gameplay signature الـ dynamic engine** (التراكم البسيط للـ resources): بوجود **عدة invest options** وكلها **بتضيف للـ progress**.
  - ★★ **أثر جانبي لقياس التقدم غير المباشر: اللاعب مش بيعرف يقرا حالة اللعبة بسهولة.**
    - تشوف عدد cities وvillages وresources بسهولة، لكن بسبب حساب النقاط غير المباشر صعب تعرف مين أقرب للفوز.
    - عدد مواقع البناء محدود: ممكن تحتاج village واحد زيادة لنقطة، بس كل المواقع اتاخدت.
    - الـ city محتاجة ore وwheat كتير ممكن مش سهل الحصول عليهم. يعني «قريب» ممكن يبقى بعيد.
    - **طبيعة** trade goods كل لاعب مخفية (مش عددها)، والـ dynamic engine بيعتمد على عشوائية.
    - **للمقارنة:** في Monopoly واضح لأن كل الممتلكات مكشوفة.
  - ★★ **ميزة القياس غير المباشر: أكتر من طريقة فوز.**
    - مسار آمن: villages وcities كتير، محتاج resources كتير.
    - مسار high-risk high-reward: development cards، مناسب لما resources قليلة.
- **The Sims:**
  - اللاعب بيتحكم في sims في «dollhouse» افتراضي. النجاح بيتقاس بالممتلكات المادية (أثاث وfeatures البيت) **و**التقدم المهني للـ sims.
  - هي time-management game: وقت محدود لكل الأنشطة اللازمة لسعادة وصحة الـ sims.
  - السلسلة: رعاية كويسة ← وظيفة ← وصول في الميعاد بصحة ومزاج كويسين ← ترقية ← فلوس أكتر ← أغراض للتسلية وروتين أكفأ.
  - اللعبة ما بتقولش إن الهدف نجاح مادي ومهني، لكنه **ضمني في الـ mechanics** وناس كتير بتلعبها كده.
  - ملحوظة: اتنقدت إنها materialistic جدًا (مفيش حياة روحية والسعادة من الأثاث الفخم). وصف الأثاث الساخر في اللعبة بيوضح إن المطورين واعيين، يعني **الـ game satire**.
- **الباترن ورا التاكتيك:** التقدم غير المباشر بيقاوم الـ dominant-strategy وبيخلق multiple win paths، وبيدفع ثمنه في readability (مين كسبان؟). ده trade-off مقصود.
- **لموسفولك:** الـ rival contests والـ side quests ممكن تقيس التقدم على أكتر من resource بدل score واحد. لكن عندنا الـ merge puzzle readability عالية، فالـ readability loss هنا تقيل. نحسبه قبل ما ناخد الباترن.

### 11.ج Emergent Progress and Gameplay Phases ★★★

- **المشكلة:** الـ level design التقليدي بيتحكم في الـ pacing والتنوع بتشكيل المساحة. لما التقدم emergent property للـ mechanics، مفيش تحكم مباشر كده. الـ pacing والـ variation لازم **يجوا من مراحل (phases)**.
- **Gameplay phase:** فترة زمنية الـ dynamic behavior بتاعها بيتبع pattern معين. لما فيه **تغيير significant** في الـ dynamic behavior، اللعبة تنتقل لـ phase جديدة.
- **مثال RTS (Figure 11.22):**
  1. **Building phase:** حصاد resources وبناء base، تراكم سريع واستثمار في دفاعات ووحدات. اللاعب بيصرف resources بسرعة وـ production rate بيكبر بسرعة.
  2. **Exploration phase:** قوة هجومية لاستكشاف الماب، السيطرة على نقاط استراتيجية، تأمين resources مستقبلية. الـ resources **بتتراكم** لأن التركيز في حتة تانية.
  3. **Offensive phase:** هجوم ضخم. الـ resources **بتطلع وتنزل** وهو بيبدّل بين البناء وموجات الهجوم.
- المراحل دي مش لازم تحصل، وممكن تيجي بترتيب مختلف:
  - **Rush strategy** (من «Balancing SimWar» في Chapter 8): building قصير جدًا ويتخطى exploration ويهاجم فورًا.
  - مراحل تانية: **consolidation** متخللة بين exploration phases (لما resources مبعثرة)، وبعد أول offensive لو فيه أكتر من enemy base.
  - **Research phase** في games الـ technology tree: لا هجوم ولا بناء، الاستثمار في ترقيات الوحدات والمباني.
- **Sidebar: Phase transitions & Complexity Theory ★:**
  - في علم التعقيد، الانتقال بين stable states متعددة موضوع بحث مهم. مثال: زحمة المرور، فيه حالتين رئيسيتين (normal flow وtraffic jam) وبينهم حالات وسيطة.
  - تشبيه بالتحول بين solid/fluid/gas: تسخّن المياه ومفيش حاجة تحصل لحد نقطة الغليان فتتحول فجأة.
  - الطريق: تزوّد «traffic pressure» والسرعة طبيعية لفترة، وفجأة تنهار. **الرجوع للحالة الحرة محتاج تقليل الضغط لمستوى أقل بكتير من نقطة بداية الزحمة.**
  - ★ **Asymmetry rule:** الـ asymmetry الكبير بين التغيير في اتجاهين = phases أكتر استقرارًا. الـ asymmetry الصغير = النظام يتذبذب بين الـ phases بسهولة.
- **لموسفولك:** الجرّة نفسها لها phases طبيعية: **فاضية ← مزدحمة ← على حافة الامتلاء**. التيستر-بوت يقدر يرسم رقم الـ jar fill/تعقيد الكتل على زمن الليفل ونشوف الـ phases ونقيس طولها.

### 11.د Composing Gameplay Phases ★★★

- **التاكتيك:** وإنت بتصمم level فيه emergent phases، دورك **تركّب تجربة مرغوبة** منها.
- **مثال:** عايز تبرز الـ building phase الأولى في RTS level: بتضايق اللاعب بدري بمجموعات أعداء صغيرة بتهاجم كتير. ده بيجبر اللاعب يوازن بين زيادة الـ production وبناء الدفاع، وبيبطّئ الـ production كتير، فالـ building phase بتطول. عايز exploration وconsolidation phases كتير: ماب بـ resources **نادرة ومبعثرة**.
- **Sidebar Scripting vs Emergence ★★:**
  - تقدر تسيب كل الـ phases تطلع طبيعي، لكن في حالات كتير أنجح تفرض كام تغيير بـ deterministic أو dynamic scripts.
  - **StarCraft campaign:** المصممين خططوا لموجات هجوم من الـ AI. بعضها في وقت ثابت، وبعضها بيتفعل لما اللاعب يوصل نقاط معينة في الماب.
  - **القاعدة:** حتى لو بتستهدف gameplay emergent، متخافش تخلط **forms of progression مباشرة**. لو اتعملت بخفة تطلع لعبة/ليفل dynamic جدًا بتنوّع كبير وreplay value عالية.
- **أربع patterns بتصنع events كبيرة تنقل اللعبة لـ phase جديدة** (لأن اللاعب بيستقر في إيقاع جوه الـ phase):
  1. **Slow cycle:**
     - اتشرح في الفصل 10 في StarCraft II لتحويل اللعبة بين phases دفاعية وهجومية.
     - فعال لكن **ناقص subtlety** خصوصًا لو اللاعب تأثيره قليل على الـ cycle. وأحداثه أقل دراما من التلاتة التانيين.
     - تشبيه: **King Canute** وهو بيوضح حدود سلطة الملك بإنه ما قدرش يمنع المد (slow cycle كلاسيكي).
  2. **Static friction / static engines:**
     - **Static friction نادرة بتأثير عالٍ** تسبب phase shift. مثال **Caesar III**: غزاة دوريين + طلبات دورية من الإمبراطور لسلع تجارية. لأن الاقتصاد حساس، الأحداث دي ممكن تدخله في **decline phase**: فقد الوصول لـ resources ← المواطنين بيغادروا ← قوة العمل بتقل ← الإنتاج بيقل.
     - **العكس: static engine بتنتج resources كتير نادرًا** = انتقال من scarcity لـ abundance. مثال Caesar III: وصول **قوافل تجارية** من مدن مجاورة.
  3. **Escalating complexity:**
     - يعتمد على انتقال بين phase تحت السيطرة وphase خسارة. طول ما اللاعب بيواكب معدل توليد التعقيد، الوضع تحت السيطرة. أول ما السرعة تعدّي threshold، الـ **positive feedback** بيدفع اللعبة لنهاية سريعة: **losing phase قصيرة** بتحصل فيها reverses.
     - **Tetris:** غالب الوقت اللاعب متحكم، وأول ما الكتل تنزل أسرع من قدرته يبدأ الـ losing phase. توليد التعقيد فيه **random factor** (نوع الكتلة)، فبشوية حظ ومجهود اللاعب يقدر يرجّع اللعبة من الـ losing phase للـ normal.
  4. **Stopping mechanism / multiple feedback:**
     - لو الـ phase بتعتمد على action معين، تخلّي الـ action ده **أقل فعالية كل ما اتستخدم أكتر**. فالـ phase ما تدومش للأبد وتحصل shift.
     - **The Seven Cities of Gold:** «Amaze the natives» بتتجنب الصراع مع السكان الأصليين. بتشتغل كويس أول، وبتقل فعاليتها بمرور الوقت، فاللاعب لازم يستعمل استراتيجيات تانية. كده فيه phase shift.
     - الـ stopping mechanism عادة **خفي**. لو أثره ما دامش ممكن اللعبة ترجع للـ phase القديمة. أي شكل بطيء وخفي من multiple feedback بيعمل نفس الأثر.
- **Design Challenge (من الكتاب):** إيه الـ mechanisms/patterns التانية اللي بتخلق gameplay shifts في Caesar III أو StarCraft II؟ اللستة مش شاملة.
- **الخلاصة ★★:**
  - progression عبر emergent phases صعب التحكم. لكن بتوليد mechanisms **على الأرجح** تعمل phase shifts تقدر **تتنبأ بنوع الـ phase progression**.
  - مثال Tetris: ما تعرفش إمتى بالظبط الـ losing phase، لكن لأن واحد من أسبابها (drop rate) بيزيد ببطء، تعرف إنها هتحصل.
  - بالخبرة بتقدر تبني emergent progression ما بيعتمدش على scripted events.
- **لموسفولك:**
  - **Escalating complexity = جرّة Mossfolk بالظبط:** كل ما الجرّة تتملى، الـ positive feedback بيسرّع الخسارة (مفيش مكان لإسقاط تاني). والـ random factor (المخلوق اللي هيجي) هو اللي بيدّي فرصة للتعافي.
  - الـ **drop budget** والـ **mossy shells/stones/rot** (من 2501) تقدر نعتبرهم phase-shift events: static friction نادرة بتأثير عالٍ، أو stopping mechanism.
  - تيستر-بوت: نصنف أي ليفل بالـ phases بتاعته. **bot_difficulty** ممكن يتفسّر كـ «إمتى تحصل نقطة الانهيار وهل بتتعافى».
  - **Scripting vs emergence:** الـ scripted drops/events في ليفلات الـ rival contests مقبولة طالما بخفة (زي attack waves في StarCraft).

### ملخص فصل 11 والتمارين

- **الملخص:**
  - النص الأول: lock-and-key التقليدي ممكن يتوسّع بـ dynamic systems كـ keys تفتح مناطق أو features.
  - النص التاني: خلي progression **emergent property** مش مجرد موقع اللاعب في المساحة. تعامل مع progress كـ resource أو قيمة محسوبة من عوامل، وتقدر تكسر progress لـ phases بـ slow cycle وpatterns تانية.
  - الفصل الجاي: استخدام الـ mechanics لتوصيل رسالة.
- **التمارين (4):**
  1. لقيت lock-and-key في تصميماتك. من غير mechanisms جديدة، 3 locks مختلفة لنفس الـ key.
  2. اختار 2 patterns من Appendix B واعمل dynamic lock-and-key. ينفع يبقى هيكل ليفل كامل؟
  3. لعبة emergence ليها عدد واضح من الـ phases: إيه الـ mechanisms اللي بتثبّت الـ phase وإيه اللي بتنقل؟
  4. أي patterns تعمل emergent gameplay phases في لعبة Lunar Colony (من Chapter 9)؟
- **لموسفولك:** التمرين 1 و3 ينفعوا نطبقهم على Mossfolk مباشرة: ليفل بهدف واحد (key) بـ 3 locks (stones، shells، rot).

---

## الفصل 12: Meaningful Mechanics (الفصل الأخير)

**الهدف المعلن:** إزاي نعمل mechanics ليها معنى. الترتيب: serious games ← communication theory وsemiotics ← multiple layers of meaning وintertextual irony. حتى لو بتعمل entertainment، تقدر تطبق عشان تعمل لعبة ليها رسالة.

### 12.أ Serious Games ★★

- **اللعب والتعلم تاريخ مشترك:** البشر وحيوانات كتير بتلعب عشان تتحضّر للمهام الجدية. Hide-and-seek بيمرّن مهارات الصيادين، وplaying house وpedal cars للأنشطة المستقبلية.
- **Raph Koster, A Theory of Fun for Game Design (2005):** أي لعبة، التعلم والإتقان هو اللي بيطلّع الفن. التعلم المستمر: الأهداف، الحركات، الاستراتيجيات. حتى الـ abstract زي Tetris. **تقييم المؤلفين:** مبالغ فيه شوية (فيه مصادر fun تانية: اجتماعي وجمالي) لكن جوهره صح: gameplay = learning في صورة ممتعة.
- **Sidebar: Gamer Generation (Beck & Wade, The Kids Are Alright, 2006):** جيل الألعاب له موقف مختلف من الشغل. بيشوف الفشل كـ **temporary setback** مش كارثة (حياة من محاولات فاشلة وrestore). في الألعاب **كل مشكلة ليها حل** وفيه ثقة ضمنية إن اللعبة fair. ده بيدّي **can-do mentality** حتى لو الحياة مش fair زي الألعاب.
- **تعريف serious game:** مفيش تعريف قياسي. **Ben Sawyer: «Serious games solve problems.»** مصممة لتحقيق **real-world effect**. كتير منها بيستغل انفتاح اللاعب للتعلم. وبتسمح بتجريب approaches **بأمان ورخص وبدون عواقب**.
- **ألعاب مبكرة:**
  - **Monopoly ← The Landlord's Game (1904، Elizabeth Magie):** صُممت لتوضح عواقب اقتصاد رأسمالي غير مقيّد (ملاك العقارات بيغتنوا والمستأجرين بيفتقروا). اسم Monopoly **انعكاس ساخر** للرسالة الأصلية. وده يفسر **شرط الفوز: إفلاس الباقين** مش أكبر ثروة.
  - **Kriegsspiel (1812، Lt. Georg Leopold von Reiswitz):** طوّره هو وابنه لتدريب ضباط بروسيا. قطع خشب ملونة على خريطة، قواعد حركة، **dice** للنيران والاشتباك القريب. ثورة في تدريب الضباط، **حسّنت المهارات الاستراتيجية رغم القواعد البسيطة**. فرصة تجرّب استراتيجيات بدون عواقب وتحط نفسك مكان الخصم. بعد حملات ناجحة في القرن 19 تبنتها دول أوروبا وغيرها.
  - **Sidebar Taking Games Seriously ★:** بعض الدول لم تأخذ war games بجدية (إزاي dice تمثل فوضى القتال؟). **Admiral Chester Nimitz (1960):** الصراع مع اليابان في الحرب العالمية الثانية اتجرّب في war games لدرجة إن الحدث الوحيد غير المتوقع كان الـ **kamikaze**. **الروس تجاهلوا نتائج war games** في أوائل الحرب العالمية الأولى فخسروا كارثيًا في **Battle of Tannenberg**. ★ **الدرس:** قواعد بسيطة وغير واقعية ممكن تلتقط جوهر الموقف الحقيقي وتبقى أداة تعلم ممتازة.
- **Serious video games:**
  - من الثمانينات كأدوات تعليمية. اللي سبق: كتير **خيّب الأمل** بسبب التسرع، ومصطلح **edutainment** اتجنب. معظمها كان **multiple-choice tests متنكرة** = gameplay مقيّد ممل (استثناء: **Oregon Trail**).
  - الحديثة أحسن: بتدمج الـ gameplay مع الموضوع وبتستخدم **emergent mechanics لتعليم مبادئ مش حقائق بس** (مثال: **Refraction** يعلّم الكسور).
  - أكتر من تعليم: **advergames** (إعلانات)، ألعاب حملات سياسية، ألعاب أخبار كبديل الكاريكاتير، علاج نفسي وجسدي وتدريب جراحين.
  - ★ **تحدي:** توصيل رسالة في لعبة emergent حرة صعب، لكن ممكن. أمثلة تجارية استخدمت تعليميًا: **SimCity، Civilization** (جغرافيا اجتماعية وتاريخ سياسي). **Balance of Power** استخدمتها وزارة الخارجية الأمريكية في الثمانينات لتدريب دبلوماسيين (صراع أمريكا والسوفيت).
- **Sidebar Gamification:**
  - تطبيق mechanics على أنشطة مش ألعاب لتغيير سلوك أو جعل مهام مملة ممتعة.
  - مش جديدة: **frequent-flier** برامج الطيران، وكارت قهوة «كوب مجاني بعد 10» (gamification تافهة).
  - أمثلة: **Foldit** (crowdsourced بحث عن بروتينات كـ puzzles)، **Experts Exchange** (إجابات تنافسية، نقاط، badges، دخول مجاني).
  - **حقيقة:** قليل من جهود الـ gamification ليها strategy أو complexity حقيقية، لكن ممكن.
- **لموسفولك:** الـ rival contests والـ side quests وminigames نقيّمها: هل بتعلّم اللاعب شيء حقيقي (مهارة merge/تخطيط) ولا هي «multiple-choice متنكر»؟

### 12.ب Communication Theory ★★

- **النموذج:** sender ← message ← channel ← receiver. 5 عناصر:
  - **Sender:** اللي عايز يوصّل الرسالة.
  - **Receiver:** الجمهور.
  - **Channel/medium:** نص، صور...
  - **Signal:** الحاجات الملموسة (كلمات وحروف، اهتزازات صوت).
  - **Message:** الجزء غير الملموس في الدماغ (المعنى). الهدف نقل الـ message.
- الخصائص بتأثر: القافية بتجذب انتباه وتتحفظ (**«I like Ike»**، حملة Eisenhower). والـ channel مهم: **الموسيقى ممتازة في المزاج والعواطف وضعيفة في الادعاءات العقلانية**.
- ملحوظة: الـ subconscious لأن فيه senders بيبعتوا subliminal. بيشتغل في بعض الاختبارات النفسية، لكن **مفيش دليل كافٍ** إنه يغيّر قرارات الشراء أو الآراء السياسية.
- **Sidebar Art & Entertainment ★:**
  - النظرية بتنطبق حتى لو لعبتك entertainment بحت.
  - **Roman Jakobson (1960):** الاتصال ممكن يركّز على حاجات مختلفة، سماها **functions**. التركيز على المستقبل = تعليمة (**ملصق Uncle Sam «I want YOU»**). التركيز على المرسل = تحسين سمعته. **Poetic function:** التركيز على الـ signal نفسه (مصنوع بحرفية، قافية). الأدب والشعر = poetic function قوية.
  - ★ **الباترن:** بنقدّر ألعاب الفن **وكمان الـ entertainment** جزئيًا لأن الـ signals مبنية بمهارة.
- **حدود النموذج:** الإشارة في اتجاه واحد (broadcast): مرسل قوي، جمهور سلبي. الـ broadcast فعّال لأن المرسل عنده وقت وموارد لـ signals طويلة عالية الجودة. **لكن** في التعليم عايز المستقبلين **active** يلعبوا بالرسالة (ولهذا تمارين الكتاب وأمثلة تفاعلية على الموقع).

### 12.ج How the Medium Affects the Message ★★

- **McLuhan «the medium is the message»:** مبالغة دراماتيكية لكن فيها نقطة: الـ medium نفسه بيكشف عن الرسالة قبل إرسالها. لناس معتقدات مسبقة عن الـ media. مثال: كتاب يبدو **أكثر سلطة** من فيلم.
- **قوة الألعاب:** interactive communication بين المصمم واللاعبين وبين اللاعبين بعض. الجمهور **involved مع الـ signal**. يعني ميزة، وبيخلّي التواصل أصعب/مختلف. **العملاء** اللي بيدفعوا لـ serious games لسه بيفكروا بعقلية broadcast (عرض بيانات، مش حاجة مثيرة يعملها الجمهور).
- **Sidebar «Sometimes it is better to make a Film»:** لو قصتك طويلة ومفصلة وما فيهاش مساحة للتفسير والتجريب، الفيلم أفعل. اللعبة تحتاج مشاركة. لو رسالتك مفيهاش مجال للمشاركة النشطة، **ماتعملهاش لعبة**.
- ★★★ **الخاصية الفريدة: الألعاب هي الـ medium الوحيد اللي الـ signal فيه بيتولد من الـ mechanics.**
  - الصوت والفيديو والأنيميشن والنص = presentational media.
  - **قوة اللعبة في الـ mechanics.** لو بتستخدم presentational فقط، استخدم medium تاني.
- **Production value expectations:** الألعاب والأفلام ليها production value عالية فالجمهور بيتوقع جودة. عملاء serious games بيقارنوا بـ Hollywood وtriple-A. الميزانيات الأصغر بتعاني لأن في الألعاب شغل كتير **مخفي** (software engineering، tuning، testing). الألعاب مش مجرد signals، **هي machines مصممة لتخلق الـ signal**.
- **لموسفولك:** لو بنحكي رسالة في Mossfolk (ثيمة طحلب/تعايش مثلًا)، نمررها عبر الـ mechanics مش عبر نص وcutscenes.

### 12.د How Mechanics Send Messages ★★★

- **المبدأ:** الألعاب الجيدة **ما بتحاضرش ولا بتعظ**. بدل signal ذكي، بتبني machine (الـ mechanics) بتنتج الـ signal. أقل كفاءة من «القول المباشر» لكنه بيخلق فهم وقبول أحسن. **اللاعب يستنتج الرسالة** من التفاعل ومراقبة الـ outputs.
- **SimCity الأصلية:**
  - ضريبة الملكية + قرار الإنفاق. mechanic: لو ضريبة عالية جدًا، **الشركات تغادر** (فسّرها ناس كأجندة pro-business رأسمالية).
  - mechanic تانية: إنفاق ضرائب على مرافق (ملاعب، حدائق) بيزوّد سعادة المواطنين، **والمواطنين بيطالبوا بيها** (فسّرها ناس كأجندة اشتراكية).
  - اليمين واليسار قروا رسائل سياسية. الحقيقة: simulation متوازنة لبلدة أمريكية متوسطة. **الرسالتين مقصودتين لكن ما اتقالوش كـ assertions، اللاعب اكتشفهم باللعب.**
  - لو لعبت كاشتراكي ضرائب عالية: الشركات تهرب. لو libertarian ضرائب منخفضة: السكان يمشوا لأن الفلوس ما تكفيش للمرافق. **الرسالة الشاملة: السياسات المتطرفة ما بتنجحش، النهج المتوازن بينجح.**
- **PeaceMaker (persuasive game، نوع من serious games):**
  - الهدف سلام بين الفلسطينيين والإسرائيليين، تلعب كرئيس السلطة الفلسطينية أو رئيس وزراء إسرائيل. في الدورين لو اتخذت موقف hawkish متشدد **فاشل**. **الـ mechanics مضبوطة بحيث إن الانخراط البنّاء فقط ينجح.**
- ★★★ **النقطة الجوهرية: اللي بيخلّي mechanics-as-messages تشتغل هو المجهود اللي اللاعب بيبذله للفوز.**
  - الألعاب بتعاقب سلوكًا وبتكافئ تانيًا، واللاعب لازم **يتعلم ثم يعمل** اللي اللعبة عايزاه.
  - **Sandbox بموارد غير محدودة وبدون عواقب** = اللاعب يتجاهل أي رسالة، وغالبًا ما يعرفش إن فيه رسالة لأن اللعبة ما قيّدتش سلوكه.
  - الفعل المطلوب من اللاعب خاصية مهمة: التوصيل غير مباشر لكن اللاعب **يفتكرها أكتر** لأنه استنتجها بنفسه على فترة. «يعمل ويفكر في العواقب» أفعل من «تقوله المطلوب».
- **تحديات التصميم ★★:**
  - مع مقال أو وثائقي عندك تحكم كامل في الـ signal. مع الـ mechanics: أنت تتحكم في محتوى الـ signal (الأصوات والصور) لكن **أفعال اللاعب بتأثر على إزاي الـ signal بيتولد**: ممكن يظهرها بترتيب مختلف أو ما يظهرهاش. ممكن ما يستنتجش الرسالة صح (مش بقد كفاية متنبه، أو مش مهتم). **اللاعبين hardcore** غالبًا بيعاملوا اللعبة كـ abstract system للـ optimization ولا يهتموا بالسياق.
  - ★★★ **فحص الرسالة الضمنية:** بص على actions اللي الـ mechanics **تتطلبها** للفوز، وعلى الـ actions الاختيارية.
    - لو الإطلاق core mechanic مطلوب للفوز: **ماينفعش تنكر إن اللعبة بتقول «العنف ينجح»**.
    - لو عايز استراتيجية سلمية لازم تكون **واضحة وقابلة للتطبيق ومؤدية للفوز**.
    - الاستراتيجيات الأكفأ بتبعت رسالتها بوضوح أكتر. لو العنف يكسب بسرعة وسهولة والسلمية ببطء وصعوبة = رسالة «العنف طريقة فعالة».
  - **التحذير من الوعظية:** لو بتقدم خيارين (عنف/تفاوض) وبتعاقب واحد دايمًا، اللاعب سيكتشف إنه false choice. **Jesus/Hitler dichotomy** في RPGs اللي بتفرض character alignment: الخيّرين لازم قديسين مطلقين والأشرار قتلة مهووسين، mechanics التحقق من alignment بلا subtlety.
  - **PeaceMaker يتجنبها:** لازم تهدّي صقور جانبك. «تكون حمامة طول الوقت» تخلي شعبك يطردك من المنصب. فاللاعب لازم يوازن بين **معيارين للنجاح**: البقاء في المنصب وصنع السلام. في البداية الميليشيات المتشددة في جانبك قوية، وبتقل أهميتها مع نجاح السياسات.
  - **حتى الـ abstract mechanics بلا خلفية ليها نبرة عاطفية:** resources بتتراكم أسرع وأسرع من positive constructive feedback ≠ مفيش إنتاج واللاعبين لازم يعيشوا بالقليل. نظرية وطرق الفصول السابقة بتساعد تفهم إيه الرسالة.
- **Sidebar Games and Ethics ★:**
  - مسؤولية مشتركة للاعب والمصمم عن الـ signals = منطقة رمادية أخلاقيًا. لعبة ضد التنمر: هل تتحمل لو لاعب حوّل الـ mechanics لـ bully simulator؟
  - **GTA III (2001):** ناقدين قالوا إن اللعبة تطلب قتل البغايا للتقدم. **الحقيقة:** ما بتتطلبش. الزيارة بتزوّد الصحة لـ **125%** وممكن تسترد **$50** لو قتلتها بعد. مش لازم، و$50 قليلة جدًا على الفلوس اللي بتبقى معاك. **لكن** اللعبة وفرت كل مكونات الـ signal (بغايا وأسلحة) والسماح بدون عواقب أنتج **رسالة غير مخططة**. يبدو أسوأ من فيلم لأن الجمهور في الفيلم مش مسؤول عن الأحداث. (هيرجعوا لـ GTA III آخر الفصل.)
- **لموسفولك:**
  - **فحص رسالة الـ mechanics:** الأفعال الأكثر كفاءة في لعبتنا بتقول إيه؟ لو الإسقاط السريع العشوائي بيكسب غالبًا فالرسالة «السرعة تفوز»، ولو الصبر والتخطيط للدمج يكسب فالرسالة عكسها. التيستر-بوت يقدر يقيس أي استراتيجية أكفأ فعلًا.
  - **False choice:** لو بنقدّم اختيارين (power-ups أو تكتيكات) ونعاقب واحد دايمًا اللاعب هيكتشف.
  - الـ sandbox بدون عواقب ما يوصّلش رسالة. القيود (drop budget) هي اللي بتعمل المعنى.

### 12.هـ The Semiotics of Games and Simulations ★★

- **Semiotics = علم العلامة (sign):** العلاقة بين الـ signal وما يقصده (message). **العلامة = كيان مزدوج:** signal مادي يمثل معنى غير مادي. 3 أنواع حسب العلاقة:
  - **Icon:** الـ signal **يشبه** معناه. مثال: صورة شخص. كلمات onomatopoeia (نباح الكلب) نادرة.
  - **Index:** الـ signal **مرتبط سببيًا** بمعناه. مثال: بصمة قدم تدل إن حد كان هنا. الدخان يدل على نار.
  - **Symbol:** مرتبط بالمعنى **بالاتفاق/التقاليد** فقط. أسماء الأفراد، أغلب الكلمات، **الورود = حب** (ثقافات بلا ورود بتستخدم رموزًا تانية).
- **Sidebar المصطلحات الكلاسيكية:** سوسير (1915): sign = **signifier** (الـ signal) + **signified** (المعنى). **Charles Sanders Peirce** (أعماله نُشرت بعد وفاته 1914): تصنيف icon/index/symbol وتم تكييفه لاحقًا مع سوسير. الكتاب بيستخدم **representation** للعلاقة بين signal ومعناه. **توصية:** لا ترجع للأصول (مش accessible)، اقرأ **John Fiske, Introduction to Communication Studies (2010)**.
- **أهمية الـ symbols:** تخلينا نتكلم عن حاجات بشكل عام وننقل الملاحظات من حالات فردية لعامة. مثال كلمة **apples**:
  - ممكن تشير لمجموعة تفاح معينة أو لمفهوم التفاح العام.
  - **aardappel** (الهولندي للبطاطا = «earth apple»): غيّروا كلمة مألوفة لما وصلت البطاطا من العالم الجديد.
  - «comparing apples and oranges» = مقارنة غير صحيحة (مش عن التفاح).
  - تفاحة حواء (مش في الإنجيل فعليًا) صارت رمز الإيروتيكا في الفن.
  - ★ **الخلاصة:** الكلمات اختصارات بتنقل معاني كبيرة ومعقدة بكفاءة.
- **تطبيق على الألعاب:** مدخلان:
  1. الـ signals اللي تنتجها لعبة = نتعامل معها كأي medium، ونتكلم عن **realism** (التشابه مع المعنى).
  2. اللعبة نفسها (نظام قواعد ملموس) **تمثّل نظامًا آخر**. مثال: World of Warcraft (بكل mechanics) تمثل عالم فانتازيا خيالي. ده التفكير الشائع في الـ simulation.
- **Games and Simulations:**
  - **Chris Crawford (1984):** «Accuracy is the sine qua non of simulations; clarity the sine qua non of games.» simulation مقابل game = رسم فني مقابل لوحة. اللعبة **تقمع التفاصيل عمدًا** لتبرز الرسالة العامة: simulation = detailed، game = stylized.
  - **Jesper Juul (2005):** الألعاب غالبًا stylized simulations، مطورة لأغراض جمالية مش مجرد fidelity. بتركز على الجوانب المثيرة المدركة (كرة قدم، تنس، مجرم في مدينة).
  - **رأي المؤلفين:** Crawford كان بيفرق بين simulations للعلم/الهندسة وللألعاب. الألعاب كمان بتحاكي، لكن **أشياء مختلفة لأسباب مختلفة**.
- **Simulations in Science:**
  - ملاحظة ← hypothesis ← تجارب على الواقع ← تأييد أو رفض ← تعديل.
  - لو التجربة مكلفة أو مستحيلة (أنظمة ضخمة أو بطيئة جدًا زي المجرات، أحداث ماضية زي الجيولوجيا): تبني simulation وتقارن نتائجها ببيانات واقعية وتعدّل الاتنين لو اختلفت.
  - لما الفرضية تتأكد بتبقى theory وتتنبأ (مثلًا موعد الكسوف)، والمهندسون بيصمموا مباني وطيارات.
  - **التركيز على الدقة.** semiotically: **iconic** (قواعد الـ simulation تشبه الآليات الحقيقية).
- **Simulations in Games:**
  - الهدف **المتعة** مش الدقة. التصميم static (وثائق ومخططات)، والمبرمجون ينفذون. بيستعيروا أفكارًا من الواقع (الجاذبية، أداء الطيران) لكن **يتجاهلوا أو يعدلوا** لأغراض الترفيه ← **cartoon physics** (شخصيات تسقط مسافات طويلة بدون أذى).
  - ★★ **الاختبار بـ playtest للمتعة لا بالمقارنة بالواقع.** الدقة مهمة **فقط لو اللاعبين يهتموا بها**: في vehicle simulations وsports الجمهور بيهتم بجوانب معينة، وفي genres تانية أقل. **اعرف أي جوانب بتهم جمهورك.**
  - **semiotically:** الألعاب تستخدم **indexical وsymbolic** أكتر من iconic. مثال: **power bar** بدل ما نوري حالة صحة المقاتل بمظهره (يحتاج أنيميشن ضخم). أكفأ (assets أقل) وأفعل (قراءة فورية). كمان الـ simulation مش دقيقة أصلًا لأن المقاتل بيقاتل بقوة كاملة حتى اللحظة الأخيرة.
  - **انتقاد:** غريب إن المطورين يبذلوا جهد في الـ realism. الألعاب الواقعية = iconic simulation. ليست سيئة لكنها **غلطة لو على حساب gameplay ممتع أو افتراض إن realism = fun**. لعبة الترفيه تركز على noniconic forms (analogous وsymbolic).
- **Abstraction ★★★:**
  - لازم الـ simulation أبسط من الأصل، وإلا هتبني **replica** بنفس السرعة والمقياس ومش هتقدر تسرّع الزمن أو تجرّب بأمان. قرار حذف تفاصيل = abstraction. نوعين:
  - **Elimination:** تحذف عوامل تأثيرها ضئيل أو صفر. مثال aerodynamics سيارة: **ممسحات الزجاج وهوائي الراديو** تأثيرها قليل، **الديكور الداخلي** غير ذي صلة.
  - **Simplification:** تعمل model بسيط لـ feature بتساهم في الـ mechanics لكن تفاصيلها الداخلية مش مهمة. **مثال هبوط الطائرات:** إحصاء إن **1 من كل 10,000 هبوط** يعطّل الطائرة من تلف جهاز الهبوط. بدل ما تنمذج الآلية بتفاصيلها تحط **random 1-in-10,000 loss factor**. تقدر تغيّر المعدل لدراسة أثر تحسين الجهاز حتى لو ما تعرفش إزاي تحسّنه فعليًا.
  - مثال ألعاب: **الفلوس في الـ avatar** بتتتبع كـ **$25.37** مش فئات الأوراق. تفاصيل بسّطوها لأن اللاعب مش بيهتم ومش بتأثر على باقي الـ mechanics.
  - **الفرق:** العالم عايز نتيجة دقيقة، المصمم عايز نتيجة ممتعة.
- **Sidebar Simulations can Lie ★★:**
  - **Umberto Eco (1976):** semiotics = «theory of the lie»: العلامات = أي حاجة ممكن تُستخدم للكذب، فالـ semiotics تهتم بالكذب والحقيقة.
  - **Ian Bogost (2006, ص 98–99):** مهما بدت الـ simulation واقعية فهي **subjective** لأن الـ abstraction هو قرار بما يُستبعد. اعرف اختيارات المنشئين ولماذا.
  - **America's Army:** FPS متعدد اللاعبين واقعي جدًا (حتى تدريب أسلحة قبل المهمات «الحقيقية»)، نشره الجيش الأمريكي للتجنيد فمصلحته يبدو واقعيًا.
    - **دم وأشلاء قليلة** (القتال الحقيقي فوضوي ومروع ومش الرسالة المطلوبة للتجنيد).
    - **الأهم:** فرق متقابلة، **كل فريق يرى نفسه جنود أمريكيين والخصم insurgents**. الجيش ما يريدش لعبة تدرّب على قتال جنود أمريكيين. **النتيجة:** gameplay **symmetric** (نفس المعدات والتكتيكات الأمريكية) عكس الـ asymmetric warfare اللي بتدعي تمثيله. فاللعبة **ما تقدرش تدرّب على مكافحة التمرد**.
- **Simulation in Serious Games ★★:**
  - في المنتصف بين العلمية والترفيهية حسب الغرض. اللعبة الإقناعية **تحرّف الـ mechanics** لتوصيل نقطتها (PeaceMaker). اللعبة التعليمية **تمثّل الموضوع صح** (flight simulator احترافي).
  - الترفيه بيحذف الـ unfun: war games لا تتناول **اللوجستيات** (نقل الطعام والوقود للجبهة، والجرحى للمستشفيات) لأنها أقل متعة من الـ tactics.
  - لو serious game عايزة تعلّم اللوجستيات **ما تقدرش تتجاهلها** وبتدخل صراع بين المتعة والرسالة الصحيحة.
  - ★★ **الحل:** صمّم اللعبة **حوالين الموضوع اللي عايز تعلّمه** واعمل abstraction للباقي حتى لو أمتع في منتج ترفيهي. للوجستيات: ابحث الاقتصاد والتحديات، ابني mechanics تحاكيها، **احذف أو بسّط القتال** بحيث اللاعب مش بيشارك فيه، ركّز على جعل التحديات اللوجستية ممتعة بحد ذاتها.
  - **«Serious does not mean serious about everything»:** مقبول لعبة لوجستيات بـ cartoon physics وgraphics طالما بتعلّم المبادئ الأساسية صح.
  - ★ **غلطة شائعة:** تبدأ تصميم serious game بنسخ لعبة ترفيهية موجودة. ابني حوالين الموضوع.
  - **Note: subject-matter expert** = شخص يعرف الموضوع كويس وغالبًا لا يعرف game design. شغل أكتر **compromise ودبلوماسية** من الترفيه.
- **لموسفولك:**
  - **Abstraction بالظبط هو Mossfolk:** 9 أحجام مخلوقات والـ merge = abstraction للنمو/الاندماج. ما نحتاجش «واقعية» للـ physics أكتر مما اللاعب يهتم.
  - **Playtest للمتعة، مش للدقة**: نفس معيار التيستر-بوت.
  - فحص «كذب الـ sim»: أي abstraction بنعمله ليه تأثير على الـ fairness (مثال: الـ physics randomness اللي مش بيعكس الواقع) نكتبه كقرار معروف.

### 12.و Analogous Simulation ★★★

- **التعريف:** الـ mechanics ما تشبهش آلية النظام الممثَّل مباشرة لكن الأفكار الأساسية **مرتبطة سببيًا** (= indexical sign).
- **Inventory (من Adventure، 1976):** اللاعب يلتقط أغراضًا ويديرها في شاشة inventory. أغلب الألعاب تحدد الحمولة: عدد ثابت أو **weight** لكل غرض مع حد إجمالي.
- **Diablo inventory ★★:**
  - **الحجم النسبي** هو العامل المقيّد الأساسي بدل التفاصيل (الحجم والشكل والوزن).
  - كل غرض ياخد عدد من الـ **slots** منظمة في **grid** (1x1، 2x2، 1x4...). تلتقط الغرض فقط لو فيه مساحة.
  - **علاقة تناسبية** بين slots الأغراض الافتراضية ووزن وشكل وحجم مقابلاتها. القواعد **واضحة وبديهية فورًا** (مصممة للعرض البصري). ومشاكل الإدارة شبه الحياة الحقيقية. بتسمح للاعب بعمل **فوضى غير كفؤة** في inventory، فبتعلّمه ينظّم عشان يحمّل أكتر (مع إن البعض يعتبره مهمة مملة في fantasy).
  - **التضحية بالدقة:** في Diablo غرض ما يقدرش يكون كبير وخفيف في نفس الوقت. **لكن السلوك العام باقي** (اللاعب محدود فيما يحمل).
  - **الذكاء:** ينهار كل تعقيدات إدارة الـ inventory في **size puzzle** سهل العرض على الشاشة بدل الوزن (الاختيار الأشهر قبله، ويترجم للوسيط البصري بشكل أسوأ).
- **Health:** صحة الشخصيات/الوحدات تتمثل بنسبة مئوية أو **hit points**. في الواقع الصحة/السلامة الهيكلية معقدة، واللعبة **تجمّع كل الجوانب في mechanism واحد** يفهمه اللاعب والكمبيوتر.
- **الباترن ورا التاكتيك:** استبدل مجموعة قيود واقعية بـ **مقياس واحد يترجم بصريًا** مع الحفاظ على السلوك العام.
- **لموسفولك:** حجم الجرّة وعدد الـ drops هما analogous simulation لـ «مساحة محدودة». الـ 9 أحجام = تبسيط تدرج النمو في قيمة واحدة مقروءة بصريًا (الحجم).

### 12.ز Symbolic Simulation ★★★

- **التعريف:** خطوة بعد analogous: العلاقة بين النظام الأصلي والـ mechanics **عشوائية/تقليدية** مش سببية.
- **Dice:**
  - في **Risk**: رمية كام نردة تمثل **نتيجة معركة كاملة**. العلاقة اعتباطية، وaction واحد معروف من ألعاب تانية يمثل عدد كبير من الأفعال اللي أغلب اللاعبين مالهومش خبرة فيها.
  - **ليه تنفع:** اللاعب **ما ينبغيش** يكون له تأثير كبير على النتيجة. Risk عن استراتيجية عالمية مش مناورات ميدان. **القائد الأعلى** ما يدير كل معركة بنفسه لكن يحدد كام قوات يلتزم بها ومتى ينسحب.
  - **Kriegsspiel وغيرها:** عن مناورات تكتيكية فقواعدها معقدة، لكن قتال الأفراد متروك لـ dice وجداول attrition. صُممت لتدريب مهارات تكتيكية **مش استخدام البندقية**.
  - **Dice** بتخلق تأثير nondeterministic من غير قواعد مفصلة. على مستوى abstraction كافٍ، نظام معقد nondeterministic (قتال فردي) له تأثير يشبه رمي نرد. **العشوائية المميزة لـ dice mechanics بتطابق أنماط سطحية nondeterministic لأنظمة أعقد.**
- **Super Mario Bros.: القفز على الأعداء ★★★**
  - بين symbolic وanalogous. التنفيذ يختلف من عدو لآخر ولا يشتغل مع الكل، لكنه ثابت في اللعبة والسلسلة. الربط بين القفز على حاجة وهزيمتها ليس عشوائيًا تمامًا، لكن استخدامه في platformers بقى **تقليدي** (conventional) زي الـ symbolic sign في اللغة.
  - في الواقع بعض الكائنات تُسحق بالقفز، لكنه غريب مع روبوت أو سلحفاة. الدافع هو **متعة القفز** (الـ action المميز للجنر) مش الواقعية. **Sonic: هجوم واحد في اللعبة كلها: القفز.**
  - فيه علاقة بالمهارات: **توقيت ودقة** (مهارات القتال الحقيقي).
  - ★★★ **الجوهر:** المهم إن التمثيل البسيط يتيح أكتر من تمرين المهارات. الـ metaphor سهلة، واللعبة بتدعو اللاعب للتجريب وتطوير استراتيجيات. **«جمع combat rules في لعبة قفز» من غير أي action جديد** (استبدال الأكشن الممثَّل بقواعد اعتباطية موجودة أصلًا). ده **يقلل عدد الـ actions اللي يتعلمها اللاعب** فيروح بسرعة لتفاعل تكتيكي/استراتيجي أعمق بدل ما يتلخبط في الـ interface.
  - ★ **تقليل نظام لبناء أبسط بسلوك ديناميكي مكافئ تقريبًا.**
- **لموسفولك:** الـ merge نفسه symbolic: «اتنين نفس الحجم = أكبر» قاعدة اتفاقية، مفيش علاقة واقعية. القوة إن **action واحد** (إسقاط) يتحمل كل شيء. أي mechanic جديدة (shells/stones/rot) نسأل: بتضيف action جديد يتعلمه اللاعب ولا بتعيد استخدام الإسقاط؟

### 12.ح Less Is More ★★★

- Analogous وsymbolic **بتعمل أنظمة أبسط** من الـ iconic realistic بآثار مفيدة: ألعاب أسهل في التعلم وصعبة في الإتقان. «Less is more» في أي فن تمثيلي: الإيجاز والاقتصاد (كلمة واحدة صحيحة أفضل من 20 غلط).
- **Sidebar: هل فيه حد أقصى لعدد الـ mechanisms؟** مستحيل رقم محدد. تعتمد على الجمهور (ألعاب الأطفال أبسط لكن حتى الكبار يستمتعوا ببساطة). **المبدأ:** mechanics تعطي أكبر عدد من gameplay options يستمتع بها الجمهور (متسقة مع fantasy) **ومن غير عبء إدراكي غير معقول**.
  - **Ernest Adams: player-centric approach:** حط رغبات اللاعب في بالك. مثال: ألعاب fighting بسّطت mechanics بـ **Quick Time Events** → **اشمئزاز** المشجعين التقليديين.
  - **Antoine de Saint-Exupéry (1939):** «perfection is reached not when there is nothing left to add, but when there is nothing left to take away» تنطبق **طالما اللاعبين سعداء!**
- **عدد صغير من patterns يولّد gameplay معقد:** أسهل للمصمم، أسهل تنفيذ للمبرمجين والفنانين، أسهل تعلم للاعب.
- **في Machinations:**
  - analogous: **يقلل عدد العناصر** باستبدال mechanisms متشابهة بواحدة.
  - symbolic: **يربط mechanics حيث لا ترتبط مباشرة في الواقع**.
  - ★ **أفضل الـ symbols** تربط قاعدتين غير مرتبطتين لكن بينهم **affinity** (Mario: التوقيت والمهارة البدنية في القفز والقتال).
  - الاستخدام الصحيح **يقلل العناصر بدون المساس بالتعقيد البنيوي** (عدد feedback loops) والـ emergent properties كتير.
- **3 مزايا:**
  1. اللاعب **يركز على الخصائص البنيوية والتفاعل الاستراتيجي** (وبيقل تعقيد الـ UI). الخصائص البنيوية تقود السلوك الـ emergent. نسخة أبسط تدرّب اللاعبين على فهم أنظمة حقيقية أكثر تعقيدًا.
  2. **جلسة كاملة في وقت أقل بكتير** من النظام الممثَّل. اللاعب يتعلم نتائج قراراته بسرعة، فيكررها أكتر، ويحس بـ **agency and power** (المحرك لكتير من الـ commercial entertainment). الـ scientific simulations أبطأ غالبًا من real time.
  3. للمصمم **أسهل في الإدارة والـ balance**: يركز على العناصر المساهمة في الـ emergent behavior. أقل تكلفة اقتصاديًا ورسالة أفعل. التحفظ: الجمهور يؤثر (عشاق السباقات الهاردكور ما يرضوا بـ Mario Kart).
- **Sidebar Discrete Infinity ★★★:**
  - **Noam Chomsky (1972، ص 17):** المفردات محدودة (عشرات الآلاف من الكلمات) لكن عدد الأشياء المقولة **لا نهائي** لأن الكلمات تتركّب بطرق مختلفة. سماها **discrete infinity** = استخدام لا نهائي لوسائل محدودة.
  - **تطبيق:** **عدد الاتصالات الممكنة بين العناصر أهم من عدد العناصر**. دوّر على أنظمة فيها combinations ذات معنى كبيرة وربما غير منتهية.
  - **المخاطرة:** نتائج غير متوقعة. **الفائدة:** لعبة يطلع منها أكتر مما حطيت.
  - **Super Mario Bros.:** حفنة mechanics متجمعة في تحديات كتير. قيمة كل mechanism من التركيبات اللي بتسمح بها مش من تمثيل واقعي لاستكشاف غابة أو dungeon.
  - ★ **رسالة اللعبة الأقل iconic أكثر قابلية للتطبيق خارج اللعبة** لأن المهارات والمعرفة أعمّ. **تعلم من Monopoly** يطبق في مواقف كتير. كان هيتعلم أقل لو كانت simulation دقيقة لسوق العقارات في **Atlantic City, New Jersey** (مكان النسخة الأصلية).
- **لموسفولك:**
  - **Mossfolk = discrete infinity:** عدد قليل من العناصر (9 أحجام + physics + تحديات) والتنوع من combinations (3000 ليفل بأهداف وميزانيات مختلفة).
  - **قاعدة مقترحة:** قبل ما نضيف عنصر جديد (مثلًا من 2501) نسأل: هل بيضيف **connections** جديدة مع الموجود، ولا مجرد عنصر؟
  - **Quick Time Events warning:** تبسيط الـ mechanics على حساب فرق الجمهور الأساسي ممكن يضر. نراقب اللي محتاج تبسيط من التيستر-بوت مقابل اللاعب الأساسي.

### 12.ط Multiple Layers of Meaning ★★★

- **Umberto Eco عن Shakespeare (2004، ص 212–235):** مسرحياته لها **جاذبية شعبية** (رومانسية ودراما وكوميديا وتراجيديا مفهومة للجميع) و**جاذبية للنخبة السياسية والاجتماعية** (تعليقات على الشأن الجاري رغم الأزمنة والأماكن البعيدة) **مع** نثر وشعر جميل لحد النهارده.
- ★★★ **Eco: فوائد الـ layers المتعددة (3):**
  1. **جاذبية واسعة** لناس كتير.
  2. **تدعو الجمهور لاستكشاف العمل بطرق مختلفة** (= replay value).
  3. **التناقض بين layers يخلق فرصة للفكاهة والسخرية** (humor وirony).
- الألعاب طبيعيًا مناسبة: تتواصل عبر الـ signals **وعبر الـ mechanics** اللي بتنتجها.
- **Unrelated Meanings:** شكسبير قدّم للطبقات المختلفة ترفيه مناسب حتى لو غير مرتبط (سخرية سياسية للنخبة ونكات وتلاعب ألفاظ للعامة) محتفظًا بالتناغم. **Romeo and Juliet** تبدأ بـ **wordplay سخيف** يضحّك أقل الجمهور تعليمًا، ثم يتطور لـ swordplay ويصير جديًا.
- **Bioshock ★★★ (4 layers):**
  1. **Physical layer:** survival horror FPS مع عناصر RPG. اللاعب لو أراد يتجاهل كل حاجة، يركز على البقاء، قتل خصومه بلا أخلاق، وتحسين attributes.
  2. **Moral layer:** اللاعب يأخذ الخيارات الأخلاقية بجدية ويلعب **بدون قتل Little Sisters**. مش مجبر. **أخطر** واللعبة تدّي **مكافآت قصيرة المدى أكبر** لقتلهم. لكن يجرّب gameplay مختلف ويحصل على **نهاية مختلفة**.
  3. **Aesthetic layer:** منظر **Art Deco** استثنائي (اتطبع وبيع **كـ coffee-table book**، إنجاز نادر). ما بيعتمدش عليه الـ physical أو الـ moral، **ترفيه قائم بذاته**.
  4. **Political layer:** سخرية من فلسفة **Ayn Rand (Objectivism)**. مؤسس العالم **Andrew Ryan** (إشارة مقصودة وهي **indexical sign** لـ Ayn Rand). Objectivism نسخة من Libertarianism تدعو لـ «uncontrolled, unregulated laissez-faire capitalism» (Rand 1964، ص 37). Bioshock تقدّم رؤية لو مجتمع Objectivist مارس **تجارب بيولوجية بلا ضوابط**: كارثة ودمار.
  - **مصدر كل طبقة:** physical وmoral من الـ **mechanics** (ضرورة البقاء وحساب عواقب القرارات)، aesthetic من **الفن**، political من **القصة** (narration). مش لعبة تتقلد بسهولة لكنها تستحق الدراسة.
- **Contrast between Appearance and Mechanics ★★★:**
  - **September 12 (Gonzalo Frasca):**
    - تقول في شاشة التعليمات إنها **مش لعبة بل simulation** لـ «explore some aspects of the war on terror».
    - مدينة عربية كرتونية isometric. مدنيون وإرهابيون (حاملين أسلحة). اللاعب يطلق صواريخ تدمر مباني وتقتل إرهابيين ومدنيين. **صعب التصويب** وأضرار جانبية كبيرة.
    - ★ **أهم mechanic: الخسائر المدنية تحوّل المدنيين لإرهابيين.** أفضل طريقة للسيطرة على عدد الإرهابيين هي **فعل لا شيء**، لأن الإرهابيين **يتحولون لمواطنين بمرور الوقت**.
    - simulation مبسطة جدًا، لكنها **مش iconic**.
    - ★★ **القوة من التناقض بين المظهر والـ mechanics:** المظهر يشبه shooter كرتوني، والـ mechanics تعكس الـ shooters (الإطلاق مش بيقربك للهدف). تستغل توقعات اللاعب من ألعاب كتير لتوقعه في موقف خاطئ. الاكتشاف ده **turning point** ذو معنى يقوي حجتها: **القوة الغاشمة العشوائية وسيلة غير فعالة** لمشكلة الإرهاب. وبسبب إشارتها لألعاب الـ shooter لها **جاذبية شعبية**. المصمم تلقى **مئات الآلاف من الرسائل** وكتير فهموا الرسالة.
  - **Train (Brenda Brathwaite، 2009، tabletop):**
    - الأدوار **معكوسة** عن September 12: القواعد بسيطة وغامضة، **تفسير المظهر** هو اللي يخلق التناقض.
    - القواعد: سباق عربات قطار لوجهة وتجميع أكبر عدد من **ركاب صفر**. تلميحات: الركاب في **عربات شحن**، **نافذة مكسورة** كـ «board» (جو مقلق).
    - **لما أول قطار يصل، الوجهة معسكر إبادة نازي**. تظن إنك كسبت وتكتشف إنك شريك في فظاعة. حتى «ما كنتش أعرف، كنت بلعب بس» تجعلك تتساءل هل كان لازم تلاحظ التلميحات.
    - الزجاج المكسور = **Kristallnacht (1938)** (هجوم منسق على يهود ألمانيا والنمسا ترك الشوارع مليئة بالزجاج)، والركاب صفر لأن اليهود أُجبروا على ارتداء **نجوم صفراء**.
- **لموسفولك:** Mossfolk: نخطط layers ببساطة: (1) الـ merge physics، (2) طبقة الأهداف/الميزانية، (3) side quests/rival، (4) الفن والمخلوقات. المسألة: أي layer نبقيها «غير مرتبطة» تخدم جماهير مختلفة (casual/hardcore).

### 12.ي Intertextual Irony ★★

- **التعريف (Eco):** تنشأ لما **style اللعبة** يشير لأنواع أو مواقف معروفة خارجها، **بينما** يتناقض هذا مع معنى مضاد في طبقة تانية.
- **GTA III:**
  - mechanics: سرقة سيارات وجرائم → «joyride simulator» أو «SimCrime».
  - مدينة تشبه نيويورك، مواقع وسكان تشير لمواقع ونمطيات حقيقية، مراجع ثقافة شعبية كتير.
  - **إعلانات** ظاهرها حقيقي وباطنها ساخر: فيلم **Soldiers of Misfortune** بتاج لاين «They left together but come back in pieces».
  - **راديو السيارات:** إعلانات وجينجلز تبدو صح وهي مزعجة: محطة تفتخر إنها تملك **عدة شبكات وأقمار صناعية وعشرة senators**، شركة تبعت **حيوانات أليفة في صناديق بالبريد**، reality show **سجناء سابقين يقاتلوا في الشوارع بأسلحة حقيقية** لحد ما يبقى واحد.
  - اللعبة **satirical** تعكس صورة مشوّهة للمجتمع. **الـ mechanics تولّد ثروة هائلة** وكل واحد في عالم GTA يطمح لها **أيًا كانت وسيلة التراكم**.
- **GTA: San Andreas:** تشت

# Game Mechanics: Advanced Game Design (Ernest Adams & Joris Dormans) — جزء 7/8 — نوتس مذاكرة

**المصدر:** كتاب، مفيش مدة. الجزء ده يغطي ص308–368: باقي Appendix B (Design Pattern Library) + Appendix C + المراجع + الفهرس. وبعدهم نسخة الـ Online Appendix B (من B-1 لحد B-11) اللي بتدينا باترنز Static Engine وDynamic Engine بالكامل.

**ملاحظة ترقيم:** مفيش ترقيم فصول سابق في الرسالة، فرقّمت الأقسام بترقيم الكتاب نفسه (B.1، B.2…). لو عايز ترقيم متصل مع الأجزاء 1–6 قولّي آخر رقم وبعدّله.

**ملاحظة نطاق:**
- الجزء ده كله تصميم، مفيش برمجة تتجاهل.
- Converter Engine وEngine Building ظاهرين مرتين (نسخة الكتاب ونسخة الأونلاين). كتبتهم مرة واحدة ودمجت الاتنين.
- النص بيقطع في نص مثال Puerto Rico في نسخة الأونلاين. الباقي من Engine Building (والباترنز الأونلاين التانية) يتوقع يكون في جزء 8.

**الفكرة الجامعة للجزء:** كل باترن بيتوصف بنفس القالب: Type / Intent / Motivation / Applicability / Participants / Collaborations / Consequences / Implementation / Examples / Related. ولما بتجمعهم تطلع **خريطة علاقات** بين الباترنز (في آخر النوتس). الأنواع: Engine (إنتاج)، Friction (مقاومة الإنتاج)، Escalation (تصعيد)، Miscellaneous.

---

## B.1 Static Engine ★★★ (نسخة الأونلاين)

- **Type:** Engine. **Intent:** مصدر بيطلّع flow ثابت من الموارد مع الوقت، اللاعب يستهلكه أو يجمعه. **Motivation:** flow مش بيجف أبدًا.
- **Applicability:** عايز تحدّ من أفعال اللاعب من غير ما تعقّد التصميم. اللاعب لازم يفكر هيصرف موارده على إيه، من غير حاجة لتخطيط طويل المدى.
- **Participants:** energy، source بينتجها، actions اللاعب يصرف عليها.
- **Collaborations:** الـ source بيطلّع بمعدل ثابت **أو غير متوقع**.
- **Consequences:**
  - معدل الإنتاج ما بيتغيرش، فأثره على الـ balance **متوقع جدًا**.
  - ممكن يسبب imbalance **بس لو المعدل مش واحد لكل اللاعبين**.
  - ★ لازم فيه خيارات صرف: **static engine بخيار صرف واحد قليل الفايدة**.
  - مبيشجعش long-term strategies لأن الجمع بديهي.
- **Implementation:**
  - عادةً source واحد يكفي. خطوات إنتاج متعددة بتضيف قليل جدًا.
  - ★ **Unpredictable static engine:** تغيّر الـ output أو الزمن بين مرات الإنتاج بـ randomness، أو skill، أو multiplayer dynamics. الباترن ورا ده: اللاعب لازم يستعد لفترات شحّ، واللي بتخطيطه بيستحمل سوء الحظ بيتكافأ.
  - ★★ **نفس النتيجة العشوائية لكل اللاعبين** بتعادل الـ luck من غير ما تقتل الـ unpredictability، وبتحط الضغط على التخطيط والتوقيت.
  - مثال آلية: كل اللاعبين بيقرروا سرًّا كام مورد يدخل اللعب للكل. **أقل رقم هو اللي يدخل**، ومقترحه يلعب الأول. ده بيعمل feedback من حالة اللعبة ويمنع التضخم (inflation).
- **أمثلة:**
  - **Star Wars: X-Wing Alliance:** الطاقة اللي بتولّدها المركبة تتحول بين shields وspeed وlasers. القرار استراتيجي وبيتغير في أي لحظة. نفس معدل الطاقة لكل المركبات من نفس النوع.
  - **Descent: Journeys in the Dark:** كل دور اللاعب بياخد **2 action**. الخيارات: move / attack / special action. الـ special مرة واحدة في الدور. النتيجة **5 توليفات**: attack×2، move×2، attack+move، attack+special، move+special. والـ actions **مبتتخزنش** للدور اللي بعده. الفوكس على اختيار الأفعال.
- **Related:** weak static engine بيمنع الـ deadlock في converter engine. الـ static engine بيتطور بـ dynamic engine أو converter engine أو slow cycle.
- **لموسفولك:**
  - **ميزانية الإسقاطات (drop budget) هي static engine بالكتاب:** عدد ثابت من الأفعال لا يتخزن، والتصميم كله في اختيار الإسقاط. نفس منطق Descent.
  - **Unpredictable static engine = طابور القطع العشوائي.** وبند "نفس النتيجة العشوائية للكل" يتطبق مباشرة: في الـ rival contests نسلّم الاتنين **نفس seed للطابور**. ده يلغي الحظ ويخلي الفوز مهارة.
  - التيستر-بوت يقدر يعيد نفس الـ seed على كل bot_difficulty عشان يقارن مهارات من غير ضوضاء حظ.

---

## B.2 Dynamic Engine ★★★ (نسخة الأونلاين)

- **Intent:** source بيطلّع flow قابل للتعديل، واللاعب يستثمر موارد عشان يحسّنه. **Motivation:** إمكانية استثمار طويل المدى. القلب = **positive constructive feedback loop**.
- **Applicability:** عايز trade-off بين استثمار طويل المدى ومكسب قصير المدى، وتحكم أكبر في معدل الإنتاج من الـ static.
- **Participants:** energy، source، upgrades بتأثر على معدل الإنتاج، action اسمها invest بتعمل upgrades، actions الصرف (والـ invest منهم).
- **Collaborations:** نوعين upgrades:
  1. **تردد الإنتاج (frequency)**.
  2. **عدد التوكنز في كل مرة**.
  - الفرق: التردد العالي = flow ثابت. العدد العالي بتردد قليل = **bursts**.
- **Consequences:**
  - الـ loop قوي ومحتاج negative feedback (أي friction) أو escalation بتحديات متصاعدة.
  - ★★ **خطر الـ dominant strategy**: إما بتفضيل الـ long-term أكتر من اللازم، أو بتكاليف long-term عالية جدًا.
  - ★★ **الـ gameplay signature المميزة:** اللاعب يستثمر في الأول ويبان إنه ما بيتقدمش، وبعد نقطة معينة التقدم يبدأ ولازم يسرّعه بأقصى سرعة.
- **Implementation:**
  - randomness بتقلل فرصة dominant strategy، **لكن** الـ positive loop **بيضخّم حظ بداية اللعبة** فتبقى العشوائية كتير بسرعة. العلاج: نفس النتيجة العشوائية لكل اللاعبين (تقلل الحظ وتفضل unpredictable وتركّز على الاستراتيجية).
  - بعض الـ dynamic engines بتسمح بتحويل upgrades **رجوع لـ energy بمعدل أقل** من الاستثمار الأصلي. ده خيار قابل للتطبيق لما الـ upgrades غالية واللاعب محتاج طاقة كبيرة كتير.
- **أمثلة:**
  - **StarCraft:** SCV بتحصد minerals تتصرف على SCVs أكتر. الباترن في جوهره، مع إن الـ minerals محدودة والـ SCV ممكن تتقتل. اللاعب بيتعرض فورًا لخيار long-term (SCVs كتير) وshort-term (وحدات عسكرية للهجوم أو التهديدات الفورية).
  - **The Settlers of Catan:**
    - رمية النرد تحدد أي tiles تنتج في أول دور كل لاعب.
    - قرى أكتر = فرصة موارد أكبر.
    - ترقية قرية لمدينة **تضاعف output كل tile**.
    - بيتخطى الـ signature المعتادة بأمرين: **أنواع invest مختلفة**، وإن الفوز بيتقاس بـ **الـ upgrades مش الـ energy**.
- **Related:** dynamic friction وattrition بيقاوموا فايدة الـ long-term. static friction **بتبالغ** في فايدتها. الـ dynamic engine بيطوّر static engine، ومتطوّر بـ engine building وworker placement.
- **لموسفولك:**
  - منحنى الـ merge الطبيعي (دمج صغير كتير في الأول وتقدم بطيء، وبعدين cascade كبير) **هو الـ signature دي بالظبط**. مفيد لوصف "المنحنى المتوقع" لكل ليفل.
  - تفرقة التردد مقابل العدد = تفرقة بين تدفق دمجات صغيرة منتظمة وbursts (شين كبير نادر). تتحكم في طابع الليفل.
  - لو أي sub-system فيه استثمار (boosters / meta)، نفحص خطر dominant strategy على المحورين.

---

## B.3 Converter Engine ★★ (دمج نسختين)

- **Type:** Engine. **Intent:** **اتنين converters في loop** بيعملوا فائض موارد يتستخدم في أماكن تانية.
- **Motivation:** موردين بيتحولوا لبعض وبيغذوا feedback loop. **واحد على الأقل** من الـ converters بيطلّع أكتر مما بياخد. أعقد من باقي الـ engines لكنه بيدّي فرص تحسين أكتر، فهو **تقريبًا دايمًا dynamic**.
- **Applicability:**
  - عايز mechanism أعقد بيدي موارد أكتر من static/dynamic. (مثال الكتاب فيه **عنصرين interactive** مقابل واحد في الـ dynamic.)
  - بيزود الصعوبة لأن **قوة الـ loop والاستثمار المطلوب أصعب في التقييم**.
  - محتاج خيارات متعددة لضبط **profile الـ feedback loop**.
- **Participants:** موردين (energy وfuel)، converter بيحول fuel→energy، converter بيحول energy→fuel، actions بتستهلك energy.
- **Collaborations:** عادةً اللاعب بيخلص بطاقة أكتر مما بدأ بيها.
- **Consequences:**
  - ★★ **خطر deadlock:** لما المورديـن يجفوا، الـ engine بيقف. واللاعب نفسه بيتسبب فيه لو نسي يستثمر energy عشان fuel جديد. **العلاج: weak static engine مدموج**.
  - بيطلب شغل أكتر من اللاعب (خصوصًا لو الـ converters يدوية).
  - positive feedback loop زي الـ dynamic، فمحتاج friction.
- **Implementation:**
  - ★★ **عدد الخطوات في الـ loop**: أكتر = أصعب في التشغيل بكفاءة، وفرص tuning أكتر. قليل جدًا = الميزة محدودة (ففكّر في dynamic engine). كتير جدًا = engine مرهق (خصوصًا في board games بدون automation).
  - ممكن يبقى unpredictable بـ randomness أو multiplayer أو skill. ده بيعقّده وبيزود احتمال الـ deadlock.
  - ★★ **Limiter** في الدورة بيمسك الـ positive engine: مثلًا حد أقصى لعدد الـ fuel المتحول كل دور = سقف لأقصى معدل. في Machinations: **gate node**. تشبيه السيارة: المحرك يحول fuel لطاقة، الطاقة تشغّل الـ fuel pump، والـ pump يستهلك طاقة ويبعت fuel أكتر. **loop موجب محدود بالـ throttle**.
- **أمثلة:**
  - **Elite (الثمانينات):**
    - كل كوكب له سوق خاص.
    - الاقتصاد **أحيانًا** converter engine: تشتري سلعة في كوكب A وتبيعها بربح في B وترجع بسلعة مطلوبة في A (أحيانًا 3 كواكب أو أكتر).
    - الحد الأقصى = سعة الشحن (قابلة للتكبير بالفلوس).
    - خصائص السفينة (مدى hyperspeed، قدرة النجاة في المناطق الخطرة) بتأثر على ربح كل خط.
    - الخطوط **بتقل ربحيتها** مع الوقت لأن مجهود اللاعب بيقلل الطلب والسعر (آلية متشالة من الدياجرام).
    - مكان اللاعب (A أو B) هو اللي بينشّط الـ converters.
  - **Power Grid:**
    - اللاعب يصرف فلوس يشتري fuel من السوق ويحرقه يطلّع فلوس في محطات الطاقة. اللعبة ما بتنمذجش الكهرباء، التحويل مباشر fuel→money.
    - الفائض يتستثمر في محطات أكفأ وربط مدن أكتر.
    - **محدود:** الفلوس تتكسب بس **عن كل مدينة متصلة** (سقف على output الدور).
    - ★ **weak static engine ضد الـ deadlock:** اللاعب بياخد مبلغ صغير في الدور حتى لو فشل يطلّع فلوس من المحطات.
    - **غير متوقع بدرجة طفيفة:** تخزين الـ fuel بيرفع سعره، وده بيشتغل كـ stopping mechanism كمان.
- **Related:** مناسب جدًا لـ engine building (فرص تغيير: معدلات الـ converters واحتمال الـ limiter). بيتوازن بـ friction. بيطوّر static engine، ومتطوّر بـ engine building وworker placement.
- **لموسفولك:**
  - **قاعدة الـ weak static engine** هي ضمان إن اللاعب مش بيتحبس: لو أي اقتصاد meta (عملات ↔ boosters) اتحط، لازم يكون فيه مصدر صغير مضمون يمنع الـ soft-lock. ده منسجم مع خط حسام "مفيش حاجة بتمنع اللعب".
  - لو أي loop عملات→booster→ليفل→عملات اتبنى، نعد خطواته. 2–3 خطوات مقبولة، والـ ads (rewarded) ممكن تتحسب كـ limiter أو مدخل خارجي حسب التصميم.

---

## B.4 Engine Building ★ (دمج نسختين، النص مقطوع عند Puerto Rico)

- **Type:** Engine. **Intent:** جزء كبير من اللعب مخصص لبناء وضبط engine لإنتاج flow ثابت.
- **Motivation:** dynamic engine أو converter engine أو توليفة = قلب معقد وديناميكي. اللعبة فيها **mechanic تحسين واحد على الأقل (ويفضّل أكتر)**، وممكن تكون متعددة الخطوات. ★ **لازم يكون مش تافه إن اللاعب يقيّم حالة الـ engine**، وإلا مفيش gameplay.
- **Applicability:** تركيز قوي على البناء والتشييد، وتركيز على الاستراتيجية بعيدة المدى والتخطيط.
- **Participants:** core engine معقد من أنواع engines متعددة، mechanisms بناء (واحدة على الأقل وعادةً متعددة)، energy هي المورد الأساسي.
- **Collaborations:** الـ building mechanisms بتزود output الـ engine. لو تفعيلها بيطلب energy فيتعمل **positive constructive feedback loop**.
- **Consequences:** بيزود الصعوبة، ويناسب الألعاب **بطيئة الإيقاع** (تخطيط وقرارات استراتيجية).
- **Implementation:**
  - عدم القابلية للتنبؤ بيزود الصعوبة والتنوع ويمنع dominant strategies. الـ engine فيه آليات كتير فبيفتح فرص ده، وتعقيده بيجيب unpredictability لوحده.
  - ★★ الـ positive constructive feedback **لازم ميبقاش قوي ولا سريع زيادة**، و**وزّع عملية البناء على اللعبة كلها**.
  - ممكن يشتغل **من غير feedback** لو التفعيل مش بيستهلك energy. ده مقبول لما الـ engine بيطلّع أنواع طاقة مختلفة تفضّل استراتيجيات مختلفة، لكن لازم يتقيّد التفعيل بشكل ما.
  - الـ dynamic engine نسخة **بسيطة** من الباترن (نوع أو اتنين upgrades). الـ engine building الحقيقي بيدي خيارات كتير.
- **أمثلة:**
  - **SimCity:** الطاقة = فلوس. الـ mechanisms: تجهيز مواقع، zoning، infrastructure، مباني خاصة، هدم. موارد داخلية: ناس، وظائف شاغرة، كهرباء، سعة مواصلات، 3 أنواع zones. الـ feedback loops الداخلية بتعمل friction وتوازن الـ loop الموجب، ولدرجة إن **الـ engine ممكن ينهار** لو اللاعب مش حذر.
  - **Puerto Rico:** كل لاعب يبني مستعمرة (plantations، buildings، colonists، فلوس، محاصيل). الموارد تتعاد استثمارها أو تتحول لـ victory points. اللاعبين بيتنافسوا على **عدد محدود من الـ positions** اللي بتسمح بأفعال تحسين مختلفة = **multiplayer dynamic قوي**. (النص بيقطع هنا.)
- **Related (من نسخة الكتاب):** multiple feedback على الـ building mechanisms يزود الصعوبة. كل أنماط friction تناسب توازن الـ positive feedback. الـ dynamic engine أبسط تطبيق. الباترن بيطوّر dynamic/converter engine ومتطوّر بـ worker placement.
- **لموسفولك:** مش ضروري في الـ core merge. لو فيه meta-layer (تطوير مخلوقات/جاردن/كوليكشن)، نختبر: هل حالة الـ engine **مش تافهة** للتقييم؟ وهل التسارع موزع على اللعبة ولا بيتفرقع بدري؟

---

## B.5 Static Friction ★★

- **Type:** Friction. **Intent:** drain بيستهلك تلقائيًا موارد اللاعب. **Motivation:** يقاوم الإنتاج باستهلاك **دوري** بمعدل ثابت أو عشوائي.
- **Applicability:** mechanism بيقاوم الإنتاج لكن اللاعب **يقدر يتغلب عليه في الآخر**، ومبالغة في فايدة الاستثمار في upgrades الـ dynamic engine على المدى الطويل.
- **Participants:** energy، static drain، production mechanism، actions تانية بتستهلك energy.
- **Collaborations:** الإنتاج بيدّي طاقة، والـ drain بيسحب بره تحكم اللاعب المباشر.
- **Consequences:** طريقة بسيطة نسبيًا لمقاومة الـ positive feedback. **بيبرز الـ long-term strategy** لأنه بيقلل output البداية من غير ما يمس الـ upgrades.
- **Implementation:**
  - ★ **ثابت (constant) = أسهل وأوضح، عشوائي = ضوضاء ديناميكية أكتر.** العشوائي بديل كويس لـ randomness في الإنتاج.
  - ★★ **التردد:** feedback على فترات قصيرة = نظام **أكثر استقرارًا**. فترات طويلة/غير منتظمة = ممكن **سلوك دوري (periodic)**.
  - ★ فقدان طاقة **مستمر** أضعف تأثيرًا من فقدان **دوري** بنفس الكمية الكلية.
- **أمثلة:**
  - **Caesar III:** اللاعب يدفع **tribute للإمبراطور** في لحظات محددة كل مهمة. الجدول ثابت لكل مهمة ومش متأثر بأداء اللاعب. فعليًا static friction **نادر جدًا وعالي** = "هزة" ضخمة في الاقتصاد (تفصيل في Ch.9).
  - **Monopoly:** الـ dynamic engine بيقاومه أنواع friction أهمها static friction عبر **Chance cards** (خسارة فلوس نادرة، أغلبها مش بيعتمد على ممتلكات اللاعب).
    - ★ **الإيجار للاعبين التانيين مش static friction، ده attrition:** المعدل بيتغير مع الوقت واللاعب له تأثير غير مباشر عليه (لما أنت كويس، خصومك مش كويسين، فبيقل الـ friction). الدياجرام من منظور لاعب واحد فمش مشتمل على ده. (الكتاب بيشير لـ Figure B.8 بالغلط، والصحيح B.6.)
- **Related:** يناسب static/converter engine أو engine building. بيتطور بـ dynamic friction أو slow cycle.
- **لموسفولك:** لو **rot** (من 2501) بيشتغل كـ drain تلقائي، نحدد: ثابت ولا عشوائي؟ وبتردد قصير (مستقر) ولا حدث نادر كبير (هزة زي tribute)؟ ده مقبض مباشر لـ difficulty tuning يتقاس بالبوت.

---

## B.6 Dynamic Friction ★★★

- **Type:** Friction. **Intent:** drain بيستهلك تلقائيًا، **معدله متأثر بحالة عناصر تانية**. **Motivation:** يقاوم الإنتاج لكن يتكيف مع أداء اللاعب. ★ **تطبيق كلاسيكي لـ negative feedback**.
- **Applicability:** موازنة ألعاب بتنتج موارد بسرعة زيادة، mechanism يقاوم الإنتاج ويتسكّل مع تقدم/قوة اللاعب، وتقليل فعالية الاستراتيجيات الطويلة لصالح القصيرة.
- **Consequences:** طريقة كويسة تقاوم الـ positive feedback. بيضيف negative feedback loop.
- **Implementation:**
  - ★★ **إيه اللي بيغيّر معدل الاستهلاك؟** ثلاث خيارات:
    1. كمية الطاقة المتاحة نفسها: **feedback سريع**.
    2. عدد upgrades في dynamic/converter engine.
    3. تقدم اللاعب نحو الهدف: غير مباشر وأبطأ.
  - ★★★ **تطابق خصائص الـ loops:** لو الـ positive والـ negative loops متشابهين (نفس السرعة والمتانة) = استقرار أكبر بكتير. لو فيه اختلاف كبير: **friction بطيء ومتين ضد positive feedback سريع وقصير بيدي return كويس في الأول** = اللاعبين يتقدموا بسرعة في الأول ثم يعانوا على المدى الطويل. ★ **أكتر توليفة شائعة: positive سريع + negative بطيء**.
- **أمثلة:**
  - **Tower defense:** الأعداء = dynamic drain على حياة اللاعب، والتحكم فيه ببناء أبراج. **هدف اللعبة هو منع الـ friction من إنه يأخذ مفعوله**. (استراتيجية اختيار الأبراج مش في الدياجرام.)
  - **Civilization (اقتصاد المدينة):**
    - المدينة بتنتج food وshields وtrade.
    - كل ما تكبر تحتاج food أكتر.
    - اللاعب يتحكم نسبيًا في نسبة food مقابل الموارد التانية (محدود بالأرض).
    - **food كتير بدري** = موارد أقل حاليًا لكن نمو أسرع.
    - ★ **النمو السريع مشكلة:** الـ happiness لازم تكون ≥ **نصف عدد السكان** وإلا الإنتاج يوقف بسبب **civil unrest**. المدينة تبدأ بـ happiness = 2.
    - طريقتان لزيادة happiness، وكلاهما بيعمل friction بـ profile مختلف:
      - **مباني خاصة:** بطيئة، استثمار عالي، **متينة**، return نسبيًا عالي.
      - **تحويل trade إلى culture:** **سريع** لكن return قليل نسبيًا.
    - إعدادات الـ culture والـ research **global** وبتأثر على كل المدن بالتساوي (كابشن Figure B.8).
- **Related:** بيوازن أي باترن بيعمل positive feedback وغالبًا جزء من multiple feedback. attrition بيطوّره لو ناتج عن تفاعل لاعبين. بيتطور بـ stopping mechanism.
- **لموسفولك:**
  - ★★ **امتلاء البرطمان هو dynamic friction طبيعي** (كل ما اتراكم، المساحة والوقت قلّوا): negative feedback سريع وبيعتمد على حالة اللعب.
  - **قاعدة السرعتين:** لو أي مكافأة/combo بيدي positive سريع والضغط بيجي بطيء ومتين، اللاعب يسمع حلاوة في الأول وبعدين يتخنق. البوت يقدر يرصد ده في منحنى النجاح.
  - **Civilization happiness** نموذج ممتاز لـ "النمو السريع بيكلف": نفس المنطق لو سمحنا بنمو سريع في جزء ما (دمج/rival).

---

## B.7 Stopping Mechanism ★★★ (aka Law of Diminishing Returns)

- **Type:** Friction. **Intent:** تقلل فعالية mechanism **كل مرة بيتفعّل**. **Motivation:** منع إساءة استخدام mechanism قوي. أحيانًا دايم، **وعادةً لأ**.
- **Applicability:** منع إساءة استخدام أفعال معينة، مقاومة dominant strategies، تقليل فعالية positive feedback mechanism.
- **Participants:** action بتنتج output، مورد energy مطلوب، الـ stopping mechanism اللي **بيزود التكلفة أو يقلل الـ output**.
- **Collaborations:** الـ action لازم يكون لها تكلفة طاقة أو تنتج موارد أو الاتنين.
- **Consequences:** ممكن يقلل أثر positive feedback loop بشكل كبير، وحتى **يخلي الـ return غير كافي**.
- **Implementation:**
  - ★★ **دايم ولا لأ؟** لو بتقيس قوة الـ stopping بـ **output متراكم** فالأثر **مؤقت**، واللاعب لازم **يتناوب** بين إنتاج الـ output واستخدامه في أفعال تانية.
  - ★★ **فردي ولا مشترك؟** لو بيأثر على لاعبين متعددين بالتساوي، اللعبة **بتكافئ اللي يستخدم الفعل الأول**، ويبقى فيه feedback حسب إن القائد ولا المتأخر هو اللي بيلعب الأول.
- **أمثلة:**
  - **Warcraft III (قطع الخشب):**
    - الفلاحين لازم ينقلوا الخشب للقاعدة ومش بيقطعوا أثناء النقل.
    - **المسافة للغابة** بتؤثر على الفعالية.
    - قطع الخشب بيصفّي الغابة فالمسافة تزيد.
    - معدل إنتاج كل فلاح **ينزل لـ 0.4** لما الغابة تقريبًا تخلص (كابشن Figure B.9).
    - "stopping mechanism خفي": ما بيتنظرش على إنه عقوبة.
  - **Power Grid (سعر الـ fuel):**
    - شراء fuel كتير يرفع السعر **على كل اللاعبين**.
    - القائد بيلعب **آخر** فالـ stopping بيدّي negative feedback قوي ضده.
- **Related:** متكرر في نظم multiple feedback. بيطوّر dynamic friction، ومتطوّر بـ slow cycle. (واستعماله في gameplay phases من الفهرس: ص269.)
- **لموسفولك:**
  - ★★★ **كل booster / re-roll / أداة قوية** تتفحص: هل فعاليتها بتقل أو تكلفتها بتزيد مع التكرار؟ ده يمنع إن اللاعب "يكسر" الليفل بأداة واحدة، وكمان يضبط **قيمة الإعلان الـ rewarded** (مش كل إعلان يدي نفس القوة).
  - الاختيار **مؤقت ولا دائم** قرار تصميمي: دايم = أشد.
  - في الـ rival contests: لو في آلية مشتركة، السؤال "مين يلعب الأول؟" بيحدد مين اللي بيستفيد (قاعدة Power Grid: القائد يلعب آخر).

---

## B.8 Attrition ★★

- **Type:** Friction. **Intent:** لاعبين **يسرقوا أو يدمّروا موارد بعض بنشاط**. **Motivation:** يخلي اللاعبين يتصارعوا على السيطرة وممكن يقصوا بعض.
- **Applicability:** تفاعل مباشر واستراتيجي بين لاعبين، وإدخال feedback في نظام طبيعته بتحددها **تفضيلات/نزوات اللاعبين**.
- **Participants:** لاعبين بنفس الـ mechanics، مورد strength (اللي يخسرها كلها يطلع)، **special attack action** بتسحب/تسرق strength.
- **Collaborations:** الهجوم **ممكن يكلّف strength وممكن لأ**، ولو مش بيكلّف لازم يطلب **وقت أو مهارة أو عشوائية**.
- **Consequences:**
  - ديناميكية عالية لأن اللاعبين بيتحكموا في القوة التدميرية.
  - ★★ **feedback تدميري (destructive)**، وممكن يكون **سلبي** (لما اللاعبين يتحالفوا ضد القائد) **أو إيجابي** (لما يهجموا ويقصوا الأضعف). ملحوظة الكتاب: constructive/destructive مش هو نفسه positive/negative.
- **Implementation:**
  - ★★★ **لازم الهجوم يكلّف استثمار مورد** (كان ممكن يتصرف في حاجة تانية). لو لأ، في لعبة لاعبين اتنين يتحول لـ **سباق تدمير بلا خيارات استراتيجية**. في multiplayer بيشتغل أحسن شوية لأن لازم تختار تهاجم مين.
  - تطبيق شائع: **موردين life وenergy**. الطاقة للأفعال، وخسارة الـ life = الخسارة. لازم يكونوا مرتبطين، غالبًا بصرف energy لكسب life، أو ضمنيًا عبر اختيار "إما أو" بينهم.
  - في لعبة لاعبين اتنين لازم أفعال تانية، وعادةً production mechanism للـ strength (فيتحول لـ **arms race**). RTS عندها كل ده.
  - شرط الفوز مش لازم يكون الإقصاء. نقاط أو هدف خارج الـ attrition بيوسّع الاستراتيجيات. بونص للهجوم/الإقصاء بيحفّز إقصاء الأضعف.
- **أمثلة:**
  - **Magic: The Gathering:**
    - كارت واحد في الدور.
    - الأفعال كلها (غير الأراضي) بتكلف **mana**.
    - مخلوقات تحارب مخلوقات، ولو مفيش فبتضرب اللاعب. خسارة كل الـ life = إقصاء.
    - **life وmana منفصلين.**
    - ★ **أنواع الـ drain:** direct damage = drain لحظي سريع ومباشر. استدعاء المخلوقات = **drain دائم متراكم** أضعف لكن مدمّر بالوقت.
    - الكروت في الإيد بتحدد الخيارات وقوتها، وبناء الـ deck جزء أساسي.
  - **Space Hulk (غير متماثل):**
    - لاعب بمجموعة space marines يحاول ينجز مهمة، والتاني بعدد غير محدود من genestealers يمنعه.
    - الـ genestealers بيفوزوا بتدمير عدد كافٍ من الـ marines.
    - الـ marines **غالبًا مبيفوزوش بتدمير genestealers** لكن لازم يتحكموا في عددهم لأنهم **بيقووا بزيادة أعدادهم**.
- **Related:** يشتغل مع أي engine. **Trade** بديل feedback multiplayer **constructive وسلبي تقريبًا دايمًا**. بيطوّر dynamic friction، ومتطوّر بـ arms race وworker placement.
- **لموسفولك:**
  - الـ **rival contests** حاليًا شكلها سباق نتيجة. **لو** اتضاف أي "تأثير على الخصم" (مثلًا إرسال عائق)، لازم **يكلف حاجة** وإلا اتحول لسباق تدمير. ده شرط حاسم.
  - ★ التمييز **destructive vs constructive** مفيد في تقييم حس الـ rival: مين بيتحفز يضرب القائد، ومين بيضرب الضعيف.
  - **Space Hulk (غير متماثل)** نموذج لمواجهة لاعب مقابل "مقاوم" بقواعد مختلفة، شبه ما يعمله الـ rival البوت.

---

## B.9 Escalating Challenge ★★

- **Type:** Escalation. **Intent:** التقدم نحو الهدف **بيزود صعوبة** التقدم اللاحق. **Motivation:** positive feedback loop بين تقدم اللاعب وصعوبة اللعبة. اللعبة **بتتكيف بسرعة مع مستوى المهارة**، خاصةً لما الأداء الجيد بيسرّع التقدم.
- **Applicability:** لعبة سريعة قائمة على المهارة (غالبًا جسدية) واللعبة بتصعب كل ما تتقدم. وعايز **mechanics ناشئة (emergent) تستبدل جزئيًا level progression مصمم مسبقًا**.
- **Participants:** targets (مهام غير محلولة)، progress، task (بتقلل الـ targets أو تنتج progress)، feedback mechanism (بيصعّب كل ما تتقدم أو الـ targets تقل).
- **Consequences:** loop موجب بسيط على الصعوبة، بيعدّل الصعوبة بسرعة. **لو فشل المهمة بينهي اللعبة، اللعبة بتبقى سريعة جدًا**.
- **Implementation:** الـ task عادةً بتتأثر بـ **مهارة اللاعب**. لو random/deterministic فاللاعب مفيش له تحكم، ولا بتشتغل إلا لو الباترن جزء من نظام أعقد واللاعب له تحكم غير مباشر في فرصة النجاح.
- **أمثلة:**
  - **Space Invaders:** كل غريب تقتله بيسرّع **كل الباقين**.
  - **Pac-Man:** مهمة أكل كل النقط، والأشباح بتصعّب الوصول للنقط الأخيرة.
- **Related:** مع static أو dynamic friction = لعبة بتطابق صعوبتها لقدرة اللاعب بسرعة.
- **لموسفولك:** ده منطق مفيد لـ **Endless / Daily** أو أي نمط بدون ليفلات مصممة: التقدم نفسه يصعّب. والـ bot_difficulty يقدر يقيس سرعة التطابق مع مهارة اللاعب.

---

## B.10 Escalating Complexity ★★★ (أقرب باترن لقلب Mossfolk)

- **Type:** Escalation. **Intent:** اللاعب يتصرف ضد **تعقيد متنامٍ**، يحاول يسيطر لحد ما الـ positive feedback يقوى زيادة والتعقيد المتراكم يخليه يخسر.
- **Motivation:** مهمة بتتعقد لو اللاعب فشل، والتعقيد نفسه بيزود صعوبتها. طول ما بتلاحق تفضل تلعب، **ولما الـ feedback يفلت تنتهي اللعبة بسرعة**. ومع التقدم الآلية المنتجة للتعقيد **بتتسارع**، فاللاعب لازم يخسر في لحظة ما.
- **Applicability:** لعبة ضغط عالي قائمة على المهارة، و**emergent mechanics تستبدل جزئيًا level progression مسبق**.
- **Participants:** اللعبة بتنتج complexity لازم تفضل تحت حد معين، task بتقلل التعقيد، **progress mechanism** بيزود إنتاج التعقيد بالوقت.
- **Collaborations:** التعقيد يزود فورًا إنتاج تعقيد أكتر = loop موجب قوي لازم يتسيطر عليه. اللاعب يخسر لما التعقيد يتخطى قدرته.
- **Consequences:** بمهارة كفاية اللاعب يلاحق لفترة طويلة، ولما ما يلحقش اللعبة **تنتهي بسرعة**.
- **Implementation:**
  - الـ task بتتأثر بمهارة اللاعب.
  - ★★ **عشوائية في إنتاج التعقيد** = **إيقاع متنوع**: اللاعب بيتعب في القمة وبياخد نفس لما الإنتاج يهدأ.
  - الـ progress mechanic يتراوح من زيادة بالوقت لبنية معقدة. ممكن **تدمجه مع escalating challenge** بإضافة positive feedback للـ progress نتيجة تنفيذ الـ task.
  - ★ **Multiple feedback:** التعقيد يغذي loops متعددة بـ signatures مختلفة. مثلًا توازن جزئي بإن الـ task تغذي loop سلبي **أبطأ بكتير** يتحكم في إنتاج التعقيد.
- **أمثلة:**
  - **Tetris:**
    - تدفق ثابت من tetrominoes = إنتاج تعقيد، مع **عشوائية خفيفة** في أنواعها.
    - اللاعب لازم يرتبهم بإحكام. خط كامل = يختفي ويفتح مكان.
    - لو ما لحقش، **الكومة تتراكم بسرعة** ويقل الوقت للقطع التالية، فيخسر لو وصلت للأعلى.
    - الـ progression = **levels**: كل **10 خطوط** ينتقل لليفل ويسرّع النزول (ده نفسه escalating challenge).
    - ★★ في الدياجرام (Fig B.13): tetrominoes تتحول لنقاط، **والنقاط ترتفع كل ما فيه tetrominoes أكتر** (إمكانية مسح خطوط أكتر مرة واحدة) = **استراتيجية high-risk high-reward**. الشارت يوضح إن لما الإيقاع يفوق قدرة اللاعب اللعبة **تلف خارج السيطرة بسرعة**.
  - **Super Crate Box:**
    - لاعب يجمع صناديق فيها أسلحة ويتحكم في عدد الأعداء بالقتل. لمس عدو = موت.
    - الأعداء بينزلوا من فوق لتحت ويختفوا. اللي يوصل لتحت **يظهر تاني من فوق أسرع كتير**.
    - سلاح واحد في المرة وغير متساويين في القوة، والطريقة الوحيدة للتقدم هي جمع صناديق وتغيير الأسلحة، فاللاعب مجبر يستغل أي حاجة معاه.
    - ★ **التناوب** بين مهمتين: قتل الأعداء للتحكم في أعدادهم، وجمع الصناديق للنقاط.
- **Related:** أي engine يصلح كـ progress mechanism. الـ progression غالبًا بيتطبق كـ escalating challenge.
- **لموسفولك:** ★★★
  - **البرطمان = escalating complexity بالكتاب:** الإسقاط بينتج تعقيد، والدمج بيقلله.
  - **نقطة Tetris الذهبية:** كمية أكبر في البرطمان = إمكانية cascade أكبر = **high-risk/high-reward**. نفحص إن ده موجود مصمم عن قصد عندنا.
  - **عشوائية الإنتاج = فترات التقاط نفس.** طابور القطع لازم يسيب "نفس" بشكل مقصود، مش مجرد RNG أعمى.
  - **ميزانية الإسقاطات ثابتة** فتكسر الـ spiral عمدًا: التعقيد مش بيتصاعد للأبد زي Tetris. ده يفرق بين ليفل بهدف وميزانية وبين endless.
  - **قياس الـ spiral في البوت:** نقطة اللا رجوع (لما التعقيد يتخطى قدرة اللاعب) تظهر في المنحنى، وتبقى مقياس لصعوبة الليفلات.
  - حقيقة Super Crate Box (الاضطرار للتناوب بين مهمتين) قابلة للتطبيق على تحديات **mossy/stones/rot** كمتطلب ثانوي يتناوب مع الدمج.

---

## B.11 Arms Race ★★

- **Type:** Escalation. **Intent:** لاعبين يستثمروا موارد لتحسين **قدراتهم الهجومية والدفاعية** ضد بعض. **Motivation:** خيارات استراتيجية كتير، واللاعب يختار استراتيجية تناسب مهاراته وتفضيلاته.
- **Applicability:** خيارات أكتر أو تجنب dominant strategies في ألعاب attrition، **إطالة زمن اللعب**، تشجيع أساليب لعب شخصية.
- **Participants:** لاعبين بنفس (أو مشابه) هجمات، strength، energy اختياري بتستهلكه الـ upgrades (وأحيانًا هي نفسها strength)، upgrade mechanism واحد على الأقل.
- **Collaborations:** الهجوم والـ upgrade بيطلبوا استثمار طاقة أو وقت.
- **Consequences:**
  - خيارات كتير = صعب الـ balance.
  - ★★ **الأفضل intransitive (حجر-ورقة-مقص)** في خيارات الـ upgrade عشان لكل استراتيجية counter: مشاة ثقيلة تهزم الفرسان، الفرسان تهزم المدفعية، المدفعية تهزم المشاة. **أفضل تركيبة جيش بتتحدد جزئيًا باختيارات الخصم.**
  - اللاعب يستخدم الـ mechanism اللي بيحبه ويتجاهل اللي مش بيحبه = أساليب لعب شخصية.
  - ★ **بيطوّل اللعبة** لأن اللاعب دايمًا يقدر يلعب دفاعي في الأول، وده ممكن يأخّر المواجهة كتير.
- **Implementation:**
  - ★★ **strength = energy** (نفس المورد): اللاعب ممكن يستثمر زيادة ويعرّض نفسه للخطر، خصوصًا لو الـ upgrades بياخدوا وقت.
  - **منفصلين:** لازم تفكر في علاقتهم: strength تحدد معدل إنتاج energy (**loop موجب تدميري قوي**)، أو energy تتحول لـ strength، أو تتستثمر لإنتاج strength بالوقت.
  - ★★ **لمنع الإطالة الزيادة:** خلّي مورد الـ upgrades **متنازع عليه بشدة** (كل اللاعبين بيحصدوا نفس الموارد) أو الـ upgrades بتطلب استثمار strength.
  - مش لازم متماثل، لكن أصعب في الـ balance.
- **أمثلة:**
  - **StarCraft II وWarcraft III:** تكنولوجيا تحسن الوحدات. strength = **مجموع الوحدات والمباني**، والطاقة بيحصدها العمال وتتصرف على الـ upgrades والبناء.
  - **Tower defense (غير متماثل):** آلية زرقاء تزود قدرة اللاعب الهجومية، وآلية خضراء تزود قدرة الأعداء. في الألعاب الحقيقية في upgrade mechanisms أكتر (ترقية أبراج، أنواع أبراج مختلفة، موجات بأنواع أعداء مختلفة تحتاج رد مختلف).
- **Related:** يتماشى مع dynamic engine لإنتاج energy وstrength (RTS). بيطوّر attrition، ومتطوّر بـ worker placement.
- **لموسفولك:**
  - ★★ **tower defense غير المتماثل = علاقة المصمم باللاعب في الليفلات:** تحديات **mossy shells / stones / rot** هي الجانب "الأخضر" (العدو)، وأدوات اللاعب هي "الأزرق". قاعدة الـ intransitive: **كل تحدي له counter واضح** (مش بالضرورة بوستر مدفوع). والبوت يقيس إن ولا تحدي بيكسر كل الأدوات.
  - لو rival contests اتطورت لعدّة استراتيجيات، نختبر dominant strategy بنفس منطق الباترن.

---

## B.12 Playing Style Reinforcement ★★ (aka RPG elements)

- **Type:** Miscellaneous. **Intent:** بـ feedback **بطيء، موجب، constructive** على أفعال اللاعب، اللعبة تشجع التخصص وتتكيف تدريجيًا مع أسلوب لعبه المفضل.
- **Motivation:** الـ avatar أو الوحدات بتتطور بالوقت. الأفعال نفسها بتغذي الآلية فالـ avatar **يتخصص** في مهمة معينة. طول ما فيه **استراتيجيات وتخصصات متعددة قابلة للتطبيق** هيعكس تفضيلات اللاعب.
- **Applicability:** استثمار طويل المدى **عبر جلسات متعددة**، مكافأة البناء والتخطيط المسبق واستراتيجيات شخصية، وتنمية دور/استراتيجية محددة.
- **Participants:** actions نجاحها يعتمد جزئيًا على خصائص الشخصية، مورد **ability** بتؤثر على فرصة النجاح وبتنمو، مورد **experience points** اختياري (بعض الألعاب تسميها skill points وعندها XP منفصلة لا تتبادل).
- **Collaborations:** الـ ability تأثر على نسبة نجاح الأفعال. المحاولة تولّد XP أو تحسّن ability مباشرة (بعض الألعاب تشترط نجاح الفعل وبعضها لأ). XP ممكن تتصرف على تحسين ability.
- **Consequences (ستة):**
  1. بيشتغل أفضل في ألعاب **متعددة الجلسات وطويلة المدى**.
  2. ★★ بيشتغل بس لو **استراتيجيات وأساليب متعددة قابلة للتطبيق**، وإلا الكل يستخدم نفس الاستراتيجية.
  3. ★★ بيشجع **min-maxing**: البحث عن أقوى تركيبة بأسرع وقت. لو نجح ده بيبقى dominant strategy، وبيحصل لما قوة الـ feedback مش موزعة بالتساوي على الأفعال والاستراتيجيات.
  4. بيفضّل اللاعبين الخبراء (فاهمين الخيارات وعواقبها طويلة المدى).
  5. ★★ **بيكافئ اللي بيقدر يستثمر أكبر وقت**: الوقت ممكن يعوّض فروق المهارة، وده **تأثير مرغوب أو غير مرغوب**.
  6. تغيير الاستراتيجية بالوقت مكلف لأن اللاعب بيخسر استثمار الأسلوب السابق.
- **Implementation:**
  - ★★★ **XP ولا لأ؟**
    - **مع XP:** مفيش ربط مباشر بين النمو والفعل، فاللاعب يحصد XP باستراتيجية ويطور مهارات لاستراتيجية تانية.
    - **من غير XP:** لازم توازن الـ feedback حسب تكرار الفعل: **الأفعال الأكتر تكرارًا feedback أضعف** من اللي بتتمارس نادرًا.
  - RPGs feedback loops بطيئة غالبًا وموازنة بـ escalating challenge أو dynamic friction أو stopping mechanism لتجنب التقدم السريع. التوازن المعتاد: **سريع في الأول ويبطئ تدريجيًا** لأن XP المطلوبة تزيد أُسيًّا.
  - ★★★ **هل لازم النجاح؟**
    - **نجاح مطلوب:** الـ loop أقوى، فالأفضل إن صعوبة المهام تأثر على النجاح، وتحدي بمستويات صعوبة متنوعة يخلي اللاعب يدرب شخصيته.
    - **نجاح غير مطلوب:** اللاعب يحسّن قدرات مهملة في مراحل أصعب، **لكن** ممكن يكرر فعل في كل فرصة (نتائج غير مقصودة/مضحكة، خصوصًا لو الفعل قليل المخاطرة).
- **أمثلة:**
  - **Warhammer Fantasy Role-Play وVampire: The Masquerade:** XP لتحقيق أهداف، تتصرف على تحسين قدرات الشخصية.
  - ★ **Dungeons & Dragons الأصلية لا تملك** playing-style reinforcement: XP تتجمع للوصول لليفل، لكن اللاعب **مالوش تأثير** على كيفية تحسن قدرات الشخصية عند الترقي.
  - **The Elder Scrolls IV: Oblivion:** تقدم الـ avatar مربوط مباشرة بأفعاله، **القدرة = عدد مرات تنفيذ الفعل المرتبط**. تطبيق **من غير XP**.
  - **Civilization III:** طرق فوز متعددة (عسكري/اقتصادي/ثقافي/علمي أو توليفة). اللاعب يعزز استراتيجيته ببناء تحسينات وعجائب. **موارد زي الفلوس والإنتاج تلعب دور الـ XP**، مش مربوطة باستراتيجية واحدة، والفلوس من مدينة تتصرف على إنتاج مدينة تانية.
- **Related:** لو معتمد على نجاح الأفعال فالـ feedback قوي، وغالبًا يتستخدم **stopping mechanism** لرفع سعر الـ upgrades.
- **لموسفولك:**
  - لو أي نظام ترقية/تطوير في الـ meta أو الـ side quests، لازم يتفحص بالـ 6 consequences. خصوصًا **#5 (الوقت يعوّض المهارة)**، لأنه يمس مباشرة قرارات الـ monetization والـ progression (ينفع أو يضر).
  - سؤال التصميم: **XP ولا من غير؟** والباترن بيقول: لو من غير XP، الأفعال المتكررة تاخد feedback أضعف.

---

## B.13 باترنز موجودة في النسخة الأونلاين بس (مفيش وصف في الجزء ده)

- **Multiple Feedback** و**Trade** و**Worker Placement** و**Slow Cycle**: الكتاب بيحيل كل واحد لـ www.peachpit.com/gamemechanics. **الوصف الكامل مش في النص اللي معايا**، فمتسجّلوش من عندي.
- اللي نعرفه من الباترنز التانية عنهم:
  - **Slow Cycle:** بيطوّر static friction وstopping mechanism وstatic engine. بيستعمل في gameplay phases (الفهرس ص160–161، 268).
  - **Trade:** بديل multiplayer feedback **constructive وسلبي تقريبًا دايمًا** مقابل attrition.
  - **Worker Placement:** بيطوّر engine building وdynamic/converter engine وattrition وarms race.
  - **Multiple Feedback:** بيتضمن stopping mechanism وdynamic friction، وبيتستخدم في gameplay phases (ص269) وCaesar III.
- ★ لو وصلت نسخ الأونلاين بعد كده، تتسجل في جزء منفصل.

---

## Appendix C — Getting Started with Machinations ★

- 3 أسطر: ده تيوتوريال أونلاين (peachpit.com/gamemechanics) على واجهة الـ Machinations Tool (محرر ومحاكي رسومي من Joris Dormans). بيشرح الـ UI وبناء diagram خطوة بخطوة. **الباقي تيوتوريال أداة، متجاهل.**
- **لموسفولك:** الأداة نفسها مرتبطة بفكرة رسم نموذج اقتصاد الليفل ومحاكاته، وده قريب من شغل التيستر-بوت. نراجعها لو قررنا نرسم دياجرامات.

---

## المراجع (References) ★ — قايمة قراءة

المعلومة هنا إن الكتاب بيبني على الأعمال دي. أهمها بالنسبة لنا:

- **أساس الباترنز:** Alexander et al. 1977 *A Pattern Language* (أصل فكرة الـ pattern language). Gamma/Helm/Johnson/Vlissides 1995 *Design Patterns* ("Gang of Four" في البرمجة). Björk & Holopainen 2005 *Patterns in Game Design*. Kreimeier 2002 "The Case for Game Design Patterns" و2003 "Game Design Methods: A 2003 Survey". Church 1999 "Formal Abstract Design Tools".
- **Feedback وديناميكيات:** LeBlanc 1999 "Formal Design Tools: Feedback Systems and the Dramatic Structure of Completion". Wright 2003 "Dynamics for Designers" (GDC). Cook 2007 "The Chemistry of Game Design". Hopson 2001 "Behavioral Game Design".
- **Emergence وprogression:** Juul 2002 "The Open and the Closed: Games of Emergence and Games of Progression". Juul 2005 *Half-Real*. Jenkins 2004 "Game Design as Narrative Architecture". Fromm 2005 "Types and Forms of Emergence". Wolfram 2002 *A New Kind of Science*. Ball 2004 *Critical Mass*. Ashmore & Nitsche 2007 "The Quest in a Generated World".
- **تصميم عام:** Adams 2009 *Fundamentals of Game Design* (2nd ed.). Crawford 1984 *The Art of Computer Game Design*. Koster 2005 *A Theory of Fun for Game Design* وKoster 2005 "A Grammar of Gameplay". Smith 2001 "The Future of Game Design" وSmith 2003 "Orthogonal Unit Differentiation" (GDC). Bogost 2006 *Unit Operations*. Caillois 1958 *Man, Play, and Games*. Poole 2000 *Trigger Happy*. Grünvogel 2005 "Formal Models and Game Design". Järvinen 2003 "Making and Breaking Games: A Typology of Rules". Sheffield 2007 "Defining Games: Raph Koster's Game Grammar". Guttenberg 2006 "An Academic Approach to Game Design: Is It Worth It?". Elrod 2011 "So You Wanna Call Yourself a Game Designer?". Wardrip-Fruin 2009 *Expressive Processing*.
- **سيميوتكس وتواصل:** Peirce 1932 وSaussure 1915 وEco 1976/2004 وJakobson 1960 (Linguistics and Poetics) وChomsky 1972 وFiske 2011.
- **Serious games والتعلّم:** Beck & Wade 2006 *The Kids Are Alright*.
- **متفرقات:** Vogler 1998 *The Writer's Journey* (الـ hero's journey)، Rand 1964 *The Virtue of Selfishness*، Saint-Exupéry 1939 *Wind, Sand and Stars* (اقتباس "less is more" من الفصل التاني)، Shannon 1950 "Programming a Computer for Playing Chess".
- **لموسفولك:** أولوية قراءة لو عايزين نتعمق: LeBlanc (Feedback Systems)، Wright (Dynamics for Designers)، Koster (Theory of Fun)، Juul (Open & Closed)، وHopson (Behavioral Game Design — صلته بالـ retention والمكافآت).

---

## الفهرس (Index) ★ — خريطة لباقي الكتاب

الفهرس نفسه مش محتوى، لكن بيكشف أماكن مواضيع في الأجزاء التانية. الأهم:

- **Machinations:** nodes وgates وpools وregisters وdelays وqueues وintervals وmultipliers وreverse triggers، وأوامر الـ artificial players (fire(node)، fireAll()، fireRandom()، fireSequence()، activate، deactivate، endTurn، stopDiagram، Quick Run). **الباقي أداة، متجاهل.**
- **Case studies (ص179–219):** Monopoly (ص179–187: deterministic version، تأثير الحظ، rent balance، property tax، dynamic friction)، **SimWar** (ص187–195: rush مقابل turtle، تكلفة المصانع، tweaking values)، **Caesar III** (ص199–206: مثال لـ converter engine وdynamic friction وengine building وmultiple feedback)، **Lunar Colony** (ص206–219: dynamic engine + converter engine + engine building).
- **Progression:** lock-and-key (ص247–258)، producing progress indirectly (**Settlers of Catan** ص263–265)، gameplay phases وemergent progression (ص265–269)، skill atoms (ص238–240)، Kihon/Kata/Kumite (ص241–244).
- **Emergence/complexity:** cellular automata، Game of Life (ص53–56)، emergence categories (nominal / weak / strong / intentional / multiple).
- **تصنيفات مفيدة:** Economic functions (sources/drains/converters/traders)، RTS mechanics (building/fighting/harvesting)، FPS economy، RPG elements، racing games rubber banding.
- **السيميوتكس والمعنى (Ch.12 تقريبًا):** icon/index/symbol، analogous مقابل symbolic simulation، intertextual irony (Grand Theft Auto III وSan Andreas)، Bioshock (طبقات: physical/moral/political)، September 12 وTrain وPeaceMaker وAmerica's Army.
- **تلميحات تصميم عابرة في الفهرس:** "make the toy first" (ص15)، reference games (ص21)، tech demos (ص20)، paper prototyping مزاياه وعيوبه (ص17–19)، "less is more" (ص291–294)، ومبدأ **اقتصاد اللعبة كأداة للتحكم في gameplay** (ص75–76).
- **لموسفولك:** نستخدم الفهرس كمرجع سريع لما نذاكر الأجزاء 1–6 و8، وفحص تقاطع الأمثلة (Tetris، Monopoly، Settlers) بين الأجزاء.

---

## خريطة علاقات الباترنز (من حقول Related) ★★★

- **Static Engine** → بيتطور بـ Dynamic Engine وConverter Engine وSlow Cycle. وweak static engine **حماية** لـ Converter Engine من الـ deadlock.
- **Dynamic Engine** → بيطوّر Static Engine. متطوّر بـ Engine Building وWorker Placement. بيتقاومه Dynamic Friction وAttrition، وStatic Friction بتبالغ في ميزته.
- **Converter Engine** → بيطوّر Static Engine. متطوّر بـ Engine Building وWorker Placement. أنسب لـ Engine Building.
- **Engine Building** → بيطوّر Dynamic/Converter Engine. متطوّر بـ Worker Placement. Multiple feedback على الـ building يزود الصعوبة، وكل Friction patterns توازنه.
- **Static Friction** → أنسب مع Static/Converter Engine أو Engine Building. متطوّر بـ Dynamic Friction أو Slow Cycle.
- **Dynamic Friction** → متطوّر بـ Stopping Mechanism. Attrition بيطوّره (لو الناتج تفاعل لاعبين). غالبًا جزء من Multiple Feedback.
- **Stopping Mechanism** → بيطوّر Dynamic Friction. متطوّر بـ Slow Cycle. متكرر في Multiple Feedback.
- **Attrition** → بيطوّر Dynamic Friction. متطوّر بـ Arms Race وWorker Placement. بيشتغل مع أي engine، وTrade بديله الـ constructive.
- **Arms Race** → بيطوّر Attrition. متطوّر بـ Worker Placement. يشتغل مع Dynamic Engine (RTS).
- **Escalating Challenge** → يتدمج مع Static/Dynamic Friction لمطابقة الصعوبة بسرعة. غالبًا بيطبّق الـ progression في Escalating Complexity.
- **Escalating Complexity** → أي engine ممكن يكون الـ progress mechanism.
- **Playing Style Reinforcement** → لما يعتمد على نجاح الأفعال، يتستخدم Stopping Mechanism لرفع سعر الـ upgrades.

**الباترن ورا الخريطة:** الـ engines بتنتج، الـ frictions بتقاوم، والـ escalations بتخلي المقاومة نفسها لعبة. المصمم يختار توليفة بحيث الـ positive feedback ما يهزمش الـ negative، أو العكس.

---

## ملخص تطبيقي سريع لموسفولك (ترتيب أولويات)

1. ★★★ **Escalating Complexity (B.10):** هو وصف قلب اللعبة. نتأكد من الـ high-risk/high-reward cascade وإيقاع الـ breather، وبنستعمل نقطة اللا رجوع كمقياس للبوت.
2. ★★★ **Static Engine (B.1):** ميزانية الإسقاطات، وبند "نفس العشوائية لكل اللاعبين" في الـ rival contests (نفس seed).
3. ★★★ **Dynamic Friction (B.6) + قاعدة تطابق الـ loops:** امتلاء البرطمان، وتجنب positive سريع مع negative بطيء ومتين.
4. ★★★ **Stopping Mechanism (B.7):** على الـ boosters والـ rewarded ads والـ re-rolls.
5. ★★ **Attrition (B.8):** أي تفاعل بين الـ rivals لازم يكلف، وإلا سباق تدمير.
6. ★★ **Arms Race (B.11):** كل تحدي (mossy/stones/rot) له counter، والبوت يختبر الـ dominant strategies.
7. ★★ **Converter Engine (B.3):** لو فيه اقتصاد meta، لازم weak static engine ضد الـ soft-lock (منسجم مع خط "مفيش حاجة تمنع اللعب").
8. ★★ **Playing Style Reinforcement (B.12):** لو فيه ترقيات meta، نفحص "الوقت يعوّض المهارة" والـ dominant strategy.
9. ★★ **Static Friction (B.5):** لو

# Game Mechanics: Advanced Game Design (Adams & Dormans) — الجزء 8/8 — نوتس مذاكرة

**المصدر:** آخر الملحق B (Design Pattern Library، ص B-11 → B-43) + الملحق C كامل (Getting Started with Machinations، C-1 → C-29). الحجم حوالي 62 صفحة (PDF 381–442).

**ملحوظة ترقيم:** مفيش ترقيم فصول سابق في السياق (الـ exemplar كان ترقيم فيديوهات). عشان كده رقّمت أقسام الجزء ده 1→14 وحطيت أرقام صفحات الكتاب. أول جملة في الجزء مقطوعة من نص جملة قبلها (آخر Engine Building). المصدر ما بيقولش أنهي لعبة، فمش هخمّن.

---

## 1. تكملة Engine Building (آخر الباترن، ص B-11→12) ★★

- الفكرة المتبقية: **multiplayer game اللاعيبة فيه بيتنافسوا على عدد محدود من المراكز (positions)**. كل مركز بيسمح بفعل مختلف يحسّن الـ engine، فهم بيتنافسوا على **building mechanics مختلفة**. النتيجة: **multiplayer dynamic قوي بيدي جزء كبير من الـ gameplay**.
- **Related Patterns:**
  - تطبيق **multiple feedback** على الـ building mechanisms = أحسن طريقة **تزوّد صعوبة** engine building.
  - **كل أنماط الـ friction** مناسبة توازن الـ positive feedback المعتاد لـ engine building اللي بيستهلك energy عشان يفعّل الـ building mechanisms.
  - **Dynamic engine** = أبسط implementation ممكن لـ engine building.
  - Engine building **بيوسّع (elaborates)** الـ dynamic engine والـ converter engine.
  - Engine building **بيتوسّع بـ worker placement**.
- **الباترن ورا الباترن:** المراكز المحدودة + منافسة = **صراع غير مباشر** من غير هجوم مباشر (نفس منطق worker placement، قسم 12).
- **لموسفولك:** الـ rival contests لو فيها «مراكز/فرص محدودة» يتنافس عليها اللاعب والمنافس، تبقى بتولّد multiplayer dynamic بدون attrition مباشر.

---

## 2. Static Friction (B-12→13) ★★★ — drain ثابت بيقاوم الإنتاج

- **Type:** Friction. **Intent:** drain بيستهلك تلقائيًا resources اللاعب منتجها.
- **Motivation:** بيعاكس الـ production mechanism باستهلاك **دوري**. معدل الاستهلاك **ثابت أو فيه randomness**.
- **Applicability:**
  - عايز mechanism يقاوم الإنتاج **لكن اللاعب يقدر يتغلب عليه في الآخر**.
  - عايز **تضخّم مكاسب الاستثمار طويل المدى في ترقيات dynamic engine**.
- **Participants:** resource (energy) + static drain + production mechanism + actions تانية بتستهلك energy. الـ drain بيستهلك **برّه سيطرة اللاعب المباشرة**.
- **Consequences:** طريقة بسيطة نسبيًا تقاوم الـ positive feedback بتاع الـ engine patterns. بس **بتبرّز الاستراتيجية طويلة المدى**، لأنها بتقلل الـ output الابتدائي ومش بتأثر على الترقيات.
- **Implementation (قرارات تصميمية):**
  - **ثابت vs عشوائي:** الثابت أسهل فهمًا وأكتر قابلية للتوقع. العشوائي بيضيف **noise** في السلوك الديناميكي، وممكن يبقى **بديل لإن الـ randomness تبقى في الإنتاج**.
  - **التردد (frequency):** feedback على فترات قصيرة = نظام **أكتر استقرارًا**. على فترات طويلة أو غير منتظمة = ممكن يطلع **سلوك دوري (periodic)**.
  - ★ **قاعدة عامة:** خسارة energy **مستمرة** أضعف في تأثيرها الديناميكي من خسارة **دورية** بنفس الكمية.
- **أمثلة:**
  - **Caesar III:** اللاعب بيدفع **tribute للإمبراطور** في لحظات محددة في كل mission. الجدول **ثابت لكل mission ومش متأثر بأداء اللاعب**. النتيجة: static friction **نادر جدًا وعالي** بيعمل «**هزة ضخمة**» في اقتصاد اللعبة (Ch.9).
  - **Monopoly:** الـ dynamic engine فيه بيتقاوم بأنواع friction. الـ static friction = **كروت Chance** (اللاعب بيخسر فلوس نادرًا). بعضها بيراعي ممتلكات اللاعب، **أغلبها لأ**.
  - ★★ **تمييز دقيق:** دفع **الإيجار (rent)** للاعيبة تانيين شكله static friction (التكرار والحدّة برّه تحكم اللي بيدفع)، **لكنه attrition مش static friction**. السبب: معدله **بيتغير مع الوقت** واللاعب له **تأثير غير مباشر** عليه. لو لاعب ماشي كويس غالبًا خصومه لأ، وده بيأثر سلبًا على الـ friction. الدايجرام (Fig B.6) مش بيعرضه لأنه مرسوم من وجهة نظر لاعب واحد. *(المتن بيشير لـ B.8 والصورة اسمها B.6 — غلطة في الكتاب.)*
- **Related:** الأنسب مع **static engine / converter engine / engine building**، لأنه بيضخّم الاستثمار طويل المدى. بيتوسّع بـ **dynamic friction** أو **slow cycle**.
- **الباترن ورا الباترن:** الـ static friction بيأثر على **الإنتاج الابتدائي بس** والترقيات بتفلت منه. فاللاعب اللي بيستثمر بدري بيتفوق، يعني **بيكافئ الصبر والتخطيط**.
- **لموسفولك:** لو الـ **rot** (من 2501) بيتقدم بإيقاع ثابت مستقل عن أداء اللاعب، فده static friction: مقروء ومتوقع، وبيرفع قيمة التخطيط. الأقصر والمنتظم أثبت من الضربات النادرة (زي tribute بتاع Caesar). **تحذير:** الباترن ده جوه الليفل بس. أي drain زمني بين الجلسات = energy system وده ضد خط حسام.

---

## 3. Dynamic Friction (B-14→16) ★★★ — negative feedback كلاسيكي

- **Intent:** drain بيستهلك تلقائيًا، **ومعدله بيتأثر بحالة عناصر تانية** في اللعبة. **Motivation:** بيقاوم الإنتاج **ويتكيّف مع أداء اللاعب**. تطبيق كلاسيكي لـ **negative feedback**.
- **Applicability:**
  - لعبة الـ resources فيها بتتنتج **بسرعة زيادة**.
  - mechanism بيقاوم الإنتاج و**بيتدرّج تلقائيًا مع تقدم/قوة اللاعب**.
  - **تقلل فعالية الاستراتيجيات طويلة المدى** (بتاعة dynamic engine) **لصالح القصيرة**. ده عكس static friction.
- **Participants:** resource + dynamic drain + production mechanism + actions تانية. الـ drain **برّه تحكم اللاعب لكن بيتأثر بحالة عنصر واحد على الأقل**.
- **Consequences:** طريقة كويسة تقاوم positive feedback، وبتضيف **negative feedback loop** للنظام.
- **Implementation:**
  - **إيه اللي بيغيّر معدل الاستهلاك؟** ثلاث اختيارات:
    - كمية الـ **energy المتاحة نفسها**: الـ negative feedback **سريع**.
    - **عدد ترقيات** dynamic/converter engine.
    - **تقدم اللاعب نحو الهدف**: الـ feedback **غير مباشر وأبطأ**.
  - ★★★ **قاعدة الاستقرار:** لما خصائص الـ positive loop والـ negative loop **متشابهة** (نفس السرعة، نفس الديمومة)، التأثير **أكتر استقرارًا بكتير** من لما الفرق كبير. مثال: friction **بطيء ودائم** ضد positive feedback **سريع بس مش دائم** وعائده الأول كويس = اللاعبين هيتقدموا كتير في الأول وبعدين **يعانوا على المدى الطويل**.
  - **أكتر تركيبة شائعة: fast positive + slow negative.**
- **أمثلة:**
  - **Tower defense:** الميكانيكس بتدور حوالين **dynamic drain على life points** بيسببه الأعداء، واللاعب لازم يسيطر عليهم ببناء tours. **هدف اللعبة إنك تمنع الـ dynamic friction من إنه يشتغل.** (استراتيجية اختيار نوع البرج محذوفة من الدايجرام.)
  - ★★ **Civilization (city production، Fig B.8):**
    - المدن بتنتج **food وshields وtrade**. كل ما المدينة تكبر بتحتاج food أكتر لسكانها.
    - اللاعب عنده تحكم في نسبة food مقابل الباقي، **محدود بالتضاريس**.
    - food كتير بدري = إنتاج أقل من الباقي في الأول **لكن نمو أسرع**.
    - **النمو السريع بيعمل مشكلة:** رضا المدينة (happiness) لازم يبقى **≥ نص السكان** وإلا الإنتاج يقف بسبب **civil unrest**. الـ happiness الابتدائي = **2**.
    - طريقتين لزيادة happiness، وكلتاهم بتعمل dynamic friction بـ profile مختلف:
      - **مباني خاصة:** بطيئة وبتتطلب استثمار عالي، لكنها **دائمة وعائدها عالي نسبيًا**.
      - **تحويل trade لـ culture:** **سريع لكن عائده قليل**.
    - إعدادات culture/research **global وبتأثر على كل المدن بالتساوي**.
- **Related:** حل كويس لأي pattern بيسبب positive feedback، وغالبًا **جزء من multiple feedback**. **Attrition** بيوسّع dynamic friction لما يكون نتيجة تفاعل لاعيبة. Dynamic friction بيتوسّع بـ **stopping mechanism**.
- **الباترن ورا الباترن:**
  - Static = يعاقب الابتداء ويكافئ الاستثمار. Dynamic = يعاقب التضخم **المتناسب** مع النجاح.
  - السر في **تطابق profiles** (سرعة/ديمومة) الـ loops. التفاوت بينها بيدي نمط «بداية قوية → انهيار».
- **لموسفولك:**
  - البرطمان نفسه فيه dynamic friction طبيعي: كل ما امتلأ، كل إسقاطة بقت أخطر.
  - لو بنربط الـ rot بالتقدم نحو الهدف أو بمستوى الامتلاء، ده feedback غير مباشر/أبطأ. التيستر-بوت لازم يسجّل **منحنى امتلاء البرطمان عبر الزمن** مش بس win/lose، عشان يظهر نمط «بداية ممتازة وانهيار متأخر».

---

## 4. Stopping Mechanism (B-17→19) ★★★ — Law of Diminishing Returns

- **Intent:** تقلل فعالية mechanism **كل ما يتفعّل**. اسمه التاني: Law of diminishing returns. **Motivation:** منع إساءة استخدام mechanism قوي. أحيانًا التقليل **دائم** لكن غالبًا **لأ**.
- **Applicability:** منع إساءة فعل معين، **مقاومة dominant strategies**، تقليل فعالية positive feedback.
- **Participants/Collaborations:** action بيطلع output + resource energy + الـ stopping mechanism اللي **بيرفع التكلفة أو بيقلل الـ output**. لازم الـ action يكون له تكلفة أو ينتج resources (أو الاتنين).
- **Consequences:** ممكن يقلل أثر positive feedback loop **جدًا** وحتى يخلي عائده **غير كافي**.
- **Implementation:**
  - **دائم ولا لأ؟** لو قوة الـ stopping اتقاست بـ **الـ output المتراكم**، التأثير مش دائم، واللاعب لازم **يبدّل كتير بين إنتاج الـ output واستخدامه**.
  - **فردي ولا مشترك؟** لو بيأثر على عدة لاعيبة بالتساوي، اللعبة **بتكافئ اللي يستخدم الـ action قبل غيره**. فبيتحول لـ **شكل feedback** حسب مين بيتحرك الأول: المتصدر ولا المتأخر.
- **أمثلة:**
  - **Warcraft III (قطع الخشب):** peasants بيقطعوا خشب وبينقلوه للقاعدة، ومبيقطعوش وهم بينقلوا. فالمسافة للغابة بتأثر. وبما إن قطع الخشب **بيفضّي الغابة**، **المسافة بتزيد** كل ما اللاعب يقطع أكتر. (Fig B.9: معدل إنتاج الـ peasant بينزل لـ **0.4** لما الغابة تقارب تخلص.)
  - **Power Grid (سوق الوقود):** اللاعب بيشتري وقود بفلوس وبيحرق وقود يولّد فلوس (positive loop). **شراء وقود كتير بيرفع السعر على كل اللاعيبة.** ولأن **المتصدر بيلعب آخر**، الـ stopping mechanism بيعمل **negative feedback قوي على المتصدر**.
- **Related:** كتير في أنظمة **multiple feedback**. بيوسّع **dynamic friction**. ممكن يتوسّع بـ **slow cycle**.
- **الباترن ورا الباترن:** الفعل الأكتر ربحية هو الأكتر عرضة للتضخم. الحل مش منعه، **خليه يتآكل باستخدامه**. وترتيب اللعب (مين الأول) بيحوّله لأداة rubber-banding.
- **لموسفولك:**
  - أي booster أو مكافأة extra drops بيتكرر استخدامها (خصوصًا من الإعلانات المكافأة، مثل «شوف إعلان خد drops زيادة») لازم تتآكل مع الاستخدام (تكلفة تتصاعد أو عائد يتناقص). كده تتجنب dominant strategy «شاهد إعلان واكسب».
  - شوف بردو لو في سلاسل merge combos: كل واحدة تفضل تدّي أكتر من اللي قبلها؟ ولو آه هل ده مقصود ولا لأ.

---

## 5. Attrition (B-19→23) ★★

- **Intent:** لاعيبة بيسرقوا أو يدمروا **بنشاط** resources بعض (اللي محتاجينها لأفعال تانية). **Motivation:** اللاعيبة يقدروا يقصوا بعض في صراع على الهيمنة.
- **Applicability:** تفاعل استراتيجي مباشر بين عدة لاعيبة + feedback في نظام طبيعته بتحددها **تفضيلات/نزوات اللاعيبة**.
- **Participants:** عدة لاعيبة بنفس (أو قريب) الميكانيكس والخيارات + **strength resource** (اللي يخسر كله يتشال) + attack action خاص بيستنزف أو يسرق strength الخصم.
- **Collaborations:** الهجوم **ممكن يكلف strength أو لأ**. لو مبيكلفش، لازم **يحتاج وقت أو مهارة أو عشوائية**. التوازن بين تكلفة الهجوم وفعاليته وفايدة الأفعال التانية هو اللي بيحدد هيمنة الـ attrition.
- **Consequences:** ديناميكية عالية جدًا لأن اللاعيبة بيتحكموا في قوة التدمير. غالبًا **destructive feedback** (حالة اللاعب بتستفز ردود فعل غيره). حسب شروط الفوز وحالة اللعبة ممكن يكون **negative** (اللاعيبة بيتآمروا على المتصدر) أو **positive** (بيهاجموا الأضعف ويتخلصوا منه).
- **ملحوظة التعريف:** constructive/destructive ≠ positive/negative (Ch.6، «Seven Feedback Characteristics»).
- **Implementation:**
  - ★★ **لازم الهجوم يتطلب استثمار resource** كان ممكن ينصرف في حاجة تانية. من غير كده، في لعبة اتنين = **سباق تدمير بقرارات استراتيجية قليلة أو معدومة**. في multiplayer اجتماعي الموضوع أفضل شوية لأن **اللاعيبة لازم يختاروا يهاجموا مين**.
  - **بيتنفذ كتير بموردين: life وenergy**: energy للأفعال، والخسارة لما life تخلص. لازم يكونوا **مرتبطين**: غالبًا تقدر تصرف energy لتكسب life، أو العلاقة ضمنية (اختيار بين الاتنين في نفس الوقت).
  - لعبة اتنين محتاجة **أفعال تانية**. غالبًا production mechanism لـ strength بيحسّن الدفاع/الهجوم (وده بيحوّله لـ **arms race**). الـ RTS فيها كل ده بأشكال متعددة.
  - **شرط الفوز مش لازم يكون الإقصاء**: نقاط أو هدف برّه الـ attrition = **استراتيجيات أكتر**. ولو في **bonus للهجوم أو الإقصاء**، الباترن بيحفز إقصاء الأضعف.
- **أمثلة:**
  - ★★ **Magic: The Gathering:** كل دور كارت واحد (lands، استدعاء creatures، شفاء، direct damage للخصم أو لـ creatures بتاعته). **كل الأفعال ما عدا lands تكلف mana.** كل ما mana أكتر، الأفعال أقوى. Creatures بتتقاتل، ولما مفيش أعداء بتضرب الخصم مباشرة. اللي life يخلص يتشال. **life وmana موردين منفصلين.**
    - **Direct damage:** استنزاف سريع ومباشر.
    - **استدعاء creatures:** استنزاف **دائم** على creatures وlife الخصم. أضعف عادةً لكنه **بيتراكم** وممكن يبقى مدمّر.
    - الكروت في الإيد بتحدد الخيارات وقوتها. **Deck building** مهم جدًا.
  - ★★ **Asymmetrical attrition — Space Hulk:** لاعب معاه حفنة space marines عشان يخلص mission، والتاني معاه **عدد غير محدود من genestealers** ومحاول يمنعه. الـ genestealers يفوزوا لما يدمروا marines كفاية. الـ marines **مش بيكسبوا غالبًا بتدمير genestealers** لكن لازم يحافظوا على عددهم تحت السيطرة لأن **الـ genestealers بتبقى أقوى كل ما عددها يزيد**.
- **Related:** شغال مع أي engine pattern. **Trade** = بديل multiplayer **constructive** وغالبًا **دايمًا negative**. بيوسّع dynamic friction. بيتوسّع بـ **arms race** و**worker placement**.
- **الباترن ورا الباترن:** الهجوم بقرار اللاعب يبقى مثير بس لو **ليه تكلفة فرصة**. الشرط ده هو الفرق بين strategy وسباق.
- **لموسفولك:**
  - الـ **rival contests** لو سباق نقاط صرف من غير أي قرار استثمار/توقيت، فده بالظبط «race with few/no strategic choices». المنافس في ليفل merge مفيش فيه هجوم مباشر، فالـ attrition هنا لازم يتترجم لشيء تاني: قرار **امتى تصرف booster أو إسقاطة معينة** بدل ما يتوفر مجانًا.
  - شرط الفوز غير الإقصاء (نقاط/هدف) بيفتح استراتيجيات، وده المتاح عندنا أصلًا.

---

## 6. Escalating Challenge (B-23→24) ★★★

- **Type:** Escalation. **Intent:** التقدم نحو الهدف **بيزود صعوبة** التقدم الإضافي. **Motivation:** positive feedback loop بين تقدم اللاعب وصعوبة اللعبة. اللعبة بتبقى أصعب كل ما اللاعب يقرب من هدفه، فبتتكيّف **بسرعة** مع مستوى مهارته (خصوصًا لو الأداء الكويس بيسرّع التقدم).
- **Applicability:**
  - لعبة **سريعة** معتمدة على **مهارة** (غالبًا جسدية)، بتصعب كل ما اللاعب يتقدم.
  - عايز **emergent mechanics** تحل (جزئيًا) محل level progression مصمم مسبقًا.
- **Participants:** targets (مهام لسه ما اتحلتش) + progress + task (يقلل targets أو ينتج progress) + **feedback mechanism** بيصعّب اللعبة مع التقدم/تقليل الـ targets.
- **Consequences:** positive feedback loop بسيط على الصعوبة، بيعدّل الصعوبة **بسرعة جدًا** على حسب المهارة. **لو فشل المهمة بينهي اللعبة، اللعبة بتخلص بسرعة.**
- **Implementation:** المهمة غالبًا **متأثرة بمهارة اللاعب**، خصوصًا لو الباترن هو أغلب الـ core. لو المهمة **عشوائية أو حتمية**، اللاعب ملوش تحكم في التقدم. دي بتبقى viable بس لو الباترن جزء من نظام معقد واللاعب عنده **تحكم غير مباشر في احتمال النجاح**. الـ multiplayer mechanics بتشتغل أحسن برضو في نظام معقد.
- **أمثلة:**
  - **Space Invaders:** لازم تدمر كل الغزاة قبل ما يوصلوا آخر الشاشة. **كل ما تدمر واحد، الباقيين بيسرّعوا شوية.**
  - **Pac-Man:** المهمة = أكل كل النقط، والأشباح اللي بتطاردك بتخلّي **آخر نقط أصعب وأصعب** (Ch.5).
- **Related:** ★★ بدمجه مع **static أو dynamic friction** تعمل لعبة **بتطابق صعوبتها مع قدرة اللاعب بسرعة**.
- **الباترن ورا الباترن:** الصعوبة مربوطة بـ **التقدم نفسه** مش بوقت أو رقم ليفل. اللاعب الأقوى بيتقدم أسرع فيتعاقب أسرع. فمنحنى الصعوبة بيتولّد من اللعب نفسه بدل ما يتصمّم يدويًا.
- **لموسفولك:**
  - ★★★ ده تقريبًا وصف «نهاية الليفل» عندنا: كل ما الهدف يقرب، البرطمان أكتر زحمة والإسقاطة أصعب. التيستر-بوت يقدر يقيس أثره: فرق صعوبة بين **أول 50% من الإسقاطات وآخر 50%** في نفس الليفل.
  - الباترن بيتصمم أصلًا لأجل fast-paced. لو الليفلات بتتحسب ببودجت إسقاطات (turn-style)، الأثر هيبقى أقل وضوحًا.

---

## 7. Escalating Complexity (B-25→28) ★★★ — الباترن اللي بيشبه لعبتنا أكتر

- **Intent:** اللاعيبة بيشتغلوا ضد **complexity متصاعدة**، بيحاولوا يسيطروا عليها لحد ما الـ positive feedback يقوى زيادة والـ complexity المتراكمة تخليهم يخسروا.
- **Motivation:** مهمة بتتعقد أكتر لو اللاعب فشل، والتعقيد نفسه بيزود صعوبتها. طالما اللاعب مواكب فهو بيكمل، لكن لما الـ feedback يخرج عن السيطرة اللعبة بتخلص بسرعة. ولما اللعبة تتقدم، **الـ mechanism المنتج للتعقيد بيتسارع**، يعني **حتمًا في لحظة اللاعب مش هيقدر يواكب ويخسر في الآخر**.
- **Applicability:** لعبة **high-pressure** معتمدة على مهارة + emergent mechanics بدل level progression مصمم.
- **Participants:** اللعبة بتنتج **complexity** لازم تتحفظ تحت حد + task للاعب بيقلل التعقيد + **progress mechanism** بيزود إنتاج التعقيد مع الوقت.
- **Collaborations:** التعقيد **فورًا** بيزود إنتاج تعقيد أكتر = **strong positive feedback loop** لازم يتسيطر عليه. اللاعب يخسر لما التعقيد يفوق قدرته على إدارته.
- **Consequences:** مع مهارة كافية اللاعب يواكب **فترة طويلة**، ولما يبطل يواكب، التعقيد يخرج عن السيطرة واللعبة تنتهي بسرعة.
- **Implementation:**
  - نفس قاعدة المهارة/العشوائية بتاعة escalating challenge.
  - ★★★ **عشوائية في إنتاج التعقيد = إيقاع متنوع:** اللاعب يتكافح عند الذروة وياخد نَفَسه لما إنتاج التعقيد يهدّى شوية.
  - **الـ progress mechanic** ممكن يبقى بسيط (زيادة مبنية على الوقت) أو معقد بيعتمد على أفعال اللاعب أو لاعيبة تانيين. وممكن **تدمجه مع escalating challenge** بإضافة positive feedback للـ progress mechanic من تنفيذ المهمة.
  - مناسب جدًا كجزء من **multiple feedback** (التعقيد بيغذّي عدة loops بـ signatures مختلفة). مثال: توازن جزئي بإن المهمة تغذّي **negative feedback loop أبطأ بكتير** بيحكم إنتاج التعقيد.
- **أمثلة:**
  - ★★★ **Tetris:**
    - تدفق ثابت من tetrominoes = إنتاج التعقيد. فيه **عشوائية بسيطة** في أنواعها.
    - اللاعب يرتبهم عشان يتلاءموا. لما صف يتملى بيختفي ويعمل مساحة.
    - لو اللاعب فشل، القطع **بتتكوّم بسرعة** وبيبقى عنده وقت أقل للقطع الجاية. التعقيد بيزيد بسرعة وبيخسر لو الكومة وصلت آخر الشاشة.
    - **التقدم:** كل **10 صفوف** = ليفل جديد والقطع بتنزل أسرع، وده في نفس الوقت مثال على escalating challenge.
    - Fig B.13: tetrominoes بتتحوّل لنقاط. النقاط بتزيد لما القطع أكتر في اللعبة (إمكانية تمسح صفوف أكتر مرة واحدة = استراتيجية **high-risk, high-reward**). التشارت بيوضح إن لما الإيقاع يكبر على اللاعب، **اللعبة بتنهار بسرعة**.
  - ★★ **Super Crate Box (indie action shooter):**
    - اللاعب بيلم **صناديق فيها أسلحة مختلفة** وفي نفس الوقت بيحافظ على عدد الأعداء تحت السيطرة بإنه يضربهم. **لمس عدو = موت.**
    - الأعداء بيظهروا فوق ويجروا لتحت ويختفوا. **عدو وصل لتحت بيظهر تاني فوق لكن أسرع بكتير** في المرة التانية.
    - اللاعب بيشيل سلاح واحد بس في المرة، والأسلحة مش متساوية في القوة. لكن **الطريقة الوحيدة للتقدم هي لم الصناديق وتغيير السلاح**، فاللاعب مجبر يستفيد من أي حاجة بيلاقيها.
    - لازم **يتبادل** بين قتل الأعداء (للسيطرة على عددهم) ولم الصناديق (للنقاط). (Fig B.14.)
- **Related:** أي engine pattern ينفع يتنفذ بيه الـ progress mechanism. شائع إن **progression mechanism يتنفذ كـ escalating challenge**.
- **الباترن ورا الباترن:**
  - Tetris/SCB بيعتمدوا على **تبادل بين مهمتين متعارضتين** (قلل التعقيد vs اكسب نقاط).
  - الـ **randomness بتصنع تنفس** بدل ما تصنع ظلم.
  - الخسارة بتبقى **انهيار سريع مش تدهور بطيء**، فالـ session بتخلص ومفيش مماطلة.
- **لموسفولك:**
  - ★★★ **جار الـ merge = escalating complexity بالتعريف:** المخلوقات المتراكمة = complexity، الـ merge = task بيقللها، والـ positive feedback جاي من الفيزياء (كومة غير مستقرة → إسقاطة أسوأ → تعقيد أكتر).
  - الاختلاف المهم: عندنا **ما فيش auto-production بزمن**، الإنتاج بتحكمه إسقاطات اللاعب وبودجتها. وبالتالي:
    - **تسلسل الـ drops العشوائي = عشوائية إنتاج التعقيد** (القطع الجاية)، وهو اللي بيحدد هل اللاعب هياخد «نَفَس» ولا لأ.
    - الـ **rot** (2501+) لو بيتقدم باستقلال عن اللاعب هو أقرب لـ progress mechanism بيسرّع إنتاج التعقيد.
  - تيستر-بوت: قيس الـ **«كم إسقاطة بين أول علامة خطر والانهيار»** لإثبات إن الخسارة سريعة وواضحة ومش بطيئة وممطوطة.

---

## 8. Arms Race (B-28→30) ★★

- **Intent:** لاعيبة يستثمروا resources لتحسين قدراتهم الهجومية والدفاعية ضد لاعيبة تانيين. **Motivation:** خيارات استراتيجية كتير، واللاعب يختار اللي يناسب مهاراته وتفضيلاته.
- **Applicability:**
  - **تزوّد الخيارات أو تتجنب dominant strategies** في ألعاب attrition.
  - **تطوّل زمن اللعب.**
  - تشجع اللاعيبة يطوروا استراتيجيات وأساليب تناسبهم.
- **Participants:** عدة لاعيبة بنفس آليات الهجوم + strength + energy اختياري (للترقيات، وأحيانًا هو نفسه strength) + **ترقية واحدة على الأقل**.
- **Consequences:**
  - خيارات كتير = **صعب يتوازن**. أحسن حل: **intransitive (rock-paper-scissors)** في خيارات الترقية بحيث كل استراتيجية لها counter. مثال في ألعاب الحرب الوسيطة: **المشاة الثقيلة تغلب الخيالة، الخيالة تغلب المدفعية، المدفعية تغلب المشاة.** أحسن تركيبة جيش بيحددها جزئيًا اختيارات الخصم.
  - اللاعب بيطوّر أسلوبه: لو بيحب mechanism يستخدمه أكتر، ولو مش بيحبه يتجاهله.
  - **بيطوّل اللعبة** لأن اللاعب دايمًا عنده خيار **يلعب دفاعي** في الأول، وده ممكن يأجّل المواجهة كتير.
- **Implementation:**
  - **إيه اللي بيدفع تمن الترقيات؟** لو strength = energy، اللاعب ممكن **يفرّط في الاستثمار ويبقى ضعيف** خصوصًا لو الترقية بتاخد وقت. لو منفصلين، لازم تفكر في العلاقة: strength ممكن يحدد معدل إنتاج energy (= positive **destructive** feedback قوي)، أو energy تتحول لـ strength، أو تُستثمر لإنتاج strength مع الوقت.
  - ★ **عشان ما يطوّلش زيادة:** خلّي مورد الترقيات **متنافس عليه بشدة** (الكل بيحصد نفس الموارد، أو الترقيات بتتطلب استثمار strength).
  - ممكن يبقى **asymmetrical** (جانبين مختلفين) لكن أصعب في الـ balance.
- **أمثلة:**
  - **StarCraft II وWarcraft III:** اللاعب بيبحث تكنولوجيا لتحسين وحداته. **strength = مجموع الوحدات والمباني**، و**energy بتتحصد بالـ workers** وبتتصرف على الترقيات وبناء وحدات جديدة.
  - **Tower defense (asymmetrical، Fig B.15):** الأخضر والأزرق ميكانيزمين بيزودوا قدرات اللاعب (أزرق) والأعداء (أخضر). في اللعبة الحقيقية فيه ترقيات كتير: اللاعب بيرقي tours أو يختار tours بتأثيرات مختلفة، والـ waves فيها أنواع أعداء مختلفة محتاجة ردود مختلفة.
- **Related:** بيتجمّع كويس مع **dynamic engine** (إنتاج energy وstrength) وده شائع في RTS. بيوسّع attrition. بيتوسّع بـ worker placement.
- **الباترن ورا الباترن:** الـ intransitive counters = **مفيش best strategy مطلق** (الأحسن بيعتمد على الخصم)، فالـ meta بتفضل حية.
- **لموسفولك:** لو الـ rival contests فيها boosters أو أدوات اللاعب يختار منها، خليها **intransitive** (كل أداة ليها موقف أحسن) بدل ترتيب «الأقوى يكسب». وراقب إن الـ asymmetrical (لاعب vs منافس AI) أصعب في الـ balance.

---

## 9. Playing Style Reinforcement (B-31→34) ★★ (لو في meta-progression)

- **Also known as:** RPG elements. **Intent:** **slow positive constructive feedback** على أفعال اللاعب، فاللعبة تشجع التخصص وتتكيّف تدريجيًا مع أسلوب اللاعب المفضل.
- **Motivation:** الأفعال نفسها بتغذي mechanism تطور الـ avatar/units، فبيتخصصوا مع الوقت. **طالما فيه عدة استراتيجيات viable**، الـ avatar بيعكس أسلوب اللاعب.
- **Applicability:**
  - **استثمار طويل المدى عبر جلسات متعددة.**
  - مكافأة اللاعب على البناء والتخطيط المسبق والاستراتيجيات الشخصية.
  - اللاعب «يكبر» في دور أو استراتيجية معينة.
- **Participants:** أفعال نجاحها يتوقف جزئيًا على attributes + resource «ability» بتأثر على فرصة النجاح وبتنمو + **experience points** اختيارية (بعض الألعاب بتسميها skill points وتفصلها عن XP غير القابلة للتداول).
- **Consequences (كلها قيود):**
  - بيشتغل أحسن في ألعاب **متعددة الجلسات** وطويلة.
  - **مش بيشتغل إلا لو فيه أكتر من استراتيجية viable.** لو واحدة أو قليلة، كل اللاعيبة هيستخدموا نفس الاستراتيجية واللعبة تبقى مملة.
  - **Min-maxing:** لاعيبة بيدوروا على أحسن الخيارات لأقوى avatar بأسرع وقت. لو نجح، **بيبقى dominant strategy**، وده بيحصل لما قوة الـ feedback مش موزعة بالتساوي على الأفعال والاستراتيجيات.
  - **بيفضّل الخبير على المبتدئ** (الخبير فاهم الخيارات وعواقبها طويلة المدى).
  - **بيكافئ اللي يستثمر وقت أكتر.** الوقت ممكن يعوض فرق المهارة، وده **ممكن يكون مطلوب أو أثر جانبي مش مرغوب**.
  - **تغيير الاستراتيجية بيضيّع استثمارات سابقة.**
- **Implementation:**
  - **XP ولا لأ؟** مع XP: مفيش ربط مباشر بين النمو والفعل، فاللاعب يحصد XP باستراتيجية ويطوّر مهارات استراتيجية تانية. من غيرها: لازم تـ balance الـ feedback حسب تكرار الفعل، **الأفعال المتكررة أكتر feedback أضعف** من الأفعال اللي بتتمرن نادرًا.
  - **RPG** (النموذج الأمثل): الـ loops بطيئة، ومتوازنة بـ **escalating challenge أو dynamic friction أو stopping mechanism** عشان الـ avatars ما يتقدموش بسرعة. معظمها متوازن إن **التقدم سريع في الأول وبيبطّأ تدريجيًا** (لأن XP المطلوبة بتزيد أُسيًا).
  - **لازم الفعل ينجح عشان يولّد feedback؟**
    - لو آه: تأثير الـ loop أقوى. الأحسن إن **صعوبة المهمة تأثر على النجاح** وتتحدى اللاعب بمهام بصعوبات مختلفة عشان يدرّب avatar بتاعه.
    - لو لأ: اللاعب عنده خيارات يحسن مهاراته المهملة بعدين، **لكن** ممكن يشجعه ينفذ فعل معين في **كل فرصة**، وده ممكن يؤدي لنتايج **غير مقصودة أو غير واقعية أو كوميدية** (خصوصًا لو الفعل قليل المخاطرة).
- **أمثلة:**
  - **Warhammer Fantasy Role-Play** و**Vampire: The Masquerade:** XP على تحقيق الأهداف واللاعب بيصرفها على قدرات الشخصية.
  - **D&D الأصلية: مفيهاش playing-style reinforcement.** اللاعب بيجمع XP للـ level التالي، لكن **ملوش تأثير** على إزاي قدرات الشخصية تتحسن. القدرات **ما بتتكيّفش** مع أسلوب اللاعب.
  - **The Elder Scrolls IV: Oblivion:** تقدم الـ avatar مربوط مباشرة بأفعاله. القدرة = **عدد مرات** تنفيذ الأفعال المرتبطة. **Oblivion بيطبق الباترن من غير XP.**
  - **Civilization III:** طرق فوز متعددة (عسكري، اقتصادي، ثقافي، علمي، أو مزيج). اللاعب بيعزز استراتيجيته ببناء تحسينات مدن وعجايب بتفضلها. موارد زي **money وproduction** بتلعب دور XP، **مش مربوطة باستراتيجية واحدة** (فلوس مدينة ممكن تحسّن إنتاج مدينة تانية).
- **Related:** لو الباترن معتمد على نجاح الأفعال، بيعمل feedback قوي، وساعتها غالبًا **stopping mechanism بيرفع سعر الترقيات الجديدة**.
- **الباترن ورا الباترن:** اللاعب بيبني **هوية** عبر تراكم أفعاله، وده يخلق **تكلفة تحويل (switching cost)** تثبّته في اللعبة. لكن لازم **تنوع viable** عشان الهوية تبقى فريدة.
- **لموسفولك:** لو اتعملت meta-progression (ترقيات مخلوقات/garden/…)، اختبر: (1) **أكتر من استراتيجية viable؟** (2) هل في **min-max dominant**؟ (3) تقدم سريع في الأول وبطيء بعدين (XP أُسّي)؟ (4) هل المبتدئ/اللي مدفعش بيتضرر؟ مهم في hybrid-casual لأن اللاعب العادي مش خبير.

---

## 10. Multiple Feedback (B-34→35) ★★★

- **Intent:** mechanism واحد بيغذّي **عدة feedback mechanisms كل واحد بـ profile مختلف**. **Motivation:** فعل اللاعب بيفعّل عدة loops في نفس الوقت. بعضها أوضح من غيره، فالنتيجة **متوقعة قصيرًا ولها مفاجآت على المدى الطويل**.
- **Applicability:** عايز **تزوّد صعوبة** اللعبة، **وتبرز قدرة اللاعب على قراءة الحالة الحالية**.
- **Structure (مثال الكتاب):** action واحد بيفعّل feedback مش دايم: **positive، محدود المدة، قوي** (أحمر) **+** feedback تاني **negative، دائم، ضعيف** (أزرق). ده مجرد شكل واحد من أشكال كتير.
- **Consequences:** عدة loops أصعب فهمًا من loop واحد → **اللعبة أصعب**. لو profiles اللoops **ديناميكية بتتغير** (وهي غالبًا كده)، **لازم اللاعب يقدر يقرأ الـ profile الحالي** لأن التوازن ممكن يتحول جدًا. إيجاد التوازن الصح مسألة مهمة.
- **Implementation:**
  - لازم **profiles مختلفة**، خصوصًا **السرعة**. أو تغيير الـ profile مع الوقت. إضافة **playing style reinforcement أو stopping mechanisms** لواحد أو أكتر من الـ loops استراتيجية كويسة.
  - ★★ **أشيع تركيبة: fast, constructive, positive + slow, negative** = مقايضة بين مكاسب قصيرة المدى وعيوب طويلة المدى.
- **أمثلة:**
  - **SimCity:** محطة طاقة = نمو اقتصادي على المدى القصير، لكن على المدى الطويل **بتلوّث وبتضر المناطق المحيطة**. الطرق لازمة للنمو، ومع كثرة الاستخدام بتسبب **زحمة وتلوث**.
  - ★★ **Risk (الهجوم بيغذي 3 positive loops بسرعات وقوى مختلفة):**
    1. احتلال أراضي = بناء جيوش أكتر (الأوضح).
    2. **الكروت** (أبطأ): الهجوم الناجح بيدي كارت، وتركيبات معينة من 3 كروت بتدي جيوش إضافية.
    3. **القارات:** كل قارة بتدي bonus جيوش كل دور، **loop سريع وقوي جدًا لكن محتاج استثمار أعلى**.
- **Related:** playing style reinforcement وstopping mechanisms بيضمنوا إن profile الـ loops يتغير مع الوقت.
- **الباترن ورا الباترن:** الصعوبة هنا مش في الـ mechanics الفردية، **في التفاعل بينها**. فالفضل في **القراءة**: اللاعب اللي يقرأ الـ profile الحالي يكسب.
- **لموسفولك:**
  - ★★★ الـ merge فيه أصلًا multiple feedback: الدمج بيحرر مكان فورًا (سريع/إيجابي)، لكن الكبير بيبقى أصعب في الإدارة جسديًا (بطيء/سلبي). لازم **الـ UI يخلي اللاعب يقرأ الحالة** (امتلاء، أحجام، rot).
  - mossy shells وstones من 2501 يضيفوا loops جديدة. اتأكد إن كل تحدي جديد بيغيّر profile مش بيزود رقم بس.
  - تيستر-بوت يقدر يرسم «مكسب قصير المدى» مقابل «تدهور طويل المدى» عبر الزمن.

---

## 11. Trade (B-36→37) ★ (مش مباشر عندنا)

- **Intent:** تبادل بين اللاعيبة يدخل multiplayer dynamics و**negative constructive feedback**. **Motivation:** المتصدر بيواجه مفاوضات أصعب، والمتأخرين يساعدوا بعض يلحقوا. **بيشتغل خصوصًا لما تدفق الموارد غير مستقر و/أو غير موزع بالتساوي.**
- **Applicability:** multiplayer dynamics + negative constructive feedback + mechanic اجتماعية تحفز التفاعل **بالتجارة بدل القتال**.
- **Participants:** trading mechanism + **عدة موارد قابلة للتبادل** + أفعال بتتطلب الموارد دي.
- **Consequences:** negative feedback **مش بيبطّأ اللعبة فعلًا** لكن بيساعد المتأخرين يلحقوا (لأنه **مش مدمّر**). بيفضّل لاعيبة **المهارات الاجتماعية والمساومة**.
- **Implementation:**
  - في board games سهل. في multiplayer computer games سهل بردو. لكن **التجارة مع شخصيات يتحكم فيها الكمبيوتر مش بسيطة أبدًا.**
  - لازم **عدة موارد** قابلة للتبادل، و**معدلات إنتاجها تتذبذب أو تختلف بين اللاعيبة**. التجارة مبتشتغلش إلا لو فيه **عدم توازن في التوزيع**. وتساعد كتير **أفعال بتستهلك الموارد القابلة للتبادل** وأفعال **بتستهلك أكتر من نوع في نفس الوقت** لأنها بتضخّم عدم التوازن لما اللاعيبة يختاروا مسارات مختلفة.
- **أمثلة:**
  - **The Settlers of Catan:** اللاعيبة بيبنوا **dynamic engine غير مضمون** (قرى ومدن بتنتج موارد تبني قرى ومدن أكتر). **عشوائيته بتتقاوم جزئيًا** بإن أي لاعب يقدر يتاجر مع **اللاعب اللي دوره دلوقتي**. سعر التبادل بالاتفاق، وغالبًا بيتحدد بتوفر المورد وموقف اللاعب. **المتصدر ممكن يدفع أكتر. قرب الفوز ممكن يلاقي إن مفيش صفقة ممكنة.**
  - **Civilization III:** تبادل موارد استراتيجية وفلوس ومعرفة. **بيفيد الطرفين** والحضارات الأضعف بتلحق بسرعة نسبيًا.
- **Related:** Attrition مصدر multiplayer feedback بديل، destructive مش constructive.
- **الباترن ورا الباترن:** negative feedback **بدون عقوبة** (على عكس attrition). المتأخر بيتحسن من غير ما المتصدر يتدمر.
- **لموسفولك:** عندنا single-player فالباترن مش مباشر. لو فيه طبقة اجتماعية/rival ممكن تستلهم منه: **مورد قابل للتبادل بين الأصدقاء** = negative constructive feedback بدل «هجوم». ولو مفيش، اتجاهله.

---

## 12. Worker Placement (B-37→41) ★★

- **Intent:** اللاعب بيتحكم في مورد محدود (**workers**) لازم يلتزم بيه لتفعيل أو تحسين mechanisms مختلفة. **Motivation:** مجموعة mechanisms بتكوّن نواة معقدة وديناميكية، واللاعب لازم يوزّع workers المحدودين عليها. **العدد المحدود يخلّيه يغيّر التوزيع باستمرار** عشان يشغل الـ mechanisms بأفضل شكل.
- **Applicability:** **micromanagement** مستمر كمهمة للاعب، تشجيع التكيف مع الظروف المتغيرة، **التوقيت** كعامل حاسم، **وmechanism خفي للصراع غير المباشر**.
- **Participants:** core mechanisms (غالبًا هيكل معقد) + **stations** تفعّل أو تحسّن الـ core + workers resource + worker pool اختياري للـ workers غير الملتزمين. (الـ core في الدايجرام converter engine كمثال، الباترن ينطبق على أي mechanisms معقدة كفاية.)
- **Collaborations:** Workers بتتحرك بين stations **بسهولة نسبية**، فتغيير سلوك الـ core سريع.
- **Consequences:**
  - الوقت اللي بيتصرف في نقل الـ workers: لازم **الإيقاع** يسمح بيه، واللاعب يقدر **يستعد** لأحداث بتتطلب تغيير التوزيع.
  - **أنسب للألعاب المعقدة بمراحل gameplay مختلفة** (لأن سلوك الـ core لازم يتغير من وقت لوقت).
  - الإدارة المستمرة ممكن بسهولة **تسيطر على اقتصاد اللعبة**.
- **Implementation:**
  - **وازن عدد workers مقابل عدد stations.** لو العدد ثابت، التوازن ده يفرّق بين «تغييرات مستمرة في التوزيع» و«استقرار على توزيع ثابت». **عدد قليل = تكيّف أكتر. عدد كبير = حاجة أقل للتكيف.**
  - لو العدد كبير أو اللاعب يقدر ينتج workers إضافيين، **خد بالك** إن كل stations ممكن تتشغّل ومفيش سبب لتغيير. حل: **السماح بعدة workers في نفس المكان لتحسين أثرهم أكتر** (محطة الوسط في الدايجرام).
  - **منافسة على نفس الـ stations** (مثال: منجم دهب واحد): لازم mechanism **يشيل workers من stations** — إما رجوع تلقائي للـ pool كل دور أو فعل بيشيل workers الخصم. المنافسة = **صراع خفي غير مباشر**: اللاعيبة بيعطّلوا خطط بعض بحجز stations حي

