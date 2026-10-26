# Tacticon Panel: "The Challenge of Designing the Core Game Loop of Strategy Games" (x5gwO4ZVOxw، ~100 دقيقة) — نوتس مذاكرة

**الملحوظات:**
- البانل (4X وgrand strategy) مش في مجال موسفولك المباشر. بس فيه دروس كتير عن الـ feedback loop والـ onboarding والـ upkeep والـ AI، وهي بتنطبق علينا.
- البانليستس: **Chris Park** (Arcen Games، مودريتور: Last Federation وAI War، شغال على Heart of the Machine مع Hooded Horse) و**Soren Johnson** (مصمم Civ 3 وCiv 4، مؤسس Mohawk Games: Offworld Trading Company وOld World) و**William Dyce** (Game Director في Amplitude، كان lead designer على Humankind، اشتغل على Endless Legend وEndless Space 2) و**Yussi** (Resistance Games: Houses of Calderia وCompany of Crime).
- الترانسكريبت ASR ومحرّف: اسم Yussi طالع «y AIA / UC / Juicy / yussi»، وـ Romain (مؤسس Amplitude) طالع «Roman». نسبت الكلام للمتحدث على أحسن تخمين.
- الفيديو كله تصميم، مفيش برمجة تتجاهل.

---

## 1. مشكلة الـ vertical slice في الاستراتيجي (2m–5m) ★★

- **الإطار:** غير الاستراتيجي بيبني vertical slice = core loop صغير ممتع بذاته وبره السياق. تـ demo-ه في convention سهل. الاستراتيجي (4X/grand strategy/حتى tactics) مفيهوش ده، و«conventions are hard».
- **الباترن ورا المشكلة:** متعة الاستراتيجي طالعة من تراكم الأنظمة (cerebral) مش من لحظة واحدة قابلة للتجربة. الحل الوحيد إنك تلاقي طريقة توصل لـ«الفان» بدري.
- **الرقم (Yussi):** الـ vertical slice في جنر mechanics-driven حوالي **20% من اللعبة**، لكن في grand strategy يبقى **80%** منها.

## 2. تكتيكات الوصول للفان بدري / التعامل مع غياب البروتوتايب (5m–19m) ★★★

**تكتيك Soren: Multiplayer من أول يوم**
- مشاريع Civ 4 وOffworld وOld World اتلعبت multiplayer حصريًا في **أول سنة على الأقل**.
- الأسباب:
  1. مش محتاج AI.
  2. الناس بتستثمر نفسها في لعبة قدام لاعب تاني **أكتر بكتير** من بروتوتايب «wonky وسهل تغلبه».
  3. تحدي تقني في الأول بس بيوفر «headache» ضخم في الآخر.
- **تجربة C3:** «هنضيف multiplayer بعدين» كانت كارثة، ومن ساعتها حلف مايعملهاش تاني.
- **الباترن:** الـ multiplayer غالبًا subset من الباكدج النهائي. في Offworld عمل الـ Skirmish mode وماكنش بيفكر في الـ campaign إلا في **النص التاني** من المشروع.
- **مثال Old World:** فيه switch لـ«**no character mode**» يطفي الشخصيات والـ dynasties والـ events كلها. شكله vestigial، بس ده كان **اللب الداخلي** اللي اتلعب أول سنة. الهدف: نوصل للفان بعد **3–6 شهور مش بعد سنتين**.

**تكتيك William: كل لعبة بروتوتايب للي بعدها ("choosing your battles")**
- أنظمة Endless Legend اتأخدت وطورت:
  - نظام الـ minor faction integration كان بروتوتايب لـ **culture shifting** في Humankind.
  - الـ tactical battles اتعملت iteration عليها.
- الباترن: تاخد ميكانيكس شغالة من لعبة قبلها، فتبقى «واثق إن ده شغال» وتحط المجهود في الـ new spin بس.
- **تاريخ Amplitude:**
  - المؤسسين Romain وMatthew اتقابلوا على **Civ 4 Forum**.
  - عايزين يعملوا 4X في Ubisoft، وUbisoft قالت «محدش هيشتري 4X، ده شغل التسعينات».
  - بدأوا بحاجة في الفضاء لأن modeling الكرات سهل وmتطلبات الـ art أقل.
  - كل خطوة كانت أنظمة بتتعمل sandbox، فكل اللي Amplitude عملته = بروتوتايبات في الطريق لـ Humankind. وRomain كان عنده master plan من البداية.

**تكتيك Yussi: اتباع الـ vision من غير بروتوتايب**
- آخر **3 ألعاب** اتساينت من غير بروتوتايب خالص. Calderia وCompany of Crime ماكانش فيهم **سطر كود واحد**.
- ده بيتطلب **pre-production material كتير + marketing materials** + **comparative analysis** (مقارنة بالـ market leader أو الأقرب لنا). فايدتها داخليًا إن التيم يفهم هيعمل إيه، وخارجيًا للتواصل مع الناشرين.
- بيقول إن الموضوع بقى أصعب، لأن «difficult to get far in discussions without a proper demo».
- ★★ **فلسفة الاستوديو:** أي concept جديد **ماتقفزش على demo فورًا**. 99% من الوقت محتاج demo، بس لو **حد مش هيكمل كلام من غيره → علامة إن الـ concept مش كفاية** → اعمل demo لحاجة تانية.
  - عندهم 4 concepts بيتباعوا وبيبنوا demo لكل واحد ببطء.
  - مصادفة: الناشرين حبوا concept تاني أكتر.
- **تغيير Calderia:** اتغيرت جامد في أجزاء، «لكن الـ fundamentals والـ pillars بتفضل».

**تكتيك Chris (الـ Kickstarter):** وعدنا بحاجة، بروتوتايبنا شفناها «terrible». الاختيار: نسلّم حرفيًا اللي قلناه، أو نعمل **pivot** يحترم روح الوعد لكن أحسن وممتع فعلًا.

**★★★ William: «a prototype is worth a thousand game design docs»**
- مثال: الـ diplomacy في Humankind. controversial عند لاعبين، وهو اشتغل عليها **أكتر وثائق وتبرير نظري** في حياته.
- ماعرفش يعمل لها بروتوتايب لأنها «sitting on top of everything»، وتقدر blackbox باقي اللعبة.
- فعل **paper prototypes وboard games** + **HTML5 prototype** لعبوا عليه **tournaments في الأوفيس** للـ tactical battles.
- Amplitude بتقدم vertical slices وبتبرر الصرف للمموّل.

**★★ منهجية الـ pre-production عند Amplitude (Ubisoft-inspired "rational game design"):**
- فترة طويلة لفهم ما يريده الـ stakeholders.
- **key message → pillars → domains/systems → rationales** (مثلًا «ده شعور الـ combat»، «ده شعور الـ culture»). approach top-down.
- التصميم في الـ pre-production = «ما الأهداف المحددة» ثم تبني عشان تضربها، وتبروتايب تتأكد.
- **مثال:** بروتوتايب culture changing. أكبر مخاوفهم **فقدان إحساس الملكية** (زي Britannia/Small World: تبني إمبراطورية وتتحول لفصيل وتخسر نص إمبراطوريتك). «مفيش طريقة تعرف غير بالتجربة».
- **Chris:** «كل مرة فيه design document كبير مابيصمدش».

## 3. ميزة وعبء الخبرة (19m–22m) ★★

- Chris: ناس بتحب تركيبة (زي Civ 5 من غير religion اتجنن عليها الناس، مع إنها subsystem بس). الـ combat في Last Federation وEndless Legend فيه ناس بتحبه وناس بتقول «لعبة صغيرة تانية جوه». غياب القتال في OWTC «closed doors» لناس.
- Soren: الخبرة ميزة (Old World مستحيل من غيرها). والعبء إن «الـ tracks في دماغي عميقة». احتاج **5–10 سنين** بعد C4 عشان يلاقي أفكار تكفي لـ4X جديدة. وأفكار كان شايفها كويسة في C4 بقت trade-offs أو فيها بدائل.
- **الباترن:** قرارات التصميم **trade-offs**، والسؤال دايمًا: **أي نوع قرار بتديه للاعب، وأي نوع لاعب بتفتح له؟** C4 بيستهدف لاعب، وOld World لاعب تاني.

## 4. نظام الـ Orders في Old World (22m–29m) ★★★

- **الأصل:** كان سبب Old World كله، قبل الشخصيات وقبل Classical Antiquity. الفكرة: «what if we slapped an action point system onto Civ؟».
  - بعدها يوم واحد «الـ implications انفتحت قدامي»:
    - لازم تختار فعلًا بين infrastructure وmilitary («بنقولها دايمًا بس مش بتحصل فعلًا»).
    - مرونة أكبر في استخدام الـ units.
  - النسخة الأولى: Civ مبسطة جدًا بتغطي **كل Arc of History** (زي Polytopia) بالـ order system. وشاف فورًا إنه «worth building around».
- **المشكلة: counter damage.** في Civ التقليدي الـ attacker ممكن يموت (مقارنة الـ unit بالتانية = mini battle). ده مايشتغلش مع orders، لأن **الـ orders هي وقود الجيش**، ولو الجيش ينجح من غيرها يبقى advantage ضخم. وفوق كده فيه defender advantage أصلًا.
- **الحل:** الـ combat بيتوزع على أدوار: تهاجم، التاني يرد، تهاجم تاني… لحد ما حد يموت أو ينسحب.
- ★★ **مشكلة الـ playstyle:** أكبر contingency منزعجة: لاعبي Civ اللي بيلاقوا choke point وبيحصّنوا وحدات دفاعية ويسيبوا الـ AI يبعت 5 وحدات في المرة (= They Are Billions، حسب Chris). **مفيش طريقة تدي الناس دي التجربة دي** في الـ order system.
  - الآن بيجربوا counter damage: **Tactician general** ability، وfully fortified units بيعملوا counter damage. بيتطلب ~**5 turns و5 orders**، وكل counter damage بيخسر fortification فتصرف order تاني.
- ★★ **الهدف الثاني:** تقليل micromanagement في الـ endgame (في أغلب 4X الـ endgame «chore»). كان في الأول متطرف: orders flat تقريبًا طول اللعبة، والتيم قاومه. «عندي 50 unit ومش قادر أستخدم أي منهم» = متطرف.

## 5. Caps وSoft Caps ومعاقبة النجاح (29m–34m) ★★★

- **William (Chris Crawford):** الـ action-feedback loop. لو عندك 500 unit و30 city، بتصرف **30 دقيقة** تدي أوامر. بيحب أنظمة الـ energy/orders (Solium Infernum، Eclipse).
- **Humankind:** بدل ما يحدد عدد الأوامر، حاول يحدد **عدد الـ controllable entities** بالـ nudging:
  - city merging.
  - upkeep على الـ **armies** مش الـ units («تتعاقب لو عندك armies كتير»).
- ★★ **«Soft caps are insidious hidden hard caps»:** لو فيه upkeep على عدد المدن، فيه threshold مخفي في الرياضيات بعده المدينة الإضافية مش مجزية. فالأفضل hard cap صريح (Crusader Kings بيحدد عدد الـ vassals).
- لكن اللاعبين بيكرهوا الـ hard caps («why are you stopping me»)، زي ما Soren قال: «why are you stopping me from playing They Are Billions».
- ★★★ **Soren:** «wide vs tall» في Civ 5 مش طريقة صح لتقييم اللعبة (أنظمة على cross purposes). الـ 4X بتبني إمبراطورية، **«you don't want the player to feel punished for succeeding»**.
  - الـ orders بتقيّد عدد الـ units بس بتديك حاجة قصاده: تعمل بوحدة واحدة حاجات ماكنتش تعملها. لما يرجع لـ Civ «بيحس إنه بيمشي في وحل».
  - **الـ territory system (Old World)** و**city site system (Humankind)** = نفس الحل لمشكلة «كام city اللاعب يحشرها على الماب». المدن الزيادة عن المتعة بتسبب مشاكل رياضية وmicromanagement و«you're allowing the player to ruin the game for themselves».
- **Yussi:** Paradox بتحد الـ micromanagement. في Europa Universalis حجم الماب مجرد علامة على كام فلوس وجيش تقدر تـ upkeep-ها، فالشغل ماينفجرش أُسّيًا. وهي اللعبة الوحيدة اللي **البقاء كبير من غير غزو جديد** فيها فعلًا مجزي (تمرد وأعداء بيهاجموا)، لأنها مش chore.

**لموسفولك:** عدد الإسقاطات (drop budget) = hard cap صريح، وده كويس (واضح). أي نظام زي ده يتصمم بحيث اللاعب مايتعاقبش على النجاح (مثلًا الليفلات المتأخرة فيها مخلوقات أكبر = ضغط مساحة، نتأكد إنه تحدي مش عقاب).

## 6. المتعة مقابل الاستنتاج الأمثل وLatency (34m–37m) ★★

- **Chris:** مراته بتلعب أول Civ 6 مرارًا بـ playstyles مختلفة جذريًا، لأن الـ turns snappy: **latency واطية بين قراري وتنفيذه**. نادر إن لاعب يجرب كده، **أغلب اللاعبين بيتمسكوا بطريقتهم** سواء ممتعة أو لأ.
- ★★★ **Soren/Chris:** اللاعبين بيتبعوا الـ gradient الأمثل «لحد ما يبطل يبقى ممتع ويشتكوا لنا — you did it to yourself». «لو بتكسب بإنك بتخبط راسك في الترابيزة، الناس هتخبط راسها وتقول اللعبة وحشة وهي **صح، لأن راسها وجعاها**». وده بيقفل design avenues قدامنا.
- **الباترن:** اللاعب بيحسّن الـ metric مش الفان. فلازم الـ optimal path يبقى هو الممتع (ملازم لقاعدة Soren: «intuitive way to play = the right one»).

**لموسفولك:** افحص الليفلات: لو في استراتيجية «ممل بس مضمونة» (مثلًا تكويم مخلوق بنفس الحجم بدون risk) البوت هيعتبرها optimal. نتأكد إن تيستر-بوت بيكشف dominant boring strategy. وlatency بين الإسقاط والـ merge feedback لازم تفضل minimal.

## 7. Dramatic play مقابل Strategic play (36m–40m, 67m–70m) ★★

- **William:** Paradox قريبة من simulation/role-playing، وFiraxis وAmplitude وMohawk في فضاء **board-gamey strategic challenge**. في الـ role-playing بتحاول **تعبّر عن نفسك** وتدور على مناطق مش مكتشفة (زي Minecraft)، مش «أحسن حركة». مش أبيض وأسود: Old World في النص، وCalderia مش عارف.
- **Yussi:** Calderia real-time بس قلبه turn-based. القيد: الـ early game والـ endgame **نفس كمية الأشياء** — بتتحكم في فرد/عيلة واحدة (الترانسكريبت مشوه «one fif») مع vassals كتير. ده بيسمح بتعقيد أكبر.
  - يعتبر Old World event system «brilliant» لكن العلاقة بالشخصيات فيه مش personal كفاية (شخصيات كتير بتعيّنها وبتتصل بيها قليل). فـ Calderia: **عيلتك = أدواتك** (مهاراتهم بتحدد احتمال trade، والزواج يعتمد على المهارات والعلاقات، وبكده بتتولد alliances).
- **Soren:** Old World = 4X بتستخدم الشخصيات كـ«spice». لو عايز لعبة قصصها وشخصياتها الأساس، تعمل زي Calderia.
- ★★ **CK3 مقابل CK2 (Yussi):**
  - CK3 بتربط skills الشخصية بالأحداث، فالاختيارات بقت **math problem مش choice**: في right answer (لو عدّيت الـ threshold، مفيش incentive لأي اختيار تاني).
  - في CK2 الأحداث كانت **50/50 متوازنة** وكان بيلعبها role-play.
  - Chris بيلعبه math problem برضه.
  - بس Yussi معترف إن approachability بقت أحسن، وإن stress mechanics بترجع جزء من الـ RP.
- **William:** مثال suicide option في CK. التول تيب بيقول «bad on so many levels» بس لاعبين بيختاروها عشان **dramatic virtuosity** في تمثيل الدور. بيصمموا فعليًا **لعبة مختلفة لكل نوع لاعب** (جديد/خبير، narrative/strategy). «somebody always gets left behind» (CK3 جاب Soren وWilliam وسابت Yussi).
- ★★ **الاستثناء الممتع (Chris/Yussi/William):** اللاعب بيتلذذ بـ**الاختيار الحصري** («VIP option») لما يكون **earned ونادر**:
  - Vampire: Bloodlines: خيارات حوار بـ intimidation أو seduction عالي.
  - Fallout وD&D skill checks.
  - **1 من 10 = awesome**، لكن لو دايمًا بتختار نفس الاختيار «بيكسر الوهم».
  - **Yussi:** عايز يزود أحداث «لو greedy تاخد خيار كويس».
  - **Chris:** مشكلة CK3 إن فيه خيار لكل نوع شخصية فتختار اللي بيطابقك كل مرة.
- **Soren — Tales of the Arabian Nights (board game):** كتاب سميك فيه آلاف الأحداث (الرقم في الترانسكريبت مشوه «25 200»). لو ماعندكش «Wen charm» أو «robe of many colors» بيقولك إيه حصل **بس مابيورّكش الاختيار اللي فاتك**، فبيتوسع خيالك في اللي ممكن يحصل. أحداث Old World متأثرة بيها.
- **William** رد على نقد CK3: الألعاب المفتوحة بتحط جزء من مسؤولية الـ design على اللاعب إنه يقول «خلصتها». المشكلة في Steam reviews السلبية بعد 300 ساعة (وSpace Engineers بعد **8000 ساعة** سلبي).

**لموسفولك:** الـ rival contests والـ side quests: **الاختيار الحصري النادر** (جايزة/مسار مفتوح بس لو حققت شرط صعب) أقوى من «اختيار مطابق ليك كل مرة». وحافظ على إنه نادر (~10%).

## 8. الهوية والـ Story-lets والتفاعل الثنائي (41m–48m) ★★

- ★★ **Yussi:** في 4X الهوية الصح هي «**إزاي مجتمعي/ثقافتي مختلف**» مش «شخصيتي». C4 كان الأحسن لأن Civics (slavery/emancipation) بتوضح الفروق بين الدول. تخيل أحداث على طراز Old World: «لسه بستخدم slavery وإنت emancipation» → تغير دبلوماسي → سفينة **Amistad** توصل شاطئك → ترجعهم (relation bonus) أو لأ (unhappiness داخلي).
- **Soren:** يتمنى يضيف event system في C4 مربوط بالـ game state (religion/civics) بدل «modifiers في الخلفية، شغالة بس مش compelling».
- ★★★ **William — «multiplayer events»:** Humankind بتربط الأحداث بالـ Civics (slavery، nuclear disarmament). **اللي ناقص: story-lets** (Mad Lib: «___ بيجي قلعتك لأن ___») بتتملى بـ **إمبراطوريتين**: generator يحط إمبراطورية slavery وإمبراطورية emancipation وينتج حدث يربطهم. المشكلة: «you're playing solitaire والإمبراطوريات التانية بتعمل problems بعيد على الحدود».
- **Yussi:** الفروق موجودة في tooltips بس **مش في وشك**. لو اللاعب مابيفتحش الـ status مايعرفش إن العلاقة سيئة. الأحداث الـ bump-up تبرز العلاقة وتدي فرصة للتأثير.
- **Chris:** اللاعب بيتماهى مع **قسم من الماب ومدينة** حطها (حتى مابيفتكرش هو أي civ). الشخصيات في Old World بصريًا بتتذكر («بعتت فلان للجامعة ومات بالمرض»). الـ tactical battles المرئية في Endless/Humankind بتديني ذكريات أقوى.
- **الباترن:** الذاكرة والتعلق بيتبنوا من **المرئي + الأحداث المحددة** مش من الـ modifiers.

## 9. Onboarding للـ cerebral systems (49m–53m) ★★★

- **Chris:** بنصمم الجانب الـ cerebral الأول، وبعدين لازم نعمل onboard — **لازم يبقى ممتع أثناء الـ onboarding وقبله**.
- ★★★ **William (Mark Rosewater، Magic):** **«don't mix up interesting and fun»**. مثال: ميكانيك «discard cards وخد advantage» — interesting بس الناس عايزة تلعب بالكروت مش تتخلص منها.
  - مثال Street Fighter: اللاعب الـ cerebral فاهم luring واستراتيجية، والجديد بيدوس زراير، «thank goodness مش مجرد أشكال هندسية وhitboxes، فيه fireballs وشخصيات بتتضرب».
- ★★★ **Juice كأداة onboarding:** «اعمل مكان لطيف تكون فيه وانت confused».
  - Humankind: تطارد فيلة بالـ mouse، تحريك الجيش حلو، تزوم وتسمع **birdsong** جنب الغابة، illustration حلوة، تكتشف wizard stones.
  - «مش عارف إيه اللي بيحصل بس عندي كل الـ art الجميل».
- **Intuitive hooks:** مش كل حاجة رموز مجردة. Mill = طحن = الناس لازم تاكل؛ Quarry منطقي لحضارة رومانية بتبني coliseums.
- **تمرين:** «turn your brain off ونظر كلاعب naive: لو مافهمتش orders، إيه اللي يبان بديهي؟».
- **Soren:** الطريقة البديهية للعب لازم تبقى **الصح** (مش الأفضل بالضرورة، فيه mastery) — «ماتخليش اللاعب يقع في traps صغيرة».

**لموسفولك:** عدسة الأونبوردنج: «حلو إنك ماتفهمش وانت بتلعب» — الـ juice (صوت الـ merge، حركة مخلوقات الـ Mossfolk، رد فعل البرطمان) هو اللي يشيل اللاعب لحد ما يفهم التحديات الجديدة (mossy shells/stones/rot من 2501).

## 10. الـ Trap: Upkeep مقابل Upfront Cost (53m–61m) ★★★

- ★★★ **قصة Soren مع Civ 4 (trap حقيقي):** لعب C4 بعد شهور، توسع زيادة، فجأة **الـ units بدأت تختفي**. السبب: مدن كتير → maintenance عالي → مفيش فلوس → science slider ينزل لصفر → الـ units بتتحذف لتغطية العجز. «who designed this stupid game؟ — **it was me**». الحل الوحيد: يرجع save قديم **30 turn**.
- **ليه Old World مش كده:**
  - **City Sites** تقيّد التوسع.
  - **Resource stockpiles** (تبيع حاجة تانية، نادرًا تكون عاجز عن كل حاجة).
  - ★★★ **Upfront مش backend:** تدفع 100 iron عشان تبني swordsman، ولو مش معاك مش هتبني. **مقابل** تبني swordsmen كتير ثم **الاقتصاد ينهار**. دايمًا في حاجة المدينة تقدر تعملها (festivals/councils) وتعيد بناء الاقتصاد. «النتيجة النهائية واحدة (watch your budget) بس **الترتيب بيفرق ضخم للاعب**».
- **ليه Civ 4 ماقبضتش عليها:** مش ظهرت في عصر الإنترنت الحديث. أول **100,000** لاعب هيلاقوها. وSoren: «ماجاتش feedback لأنها ingrained، وده لسه موجود في Civ 6 على حد علمي».
- ★★ **Yussi:** الـ cognitive attention هي الأساس: الـ upkeep «background system مفيش تفاعل معاه» لحد ما تتحذف الـ units. «ماقضيتش وقت معاه فماتعلمتوش ومابتتماهاش معاه». لو كان in-your-face بأحداث ممكن تدرّبه. الـ nudges («عندك مدن كتير، عايز تدمج؟»).
- **Yussi — Disco Elysium:** «اللاعبين مش بيحبوا يقروا» فكرة غلط، لما الحوار اتـ gamified الناس قرت براحتها. المهم نوع القرارات اللي نخلي اللاعب يعملها.
- ★★★ **William (Thinking in Systems، Donella Meadows، الترانسكريبت «Summers»):** مثال **مصايد الأسماك**: حسب كمية الصيد إما oscillation أو إنتاج مستقر أو **انهيار تام**. **البشر وحشين في threshold effects.** الـ upkeep مش مشكلة طول ما دخلك > مصروفك، «بس لو انقلب فجأة الحساب بيفضى وكل المشاكل تحصل»، ومش واخد خبر إن الميكانيك موجود لعشرات الساعات.
- **William:** في Humankind تجنبوا upkeep لوقت طويل، و«اتسلل بعدين» لتقليل معدل نمو المنحنى الأسي.
- **Yussi:** 600+ ساعة في EU4 ولسه مايعرفش إزاي state upkeep بتشتغل بالظبط، بس يتعامل معاه كويس.

**لموسفولك:** ★★★ المخاطر المتأخرة (الـ rot، stones، mossy shells) لازم تعتمد على **upfront cost مرئي** مش threshold مخفي بينفجر. وأي عداد ينهار (مثلًا الجرة بتمتلى) لازم **warning واضح قبل الـ flip** — اللاعب مش عارف إنه قرّب إلا لما يفشل.

## 11. الشفافية (Transparency) وUndo/Determinism (61m–66m) ★★★

- **Soren:** Paradox = **black boxes** (مايعرفش إزاي الـ combat في CK بيشتغل). Civ على الطرف التاني (تقدر تشرح اللعبة).
- **Chris:** هو كمان لعب Old World كـ black box («ماعنديش وقت أتعلم modifiers التضاريس»)، وتمنى يطفي الـ multipliers.
  - **قصة Skyward Collapse (2013):** لاعبين قالوا فيه «too much non-actionable information في tooltips» — **«مش عايزين نعرف إزاي الـ sausage بيتعمل»**. هو دايمًا sausage-maker بس في Old World كان «engaged، مش عاوز التفاصيل».
- ★★★ **Soren:** اللي سمح بالـ flow state: **deterministic combat + undo system**. «تحرك الماوس: هعمل 4 damage هنا، 8 هنا، ولو حصل غريب تـ undo». **Chris:** «ماكنتش أبدًا مش عارف إيه هيحصل. **Tool tips are worth an undo**».
- **Yussi:** رغم كده الـ tooltips ضرورية: **تعرف إن الاختيار ده يؤدي للأثر ده على الجزء ده من اللعبة** حتى لو مافهمتش التفاصيل. بيدرسوا Old World tooltips لـ Calderia.
- ★★ **William:** **Nested tooltips** أحسن حاجة. CK3 مقابل CK2: **UX team** قدر ياخد الـ sausage-making ويرتب الـ hierarchy (يعرض اللي محتاجه في السياق). «لو بتخسر فلوس من upkeep أو عندك مدن كتير في CK3 بتعرف». هو bounced off CK2.

**لموسفولك:** ★★★ في merge physics الـ outcome ممكن يبقى غير متوقع. اللاعب لازم **يعرف إيه اللي هيحصل قبل ما يسقط** (preview/guide) أو يقدر **يـ undo** (rewarded undo ممكن يبقى فرصة إعلان — مقترح مش من المصدر). والـ tooltips بتشرح *إيه الاختيار يعمل* مش الرياضة وراه.

## 12. نهاية اللعبة والـ Win State (79m–85m) ★★★

- **William:** الـ 4X «investment games» (Soren: «ناقص reason للـ invest في الآخر، فبيختفي الاهتمام»)، و**اللعبة بتفضل تجبرك تقتل آخر vestige من كل حضارة** رغم إنك كسبت فعليًا. الحل المحتمل: اللعبة **تقول للاعب «إنت كسبت، وقّف»**.
- ★★★ **Menace/Climax في الآخر:** Sorcerer King وLast Federation (تهديد قاهر بيوصل في الآخر ولازم تبقى «قوي لا نهائيًا»)، وBattle Brothers (غزو orcs/undead)، وFrostpunk (العاصفة). «المنحنى الأسي عادةً smooth sailing».
- **Yussi:** الألعاب اللي **تنتهي بـ bang** (Colonization) هي اللي بيكملها للآخر. هو بيعمل restart لما يحس إنه هيكسب في Humankind أو Civ.
- ★★ **Soren (Ambition Victory في Old World):** فوز **للإنسان فقط** (narrative-based) — اللاعب **يرسم end line بنفسه** ويحدد أهدافه والـ Ambitions بتصعب مع الوقت. «لو اتنبهت إن الـ AI كسب وإنت مش واخد بالك = major failure». الـ AI يبطّئك بس **الـ finish line لازم يكون عند اللاعب في الوقت الصح**.
- **Chris:** AI programmer قاله إن اللاعب هو الـ front runner دايمًا لأن عنده superpower (load saves/rewind) والـ AI لأ.
- **Chris — Elden Ring:** صعبة جدًا بس **مايمكنش تخسر نهائيًا** (فوز 100% مضمون بالإصرار). Mario وZelda كده. **الاستراتيجي مختلف: ممكن تخسر** (civ ماتكلمتش معاها كسبت Tech Victory → «what؟!»).
- **William:** Amplitude بتعمل 4X وroguelikes: «أقرب مما تتخيل»، الاثنين ممكن تموت فيهم، وفيه سؤال avatar power (اتقطع).

**لموسفولك:** ★★ الـ 3000 ليفل لازم كل ليفل يعرّف اللاعب إنه نجح (وضوح الـ win). ولو مناسب نحط «ذروة/bang» في الليفلات الأخيرة قبل شريحة التحديات (بدل smooth). والـ rival contests: لو الخصم هيكسب، لازم اللاعب يشوف ده قبل ما ينتهي مش بعده.

## 13. دور الـ AI (85m–98m) ★★★

- **William (السؤال):** هل الـ AI يتظاهر بإنه لاعب بشري؟ أو يبقى In Cahoots (Greece تسيب Egypt يغزوها عشان Egypt تبقى Nemesis أحسن للاعب)؟ Storyteller AI؟
- **Yussi:**
  - الـ AI لازم يكون له **شخصية** ومش بالضرورة human-like (فصائل Endless Legend بتحس مختلفة). Aztec وChinese يتصرفوا كده «حتى لو مش optimal»، مش «جيش clones».
  - **مش هيتعاونوا وراك** (feels like cheating). مش leveling the field للدراما.
  - الـ AI هو **extension of the game system** (قالها لـ Chris عن Arcen)، وبتفقد power fantasy الفوز بنفس القواعد بس بتكسب عنصر تاني.
- ★★ **William:** الـ AI بيقولك «هطعنك في ضهرك» وبعد 10 turns يعملها. **مفيش لاعب بشري يقول كده.** الـ AI عنده **narrative coherence** يحترمها (Chekhov's gun: plant & pay off). أي لاعب بشري هيدمرك من غير إنذار.
- ★★★ **Soren:**
  - الـ AI المفاجئ في الغدر **«arbitrary»** عند اللاعبين. الحل في Old World: **الملك بيموت ويتبدل بملكة بتكرهك** → «منطقي إن الحليف يبقى عدو». ميزة غير متوقعة لنظام الشخصيات.
  - **إطار Playing to win مقابل playing to lose:**
    - **Win:** Big Blue (شطرنج) — مفيش goal غير هزيمتك.
    - **Lose:** Tower Defense وroguelikes — الـ AI patterns هي الـ game mechanic.
    - **4X في «nether region»:** الناس بتفتكر الـ AI لازم يلعب to win، لكن فعليًا **في نواحي كتير لازم يلعب to lose**، ولازم يتحاشى حاجات دبلوماسية بشرية، فنلفّها narratively.
  - **مناسب جدًا إن الـ AI يقولك «هطعنك»** أو حد يقول «ماتثقش في اليونانيين».
- ★★★ **Chris:**
  - البشر والـ AI skill sets مختلفة. ماعملش لعبة الاتنين فيها يلعبوا نفس الـ faction — **asymmetric**.
  - **أمثلة:** Billiards AI بمعرفة كاملة للفيزياء يـ clear the rack كل مرة. FPS AI = **aimbot** (headshot دايمًا). RTS: Starcraft players هيعملوا Zerg rush وتخسر بسرعة = مش fun. **فالـ AI الحقيقي اللي بيحاول يكسب مش ممتع في أغلب الجنرات**.
  - الحل: **verisimilitude** («ده اللي جندي عدو هيعمله» أو «لاعب بلياردو متوسط») — «magic tricks، smoke and mirrors». في الاستراتيجي المشكلة ×100 (sneaky دبلوماسيًا وفي نفس الوقت تقول «أنا sneaky» من غير pandering: «how non-obvious can you be?»).
  - ★★★ **فلسفته:** **افصل العدو عن اللي اللاعب بيعمله.** الـ AI مش محتاج internal economy. **«if it's not visible to the player it may as well not happen»**. اديله **visible economy مختلف عن اللي عند اللاعب** يشوف إنه بيبني ويتدخل بطرق مش متاحة للـ AI. فكر **player-centric: إزاي يشوف ويتلاعب في اللي الـ AI بيعمله**، مش stand-in بشري.
- ★★★ **Chris — Lateral thinking:** «أعلى endorphin rush للاعب مش "هزمت top AI" بل **"الأمور كانت سيئة وعملت save"**». أي framework يقدر يعطي الفرصة دي. Paradox بتقدمها (القصص اللي الناس بتحكيها).
- **Soren:**
  - **Asymmetric buy-in:** في Old World الـ AI بيبدأ بمدن زيادة («مش بنتظاهر إنه even»). كتير بيرفضوا فيه إمكانية الإيقاف.
  - **Ruthless AI option** (كان اسمها «playing to win» وأربكت الناس): بتشيل الفرامل (غدر من غير إنذار)، **opt-in**.
- ★★ **William — إطار GNS (The Forge: gamist/simulationist/narrativist) للـ AI:**
  - **Gamist:** يلعب to win مهما كان (= Ruthless).
  - **Narrativist:** ينتج قصة ممتعة (مثلًا يخلي وريث العرش في المملكة المجاورة يكرهك عمدًا). في Old World ده «emerges» مش مصمم.
  - **Simulationist:** يتصرف حسب شخصيته (الـ Aztec يعمل كذا).

**لموسفولك:**
- ★★★ **تيستر-بوت:** بوت بمعرفة فيزيائية كاملة = aimbot (Chris) → هيبالغ في تقدير سهولة الليفل. bot_difficulty لازم يتـ calibrate بـ **verisimilitude** (بوت بيتصرف زي لاعب متوسط) أو نقارنه بـ human data، مش بوت optimal.
- ★★★ **Rival contests:** الخصم لازم يبقى **visible** (اللاعب يشوف تقدمه ويتدخل). اسم/شخصية/سبب (narrative reason) للتحول أو التنافس. ماتخليهوش «يفوز فجأة من العدم». وفكرة **opt-in "ruthless"** مناسبة لو عملنا درجات صعوبة للـ rivals.

## 14. ملاحظات جانبية/تاريخية (10m) ★

- Soren: Civ 5 أول Civ كان الناشر فيه مؤمن بـ 4X تمامًا. Civ 4 باعه الناشر (Atari → Take Two). وCiv 2 كان **من غير marketing support** لأن MicroProse كانت مؤمنة بلعبة **Top Gun** (حكاية Sid وBrian).
- **الباترن:** الناشر ممكن يخطئ في تقدير الـ potential. دعم الـ vision مش مضمون.
- **الخاتمة:** البانل زاد عن 90 دقيقة المطلوبة. Yussi اضطر يقتل **wasp** (عنده phobia) وفضل بعيد عن الكيبورد. كلهم اعتبروه من أفضل البانلز اللي اشتركوا فيها.

---

## ملخص «لموسفولك» (تطبيقات مباشرة)

1. ★★★ **Upfront مش hidden threshold:** مخاطر الـ rot/stones/mossy shells لازم warning مرئي قبل الانهيار، والـ failure مايفاجئش اللاعب (Soren/Donella Meadows).
2. ★★★ **Preview/Undo:** الـ determinism + preview = شفافية تخلي اللاعب مرتاح حتى مع فيزيكس. نفكر في drop preview أو rewarded undo.
3. ★★★ **تيستر-بوت مش aimbot:** calibrate بـ verisimilitude، وراقب dominant boring strategy اللي اللاعبين هيتمسكوا بيها حتى لو مش ممتعة.
4. ★★★ **Rival contests:** خصم visible، سبب سردي، ومفاجأة الفوز مرفوضة (finish line عند اللاعب).
5. ★★ **Juice كأداة onboarding للتحديات الجديدة (2501+).**
6. ★★ **اختيارات حصرية نادرة (~10%)** في الـ side quests تدي إحساس «earned».
7. ★★ **Endgame bang** في آخر الليفلات + وضوح الـ win.
8. ★★ **لا تعاقب النجاح:** كل ميكانيك صعوبة لازم يتحقق إنه مش عقاب على الأداء الجيد.