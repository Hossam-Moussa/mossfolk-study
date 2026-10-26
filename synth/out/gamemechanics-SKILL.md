```markdown
---
name: game-mechanics-adams-dormans
description: >
  مستند تشغيلي مأخوذ من كتاب Game Mechanics: Advanced Game Design لـ Ernest Adams وJoris Dormans (2012).
  بيغطي الـ internal economy، الـ Machinations، الـ 16 design pattern، الـ feedback loops، الـ emergence مقابل الـ progression،
  الـ simulation والـ balancing بالـ artificial players، الـ level design والتعليم، والـ meaningful mechanics.
  استخدمه وانت بتختار فكرة، أو بتعمل بروتوتايب، أو بتصمم اقتصاد ليفل، أو بتشخّص balance، أو بتبرمج التيستر-بوت،
  أو بتصمم rival contest / side quest / booster / rewarded ad، أو بتراجع تحديات جديدة في Mossfolk
  (mossy shells / stones / rot من ليفل 2501).
---

# Game Mechanics (Adams & Dormans): السكيل التشغيلي

> **مفتاح العلامات:**
> - ★★★ = بيخدم خط إنتاج «لعبة جديدة كل يوم/أسبوع» مباشرة (اختيار الفكرة، البروتوتايب، CPI، التيستر، الإعلانات).
> - ★★ = مهم للتصميم.
> - ★ = معرفة مساندة.
>
> **الوحدة:** صفحات الكتاب، مفيش دقايق.
> **الأجزاء الناقصة من المصادر** متجمعة في §11. ما تخترعش محتواها.

---

## 0. إزاي تستخدم السكيل ده (Flow)

1. **فكرة جديدة؟** ابدأ بـ §2-أ (اختيار الـ core) وبعده جدول القرار 3.1 وتشيك ليست 5.1.
2. **بروتوتايب؟** §2-ب + جدول 3.2 (أي نوع prototype) + تشيك ليست 5.2.
3. **اقتصاد ليفل/لعبة؟** §2-هـ و§2-و، وارسمه بـ Machinations (§2-ح)، واختار patterns من §4.
4. **Balance / تيستر-بوت؟** §2-ي + تشيك ليست 5.4.
5. **Level design / tutorial / منحنى 3000 ليفل؟** §2-ك و§2-ل.
6. **قبل الشحن:** امسح الأنتي-باترنز في §6.
7. **مرجع سريع:** الـ cheatsheet في §12.

---

## 1. المفاهيم الجوهرية (Glossary مضغوط)

| المصطلح | التعريف التشغيلي |
|---|---|
| **Mechanics** | rules متحددة بدقة: الكيانات والعمليات **والـ data اللازمة للتنفيذ**. لازم تبقى مفصّلة كفاية إن المبرمج يحوّلها كود من غير لبس. مثال Monopoly: الـ rules كام صفحة، لكن الـ mechanics فيها أسعار كل property ونص كل كروت Chance وCommunity Chest. |
| **Mechanism** | مجموعة rules مرتبطة بعنصر أو تفاعل واحد. مثال: منصة متحركة بسرعتها، والمخلوقات اللي بتقف عليها وبتتحرك معاها، وبتعكس اتجاهها لما تخبط أو بعد مسافة. |
| **Core mechanics** | الأكتر تأثيرًا، وبتتفاعل مع mechanics أصغر. مثال: الجاذبية في platformer (بتأثر على كل جسم متحرك وعلى الـ jump والـ fall damage). مش core: نقل items في الـ inventory أو AI الـ NPC. الخط بينهم مش حاد. |
| **Gameplay** | challenges بتفرضها اللعبة + actions بتسمح بيها. **الـ mechanics هي اللي بتولّد الـ gameplay.** |
| **الأنواع الخمسة** | Physics / Internal economy / Progression / Tactical maneuvering / Social interaction. |
| **Continuous vs Discrete** | Continuous: floating-point وreal-time، غالبًا physics والـ timing/rhythm. Discrete: integers، «مفيش نص power-up»، غالبًا economy. |
| **Emergence** | rules قليلة × تفاعلات كتير، فالتحديات بتطلع وقت اللعب. Juul: «Emergence is the primordial game structure». |
| **Progression** | تحديات معدّة مسبقًا بتسلسل ثابت (أو متغير قليلًا)، وغالبًا لكل تحدي حل واحد. Juul: **أي لعبة ليها walkthrough تبقى progression**. ⚠ ما تخلطهاش مع leveling أو difficulty curve أو skill tree. |
| **Probability space** | كل الـ states الممكنة من الـ state الحالية. Wide = خيارات كتير دلوقتي. Deep = states كتير بعد اختيارات متتالية. |
| **Trajectory** | مسار اللاعب جوه الـ probability space. trajectories أكتر ومثيرة تبقى gameplay أحسن. |
| **Resource** | أي حاجة بتتقاس رقميًا: فلوس، طاقة، وقت، وحدات، **وحتى الأعداء**. مش resource: المنصات والحيطان. Tangible/Intangible و Abstract/Concrete. |
| **Entity** | بتخزن كمية (= variable). Simple = قيمة واحدة. Compound = مجموعة attributes. |
| **الوظائف الاقتصادية الأربعة** | Source (بيخلق) / Drain (بيمسح نهائيًا) / Converter (بيحوّل نوع لنوع) / Trader (بيبادل، والإجمالي ثابت). |
| **Feedback loop** | تغيير بيرجع يأثر على نفس الجزء. Negative = توازن. Positive = زعزعة واستقطاب. |
| **Dominant strategy** | مسار هو الأحسن دايمًا (مش لازم يضمن الفوز). لازم يتشال. |
| **Deadlock** | اعتماد متبادل اتقفل (محتاج A عشان B ومحتاج B عشان A). |
| **Gameplay phase** | فترة سلوكها الديناميكي ماشي على pattern واحد. التغيير الكبير في السلوك = phase جديدة. |
| **Design pattern** | بنية متكررة في structure الـ mechanics (أصلها Christopher Alexander 1977/1979 ← Gang of Four 1995). |

---

## 2. القواعد التشغيلية المرقمة

### 2-أ. اختيار الفكرة والـ core ★★★

1. ★★★ **Make the Toy First** (Kyle Gabler، keynote أول Global Game Jam 2009، ضمن 7 tips): قبل أي art أو content، الـ mechanics لازم تبقى ممتعة **من غير art حلو ولا أهداف واضحة ولا level design ذكي**. لو الـ toy مش ممتع، ارمِ الفكرة.
2. ★★★ **مفيش حد يعرف إن اللعبة fun من قراية الـ rules.** الطريق الوحيد إنك تلعبها، والأحسن إن حد تاني يلعبها لك. يعني القرار بيتاخد من playtest، مش من doc.
3. ★★★ **الابتكار مكانه الـ discrete.** الـ physics بقت middleware ومجال الابتكار فيها ضيق (الـ FPS بتتميز بنظام power-ups أو item economy). أي لعبة جديدة: الفيزيكس خليها reference-standard، وحط الجدة في الـ economy والـ items والـ goals.
4. ★★★ **عدم التوقع له 3 مصادر:** Chance، Player choices، Complex rules. معظم الألعاب بتمزجهم. الـ chance أسهل في الـ implementation بس **دوره supporting مش central**. الـ pure chance مكانه الكازينو.
5. ★★★ **قاعدة الطول:** كل ما اللعبة أو الليفل أطول، **لازم المهارة تشيل نصيب أكبر من الفوز**. (Hyper-casual قصير يستحمل chance أكتر. ليفل بميزانية إسقاطات كبيرة لازم يبقى skill-dominated.)
6. ★★★ **rules قليلة تولّد states كتير = لعبة أسهل في الوصول للاعب.** الـ rules الأكتر **مش** معناها states أكتر، وأحيانًا شيل rule بيحسّن الـ emergence (Tic-tac-toe مقابل Connect Four، شوف 2-ج).
7. ★★★ **خلّي الفيزيكس تنفّذ الـ rule الصعبة** (درس Connect Four: قاعدة «أسفل مربع فاضي» بتتنفذ بالجاذبية). اللاعب يفكر في **الآثار** مش في التنفيذ. ده بالظبط سر الـ physics-merge.
8. ★★★ **Continuous محتاج forgiveness + preview.**
   - Angry Birds: فرق بيكسل = critical hit أو miss كامل.
   - World of Goo أكتر forgiving: spring forces بتشد الكرة لنفس المكان، **واللعبة بتعرض الـ connections قبل ما تفلت الكرة**.
   - الـ continuous = مهارة يدوية ويقين أقل. الـ discrete = تخطيط استراتيجي. حدد إنت عايز تبيع أنهي واحدة.
9. ★★ **Player-centric:** اسأل دايمًا «مين بيحب النوع ده؟».
   - Power Grid (أنظمة متشابكة وعشوائية قليلة) بتجذب الـ mathematical strategists.
   - لعبة أقصر وعشوائيتها أعلى تناسب الكاجوال والصغيرين.
   - الناس بتختار اللعبة على نوع الـ gameplay، والـ mechanics هي اللي بتصنعه.
10. ★★ **Consistency over Realism** (Steven Poole، *Trigger Happy* 2000): الاتساق أهم من الواقعية.
    - الفشل الكلاسيكي: صاروخ بيقتل عدو جامد وما بيكسرش باب خشب خفيف.
    - Formula 1 الواقعية محتاجة سنين تدريب، فمش ممتعة.
    - اللاعبين متوقعين blasters زي Star Wars مش ليزر حقيقي.
11. ★★ **Harvey Smith** ("The Future of Game Design" 2001): ابعد عن الحلول الخاصة لكل تحدي، وروح لـ mechanics بسيطة ومتسقة بتتركّب بطرق مثيرة **حتى لو طلّعت نتايج غريبة**. الـ Rocket jumping فرصة مش bug.
12. ★★ **لو رسالتك ما فيهاش مساحة لمشاركة نشطة، ما تعملهاش لعبة** (اعمل فيلم). الـ signal في اللعبة بيتولد من الـ mechanics.

### 2-ب. عملية التصميم والبروتوتايب ★★★

13. ★★★ **التلات مراحل:**
    - **Concept:** فكرة + audience + دور اللاعب. القرارات دي ما بتتغيرش. أي proof-of-concept افترض إنك هترميه، وما تصممش الـ mechanics النهائية قبل آخر المرحلة.
    - **Elaboration:** short iterative cycles، كل cycle تطلّع حاجة playable تتختبر.
    - **Tuning:** تبدأ بـ **feature freeze**. المرحلة **subtractive**: شيل أي حاجة مش شغالة أو قيمتها قليلة.
14. ★★★ **الـ polish والـ tuning بياخدوا من ثلث لنص وقت التطوير كله.** الناس بتقلل من تقديرهم، فاحسبهم في الجدول من الأول.
15. ★★★ **صمم الـ mechanics بدري**، لأن:
    - الـ gameplay بيطلع منها.
    - التوازن حساس، وأي feature متأخرة أو تعديل mechanism ممكن يهدمه.
    - levels وart **بعد** ما الـ core يبقى balanced وfun.
16. ★★★ **Prototype Focus:** قبل ما تبني اسأل «عايز أتعلم إيه؟». التركيز على جانب واحد بيسرّعك وبيمنع المختبر يتشتت بـ bugs ملهاش علاقة. (جدول 3.2.)
17. ★★★ **شرط نجاح الـ software prototype: سهولة customization.**
    - غيّر الجاذبية أو الـ production rate وانت بتلعب.
    - ما تضيعش وقت على UI: حط القيم في **text file بيتقري عند البدء**، أو أحسن **console off-the-shelf جوه اللعبة**.
    - الـ Spore prototypes كانت منشورة على spore.com/comm/prototypes كمرجع.
18. ★★★ **Paper prototype:**
    - لو اللعبة مش معتمدة على timing/physics، اعملها board game.
    - لو معتمدة، اعمل paper للجزء اللي مش physics (مثلًا الـ economy في لعبة physics).
    - بالمهارة بيخلص في **ساعات**، وبيتعدّل وسط اللعب: «iteration cycles مش هتبقى أقصر من كده».
    - **عيوبه:** صعب تجيب لاعبين تجريبيين (لازم تشرح الـ rules بنفسك)، والـ continuous مش بيترجم. **أنسب للـ economy والـ progression.**
19. ★★ **Kit الـ paper** (Corvus Elrod 2011 + إضافات الكتاب):
    - ديكّين كروت شبه متطابقين بضهر لونه مختلف.
    - notebook **صغير** + أقلام.
    - tokens (poker chips أو حجارة Go).
    - كذا نرد (عدد الأوجه مش مهم)، ولو النسب مئوية **نردين d10 = 1–100**.
    - إضافات الكتاب: sticky notes، كروت فاضية 3x5، **card sleeves** (زي Magic) تحط فيها الورقة المكتوبة، والتعديل يتحط فوق القديم فتاريخ تصميم الكارت يفضل محفوظ.
20. ★★ **Physical prototype** للـ continuous الجسدي (مثال: laser-tag في مبنى مكتب علشان تحس بالـ FPS). LARP مصدر أفكار.
21. ★★★ **التيستر الصح لكل focus:**
    - **Economy:** power gamer خبير، وقوله «حاول تكسر اللعبة». «لو ممكن تتكسر، لازم تعرف».
    - **Tutorial:** ناس **ما شافوش اللعبة قبل كده**، وما تتدخلش وهما بيلعبوا. السؤال الوحيد: «فاهمين اللعبة وإزاي تتلعب؟».
    - الفريق مختبر كويس بس عنده handicap: عارف الاستخدام المقصود، وغالبًا برّه الـ target audience.
22. ★★★ **Reference games = prototypes ببلاش**، خصوصًا في UI وcontrols وbasic physics (اللاعبين عايزين consistency، فما تغيرش WASD لـ ESDF عشان تبتكر).
    - اختار reference بـ **scope قريب منك** (عندك شهرين؟ ما تاخدش لعبة فريق كبير عملها في سنين)، إلا لو بتدرس تفصيلة واحدة.
    - اتعلم وما تسرقش.
23. ★★ **Design docs = living documents** بتكبر مع كل mechanism وليفل. بتمنع إنك تعيد قرارات قديمة، وبتوحّد الفريق.
24. ★★ **Tech demo:** ابنيه بدري على **أصعب وأجدد جزء تكنولوجي**، وخلي عينك على فرص الـ gameplay اللي بتظهر فيه.

### 2-ج. Emergence مقابل Progression ★★★

25. ★★★ **حط اللعبة على الـ spectrum بقرار واعي:**
    - Pure emergence: كتير من الكاجوال (Bejeweled).
    - Pure progression: نادرة (The Longest Journey).
    - الأغلب **hybrid**: emergent جوه الليفل + تسلسل صارم بين الليفلات (Half-Life، Zelda).
26. ★★★ **Table 2.1 (حرفي):**

| البند | Emergence | Progression |
|---|---|---|
| عدد القواعد | Low | High |
| عدد العناصر | High | Low–High |
| التفاعلات | High | Low |
| Probability space | Large, wide | Small, deep |
| Replay value | High | Low |
| تحكم المصمم في التسلسل | Low | High |
| الطول | قصيرة (Civilization استثناء نادر) | طويلة |
| Learning curve | Steep | Gentle |

27. ★★★ **Complexity barrier:** بعد نقطة معينة في تعقيد الـ rules، تعقيد الـ gameplay **بيقفز** (explosion في الـ probability space).
28. ★★★ **فخ الـ emergence الطويلة (X-COM: UFO Defense):** غلطة صغيرة بدري ممكن تخلّي اللعبة مستحيلة تتكسب بعد ساعات. ده **design flaw**. الـ progression بيقيّد الـ space وبيمنع الوقوع فيه.
29. ★★★ **أحسن دمج بيحصل على مستوى الـ mission** (StarCraft 2): نفس نظام الـ emergence تحت، وفوقه أحداث وقيود progression بتغيّر **الهدف والإيقاع**.
    - "The Devil's Playground": الحمم بتغرق الأجزاء السفلية بشكل دوري، والهدف إنك تعيش وتحصد.
    - "The Evacuation": تحمي **4 caravans** من المدنيين.
    - مقارنةً بـ SC1 (30 mission متشابهة، والقصة framing device بس).
30. ★★ **Crawford:** الألعاب لازم تبقى **process-intensive مش data-intensive**. مولّد الليفلات بينقل الـ data-intensity لـ process-intensity.
31. ★★ **فجوة Wardrip-Fruin** (*Expressive Processing* 2009): mechanics الـ simulation متطورة، بس تتبع القصة مجرد bottlenecks/gates. ما تعتمدش على القصة كـ mechanic.
32. ★★ **Golden age test:** أي event/bonus بـ trigger اعتباطي (زي Golden age في Civilization: 20 turn إنتاج عالي) بيأثر على اللعب لكنه مش emergent. صنّفه كـ progression/dressing. الـ historical periods في Civilization برضه triggers اعتباطية ووظيفتها بصرية بس.

### 2-د. Complex Systems وبنية الـ Emergence ★★★

33. ★★★ **الخصائص البنيوية التلاتة للـ emergence:**
    - (1) أجزاء **نشطة ومترابطة**.
    - (2) **Feedback loops**.
    - (3) تفاعل على **مقاييس مختلفة**.
34. ★★★ **صفات Wolfram التلاتة** (*A New Kind of Science* 2002):
    - خلايا بسيطة بقواعد محلية.
    - **Long-range communication**.
    - **مستوى نشاط** كفاية (قليل جدًا = مفيش تعقيد).
    - تقدر «تقراهم» من الـ rules: في أوتوماتون الـ 8 تركيبات، 4 من 8 قواعد بتغيّر اللون، فنشاط عالي متوقع.
35. ★★ **التصنيف بالتوقع:** Ordered ← Periodic ← **Emergent** ← Chaotic. هدفك إن السلوك الكلي يقع في Emergent.
    - Progression = ordered.
    - الأدوار والـ ticks = periodic.
    - مراحل Civilization = emergent.
    - النرد والـ RNG واللاعبين = chaotic.
    - تجربة الحنفية بتوضح الأربعة.
36. ★★★ **أمتع سلوك بيبان على مستوى مجموعات الأجزاء مش الجزء الواحد.**
    - Glider = 5 خلايا بتنقل خلية كل 4 iterations. Glider gun بيطلّع glider كل 30 iteration.
    - Flocking: المركز + مطابقة السرعة + تجنب القرب.
37. ★★★ **Pac-Man ghosts = «ذكاء» رخيص:** قواعد سطر واحد متكاملة، من غير ما الأشباح تعرف مكان بعض.
    - Blinky: مكان اللاعب.
    - Pinky: **4 خانات قدام** اللاعب.
    - Inky: بيجمع موقع اللاعب وBlinky.
    - Clyde: بيطارد من بعيد، ولما يقرب يروح للزاوية السفلية الشمال.
    - في الـ chase: عند كل تقاطع يختار الاتجاه اللي بيقرّب ويتجاهل الحيطان. بالتبادل مع scatter.
38. ★★ **Game of Life:**
    - حية بأقل من 2 جيران أحياء ← تموت.
    - حية بأكتر من 3 ← تموت.
    - حية بـ 2 أو 3 ← تعيش.
    - ميتة بـ 3 بالظبط ← تحيا.
39. ★★ **Fromm** (*Types and Forms of Emergence* 2005):
    - Nominal/Intentional: feedback على نفس المستوى (thermostat).
    - Weak: top-down بين مستويين (flocking).
    - Multiple: short-range positive + long-range negative (البورصة، Game of Life).
    - Strong: الحياة من الجينات، الثقافة من اللغة.
40. ★★ **فرق النشاط:** في الـ progression العناصر بتتفاعل **مع الأفاتار بس** وبتنشط على الشاشة بس، فاللعبة بتبطل تمتع بعد ما الخيارات المصممة تخلص.

### 2-هـ. الـ Internal Economy ★★★

41. ★★★ **الـ economy شغل المصمم لوحده**، وده «جوهر الحرفة». الفيزيكس مع المبرمجين، والليفلات مع الكتّاب ومصممي الليفلات.
42. ★★★ **طريقة الشغل:** حدد الـ **main resources** الأول، وبعدين صِف الـ mechanisms بالوظائف الأربعة (source/drain/converter/trader).
43. ★★★ **Converter مقابل Trader:** من منظور اللاعب شبه بعض. من منظور المصمم: الـ converter (= drain بيطلق source) **بيغيّر إجمالي الموارد**، والـ trader **بيثبّته**. مثال: درع بـ 3 ذهب = trader. Warcraft شجر ← lumber = converter.
44. ★★★ **Shapes:**
    - Negative feedback ← equilibrium (خط أفقي، أو متغير تدريجيًا/دوريًا لو فيه عامل خارجي).
    - Positive feedback ← arms race أُسّي.
    - Positive على destructive ← **downward spiral** (ده مش negative feedback).
    - ممكن negative على destructive: Half-Life بيطلّع health packs أكتر لما الـ HP يقل.
45. ★★★ **مفيش shape واحد = جودة.** الـ shape بيتحدد بأهدافك (لعبة طويلة فيها كفاح طويل، أو قصيرة بانقلابات سريعة).
46. ★★★ **Positive feedback بيضخّم الفروق الصغيرة** فبيدفع للنهاية بعد ما فرق حاسم يتكون. «محدش بيحب يكمل لما يتضح مين هيكسب.»
47. ★★★ **Long-term مقابل short-term** (StarCraft: الـ SCV بـ 50 mineral):
    - مفاضلة الاستثمار والاستهلاك هي اللي بتخلّي الاقتصاد استراتيجية.
    - في عدد SCVs مثالي حسب الهدف.
    - الاستثمار الطويل بيكسب في الآخر بس فيه **مخاطرة بدري** (tank rush من Command & Conquer: Red Alert).
48. ★★★ **Deadlock = تهديد وأداة في نفس الوقت:**
    - minerals ← SCVs ← minerals، ومحتاج HQ كمورد تالت.
    - ممكن **تستخدمه في الـ level design**: ابدأ mission من غير SCVs، واللاعب يلاقيهم وينقذهم.
49. ★★★ **قاعدة مثال الـ 10 رصاصات:** سلاح فريد بـ 10 رصاصات لعدو المخرج، واللاعب بيوصل برصاصة واحدة وبيخطئ، فبقى deadlock. **كل resource مطلوب للتقدم لازم ليه source متجدد** (Zelda pots: بتتجدد لما تنقل بين الغرف، وممكن تحتوي أي حاجة، وكمان **بتلمّح**: لو لقيت arrows كتير، القوس جاي قريب).
50. ★★ **Input variation:** مدخلات اللاعب لازم تأثر على الاقتصاد، **بس كتير منها ومفيش واحد ضخم التأثير.**
51. ★★★ **Risk/Reward للـ collectibles** (Super Mario coins):
    - العملات = breadcrumbs، وافترض إن كل coin ممكن توصلها.
    - **coin واحدة في فخ مميت = ظلم.**
    - **مكافأة مرئية ومستحيل توصلها = أسوأ.**
    - خلي بالك خصوصًا من الأماكن القريبة من مسار المبتدئ.
52. ★★ **الذخيرة/الـ power-ups:** لو اللاعب وصل للـ boss وذخيرته ناقصة، يبقى بتعاقبه على مجهوده.
    - Action: ذخيرة كتير، وكافئ القتل الزيادة.
    - Survival: اقتصاد شحيح = توتر (وتوازنه صعب).
53. ★★★ **Versatile resource** (Prince of Persia: Sands of Time): رمل محدود للـ rewind والـ freeze، **وبيتعوّض بهزيمة الأعداء**. اللاعب بيقرر يصرفه فين. ده أحسن قالب لـ booster مكتسب بالأداء.
54. ★★★ **Probability space الكبيرة، 3 تحذيرات:**
    - (1) التوليفة الأكفأ بتنتشر (online RPG) والعلاج negative feedback (XP أكتر لكل level).
    - (2) الـ space لازم يبقى **أكبر من إنه يتستكشف في session واحدة**. ما تطلبش ترقية كل الـ stats (1–5) للأقصى عشان تخلص.
    - (3) **خيارات mutually exclusive** = عواقب حقيقية (class واحد، أو Deus Ex: invisibility قصيرة **أو** subdermal armor).
55. ★★★ **Deus Ex: Human Revolution flaw:** طرق لعب كتير **بس طريقة واحدة تهزم الـ bosses**، وده بينسف الـ customization. الـ levels لازم تتعمل عامة لما ما تكونش عارف build اللاعب (Deus Ex: combat/stealth/hacking، والـ XP مش متجدد).
56. ★★ **ألعاب بناء الاقتصاد (SimCity)، 3 استراتيجيات للتحكم في التعقيد:**
    - (1) **ما تقدّمش كل الـ building blocks مرة واحدة** (Civilization بتفتحهم واحد واحد).
    - (2) **الأنماط اللي بتنفع بدري تبطل تنفع بعدين** (zones فعالة للنمو بس بتلوّث على المدى الطويل = slow-working destructive positive feedback).
    - (3) **الخرايط والكوارث** بتمنع الـ dominant meta-structure وبتجبر على الارتجال.

### 2-و. الـ Feedback Loops ★★★

57. ★★★ **العدد المثالي: 2–4 major loops.** major = بيضم mechanics مهمة كتير وتأثيره كبير. الـ minor ممكن تزيد عن 4. **أكتر من 4 major = لعبة صعبة الإتقان.** ⚠ المصمم فاهم الـ loops، اللاعب لأ.
58. ★★★ **«Positive» لوحده مش كفاية. اوصف كل loop بالخصائص السبعة:**

| الخاصية | إزاي تقراها من الدياجرام |
|---|---|
| **Type** (+/−) | الأصعب. modifier موجب على flow إنتاج = positive. موجب على flow رايح لـ drain/converter = غالبًا negative. الـ activators محتاجة دراسة. |
| **Effect** (constructive/destructive) | مربوط بـ win condition = غالبًا constructive. بـ lose = destructive. |
| **Investment** | كام مورد وكام element لازم اللاعب يفعّلهم. |
| **Return** | الناتج، **قارنه بالـ investment**. |
| **Speed** | delays/queues = أبطأ. automatic أسرع من interactive. state connections أسرع من resource connections. |
| **Range** | عدد العناصر في الـ loop. |
| **Durability** | محدود لو معتمد على موارد مش بتتعوض أو بتتعوض على فترات طويلة. |
| (+ **Determinability**) | الرموز: D نرد / M multiplayer / S skill / ST strategy. كلها في الـ Tool بتطلّع قيمة 1–6. |

59. ★★★ **positive ≠ constructive، negative ≠ destructive.** الشطرنج: خسارة قطعة = positive destructive. Civilization: corruption بيبطّأ نمو المدن الكبيرة = negative على constructive.
60. ★★★ **Strength = تفاعل الخصائص.** loop دائم بـ return صغير ممكن يبقى قوي. loop **غير مباشر وبطيء بـ return كبير ومش دائم = مزعزع جدًا**، حتى لو negative (حدث كبير متأخر محدش يقدر يتوقعه).
61. ★★★ **Basketball (Marc LeBlanc، GDC 1999)، النموذج بأرقامه:** الأزرق 40% والأحمر 20%، و**كل 5 نقاط فرق** = لاعب زيادة، والحد الأدنى 5 لاعبين.
    - **Positive** (المتقدم بياخد لاعب): الأقوى بيدخل spiral. فريقين متكافئين: الحظ بيحدد مين يبدأ الـ spiral (الميل بيبان بعد حوالي 30 step).
    - **Negative** (المتأخر بياخد لاعب): **الفرق بيتثبت وما بيتقلبش**. الأضعف ما بيعديش.
62. ★★★ **Feedback على الـ relative score** نتايجه غير بديهية. الـ equilibrium هنا **dynamic** مش ثابت، وأغلب تطبيقات الـ negative المثيرة كده.
63. ★★★ **Rubberbanding:**
    - البسيط: بطّأ المتصدر وسرّع المتأخر.
    - الأدق (Mario Kart): المتأخر فرصته أكبر في أقوى power-up، والأسلحة بتضرب اللي قدامك، فالمتصدر هدف أكتر والصدارة بتتبدل وفيه last-minute surge.
    - الرابرباند العادي **بيقرّب من غير ما يقلب**. لو عايز تبادل صدارة: boost أقوى وأطول (المثال: مهارة 60% مقابل 40%، register بفرق المسافة، boost مدته 20 step و+5% لكل boost، فالصدارة بتتبدل). المثال **متطرف عمدًا**، والألعاب الحقيقية أخف.
64. ★★★ **قاعدة تطابق الـ profiles:** positive وnegative بنفس السرعة والديمومة = استقرار. **positive سريع + negative بطيء ودائم (أشيع تركيبة)** = اللاعب بيتقدم كويس في الأول وبعدين يعاني. اختارها عن قصد، أو تجنبها.
65. ★★ **Risk: 4 loops:**
    - territories (مباشر وبطيء، الـ build بيزيد +1/3، استثمار عالي).
    - cards (أبطأ: كارت/turn ومحتاج 3 للـ set، بس بيدي بين **4 و10 armies**).
    - continents (أسرع وأقوى، 5 territories = continent = **2 armies/turn**، وبيستدعي countermeasures شرسة).
    - opposition (friction من اللاعبين = negative، خصوصًا مع collusion ضد المتصدر).
    - **أثر سلوكي:** الكارت اللي بيكمّل set بيخلّي اللاعب يخاطر أكتر **من غير ما فرصته في المعركة تتحسن**، والـ continent بيخليه يخاطر أكتر من اللازم.
66. ★★ **Asymmetry rule للـ phases:** الرجوع من الزحمة محتاج ضغط أقل بكتير من اللي بدأها. asymmetry كبير = phases مستقرة، وصغير = تذبذب.
67. ★★★ **أضف loops واحد واحد** (تمرين 5 في فصل 6): loop واحد ← prototype + playtest ← loop بـ signature مختلف ← كرر لحد ما تبقى ممتعة ومتوازنة وemergent.

### 2-ز. الـ Randomness ★★★

68. ★★★ **الأحسن: emergence من deterministic loops، والـ chance باقتصاد.** لما الـ emergence هي المصدر، كل قرار بيفرق.
69. ★★★ **Frequency × Impact:** لألعاب الـ emergence، استخدم **عشوائية بتكرار عالي وتأثير منخفض**. زيادة التكرار بتقلل التأثير لأن الاحتمالات بتتعادل.
    - نرد واحد = توزيع متساوي.
    - نردين = 2–12 و**7 الأكتر احتمالًا**.
70. ★★★ **الاستخدامين المفيدين للعشوائية:**
    - (1) **إجبار الارتجال:** خرايط Civilization/SimCity، أو Magic: ديك حوالي **40 كارت** بيتخلط. الملعب لازم يبقى **عشوائي بس متساوي للكل**.
    - (2) **كسر الـ dominant strategy.**
71. ★★★ **مثال الـ Harvester بالأرقام:** تبدأ بـ harvester بيجمع 0.1/turn، والإضافي بـ 3 طاقة، والهدف 30.
    - **Table 6.3** (harvesters إضافية ← turns): 0←300، 1←181، 2←146، 3←133، 4←125، 5←121، 6←120، **7←119**، 8←120، 9←120، 10←121، 11←121، 12←122.
    - deterministic: الأحمر (7) بيكسب الأزرق (2) دايمًا (119 مقابل 146).
    - **عشوائي** (كل harvester بيزود احتمال الحصاد 10%): الأزرق بياخد حوالي **15%** فوز بعد 1000 run.
72. ★★ **Power Grid** = عشوائية محسوبة: عاملين عشوائيين بس (ترتيب البداية + كروت المحطات)، والتعادل بيحصل كده:
    - الترتيب بيتغير لصالح المتأخر.
    - المحطات الرخيصة بس متاحة والغالية بترجع الديك لحد النهاية.
    - **مفيش قرار لاعب معتمد على نرد** (مزايدة).
    - ألعاب تانية تستاهل التحليل: Puerto Rico، Caylus، Agricola.
73. ★★★ **Random intervals** (John Hopson، "Behavioral Game Design" 2001):
    - مكافأة على intervals منتظمة = النشاط بيعلى **عند** الـ interval.
    - intervals عشوائية = اللاعب **نشط معظم الوقت**.
    - «استخدمها بحذر.» (مهم لـ rewarded ads والـ drops.)
74. ★★★ **عشوائية مشتركة لكل اللاعبين = تعادل الحظ والـ unpredictability موجودة.** حتى مع الـ dynamic engine (اللي بيضخّم حظ البداية).

### 2-ح. الـ Machinations (نمذجة الاقتصاد) ★★★

75. ★★★ **ليه Machinations:** الكود وstate diagrams وPetri nets مش مناسبين للمصمم وما بيبيّنوش الـ feedback. **1,000 run في ثواني** من غير كود.
76. **Nodes الأساسية:**
    - **Pool:** بيخزن.
    - **Source** (مثلث لفوق): بيخلق. أمثلة: shields في X-Wing Alliance = automatic، armies في Risk = interactive، Go في Monopoly = passive.
    - **Drain** (مثلث لتحت): `all` بيفضّي كل حاجة (السيفون).
    - **Converter** (مثلث لليمين بخط): مثال sawmill شجرة ← 50 لوح.
    - **Trader:** مثال 3 فلوس ↔ 2 بضاعة، وFallout 3 تجارها مخزونهم محدود.
    - **Gate** (معيّن): بيوزع فورًا.
    - **End condition:** لازم activator.
    - **Register:** حسابات، وفيه max/min.
    - **Delay:** بيأخّر كل الموارد مع بعض.
    - **Queue:** مورد واحد في المرة.
    - **Limited source** = pool بعدد. **Limited converter** = drain + limited source.
77. **Activation modes:** Automatic `*` (كل iteration، مع بعض) / Interactive (double outline = فعل لاعب) / Starting `s` (مرة واحدة قبل البداية) / Passive (بـ trigger بس). **أي mechanic في أي لعبة بيتحط في واحد من الأربعة: النظام / اللاعب / الإعداد / نظام تاني.**
78. **Pull/Push:** الافتراضي pull بالمتاح لحد الـ flow rate. `p` = push. `&` = **all-or-none** («ادفع التمن كامل أو مفيش صفقة»، مناسب للـ costs). الافتراضي مناسب للـ harvesting.
79. **Time modes:**
    - **Synchronous:** الكل على interval، وكل interactive مرة واحدة في الـ step. الطلب المتعارض على مورد نادر **بيفشل للكل**.
    - **Asynchronous** (الافتراضي): التنفيذ فوري. الأولوية عشوائية وبعدين بتتبادل. (مثال Fig 5.10: 9 موارد ← sync 4/4 والباقي 1، async 4/5.)
    - **Turn-based:** action points وميزانية ثابتة لكل turn. ★ حيلة «End Turn»: كل الأفعال تكلفتها 0 ما عدا node نهاية.
80. **State connections (منقطة):**
    - **Label modifier:** `Lt+1 = Lt + Σ(M×ΔS)`. موجب = يتبع، سالب = يعكس. مثال: +3 والـ origin زاد 2 ← +6.
    - **Node modifier:** `Nt+1 = Nt + Σ(M×ΔS)`، وممكن يعمل shortage سالب. ⚠ **ما تستخدمهوش مع موارد ملموسة** (keys/health)، بس مع المجردة (threat level). الكسور: البسط بيتطبق كل ما الـ origin يتغير بقيمة المقام (7←8: −2/4 بيخصم 2، +1/3 ولا حاجة). Catan: village = 1 point وcity = 2.
    - **Trigger `*`:** بيطلق الـ target لما كل inputs الـ origin تتحقق، وغالبًا بيطلق passive nodes. Monopoly: الدفع بيطلق نقل الـ property.
    - **Activator:** شرط (`==0`, `<3`, `3-6`) بيفعّل أو يكبت. Caylus: workers في مبنى.
    - **Reverse trigger `!`:** «عقاب العجز». Civilization بيبيع تحسينات لما الـ upkeep ما يتدفعش، وend condition لما damage يجي بعد HP = 0.
    - **الربط:** modifiers = كمية ← كمية. triggers = حدث ← حدث. activators = حالة ← إذن.
81. **Gates:**
    - Probable: نسب ≤100% (لو أقل، فيه احتمال المورد يتدمر)، أو أوزان (1 و3 ← 1/4 و3/4).
    - Conditional: كل شرط اتحقق بيطلع مورد (ممكن duplication، ولو مفيش شرط اتحقق المورد بيتدمر).
    - Deterministic = counting gate. Random = نرد (الـ conditional 1–6).
    - كل output state من gate = trigger.
82. **Intervals والـ multipliers:**
    - `1/5` = واحد كل 5 steps. `5/10` = burst. `D6/3`. `1/(D4+2)` = واحد كل 3–6 steps. `D6/D6`.
    - dynamic بوحدة `i`. multiplier `3*50%`، وdynamic بوحدة `m`.
83. ★★ **Color-coding:**
    - موارد مختلفة في نفس الـ pool.
    - الـ connection بيسحب لونه بس.
    - الـ gate بيفرز أو **بيغيّر اللون**.
    - queue ملونة: knights (أحمر) أغلى وأبطأ من soldiers (أزرق).
84. ★★★ **النمذجة التقريبية مقبولة طالما البنية محفوظة، واكتب كل تقريب كافتراض باسمه.**
    - Pac-Man: نجاح الأكل بيبدأ 100% وبينقص 1%/dot، ولو 0.25% يبقى لاعب ماهر.
    - **أسهل تنمذج لعبة جديدة من لعبة موجودة.**
85. ★★ **Level of detail:** الدياجرام الثابت ممكن يحذف تفاصيل (رموز عشوائية) عشان البنية تبان. **التشغيل في الـ Tool محتاج كل حاجة محددة.**

### 2-ط. الـ Design Patterns (الاستخدام) ★★★

86. ★★★ **الـ patterns لغة مشتركة للفريق والتيستر-بوت والمولّد.** اكتب كل تحدي جديد بالفورمات: Name / Intent / Motivation / Applicability / Structure / Participants / Collaborations / Consequences / Implementation (**+ أثر الـ randomness**) / Examples (**مثالين على الأقل**) / Related. **بأسماء عامة مش Mossfolk-specific.**
87. ★★★ **Elaboration/Simplification كمقبض تعقيد:**
    - بسيطة زيادة ← بدّل pattern بالـ pattern اللي بيعمله elaboration.
    - معقدة زيادة ← بدّله بالأبسط.
    - السلسلة: static engine ⊂ dynamic engine ⊂ engine building ⊂ worker placement.
    - كل engine = elaboration لـ source، وكل friction = elaboration لـ drain.
    - attrition = dynamic friction متماثل.
88. ★★★ **«Elaborate اللي بيولّد أهم gameplay وبسّط الباقي»:** الأجزاء الثانوية ممكن تبقى **source بسيط بمعدل عشوائي**.
89. ★★★ **التزم بالـ patterns في الأول، واكسرها بعد ما تكسب خبرة.**
90. ★★★ **Brainstorm بالكروت:** اكتب أسماء الـ 16 على كروت واخلط واسحب 2–3، وصمم اقتصاد حواليهم (paper prototype في كل خطوة، لحد 3–4).
91. ★★ **Pattern كـ lens:** اسحب pattern عشوائي واسأل: موجود في التصميم؟ شغال؟ لو أضفته هيحل مشكلة؟
92. ★★ **التشخيص:** نتايج اعتباطية من positive قوي بيضخّم حظ بدري ← ضيف **Trade** (لو فيه موارد كتير) أو **dynamic friction**.
93. ★★ **الـ genres = تركيبات:**
    - RTS = dynamic engine + attrition (+ arms race/engine building).
    - RPG = playing style reinforcement + escalating challenge.
    - Tetris = escalating complexity + escalating challenge.

### 2-ي. الـ Simulation والـ Balancing (التيستر-بوت) ★★★

94. ★★★ **«Tune your mechanics, not your artificial players.»** لو بتصرف وقت كبير عشان تعمل AP ذكي يمشّي الاقتصاد، يبقى الاقتصاد فيه مشكلة. الـ AP وظيفته **يكشف** مش يخبّي.
95. ★★★ **الـ AP = caricature:** استراتيجية واحدة بإصرار مهما كانت العواقب. شغّل كذا AP. **AP بيغلب الباقيين باستمرار = dominant strategy ← غيّر الـ mechanics.**
96. ★★★ **منطق الـ script = priority list first-match-wins:** من فوق لتحت، وأول command بيتنفذ بيوقف الـ script.
    - `fireRandom` مع تكرار الاسم = وزن (Produce, Produce, Consume, Upgrade = 50/25/25).
    - `pregen0–9` = 10 قيم عشوائية ثابتة طول الـ run.
    - `stopDiagram(message)` بيعد **إيه اللي أنهى الـ run**.
    - الـ AP في دياجرام ملون بيفعّل nodes بلونه بس.
97. ★★★ **Multiple runs:** الافتراضي 100، وأي run بيتوقف تلقائيًا بعد 10,000 step. الـ diagram لازم فيه end condition ممكن يتوصل. بيعد الـ end conditions ومتوسط الزمن. الـ charts بتعرض آخر 25 وبتصدّر **CSV**.
98. ★★★ **Removing All Randomness** عشان تثبت الـ dominant strategy:
    - % ← كسر ثابت (20% ← 0.2 = اتنين كل 10).
    - النرد المتعدد ← متوسط = `(أوجه+1)×عدد÷2` (3D6 = **10.5**).
    - `fireRandom` ← sequential.
    - `if(random<0.3)` ← `if(steps%10<3)`.
    - نفس النتيجة كل run = مقارنة نضيفة.
99. ★★★ **افصل أثر عشوائية كل mechanic لوحدها** (Monopoly): الـ Go صغير، الإيجار أكبر، **فرصة الشراء الأكبر بكتير** لأنها بتغيّر توزيع الملكية. المؤشر الحقيقي للقوة = العقارات مش الفلوس.
100. ★★★ **Stalemate check:** لعبة ما بتخلصش = غياب escalation. Monopoly من غير rent inflation بيجرّ لأن الـ Go بيعوّض. الحل بيوت وفنادق. (دخل Go 5/(3+D5): حد بيكسب حوالي 75% و25% بتجر. 2/(3+D5): الجر = صفر. دخل عالي مع inflation مضاعف: equilibrium 2%.)
101. ★★★ **Dynamic friction بيكبح الـ engine المسيطر وبيقتل الـ stalemate** (Table 8.2، 1000 run، الأزرق بيشتري 14 والأحمر 6، ضريبة كل 6 steps):

| ضريبة (عقار/بيت) | أزرق | أحمر | مفيش فائز |
|---|---|---|---|
| 0 | 632 | 152 | 216 |
| 0.1/0.02 | 557 | 314 | 129 |
| 0.2/0.04 | 472 | 503 | 25 |
| 0.3/0.06 | 456 | 542 | 2 |

   فوق حد معين، الملكية نفسها بتبقى عيب.
102. ★★ **Reserve الـ AP بيكبر مع الوقت** (`Money > 4+steps×0.04`) عشان ما يفلسش بدري. **Linking APs:** builder + attacker + selector.

### 2-ك. Level Design والتعليم ★★★

103. ★★★ **نوع الـ end condition بيعيد تشكيل الاستراتيجية المثلى** (Harvester: هدف «عدد harvesters» بيخلّي الكل يبني بأسرع ما يمكن، ومش لازم أحسن). أي تغيير في نوع الهدف ← شغّل البوت تاني.
104. ★★★ **Gameplay كتير من core واحد** (StarCraft II):
    - (1) غيّر الهدف.
    - (2) عطّل mechanisms.
    - (3) ضيف mechanism لليفل واحد.
    - الليفل 1 من غير بناء، الليفل 2 بمباني قليلة، وبعد 3 ليفلات اللاعب بيختار.
    - Devil's Playground (حمم = slow cycle)، Outbreak (ليل/نهار).
105. ★★★ **«الليفل ممتع بقد أضعف mechanism فيه.»** ابني core متين، وكل task تبقى **zoom على جزء منه**، مش mechanic جديد كل مرة.
106. ★★★ **Crawford (1984): السرعة والجهد المعرفي لازم يتوازنوا.** جهد عالي ← بطيء أو turn-based. جهد قليل ← سريع.
107. ★★★ **سؤال تقييم دايم: «كام خيار متاح للاعب في اللحظة دي؟»** الأكتر أحسن، بشرط ما يغرقش من غير data يختار بيها. لو التسلسل ثابت والأفعال من غير اختيار يبقى gameplay = تعليم ✓.
108. ★★★ **Mapping mechanics ← mission** (مثال 10 ورود):
    - trivial.
    - ← ضيف أعداء (التجنب بيشيل 1–3 threat عشوائي = تفاوت المهارة).
    - ← **كل وردة بتزود إنتاج التهديد** (منحنى بيبدأ سهل ويصعب بسرعة).
    - ← subtasks (3) بتفتح الورد.
    - ← dependencies.
109. ★★★ **إعادة استخدام نفس الـ space لـ missions مختلفة** (GTA): بيوفر فلوس، و**بيزود إحساس السيطرة** لأن اللاعب عارف المكان.
110. ★★ **Optional task:** مكافأته تأثر على الـ gameplay **بس ما تتحولش لشرط فعلي.** **Mutually exclusive** (تسلل/رشوة/قتال): لازم **backup strategy متاحة دايمًا** (القتال)، وما تعملش وضع unsolvable.
111. ★★ **ابدأ بالـ mission غالبًا** (أسهل)، وخلي بالك من الـ space الخطي اللي بيقتل الاستكشاف. وفتح الـ space عشان تنوّع mission خطية = استراتيجية ضعيفة (backtracking).
112. ★★★ **Skill atoms** (Daniel Cook، "The Chemistry of Game Design" 2007): Action ← Simulation ← **Feedback** (الـ output) ← Modeling.
    - مثال Mario: A ← قوة قفز + جاذبية ← أنيميشن وصوت ← «A = قفز».
    - الـ atoms بتعمل chains وtrees.
113. ★★★ **Skill tree deep مش wide** (على الأقل في الأول): الـ primary skills لازم تتعلم صراحة. لو اللاعب فاته primary («ما داسش زرار الضرب أبدًا»)، فاته فرع كامل. «Easy to learn, lifetime to master» = primaries قليلة وسلاسل طويلة (الشطرنج: الحركات + castling + en passant + promotion).
114. ★★★ **Kihon ← Kihon-kata ← Kata ← Kumite** لكل عنصر جديد:
    - تكنيك واحد في بيئة آمنة.
    - تكرار لحد الأوتوماتيكية («wax on, wax off»).
    - تركيبات مع أنماط deterministic.
    - ذروة حرة (boss) أقل توقعًا.
    - الاختبار = **تحدي ما تقدرش تتفاداه ومحتاج المهارة الصح**.
    - Twilight Princess: Forest Temple (bomblings ← Gale Boomerang ← boomerang يجيب bombling ← boss)، وGoron Mines (Iron Boots ← hero's bow ← تبديل سريع ← boss). اعمل **chart زي Fig 10.14** توزّع فيه إدخال الـ mechanics على اللعبة كلها.
115. ★★ **Hidden information:** وضّح **لحظة** تغيّر الـ state حتى لو الـ state نفسها مخفية.
116. ★★ **أنواع التقدم الأربعة:** tasks مكتملة (%) / **distance to target** (فيه setbacks، و90% مش معناها قريب: Caesar III) / character growth (Deus Ex canisters: كل اختيار بيظهر مرة واحدة) / **player growth** (كوينة في مكان غريب = دعوة للاستكشاف).
117. ★★ **Shifting perspectives:** نوّع الـ backgrounds والـ landscapes بين الأقسام (لحظة القمة بعد الغابة).
118. ★★ **Mini golf:** 18 حفرة بصعوبة متزايدة، وتصميمها تمرين ممتاز. **قلعة ديزني لاند** = landmark للتوجيه.
119. ★★ **Zelda dungeon arc:** mini-boss في النص ← سلاح ← end boss. بتستكشف بيه الـ mechanic الجديد، وبتتنوع، وبتفتح مناطق، وبيتعمل dramatic arc.
120. ★★ **Hub-and-spoke:** اختيار المهمة وتغييرها لو صعبت، save points، backtracking أقل. Forest Temple: bottleneck في النص (Ook + boomerang)، وparallel قبله وبعده، والـ mini-boss بيتفتح بعد 4 قرود.
121. ★★ **Lock-and-key** = ترجمة prerequisites لبنية مكانية. نادرًا فيها feedback، فنادرًا فيها emergence. الـ boomerang سلاح ومفتاح (wind switches وجسور، و4 switches بالترتيب علشان الـ master key).

### 2-ل. Progression Mechanisms والـ Phases ★★★

122. ★★★ **لما التقدم emergent، الـ pacing بييجي من الـ phases.** RTS: Building ← Exploration ← Offensive (+ consolidation، research، rush بيتخطى).
123. ★★★ **ركّب الـ phases:** عايز building phase طويلة؟ ضايق اللاعب بهجمات صغيرة متكررة. عايز exploration/consolidation؟ خلي الموارد نادرة ومبعثرة.
124. ★★★ **4 patterns بتعمل phase shift:**
    - (1) **Slow cycle:** فعال بس ناقص subtlety (King Canute والمد).
    - (2) **Static friction/engine نادر وعالي:** Caesar III غزاة وطلبات إمبراطور ← decline، أو قوافل ← وفرة.
    - (3) **Escalating complexity:** تحت السيطرة ← losing phase قصيرة، وفيه عامل عشوائي ممكن يرجّعك (Tetris).
    - (4) **Stopping mechanism / multiple feedback:** The Seven Cities of Gold «Amaze the natives» بيضعف مع الوقت.
125. ★★★ **مش هتعرف إمتى بالظبط، بس تقدر تتنبأ بنوع الـ phase** (الـ drop rate في Tetris بيزيد ببطء، فالـ losing phase جاية جاية).
126. ★★ **Scripting + emergence مقبول بخفة** (StarCraft attack waves: بعضها بوقت وبعضها بموقع).
127. ★★ **Progress indirect** (Elite / Catan / The Sims): بيقاوم الـ dominant strategy وبيدي **multiple win paths** (آمن مقابل high-risk development cards)، **وتمنه الـ readability** (مين كسبان؟). Monopoly واضحة لأن كل حاجة مكشوفة.
128. ★ **Emergent storytelling** محدش بناه بحجم لعبة كاملة. القصة authored.

### 2-م. Meaningful Mechanics ★★

129. ★★★ **الرسالة الضمنية = الأفعال المطلوبة للفوز والأفعال الأكفأ.** لو الإطلاق core ومطلوب يبقى «العنف بينجح». لو السلمي أبطأ وأصعب يبقى الرسالة «العنف فعال».
130. ★★ **المعنى بييجي من المجهود والقيود.** Sandbox بموارد لانهائية ومن غير عواقب = مفيش رسالة.
131. ★★ **SimCity:** ضرايب عالية ← الشركات تمشي، وإنفاق قليل ← الناس تمشي. الرسالة «الاعتدال بينجح» واتكشفت باللعب. **PeaceMaker:** معيارين (البقاء في المنصب + السلام) بيمنعوا الوعظ.
132. ★★ **False choice / Jesus-Hitler dichotomy:** لو بتعاقب خيار دايمًا، اللاعب هيكتشفه.
133. ★★ **Ethics (GTA III):** حتى لو الفعل مش مطلوب (health 125% واسترداد $50)، توفير المكونات من غير عواقب طلّع رسالة ما كانتش مخططة.
134. ★★ **Semiotics:** Icon (بيشبه) / Index (سببي) / Symbol (اتفاقي). الألعاب بتكسب بالـ index والـ symbol (power bar بدل أنيميشن الإصابة). **Playtest للمتعة مش للدقة.** الواقعية غلطة لو جت على حساب المتعة.
135. ★★ **Abstraction:**
    - Elimination: ممسحات الزجاج والهوائي في الـ aerodynamics.
    - Simplification: «1 من كل 10,000 هبوط» كـ random factor، والفلوس $25.37 مش فئات.
    - **Simulations can lie** (Eco 1976، Bogost 2006): America's Army متماثلة فما بتدرّبش على مكافحة التمرد، والدم فيها قليل.
136. ★★★ **Analogous** (Diablo grid 1x1/2x2/1x4: الحجم بدل الوزن) و**Symbolic** (Risk dice = معركة، Mario القفز = قتال، Sonic هجوم واحد):
    - **اختصر الأفعال، ووصّل قاعدتين بينهم affinity.**
    - قلل العناصر **من غير ما تقلل عدد الـ loops.**
137. ★★★ **Discrete infinity** (Chomsky 1972): **عدد الـ connections أهم من عدد العناصر.** وكمان الأقل iconic بيتنقل خارج اللعبة أكتر (Monopoly مقابل نسخة دقيقة من Atlantic City).
138. ★★ **Less is more** (Saint-Exupéry 1939: الكمال لما ما يبقاش فيه حاجة تتشال) **طالما اللاعبين مبسوطين**. تحذير QTE: تبسيط ألعاب القتال اشمأز منه الجمهور الأساسي.
139. ★★ **Layers متعددة** (Eco عن Shakespeare): جاذبية أوسع + replay + humor/irony.
    - Bioshock: physical/moral/aesthetic (اتباع كـ coffee-table book)/political (Andrew Ryan ← Ayn Rand).
    - **التناقض بين المظهر والـ mechanics:** September 12 (القتل بيولّد إرهابيين، والأحسن ما تعملش حاجة) وTrain (Brathwaite 2009، ركاب صفر ← معسكر).
140. ★★ **Serious games** (Sawyer: «Serious games solve problems»):
    - ابني حوالين الموضوع وabstract الباقي.
    - «serious مش معناها جد في كل حاجة».
    - ما تبدأش بنسخ لعبة ترفيهية.
    - Kriegsspiel 1812 / Nimitz 1960 (الـ kamikaze بس اللي ما اتوقعوش) / Tannenberg / The Landlord's Game 1904 (Elizabeth Magie).
    - Gamification غالبًا تافهة (Foldit مثال جيد).
141. ★ **Jakobson (1960) — poetic function:** الـ signal المصنوع بحرفية جزء من قيمة الترفيه نفسه.

---

## 3. جداول القرار

### 3.1 اختيار الفكرة / الـ core ★★★

| لو الفكرة... | القرار |
|---|---|
| ممتعة كـ toy من غير art ولا هدف | ✅ كمّل |
| محتاجة art/content عشان تبقى ممتعة | ❌ ارمِ أو غيّر الـ core |
| جدتها في الفيزيكس نفسها | ⚠ مجال ضيق. انقل الجدة للـ discrete layer |
| جلسة قصيرة جدًا (hyper) | chance مقبول نسبيًا، بس كـ supporting |
| جلسة/ليفل طويل | لازم المهارة تحسم |
| continuous (drop/aim) | لازم forgiveness + preview (World of Goo) |
| rules كتير وstates قليلة | ❌ بسّط. دوّر على Connect Four لفكرتك |
| جمهور hyper/hybrid-casual | patterns بسيطة، 2–4 loops بحد أقصى، deep skill tree |
| جمهور mathematical strategist | أنظمة متشابكة وعشوائية قليلة (Power Grid) |

### 3.2 أي Prototype؟ ★★★

| الـ focus | النوع | التيستر | السؤال |
|---|---|---|---|
| Tech demo | software، أصعب جزء تقني، بدري | الفريق والـ publisher | نقدر نبنيها؟ |
| Game economy | **paper low-fidelity بدري** | power gamer «اكسرها» / AP | balanced؟ فيه dominant strategy؟ الخيارات مثيرة؟ النتايج متوقعة؟ |
| Interface/controls | software high-fidelity (playground) | لاعبين | بينفذوا صح؟ عايزين أفعال تانية؟ بياخدوا بالهم من الـ damage وتغيّر الـ state؟ |
| Tutorial | متأخر، بعد ما الـ mechanics تثبت | **ناس جديدة ومن غير تدخل** | فاهمين؟ |
| Moment-to-moment feel | vertical slice | جمهور | الإحساس؟ |
| Continuous physical | physical prototype | لاعبين | الإحساس الجسدي؟ |
| UI كامل من غير mechanics | horizontal slice | — | — |

### 3.3 تشخيص الـ balance ← العلاج ★★★

| العَرَض | السبب الغالب | العلاج (pattern) |
|---|---|---|
| المتقدم بدري بيكسب دايمًا ونتايج اعتباطية | positive constructive قوي بيضخّم الحظ | Dynamic friction / Trade / عشوائية مشتركة |
| اللعبة مش بتخلص (stalemate) | مفيش escalation أو friction | escalation (rent inflation) + dynamic friction |
| كل اللاعبين بيعملوا نفس الحاجة | dominant strategy | balance، ولو صعب: عشوائية / stopping mechanism / RPS / الفعّال بدري يبطل يفعّل بعدين |
| فعل واحد بيتكرر لحد الإساءة | مفيش diminishing returns | Stopping mechanism |
| اللاعب اتحبس من غير مخرج | deadlock | weak static engine / source متجدد (Zelda pots) / backup strategy |
| بداية حلوة وبعدين انهيار ممل | positive سريع + negative بطيء | طابق الـ profiles أو اقصده |
| اثنين strategies مش متوازنين | balance هش | فرّقهم في الـ risk/reward أو اعمل 3 بشكل RPS |
| اللعبة متوقعة بعد الاستكشاف | progression بحت أو أجزاء مش متصلة | زوّد الـ connections والنشاط وloops على مقاييس مختلفة |
| اللاعب مش فاهم مين كسبان | progress غير مباشر | قلّله أو اكشف الـ state |
| الصعوبة مش بتلحق مهارة اللاعب | مفيش تكيّف | Escalating challenge + friction |
| مستحيل الكسب بعد غلطة بدري | فخ X-COM | قيّد بالـ progression أو ضيف negative feedback |

### 3.4 اختيار نوع الـ Feedback ★★★

| عايز... | استخدم |
|---|---|
| استقرار / equilibrium | Negative (dynamic أحسن من الثابت) |
| نهاية سريعة بعد فرق حاسم | Positive constructive |
| مباراة قريبة من غير قلب | Rubberband عادي (negative على النسبي) |
| تبادل صدارة | Negative أقوى وأطول (boost 20 step) |
| عدالة multiplayer من غير تدمير | Trade |
| صراع مباشر | Attrition (**بتكلفة**) |
| نمط «الأقوى بدري بيدفع التمن بعدين» | slow destructive positive (تلوث SimCity) |

### 3.5 Static Friction مقابل Dynamic Friction ★★

| | Static | Dynamic |
|---|---|---|
| المعدل | ثابت/عشوائي ومستقل عن الأداء | بيتأثر بحالة اللعبة |
| بيكافئ | الاستثمار الطويل (بيضرب الإنتاج الأولي بس) | القصير (بيضرب التضخم) |
| أمثلة | tribute في Caesar III، كروت Chance في Monopoly | الأعداء في Tower defense، happiness في Civilization |
| ضبط | فترات قصيرة = استقرار. نادر وعالي = هزة / periodic. المستمر أضعف من الدوري بنفس الكمية | المحرّك: كمية الطاقة (سريع) / عدد الترقيات / التقدم (أبطأ وغير مباشر) |

### 3.6 الـ Time Mode في النموذج ★★

| اللعبة | Mode |
|---|---|
| real-time، القرار فوري | Asynchronous |
| simultaneous turns | Synchronous |
| ميزانية أفعال (زي drop budget) | Turn-based بـ action points |

---

## 4. مكتبة الـ 16 Pattern (Appendix B) ★★★

### 4.1 Engines (بتنتج)

| Pattern | Intent | استخدمه لما | تحذيرات وimplementation | أمثلة |
|---|---|---|---|---|
| **Static Engine** ★★★ | flow ثابت أو unpredictable | تحدد الأفعال من غير تعقيد | خيار صرف واحد = قليل الفايدة. imbalance لو المعدل مختلف بين اللاعبين. unpredictable = استعداد للشحّ. **نفس العشوائية للكل**. آلية «أقل رقم سري يدخل، ومقترحه يلعب الأول» ضد الـ inflation | X-Wing Alliance (الطاقة بتتوزع على shields/speed/lasers)، Descent (2 actions = 5 توليفات، مفيش تخزين) |
| **Dynamic Engine** ★★★ | source اللاعب بيستثمر يحسّنه | trade-off طويل/قصير | positive قوي محتاج friction/escalation. dominant strategy من الاتجاهين. **Signature: استثمار ببان بلا تقدم ← تسارع**. ترقية frequency = flow، count = bursts. التحويل لـ energy بأقل من الاستثمار | StarCraft SCV، Catan (city بتضاعف) |
| **Converter Engine** ★★ | 2 converters في loop بفائض | آلية أعقد بخيارات profile | **deadlock ← weak static engine**. خطوات قليلة = ميزة محدودة، كتير = مرهق. **limiter (gate)** = throttle | Elite (تجارة بين الكواكب، والسعة هي الحد، والربح بيقل)، Power Grid (فلوس عن كل مدينة متصلة + دخل صغير مضمون) |
| **Engine Building** ★ | جزء كبير من اللعب بناء engine | بناء وتخطيط طويل، إيقاع بطيء | تقييم حالة الـ engine **لازم يبقى مش تافه**. positive مش قوي ولا سريع زيادة، والبناء يتوزع على اللعبة | SimCity (ممكن ينهار)، Puerto Rico (positions محدودة = multiplayer dynamic) |

### 4.2 Friction (بتقاوم)

| Pattern | Intent | استخدمه لما | تحذيرات | أمثلة |
|---|---|---|---|---|
| **Static Friction** ★★ | drain تلقائي ثابت | مقاومة ممكن تتغلب عليها + تبالغ في الاستثمار | شوف 3.5 | Caesar III tribute، Monopoly Chance. **الإيجار = attrition مش static** |
| **Dynamic Friction** ★★★ | drain بمعدل متأثر بالحالة | الإنتاج سريع زيادة، تسكيل أوتوماتيك، تقليل فعالية الطويل | قاعدة تطابق الـ profiles | Tower defense، Civilization (happiness ≥ نص السكان، والبداية 2، مباني بطيئة دايمة مقابل culture سريع ضعيف) |
| **Stopping Mechanism** ★★★ | فعالية بتقل مع كل استخدام (diminishing returns) | منع الإساءة، dominant strategy، كبح الـ positive | مقاس بالـ output المتراكم = مؤقت وبيتناوب. مشترك = بيكافئ اللي بيلعب الأول | Warcraft III (المسافة للغابة، والمعدل بينزل لـ 0.4)، Power Grid (الوقود، والمتصدر بيلعب آخر). مثال السماد |
| **Attrition** ★★ | لاعبين بيسرقوا/يدمروا موارد بعض | تفاعل مباشر استراتيجي | **الهجوم لازم يكلّف**، وإلا لعبة الاتنين تبقى سباق تدمير. life/energy مرتبطين. شرط فوز غير الإقصاء = استراتيجيات أكتر | Magic (life/mana منفصلين، direct damage سريع، creatures دايمة وبتتراكم)، Space Hulk (غير متماثل) |

### 4.3 Escalation (بتصعّد)

| Pattern | Intent | استخدمه لما | تحذيرات | أمثلة |
|---|---|---|---|---|
| **Escalating Challenge** ★★★ | التقدم بيصعّب التقدم | سريع ومهاري، emergent بدل levels مصممة | لو الفشل بينهي اللعبة، اللعبة بتخلص بسرعة. المهمة لازم تتأثر بالمهارة. مع friction = مطابقة سريعة للمهارة | Space Invaders (كل قتل بيسرّع الباقي)، Pac-Man |
| **Escalating Complexity** ★★★ | تعقيد بيولّد تعقيد لحد الانهيار | high-pressure مهاري | **عشوائية الإنتاج = فترات نَفَس**. الخسارة انهيار سريع. multiple feedback (negative أبطأ) | Tetris (كل 10 صفوف ليفل، والكومة الأكبر = high-risk/high-reward)، Super Crate Box (تبادل قتل/جمع، واللي يوصل تحت يرجع أسرع) |
| **Arms Race** ★★ | استثمار في الهجوم والدفاع | خيارات أكتر، ضد الـ dominant، تطويل | صعب الـ balance، **اعمله intransitive RPS** (مشاة ثقيلة > خيالة > مدفعية > مشاة). بيطوّل (دفاعي). عشان يقصّر: مورد متنازع عليه | StarCraft II / Warcraft III، Tower defense غير متماثل |

### 4.4 Miscellaneous

| Pattern | Intent | تحذيرات | أمثلة |
|---|---|---|---|
| **Playing Style Reinforcement** ★★ | slow positive constructive بيخصص اللاعب عبر جلسات | محتاج استراتيجيات viable كتير. min-maxing. بيفضّل الخبير. **الوقت بيعوّض المهارة**. تكلفة تغيير. XP؟ (من غيرها: الفعل المتكرر feedback أضعف). سريع في الأول وبيبطأ (XP أُسّي). لازم ينجح؟ (لو لأ = تكرار كوميدي) | Warhammer FRP، Vampire، **D&D الأصلية ما فيهاش**، Oblivion (من غير XP)، Civilization III |
| **Multiple Feedback** ★★★ | فعل واحد بيغذّي loops بـ profiles مختلفة | أصعب. اللاعب لازم يقدر يقرا الـ profile الحالي. أشيع: fast positive + slow negative | SimCity (محطة طاقة ← تلوث، طرق ← زحمة)، Risk (3 loops) |
| **Trade** ★ | تبادل = negative constructive | محتاج موارد كتير غير موزعة بالتساوي. مع AI صعب | Catan (المتصدر بيدفع أكتر، وقرب الفوز مفيش صفقات)، Civilization III |
| **Worker Placement** ★★ | workers محدودين على stations | micromanagement وتوقيت وصراع خفي. workers قليلين = تكيّف أكتر. منافسة على stations = لازم آلية سحب | (النص مقطوع، §11) |
| **Slow Cycle** ★★ | دورة بطيئة بين حالات | phases، ضد الهيمنة، إجبار على التعديل، **بيطوّل التعلم قبل الإتقان**، صراع خفي على الـ period/amplitude | StarCraft II (حمم، ليل/نهار) — الوصف الكامل مش موجود (§11) |

### 4.5 خريطة العلاقات ★★★

```
Source ─elab→ Static Engine ─→ Dynamic Engine ─→ Engine Building ─→ Worker Placement
                    └────────→ Converter Engine ─┘
Drain ─elab→ Static Friction ─→ Dynamic Friction ─→ Stopping Mechanism ─→ Slow Cycle
                                     └─(تفاعل لاعبين)→ Attrition ─→ Arms Race ─→ Worker Placement
Static Engine/Friction ─→ Slow Cycle
Weak Static Engine ⟂ يحمي Converter Engine من الـ deadlock
Static Friction ⟂ يبالغ في Dynamic Engine | Dynamic Friction + Attrition ⟂ بيقاوموا Dynamic Engine
Escalating Challenge + (Static/Dynamic) Friction = مطابقة مهارة سريعة
Escalating Complexity ← أي engine كـ progress mechanism، وغالبًا الـ progression = escalating challenge
Playing Style Reinforcement (معتمد على النجاح) + Stopping Mechanism على أسعار الترقيات
Trade = البديل الـ constructive لـ Attrition
```

**المبدأ:** الـ engines بتنتج، والـ frictions بتقاوم، والـ escalation بتخلّي المقاومة نفسها لعبة. اختار توليفة بحيث ولا الـ positive يهزم الـ negative ولا العكس.

---

## 5. تشيك ليستات الفحص

### 5.1 فحص فكرة جديدة (قبل أي asset) ★★★
- [ ] الـ toy ممتع لوحده، ومن غير art؟
- [ ] أنهي نوع من الخمسة هو الـ core؟ وأنهي discrete وأنهي continuous؟
- [ ] الجدة في الـ discrete layer؟
- [ ] مصادر عدم التوقع التلاتة: مين بيشيل الحمل؟ والـ chance supporting بس؟
- [ ] الطول مناسب لنسبة المهارة؟
- [ ] rules قليلة وstates كتير (اختبار Connect Four)؟
- [ ] لو continuous: فين الـ forgiveness وفين الـ preview؟
- [ ] Reference game بـ scope قريب؟
- [ ] Emergence ولا progression ولا hybrid: قرار مكتوب؟
- [ ] 2–4 major loops ومتسمّيين؟
- [ ] الرسالة الضمنية للأفعال الأكفأ مقبولة؟

### 5.2 قبل بروتوتايب ★★★
- [ ] «عايز أتعلم إيه؟» مكتوبة في سطر.
- [ ] نوع الـ prototype مطابق للـ focus (جدول 3.2).
- [ ] الـ physics والـ economy قيمهم بتتغير live (console أو text file).
- [ ] التيستر مطابق للـ focus (power gamer / ناس جديدة / جمهور).
- [ ] متفق إن الـ concept prototype هيترمي.

### 5.3 فحص اقتصاد ليفل/لعبة (Machinations audit) ★★★
- [ ] كل الـ resources متعدّة ومتصنفة (tangible/intangible، abstract/concrete).
- [ ] كل mechanism متصنف: source/drain/converter/trader.
- [ ] كل loop متوصّف بالخصائص السبعة.
- [ ] مفيش deadlock من غير مخرج (weak static engine أو source متجدد أو backup).
- [ ] مفيش resource مطلوب للتقدم من غير source.
- [ ] الـ node modifiers ما بتخلقش موارد ملموسة.
- [ ] كل تقريب مكتوب كافتراض باسمه.
- [ ] الـ end conditions موجودة وممكن تتوصل.
- [ ] الـ collectibles: مفيش مكافأة صغيرة في فخ مميت، ولا مكافأة مرئية مستحيلة.
- [ ] الخيارات mutually exclusive حيث العواقب مطلوبة.
- [ ] مش مطلوب من اللاعب يستخدم كل الأدوات عشان يخلص.

### 5.4 فحص التيستر-بوت / Balance ★★★
- [ ] كذا AP caricature (استراتيجية لكل واحد).
- [ ] نسخة deterministic اتشغلت (العشوائية متشالة) لكشف الـ dominant.
- [ ] عشوائية كل mechanic اتجربت لوحدها.
- [ ] Multiple runs (100+ و1000 للقرارات) + CSV.
- [ ] `stopDiagram` برسايل لكل سبب نهاية.
- [ ] نسبة الـ stalemate/no-winner مقاسة.
- [ ] نسبة الـ dead states بدري مقاسة.
- [ ] منحنى الـ state عبر الزمن (مش win/lose بس).
- [ ] لو الـ AP محتاج ذكاء كبير ← اتعلّم إنها مشكلة mechanics.
- [ ] أي تغيير في نوع الهدف ← إعادة تشغيل.

### 5.5 فحص إدخال عنصر/تحدي جديد ★★★
- [ ] بيضيف **connections** مع الموجود، مش مجرد عنصر (discrete infinity)؟
- [ ] بيوسّع الـ probability space فعلًا، مش بس بيعقّدها؟
- [ ] بيغيّر الهدف أو الإيقاع (درس SC2)، مش بس بيصعّب؟
- [ ] secondary skill بيبني على الموجود، مش primary جديد؟
- [ ] skill atom واضح (feedback مش غامض)؟
- [ ] متقدّم بـ kihon ← kihon-kata ← kata ← kumite؟
- [ ] قواعده متسقة (اختبار الباب الخشب)؟
- [ ] مصنّف كـ pattern (static/dynamic friction أو stopping)، وبيتسكّل مع التقدم؟
- [ ] ليه counter واضح (arms race intransitive)؟
- [ ] أضعف mechanism في الليفل لسه ممتعة؟
- [ ] اتختبر بالتيستر-بوت **قبل** ما يدخل الليفلات (feature freeze logic)؟

### 5.6 فحص Tutorial/Onboarding ★★★
- [ ] الـ rules متقدمة في chunks، وبيئة آمنة بعواقب قليلة؟
- [ ] skill tree deep مش wide؟
- [ ] كل primary skill بيتعلم صراحة؟
- [ ] لحظة تغيّر الـ state واضحة؟
- [ ] اتختبر بلاعبين جداد ومن غير تدخل؟

### 5.7 فحص booster / rewarded ad / مكافأة ★★★
- [ ] فيه stopping mechanism (تكلفة بتتصاعد أو عائد بيقل)؟
- [ ] مكتسب بالأداء زي رمل Prince of Persia (versatile)؟
- [ ] مش بيكسر الليفل لوحده (مش dominant strategy «شوف إعلان واكسب»)؟
- [ ] الـ interval عشوائي ولا ثابت: قرار واعي (Hopson)؟
- [ ] مش بيظهر عند «قريب» وهو في الحقيقة بعيد (90% ≠ قريب)؟
- [ ] مفيش drain بين الجلسات (energy system) بيمنع اللعب؟

### 5.8 فحص Rival contest / Multiplayer ★★
- [ ] نفس seed/عشوائية للطرفين؟
- [ ] أي تأثير على الخصم **بيكلّف**؟
- [ ] Rubberband ديناميكي ومربوط بفرق النتيجة؟
- [ ] Positive feedback بس لو عايزين نهاية سريعة بعد فرق حاسم؟
- [ ] لو فيه 3 استراتيجيات: RPS؟
- [ ] آلية مشتركة: «مين يلعب الأول» محسوبة (المتصدر آخر)؟
- [ ] شخصية كل rival = قاعدة سطر واحد متكاملة (Pac-Man ghosts)؟

---

## 6. الأنتي-باترنز

1. ★★★ **Art-first:** محتوى وassets قبل ما الـ toy يبقى ممتع.
2. ★★★ **الحكم من الـ doc:** «باين إنها fun» من قراية الـ rules.
3. ★★★ **Tuning الـ AP بدل الـ mechanics:** إنك تذكّي البوت عشان يعدّي اقتصاد مكسور.
4. ★★★ **Feature متأخرة بعد التوازن:** بتهدم الـ balance الحساس (اكسر الـ feature freeze = debugging أكتر).
5. ★★★ **Rules أكتر = لعبة أحسن:** العلاقة مش خطية، وأحيانًا التقليل بيحسّن.
6. ★★★ **Chance كـ central في لعبة/ليفل طويل:** إحباط «قراراتي مش فارقة».
7. ★★★ **Deadlock بلا مخرج:** رصاصة Zelda الأخيرة، أو budget = 0 وفيه قطع ما بتندمجش.
8. ★★★ **Dominant strategy متسابة:** لعبة بتتلعب بنفس الطريقة كل مرة.
9. ★★★ **أكتر من 4 major loops:** صعبة الإتقان، واللاعب مش فاهم.
10. ★★★ **مكافأة في فخ مميت / مكافأة مرئية مستحيلة.**
11. ★★★ **Booster من غير diminishing returns:** «شوف إعلان واكسب».
12. ★★★ **Energy/drain بين الجلسات بيمنع اللعب:** ضد خط الاستوديو. أي static friction يفضل جوه الليفل.
13. ★★ **Deus Ex HR:** حلول متعددة وbosses بحل واحد.
14. ★★ **Mechanic جديد في كل task:** الليفل ممتع بقد أضعفها.
15. ★★ **Mission خطية من غير خيارات** = تعليم ✓، و**فتح الـ space كترقيع** = backtracking.
16. ★★ **Optional task مكافأته بقت شرط فعلي.**
17. ★★ **Mutually exclusive من غير backup** = unsolvable.
18. ★★ **فخ X-COM:** غلطة بدري بتقتل لعبة طويلة.
19. ★★ **Attrition ببلاش:** سباق تدمير من غير قرارات.
20. ★★ **Rubberband بيلغي المهارة أو ثابت:** لازم ديناميكي، ومستوى قوته متعمد.
21. ★★ **Purifier ≈ Refinery:** عناصر وظيفتها متطابقة، فرّق بينهم.
22. ★★ **Node modifier على موارد ملموسة** (keys/health): بيخلق ويمسح بشكل غامض.
23. ★★ **Realism = fun:** iconic على حساب الـ gameplay.
24. ★★ **Edutainment = multiple-choice متنكر.**
25. ★★ **False choice / Jesus-Hitler dichotomy.**
26. ★★ **Sandbox من غير عواقب** بيلغي أي معنى.
27. ★★ **QTE-izing:** تبسيط بيضايق الجمهور الأساسي.
28. ★★ **Golden-age-style triggers** بتتقدم على إنها emergence.
29. ★ **Emergent storytelling كأساس للمنتج.**
30. ★ **Branching story trees:** محتوى كتير اللاعب مش هيشوفه. **Open world بيضيّع الخط الرئيسي** (Elder Scrolls).

---

## 7. تطبيق مباشر على Mossfolk ★★★

### 7.1 تشريح اللعبة بلغة الكتاب
| عنصر Mossfolk | تصنيفه |
|---|---|
| الأنواع | Physics (Unity) core + Internal economy (9 أحجام، budget، أهداف) + Progression (3000 ليفل) + Social (rival contests) |
| البنية | **Hybrid:** emergent جوه الليفل (فيزيكس + chains + RNG القطع)، وprogression صارم بين الليفلات |
| الـ jar | **game space ثابت** (GTA reuse)، والـ goal + budget = **mission** |
| الـ merge | **converter 2:1** (الإجمالي بيتغير، مش trader). قاعدة symbolic. درس Connect Four: الفيزيكس بتنفّذ الـ rule الأعقد |
| Drop budget | **static engine / pool محدود** = action points في turn-based. كل drop = interactive node |
| طابور القطع | **unpredictable static engine** = random gate بأوزان |
| Chain merges | **triggers** = long-range communication. النشاط = دمجات/ثانية |
| امتلاء الـ jar | **escalating complexity** + dynamic friction طبيعي. مورد مجرد زي threat بـ end condition خسارة |
| «Budget خلص والهدف لسه» | **reverse trigger** على end condition |
| الهدف | end condition للفوز. Progress نوع 2 (distance to target بـ setbacks) |
| Rot (2501+) | مرشح: slow destructive positive (ضد الـ dominant stacking) أو static/dynamic friction، **حدد إيقاعه** |
| Mossy shells / stones | activators (قفل لحد شرط) أو obstacles. لازم يتربطوا بباقي العناصر |
| Side quests | زي الفاكهة في Pac-Man: **معزولة وآمنة** للمبتدئ؟ وكمان «open world» بخطر ضياع الخط الرئيسي |
| Rival contests | race متوازي حاليًا. حوّله لـ attrition بس بتكلفة |
| Skill tree | deep: primaries = drop + merge، والباقي secondary |

### 7.2 قياسات التيستر-بوت الإلزامية
1. نسبة **dead states بدري** لكل ليفل (فخ X-COM / deadlock). الـ dead state البدري = غلطة تصميم مش غلطة لاعب.
2. **منحنى امتلاء الـ jar** عبر الزمن + تصنيف الـ phases (فاضي ← متراكم ← ضغط).
3. **نقطة اللاعودة:** كام إسقاطة بين أول علامة خطر والانهيار (الانهيار لازم يبقى سريع وواضح).
4. فرق الصعوبة بين **أول 50% وآخر 50%** من الإسقاطات (escalating challenge).
5. **أطول chain + متوسط النشاط** (long-range communication).
6. **حساسية الإسقاط** (continuous): نفس الـ seed، تغيير بسيط في الموقع، النتيجة بتتغير قد إيه؟ ومقارنتها بـ **توازن الاقتصاد** (discrete).
7. **تنوع الحلول:** الـ bots بتكسب بطرق متنوعة (emergent) ولا بحل واحد (puzzle ثابت / Juul walkthrough)؟
8. **positive-only check:** اللي بيبدأ كويس بيكسب غالبًا؟
9. أقصى merges/نقاط ممكنة في الليفل (درس 40 ore / 20 ice) ← على أساسه يتحدد الـ budget والـ goal.
10. كل seed يتعاد على كل `bot_difficulty` عشان المقارنة تبقى من غير ضوضاء الحظ.
11. تأكيد فرضية «الـ jar المزدحم = downward spiral» **قبل** ما نبني عليها قرارات.

### 7.3 قرارات تصميم جاهزة
- **Forgiveness + preview** للإسقاط (World of Goo) = مساحة جودة رخيصة.
- **عشوائية الطابور تسيب «نَفَس»** بقصد (escalating complexity)، مش RNG أعمى.
- **High-risk/high-reward cascade** (Tetris): jar مليان أكتر = cascade محتمل أكبر. اتأكد إنه موجود عن قصد.
- **Rival contests:** نفس الـ seed للطرفين. rubberband ديناميكي (المتأخر فرصته أكبر في قطعة قوية). أي تأثير على الخصم بيكلّف. شخصية كل rival بقاعدة سطر.
- **Boosters / rewarded ads:** stopping mechanism + قالب Prince of Persia (مكتسب بالأداء) + لو فيه meta economy، weak static engine ضد الـ soft-lock.
- **3000 ليفل:** chart زي Fig 10.14 يوزّع إدخال العناصر. كل عنصر بـ kihon ← kumite. التنويع من **الـ mission + الـ mechanic subset** لأن الـ space ثابت. تنويع backgrounds بين الأقسام. tuning = ثلث لنص الوقت.
- **ليفلات الـ budget الضيق** (تخطيط تقيل) = pacing أبطأ ومن غير timer (Crawford).
- **Side quests / minigames** = zoom على الـ core، مش mechanics جديدة. ومكافآتها مش شرط للنهاية.
- **تمرين 3 locks لـ key واحد:** هدف واحد بـ stones / shells / rot.
- **تمرين audit:** لكل نوع من الخمسة، إيه الـ discrete وإيه الـ continuous عندنا.
- **Playtesters** من جمهور الـ hyper-casual، مش من الفريق. الـ tutorial بلاعبين جداد بس، والبوت مش بديل.

---

## 8. أمثلة الكتاب بالاسم (فهرس سريع)
Angry Birds، World of Goo، Super Mario Bros.، Boulder Dash (tile/frame)، Donkey Kong، Johann Sebastian Joust، Chess، Go، Diplomacy، Tic-tac-toe/Connect Four، Civilization (I/III)، SimCity، StarCraft 1/2، Warcraft III، Command & Conquer: Red Alert، Counter-Strike، Risk، GTA III/San Andreas، Deus Ex/Human Revolution، Half-Life 1/2، Zelda Twilight Princess (Forest Temple، Goron Mines)، The Longest Journey، Bejeweled، Tetris، X-COM: UFO Defense، Pac-Man، Space Invaders، Super Crate Box، Monopoly/The Landlord's Game، Settlers of Catan، Caylus، Power Grid، Puerto Rico، Agricola، Magic: The Gathering، Space Hulk، Descent، Star Wars: X-Wing Alliance، Elite، Eve Online، Privateer، The Sims، Caesar III، Lunar Colony، Seven Cities of Gold، Prince of Persia: Sands of Time، Mario Kart، Doom، Mario Galaxy، Fallout 3، Diablo، Oblivion، Warhammer FRP، Vampire: The Masquerade، D&D، Kings Quest، Leisure Suit Larry، Bioshock، September 12، Train، PeaceMaker، America's Army، Kriegsspiel، Balance of Power، Oregon Trail، Refraction، Foldit، Experts Exchange، Spore، Crash Bandicoot، Sonic، Knytt Stories، Robot Wants Kitty، Game of Goose، Golly (Game of Life).

---

## 9. Lunar Colony: case study بناء اقتصاد (مرجع) ★★

- **Setup:** نرد ← tokens ice/ore بالتبادل. 3 stations لكل لاعب (واحدة لامسة ice وواحدة لامسة ore بالظبط، بتعمل claim). مسافة النقل/البناء = الضلع القصير لكارت لعب.
- **الأكشنات/دور = stations÷2 مقرّب لفوق** (تبدأ بـ 2). كل station مرة واحدة في الدور. Transport وResearch ما بيستهلكوش station. Energy = ice × حجم المحطة.
- **Tech = 3 energy لكل واحدة:** Fast Ice، Efficient Ore، Transport Capacity، Long Range Shuttles، Luxurious Habitats.
- **الفوز:** النهاية لما حد يمين آخر ore/ice. نقطة لكل station حجمها ≥2، أو مع Luxury: نقطة لكل expansion فوق 2.
- **البنية:** dynamic engine ×2 + engine building، **positive بس** ← مكان البداية بيحسم. الـ friction الوحيد = way stations (static). النموذج: بناء station = 50% ore و25% ice.
- **النسخة 2:** purifier (2 energy، و1 energy/ice ← 2 purified)، refinery (**2 energy/ore**)، transporter (2 energy، +1 action، شحن بـ 1 energy). السبب إن التكرير أغلى: **ore ممكن يوصل 40، ice أقصاه 20** ← سعّر الـ converter عكس الوفرة. الـ purifier مفيد بس لو ice ← ≥2 energy.
- **Events بتأثر على الكل:** نرد 5 = 3 ice جداد، و6 = ادفع 3 energy واخد نقطة. كروت (12 كارت فيهم 2 ice = مضمون مرتين كل 12 دور). سيناريو مكتوب (بعد 10 أدوار). secret objectives (5 energy / station حجم 4). Obstacles وrough terrain.
- **Raiding:** raider بـ 1 energy. نجاح لو النرد ≤ مخزون الهدف، والـ raider بيتدمر لو النرد ≤ مخزونك = negative feedback لصالح المتأخر. **بديل أثبت: 3 استراتيجيات بشكل RPS.**
- **Sidebar:** features أكتر = upkeep وbookkeeping أكتر (مش مشكلة في البروتوتايب). Post-its على الـ tokens.

---

## 10. مراجع للتعمق (أولوية)
LeBlanc 1999 (Feedback Systems) · Wright 2003 (Dynamics for Designers) · Koster 2005 (Theory of Fun، Grammar of Gameplay) · Juul 2002 (Open & Closed) و2005 (Half-Real) · Hopson 2001 (Behavioral Game Design) · Cook 2007 (Chemistry of Game Design) · Crawford 1984 · Adams 2009 (Fundamentals، Ch.10 Core Mechanics، Ch.9 challenges، Ch.12 hub) · Church 1999 (Intention / Perceivable Consequence / Story) · Björk & Holopainen 2005 · Alexander 1977 · Gamma et al. 1995 · Fromm 2005 · Wolfram 2002 · Jenkins 2004 · Vogler 1998 · Fiske (مقدمة الـ semiotics). مفردات أونلاين: The 400 Project (اتسجل منه 112 بس، آخر إضافة 2006)، Game Ontology Project، Game Innovation Database. Machinations: jorisdormans.nl/machinations، والملاحق على peachpit.com/gamemechanics.

---

## 11. تعارضات المصادر وثغراتها (ما تخترعش الناقص)

| # | التعارض/الثغرة | المصدر |
|---|---|---|
| 1 | **Appendix A ولا C للتيوتوريال؟** الكتاب بيذكر Appendix C كتيوتوريال للأداة وAppendix A كمرجع سريع، وفي ملحوظة تانية بيقول A تيوتوريال. الجزء 7/8 بيأكد إن C = Getting Started وA = Quick Reference | نوتس الجزء 2 مقابل الجزء 7 والجزء 8 |
| 2 | **اسم Kyle:** «Kyle Gabler» مقابل «Kyle Gabbler» | الجزء 1 مقابل الجزء 5 |
| 3 | **Monopoly static friction:** المتن بيشير لـ Figure B.8 والصحيح B.6 (غلطة في الكتاب) | الجزء 7 والجزء 8 |
| 4 | **شرط الـ AP في Monopoly:** الكود `Property > Houses/5` مقابل وصف الكتاب «أكتر من 5 أضعاف العقارات مقارنة بالبيوت». القراية الحرفية ممكن تبقى عكس الوصف، والدرس مش متأثر | الجزء 4 |
| 5 | **ترقيم الصفحات:** الجزء 1 بيقول الفصل 2 لحد ص35، والجزء 2 بيكمّل الفصل 2 من ص51–57 والفصل 3 من ص43–58. فيه عدم اتساق في الترقيم | الجزء 1 مقابل الجزء 2 |
| 6 | **Multiple Feedback / Trade / Worker Placement / Slow Cycle:** الجزء 7 بيقول إنهم أونلاين بس ومش موصوفين. الجزء 8 وصف الـ 3 الأولانيين (Worker Placement مقطوع في الـ Implementation). **Slow