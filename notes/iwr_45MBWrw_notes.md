# Game Development Pipeline — Globex Studios MMORPG Flowchart (بث لايف مينتور، iwr_45MBWrw، ~115 دقيقة) — نوتس مذاكرة

ملحوظات على المصدر:
- اسم المتكلم مش مذكور في الترانسكريبت.
- الفيديو مش برمجة. ده walkthrough لـ flowchart إنتاج من ~30 صفحة اتعمل لـ MMORPG، فكله تصميم/عملية/إنتاج وكله متسجل.
- في كلمات ASR متلخبطة: «train» = terrain، «tent» = tint، «Credit player» = CAP (create-a-player).
- المتكلم قال فريقه «حوالي 250» وبعدين «200 plus». الرقم مش ثابت في كلامه.
- أرقام ساعات الشغل والتقديرات في المثال **خاصة بلعبته** وهو نفسه قال ماتعتمدهاش.

---

## 1. إيه هو الـ Pipeline ولماذا اتعمل (0m–11m) ★★★

- الـ pipeline = **flowchart** عمله لشركته Globex Studios في الصين من ~10 سنين: «الأشمل بين كل pipeline docs عملتها»، حوالي 30 صفحة. هو نفسه قال إنه **ماشافش المستوى ده من التفصيل في أي شركة اشتغل فيها** — ماتعتبرهوش standard.
- **ليه اتعمل بالتفصيل ده:** حوالي 250 واحد في الفريق، بيبنوا MMORPGs (ضخمة ومعقدة)، أغلبهم junior، ومشكلة لغة إنجليزي → الوثيقة اتترجمت صيني. الجونيور يعرف خطوة بخطوة: إزاي يعمل كل asset، character، level، إزاي يدمج، فين الـ approvals، مين بيقرر ومين متورط في كل خطوة.
- **الأخطاء الغبية اللي بتتكرر في الإنتاج وده اللي اتعمل عشانها** ★★:
  - Naming conventions (اسم الـ asset إيه).
  - الـ asset في أنهي directory.
  - اتعمله check-in في source control ولا لأ.
  - خلّص شغله وحفظه ومشي للتاني **من غير ما يرجّعه للّعبة**.
  - ماخطرش في باله **يبلّغ الشخص اللي بعده** إن الشغل جاهز.
  - حطه في الـ directory الغلط → حد تاني يضيّع ساعات يدوّر عليه.
  - ماعملش setup صح ونسي خطوة.
  - ده بيحصل أكتر مع الناس الأقل تقنية.
  - **الباترن:** الإنسان مابيفتكرش كل خطوة تلقائيًا → الـ pipeline = checklist ملموس بيتمشّى عليه ويتتأكد منه.
- **الـ Excel المرافق (ما اتكملش):** لكل خطوة في الـ flowchart بيتحدد:
  - مين الناس المتورطين (مثال: «دي هتاخد 2 artists + art director»، «دي artist واحد»).
  - الوقت بشكل تقريبي جدًا.
  - الأدوات.
- **تقدير الوقت بيتعمل ويتصحح:** في بداية المشروع الـ producers يتحققوا: «هل ده فعلًا 38 ساعة شغل؟» ويقارنوا بالتقدير ويعدّلوا → الجدولة بتبقى أدق مع الوقت. الأرقام اتراجعت من فرق اللعبة كمان مش من الـ producers لوحدهم.
- **الـ Key (legend) بتاع الفلو تشارت:**
  - عنوان، خطوات، sub-steps.
  - أشكال مخصصة للـ approvals/validation: لو فشلت **ترجع لخطوة سابقة وتلف في loop لحد ما تتوافق**.
  - **الخطوط المنقّطة = اختيارية.**
  - الصفحات بتشير لـ pipelines في صفحات تانية (cross-department).
  - الترقيم بيربطها بالـ Excel (مرجع سريع بس).
  - كان مقصود يبقى **interactive** (الأزرار تنقل لصفحة الـ pipeline الأعمق).
- **لموسفولك:** الـ pipeline الأدنى لينا = checklist لمحتوى الليفل/الـ creature: naming، المكان، check-in، **إشعار الخطوة اللي بعدها** (مين بياخد الليفل بعد المولد؟ البوت؟ المصمم؟). ونعمل جدول تقدير ساعات بنصححه من الواقع بعد أول 3–4 batches.

---

## 2. Universe → Global assets → Universal assets (12m–25m) ★★★

**الـ Universe (البداية):**
- بنبدأ بالـ universe: اللعبة إيه، الـ IP، الـ world building، نظرة high-level على كل الـ zones.
- ملحوظة مصطلحات: الـ zone ≈ level/area/map/جزء من العالم. الـ MMO/open world بيختلف عن اللعب الأصغر.
- خطوات الـ designer:
  1. **Text summary:** نص بيحدد مين عايش هناك، الأعداء، الـ NPCs، القصة، المناطق، خريطة العالم، **flowchart لتقدم اللاعب**.
  2. **High-level story overview** لكل الـ zones («10,000 foot / mile-high view»).
  3. **Visual inspirational concepts.**
  4. **ترجمة:** كان عندهم مصممين بإنجليزي ومصممين بالصيني/ماندرين، فترجمة الوثائق في الاتجاهين. **6–8 مترجمين in-house فل تايم** بيترجموا الوثائق والإيميلات بين الفرق (فريق 200+).
  5. Approval — لو مارفضتش ترجع من الأول.
  6. التذكير بـ check-in الوثائق: «بيبان غبي، بس مذهل كام مرة الناس ماعملتوش». الملاحظة: ده كان زمن MS Office من غير Google Docs live. فاللي بتتعمل live مش محتاجة check-in، **اعرف إيه المناسب لمشروعك/فريقك/تقنيتك**.

**الباترن ورا التفصيل الزيادة:** وثيقة pipeline مفصلة بالشكل ده بتبقى أهم ما يمكن مع **(أ) فرق كبيرة، (ب) فرق multinational، (ج) outsourcing**. الـ outsource art teams مابيعرفوش الـ engine ولا الـ tech ومش موجودين عندك → **كل ما كنت أدق وأدق في المطلوب، النتيجة أحسن.** قال إنها «ممكن تنقذ مؤخرتك».

**Global assets (الحدود من يوم 1)** ★★★:
- **Reuse بكثافة. حدّد standards بدري:** كام character، كام body type، كام skeletal type، modular characters/vehicles/enemies. الأساس ده بيحدد **كم الجديد/الأصلي المسموح وكم المقيّد**.
- السبب: حتى بـ 200 واحد، للعبة حجم World of Warcraft **مافيش manpower** تعمل أي حاجة تتخيلها يوم 1 → قيود تقنية وإنتاجية لازم تتقال من اليوم الأول.
- أنواع العوالم: كام نوع؟ صحرا، غابة، fantasy. لعبته كانت **time travel + universes مختلفة** (sci-fi + fantasy + modern day معًا).
- **العمارة:** عدد أنواع مباني غير محدود ولا categories (modern / fantasy / sci-fi)؟ تحديد الـ categories كان مهم.
- مشاركة assets/props/enemies/creatures. جداول تفصيلية في Excel: إيه المشترك في textures، animations، LODs، AI. بعدها ترجمة → approval → check-in للقوايم. (كان شغل Excel وWord).

**Universal assets:**
- حاجات reusable بين worlds/levels/regions. كل world مش 100% unique، فيه set عالمي (weapons، chests) للـ **consistency/coherency** + uniqueness لكل level.
- بتتفرع لـ pipelines أعمق: features الـ assets، stories، asset sets، shared object features، object pipeline، base universal assets.

**التخطيط في pre-production:**
- ده شغل designer بس لازم الـ art والـ engineering يشاركوا (الكل بيحدد إيه هيتحط في اللعبة).
- بنرجع للـ Excel: مثال تقدير terrain «40 ساعة أو 80 ساعة» → كام ناس عندنا → كام man-hours → **نضيف buffers** → ده بيقول كام حاجة نقدر نعملها. **نقيّد نفسنا من يوم 1**. المرحلة بتحاول «guesstimate» كم نقدر نعمل وفين نوفر وقت وموارد.

**★★★ تعريف الـ Done (الأهم في الجزء ده):**
- بنعمل assets أساسية، نترجم الوثائق، **ونعمل verify بوضعها في الـ engine وتشغيلها فعليًا**.
- قوله: «**مافيش حاجة اتعملت إلا لما تبقى جوه اللعبة وقابلة للعب وأقدر أشوفها وألمسها وألعب بيها.**»
- **المفهوم الغلط الشائع:** الـ artist يخلص ويقول done. «لأ، شغلك خلص، الـ asset لسه ما خلصش». ممكن يحتاج خطوة أو 100 خطوة لحد ما يدخل اللعبة. والكلمة «done» ماتتقالش لحد ما يدخل اللعبة ويخلص. **ده team effort.**
- بعدها: verify → approve → revise the list.

- **لموسفولك:**
  - عندنا لازم نكتب **تعريف done** للـ level/creature/challenge: يبقى في build + اتلعب بالبوت وطلع bot_difficulty + اتعمله check ملف الإعدادات.
  - ونحدد caps من الأول: 9 أحجام × كام skin/variant؟ (أسلوب الـ standards المبكرة).
  - المهم إن قيود الـ jar/الـ physics تتكتب قبل ما الـ content يتولّد.

---

## 3. Zone Construction + Performance Validation + Source Control (25m–40m) ★★★

**ترتيب خطوات بناء zone:**
- Concept the zone (بديهي) → construction للـ zone assets.
- **الـ objects:** الـ basic zone objects (من الشجر للمباني)، **3D models + textures + LODs**. «زي طوب الليجو». شغل artist غالبًا، ممكن يحتاج concept art.

**Dependencies والـ Parallelism** ★★:
- **ممكن بالتوازي:** objects وNPCs (عنده كانوا فريقين مختلفين). 
- **dependency:** الـ skeleton والـ skinning والـ animation **لا تتعمل قبل الـ base mesh/base character**.
- **الـ Special effects:** ممكن standalone (fireworks) أو متعلقة بـ asset: **bonfire لازم يكون فوق fire pit** (الـ object يتعمل الأول وبعدين الـ effect). نفس الشيء torches، fire pits، **flaming sword / magical swords**.
- **الـ Audio:** لو الـ asset ليه صوت unique (chest بيطلع صرير لما يتفتح).
- **سلسلة الـ chest (مثال Zelda):** animation الفتح → sparkle effect (غبار/لمعان) → audio reward. «بتتعمل بالتوازي بس **بالتسلسل أحسن**». (قال إن label «NPC animation» في الشارت غلط، لأن العلاقة zone ويشمل chest مش بس characters.)

**★★★ Validate Performance (خطوة أضافها لفريقه):**
- **المشكلة:** الليفلات بتتزوّد: «هرمي حاجات كتير وأعمل أحلى ليفل». بس لازم تحط فيها characters وAI وvehicles وgameplay logic، وكلها بتاكل memory وCPU.
- **القصة:** رأى فرق كبيرة/محترفة عند ناشرين كبار: اشتغلوا **سنين**، عملوا كل ليفلات اللعبة 100% polished مع fly-throughs مبهرة. سلموها لفريق الـ gameplay programming، رموا كام character فنزلت اللعبة لـ **5 fps**. ما عرفوش ليه، وبعدين اكتشفوا إن الـ zone ثقيلة (polygons/memory) ومافيش مكان لأي حاجة تانية. **كلفت الفريق ~سنة** يرجعوا لكل الـ process ويعملوا re-optimize.
- **القاعدة:** الـ zone performance = **memory map يتعمل قبل وقت** يعرف الكل كام ممكن تحط في ليفل **ويفضل مكان لكل حاجة تانية**.
- **بتشتغل في الاتجاهين، مش بس level art:** **Munch's Odyssey** (زي ما قال):
  - الـ default character (model + texture + skeleton + animation + AI) نسخته الأولى ~**5–10 MB** (مش متذكر الرقم بالظبط، قال «maybe 10 MB»).
  - الـ instance منه ~**100k** بس.
  - الـ levels كانت مصممة بـ **~10 characters** → ~100 MB، على Xbox **64 MB** كل الـ memory (على حد اعتقاده).
  - يعني **ضعف الـ memory في الـ characters بس**، من غير العالم.
  - الحل: شالوا كل ده، وقالوا «**4 characters لكل level وبس**» وعملوا redesign للـ levels على أساس 4.
- **الباترن:** الـ budgets لازم تتقسم على كل الأنظمة المتنافسة **قبل** ما أي قسم يبني بحرية.

**Music & SFX في الـ zone:**
- موسيقى عامة على الـ level كله أو **حسب المنطقة**.
- موسيقى diegetic localized (قرّبت من enemy base تسمع موسيقى كإنهم شغالين loudspeakers/ستيريو).
- ممكن تتربط بـ object (الـ chest لما يتفعّل يلعب SFX). بتتضاف بواسطة level designers.

**Focus test & validate:**
- **مش بس شغّال — هل ممتع؟** لو لأ نرجع نبني ونغير.
- **دورة circular: «نادرًا بتتظبط من أول مرة — عادةً 3 أو 4 أو 5 passes».** الموسيقى والـ SFX مش لازم تتعاد كل مرة بس بتتظبط وتتعدل مع إعادة بناء الـ levels.
- بعدها **final polish:** art أحسن، تفاصيل «nitpicky»، bug testing، upload لـ source control.

**★★★ Source Control وBackup (قصة الـ raw files):**
- الاسم: SVN (برنامج check in/out بيمنع الحذف بالغلط).
- عندهم **نظامين source control: واحد للـ raw files وواحد للـ game files**.
- **الخطأ الشائع (الـ artist):** بيشتغل في Maya + Photoshop، بيحفظ PSD وMaya (raw formats يمكن يتعدلوا في أي وقت)، وبيعمل export لـ **FBX** (format شائع، Unreal/Unity بيستوردوه). الـ raw files بتفضل **محليًا على جهازه** على hard drive واحد، مش على server ولا source control. لو الجهاز مات: **عندك الـ FBX بس**، و«الـ extraction من FBX للـ raw عشان تعدل = صعب لمستحيل».
- حصلت له **«مرات كتير جدًا»** وبتضرك لو الجهاز مات أو احتجت تعدل في آخر لحظة.
- خطوة «upload to SVN» بتفكّر الناس يرفعوا الـ raw files (وكل حاجة).
- **Triple redundancy:** كل واحد عنده project folder directory وpersonal directory ومطلوب منه يعمل back up للاتنين: **سيرفرين مختلفين**. فكل asset في **3–4 أماكن** (local HD + سيرفرين + SVN server) = «مافيش حاجة اتفقدت حتى لو system كامل وقع».
- بعدها approval وإكمال الـ zone.

- **لموسفولك:**
  - **memory/physics budget لـ Mossfolk** قبل الـ content: كام physics body متزامن في الـ jar، كام particle للـ merge، حد للـ mossy/rot shaders على الموبايل. لأن Mossfolk أساسها physics وهو أول حاجة تنهار في الأداء.
  - **درس Munch's:** المخلوق الأول غالي والـ instances رخيصة → نعتمد على النسخ المشتركة.
  - **مصادر الـ art الخام** (مش بس الـ exports اللي في Unity) تتخزن ويتعمل لها backup منفصل.
  - **دورة 3–5 passes** لازم تتحسب في جدول الليفلات: البوت بيقيس الصعوبة، بس «ممتع؟» لازم pass بشري على الليفلات المفصلية.

---

## 4. Zone Concept & Zone Gameplay (40m–50m) ★★★

**Concept:**
- designer بيصمم: quests، enemies، assets، 2D maps. (أشار لـ streams سابقة عن world building).
- **الترتيب:** concept approval → تقدير المدة وجدولة → **White box** (هندسة خام رمادية/بيضا، تقدر تجري فيها، **تعبّر عن الـ gameplay ومش شبه الشكل النهائي**) → concept art (المصمم حدد مسبقًا إيه في الـ zone فالـ concept artist عارف يرسم إيه).
- **Universal vs unique:** أعداء universal ممكن في أي مكان، وفيه units unique للـ zone: civilians (شغالين في مخبز)، blacksmith بيبيع armor. أعداء zone unique + NPCs zone unique. ترجمة → approval → asset lists → finalize + check-in.

**Core gameplay — الترتيب اللي المصمم بيبني بيه ★★★** (بعد ما الـ 3D maps تقريبًا خلصت):
1. **Scripts و mobs:** الـ mob = enemy NPC، وحدات أصغر swarmer بتتحارب «bulk». بنحدد AI behaviors والـ paths: **fixed patrol، منطقة بترتد فيها عشوائي، أو واقف ثابت**؛ عدواني ولا دفاعي.
2. **Quests:** لازم تعرف **الأعداء فين والحاجات المهمة فين** عشان الـ quest يمر بيهم أو يتجنبهم. مثال: A→B بخط مستقيم ممكن يعدي على **منطقة high-level اللاعب هيموت فيها** → نلف الـ route حواليها. «لازم نعرف إيه فين ومتى مقدمًا».
3. **NPCs:** مش أعداء، تفاعليين أو لأ (سواقين عربيات، راكبين خيل، ماشيين).
4. **Vendors/crafting/trainers:** helpers = NPCs بيدوا قيمة (quests، equipment…).
5. **Items & economics:** إيه هي، تكلفتها، فين، أنهي region، إيه المتاح من كل vendor، **القوايم dynamic ولا designer-controlled**.
   - **قرار مهم:** لو بدأت اللاعب بشكل وحش وأخد وقت طويل يوصل لـ «cool» ده تحدي. فلازم **يوصل للـ trainers/vendors بدري والتكاليف تبقى منخفضة كفاية**.
   - التكاليف **«bell curves»** (قال): تبدأ رخيصة جدًا وبعدين تغلى بشكل أُسّي، ونكسر اللاعب في اللعبة بالتدريج.
   - **الـ economics أهم في الـ strategy games:** لو عايز Zerg rush لازم أعرف مقدمًا. ممكن أجرب وأخسر بشدة، لكن ده جزء من الـ process. (الجملة مش واضحة تمامًا في الترانسكريبت.)
6. **Basic cutscenes، bosses، resources، portal gateways** (transit سريع teleport بين regions)، **special events** في كل region (مثال: فصيلين بيتحاربوا ملهمش علاقة باللاعب، اللاعب يدخل المنطقة ويتجنب أو يساعد — custom scripted أو جزئيًا scripted أو AI مضاف).
7. **Hazards:** traps، spike pits، fire lava، acid pools — حاجة بتأذي اللاعب لو لمسها.

- **Construction approvals:** مين يوافق ومتى وفين (level lead، chief creative officer / creative director).
- **ربط الـ zones معًا** + secondary gameplay + PVP (لأنه MMORPG).
- **Level cap = 60 من يوم 1** (WoW الأصلي 60، ورفعوه بمرور الوقت لـ 100 ويعتقد حاليًا ~180).

- **لموسفولك:** الـ rival contests/side quests تتصمم على نفس الأسلوب: **أعرف الصعوبة والموارد قبل ما أحط الهدف** (فكرة A→B). نظام الـ economy (garden/shop لو موجود) لازم **early cheap → exponential**. وبناء ليفل جديد يبدأ بـ **white box** (مثلاً: layout الـ jar + الأهداف + التحديات قبل ما أي art يتعمل عليه).

---

## 5. Endgame + قصة الـ Ghost Goggles (50m–57m) ★★★

**المشكلة (MMO):** اللاعبين بيخلصوا الـ core content ويحتاجوا حاجة تانية، ويرجعوا يعيدوا الليفلات.
- **الـ endgame mode أحيانًا الأكثر ربحية:** اللي لعب للآخر **hooked**، «ممكن يكونوا whales». **ماتتجاهلهمش.**
- **«slippery slope»:** إزاي تدّيهم اللي عايزينه من غير ما تكسر اللعبة. المحتوى لازم يكون **replayable high-level content في نفس الـ levels** (لأن عندنا قيود على الـ amount).

**★★★ الحل (Ghost Goggles):**
- عند level 60 (max) اللاعب **يشتري أو يحصل على goggles تخليه يشوف ghosts**.
- **كل الأعداء** يتعمل لهم spawn كـ **ghost versions** (نفس الـ models، لكن ghost).
- ممكن كمان يكسب **أسلحة تنفع ضد الـ ghosts**.
- **الـ level نفسه 100% زي ما هو** (المصممين ماكانوش محتاجين يعدّلوا، أحيانًا عدّلوا). اللاعبين **يضاعفوا أو يثلّثوا وقت اللعب** على نفس الليفلات. كمان **doors وحاجات** بتتفتح عن طريق «العالم التاني» (الـ ghost world).
- **التكلفة رخيصة:** ضبط transparency + visual effects + blur + شكل «ghosty». لأنها **model/اسم مختلف تقنيًا**، فممكن **stats مختلفة**: الأصلي level 5 أو 10، والـ ghost level 50 أو 60، أقوى وأكتر قدرات (حتى **psionics blast**/سحر).
- **الباترن:** محتوى جديد = **layer فوق نفس الأصول والـ levels** (طبقة تغيّر الـ visibility/stats/القواعد)، مش محتوى جديد من الصفر.

**الدرس العام (القيود تولّد الابتكار)** ★★:
- «لازم نحل مشاكل… عمرنا ما هنعمل اللعبة بالظبط زي ما عايزين… ده عالم مش موجود… ممكن Valve أو شركات unicorn قليلة بوقت وفلوس غير محدودين». غالبًا بنشتغل بـ **budgets وschedules وقيود موارد وتقنية**، **ودايمًا بندوّر نعمل الألعاب أسرع وأرخص.**
- **عشان تحلها:** افهم قيودك من الأول. هو عرف **من يوم 1 إنه محتاج level-60 gameplay** فدخّله في الـ IP بدري جدًا.
- **مثال تاني:** الأعداء يتحولوا **zombies** بعد ما تقتلهم (تحاربهم مرتين) → وممكن الـ zombie يرجع بقدرات أكتر → magical zombie.

- **لموسفولك:** ده أقوى تطبيق: **محتوى بعد الليفل 3000 / للي خلّصوا**: طبقة modifier فوق نفس الـ 3000 ليفل (مثلاً variant يغيّر القواعد/الأهداف/الميزانية بدل ليفلات جديدة). وده نفس فكرة الـ side quests والـ rival contests تعيد استخدام الليفلات بقواعد مختلفة. وكمان: **اللاعب اللي خلص الليفلات = أعلى قيمة**، فمحتاجين له سبب يفضل (ده وقت الـ replay mods). الإعلانات: مفيش في المصدر.

---

## 6. Terrain Artwork Pipeline (57m–70m) ★★

- منطقة رمادية بين level designer وlevel artist؛ بتتغير حسب الفريق (designer first pass ثم artist). **الخطوة الأولى: الجدولة** (30 يوم ولا 3 ساعات؟).
- **Exterior-heavy** (فيه interiors قليلة). engine مخصص. النحت (sculpt) للـ terrain.

**Roads (حالة خاصة)** ★:
- الطريق لازم يتبع الـ terrain، يلف حوالين الحاجات، ويربط regions.
- لازم **يبان مميز** بس **لو حواف صلبة مثالية بيبان fake**.
- الطرق الحقيقية: «**depressed**» شوية، وفيها **bridges** عند الـ dips بدل ما تنزل في gorge.
- الطرق والأنهار والحاجات الطويلة الملتوية صعبة. Unity وUnreal دلوقتي أحسن + plugins.
- **الـ AI** ممكن يحتاج يعرف إنها طريق (يسوق عليها).
- بعدها: مكان البلد والمباني (white box أو مسطح مفضي)، textures خشنة للـ terrain.

**Cliffs/Modular tiles** ★★:
- **المشكلة:** الـ terrain mesh مسطح بنشكّله زي الطين، وبنحط **texture واحد مُسقَط من فوق**. أي سطح رأسي يطلع فيه **texture بيتمطط/يتقطع** (مش عارف يتعامل مع الـ faces دي).
- **الحل:** نماذج 3D لـ cliffs/rocks/boulders **نركبها على الأسطح الرأسية** فتبان صخور custom مش mesh متمطط. (شفتها في ألعاب كتير.)

**أدوات الـ terrain الحديثة (تغيرت جدًا بعد ما كتب الوثيقة):**
- تعمل terrain واقعي وبتاخد **USGS / real-world data** وتعمل maps لأماكن حقيقية.
- **Elevation-based texturing:** مستوى البحر = texture، وكل ما تعلى: desert → dense forest → chaparral → rocky → snowy mountain tops، وكمان على **slope angle**. الـ terrain «شبه ذكي» بيتقسم بالقواعد.

**الإضاءة والوقت (الـ Time of Day)** ★:
- شمس ديناميكية ولا أوقات ثابتة؟ **في الـ MMO أصعب**: ممكن 100 واحد أو مليون في الـ level.
- في الـ single player بتتحكم وتعرف إنك راجع بعد مدة فتحط ليل.
- عادةً **24-hour clock** متسارع جدًا (24 ساعة لعبة = حوالي 4 ساعات حقيقية: noon → midnight بعد ~ساعتين → noon بعد ساعتين كمان).
- الوقت **بيأثر على الـ visuals والـ gameplay** (الـ NPCs اللي بتطلع بالليل).

**Weather/effects/animations:**
- Weather، animations جزء من مبنى أو العالم (شلالات)، حاجات triggerable (انهيار صخري).
- بعضها **one-offs بتأثر بشكل دائم** وبعضها لازم **reset**. القواعد بتختلف حسب MMO vs single player.
- بعدها performance + approval.

**Collision** ★★:
- الـ collision للاعب أو الـ NPC غالبًا **مختلف** وما بيطابقش الـ geometry المرئي.
- **Invisible walls** لمنع اللاعب من حتة. وبشكل **subtle**: لو في ثغرة صغيرة في جدار، اللاعب يقدر يدخلها شوية والـ **camera يتلخبط/يتعلق**، فنحط قطعة collision فتبان فجوة بس **ماينفعش يدخلها**.
- بتتحط لحل bugs ولمنع السقوط من cliff، وبتتعدل **يدويًا** على الـ world map.
- بعدها check شامل للـ zone (أول مستوى bug testing) + تذكير بالـ backup.

- **لموسفولك:** مفيش terrain في Mossfolk، بس الباترن واحد: **حدود الـ jar** والـ collision يتعدلوا لحل مشاكل الـ gameplay مش بس شكليًا. ممكن يفيد في التحديات بعد 2501 (mossy shells/stones/rot): تتأكد إن الـ visual يطابق الـ collision/الـ physics الفعلي.

---

## 7. Objects Pipeline + LODs + قصتين الـ budgets (70m–81m) ★★★

**Objects:**
- في الـ MMO معظم الـ objects **upgradeable**: لازم تعرف **upgrade path**: نفس الـ base object يتغير؟ tint/لون؟ الاسم؟ ينطبق على character كمان. لازم تعرف القواعد.
- Validate design → tasks → requirements (كام LOD…) → effects/audio محتاج؟

**LODs** ★★:
- الـ main object مثلاً **10,000 polygons** ثم **5000 → 2500 → … → 50**. لو الـ object على بعد ميل (silhouette) ممكن يكون كام polygon أو **texture بس**.
- نفس الـ textures: **4K** قريب → **640×480** بعيد.
- السبب: الـ engines مش سريعة كفاية (PS5 قللت الحاجة بس لسه موجودة **خصوصًا على mobile**).
- **اتجنب «Popping»:** الانتقال بين الـ LODs يبقى سريع ودرامي فتشوف الـ object **pop pop pop** لو رجع ورا قدّام عند الحد. «أسوأ حاجة».
- **للـ characters:** بعيد: الإيد ثابتة مش بتتحرك؛ متوسط: **4 صوابع كوحدة + الإبهام**؛ قريب: إيد كاملة؛ **facial animation بتشتغل لما تقرب جدًا** وتبقى textures وإنت بعيد.

**الـ Designer side:**
- الـ objects تتحط في الـ game مع **stats وتكاليف وأماكن التوفر**، في **database** عشان أي وقت تعدل الـ stats وتعيد البالانس بسهولة.
- لو weapon: projectile effects، recoil، bullets، muzzle flash، laser، audio — ده تجهيز للـ engineering.

**Concept art للـ object:**
- rough sketch → validate → **detailed sketches**. الـ concept art عادةً من perspective angle فصعب تحدد الأحجام.
- فبنعمل **side / top / back views من كاميرا مباشرة (straight-on)** عشان الكل يعرف الأحجام والتفاصيل بالظبط، والـ modeler يجيبها في الـ 3D package. (مش كل فريق بيعمل ده، بس بيوفر وقت وجهد.)
- بعدها modeling diagrams، assets (models، textures، variants، LODs).
- **فحص:** أسماء الـ assets ومواقع الملفات، polygon counts، texture sizes.

**★★★ قصة الـ Trash Can (Die Hard FPS):**
- الفريق كان عنده مشاكل performance لأسابيع ومافهموش ليه. هو سافر للـ developer وبعد **~30 ثانية** بص على نموذج **سلة زبالة**: «كام polygon؟» → **~10 مليون** (المفروض ~100). الـ artist junior ما عرفش إن فيه حدود. وضعوا **مئات** منها في الـ level → **مئات الملايين من الـ polygons** بدل «كام مليون» → **~100x over**. الـ asset صغير فماحدش فكر يفحصه.
- **القاعدة:** حدد X عدد models وحدود poly counts وtexture sizes (ونفس الشيء للـ characters: تعقيد الـ skeleton وعدد الـ animations).

**★★★ قصة الـ 122 Character:**
- المخطط: **4 body types، 4 skeletal meshes، 4 sets of animations** (~100 animation للـ set = **400 total**).
- هو سافر لأمريكا ورجع الصين: لقوا **122 model منفصل، 122 skeleton، كل واحد 100 animations** → ~**12,200** animations (قال «122,000… ولا 12,000») → حوالي **25x إلى 100x over memory**. **ضاع شهور** لأنهم ماعرفوش القيد أو نسيوه.
- **الدرس:** من غير process مثبت «سهل تعمل غلط وتفوّت خطوة (ما حطيناش audio…)». **checklist** للـ producer/artist/designer: «أنا فين في الـ pipeline، إمتى شغلي، وأتتبعه في الجدول والـ dependencies.»

- **لموسفولك:**
  - **cap رسمي على variants**: 9 أحجام × عدد skins ثابت، ولو أي حد زوّد → إنذار.
  - **ميزانية لـ effects الـ merge** (مش بس models): كل chain-merge فيه particles.
  - **فحص تلقائي في الـ import/pipeline** (حدود textures/sprite sizes) — الفكرة بس؛ التنفيذ برمجة، متجاهل.
  - الـ LOD مش مباشر على 2D، بس ينطبق إنه ماتدفعش detail في حاجة صغيرة على الشاشة (أصغر حجم مخلوق في الـ jar).

---

## 8. Characters, CAP, NPCs, Monsters (82m–93m) ★★★

**Characters:**
- الـ design: إيه بيعمل، يتفاعل مع إيه، abilities/skills/stories/الشكل. بعدها concept ثم art.
- **عنده الـ armor والـ weapons shared/reusable بين كل الـ characters**، عكس **God of War → Kratos** (outfits/weapons خاصة بيه كـ signature). ينفع لـ generic content كثير + **assets unique قليلة** لـ key villain/hero/NPC. **90–95% من الـ art reused.**

**CAP (create-a-player):**
- تغيّر الوجه، سمين/نحيف، لون الجلد، الشعر، العيون، body type.
- 60 levels، **armor set جديد كل 5 أو 10 levels**، «على الأقل 10 sets» لكل مستوى، وكل class له armor مختلف → **مئات/آلاف القطع** كلها لازم **تتركّب على نفس الـ characters**. فاحتاجوا قواعد وpipelines كثيرة، وإعادة استخدام skeleton/animation. **تتختبر بدري جدًا** لأن الـ CAP معقد وتحدي لناس كتير.

**Variants (الباترن اللي بيوفر آلاف الأصول)** ★★★:
- **Black armor و red armor** (fire armor / black knight's armor): **نفس الـ art** + **tint** + **shader change** + **effect change** (النار على الـ fire armor). لو الـ base model اتغير، **بيتكرر على كلهم** والباقي تغييرات بسيطة (اللون، الـ effect لسه شغال).
- لازم تحدد: مين يلبس إيه، مربوط بـ classes؟ أسماء، stats مختلفة.
- **Animation للـ equipment:** static (shield/helmet) vs دايناميك (helmet بريش بيتحرك في الريح) → إزاي هتتحرك؟ skin system ولا نظام تاني؟

**NPCs:**
- الـ players والـ NPCs بيستخدموا **نفس الأشياء**. بنعرّف الأدوار: vendor، enemy، trainer، named character في cutscene، generic («peasant one، peasant two»).
- **★★ قاعدة الـ 80–90% reuse + 10–20% unique:** «لو كل حاجة 100% shared مش cool». الـ 10–20% دي «oh wow ماشفتش ده قبل كده»، ممكن تتستخدم بعدين أو تبقى **signature** تخلي الشخص ملفت في ساحة المعركة (characters، vehicles، weapons).
- **Randomize ولا نفس الـ NPCs كل مرة وفي كل حتة** (consistency).

**★★★ قواعد الـ Level/Armor:**
- لو العدو level 20 vs 50: إزاي الـ stats؟ multiplier؟
- **الارتباك بين مستوى الـ armor ومستوى الـ character:** level 10 لابس armor level 50 = مربك. والعكس: **level 50 لابس armor تبان للاعب كـ level 10** → اللاعب يفتكره سهل وبعدين **يموت** ويقول «إيه اللي حصل؟».
- «**القواعد دي هي اللي بتنقذنا في إنتاج الألعاب**»، وكل واحد لازم يفهم الـ pipeline بتاع شغله: مين متورط، بيتسلّم من مين، إيه المطلوب منه (خصوصًا الجدد).
- Final polish، testing، optimization. الـ characters من **أكثر الأشياء تعقيدًا** في أي لعبة (FPS أو MMO): AI + animation + effects + levels + stats + behaviors.

**Monsters:**
- NPCs بقواعد مختلفة: **non-humanoids**، ما بيشاركوش الـ armor لكن فيهم **categories/classes** قابلة لإعادة الاستخدام. AI وattacks وanimations خاصة. أبسط/**أقل تعقيدًا عمدًا عشان يبقى فيه منهم أكتر**.
- **Skeletal types:** quadrupeds (حصان، كلب)، birds، snakes، spiders، fish. مش لازم كلهم أعداء (جزء من العالم الحي).
- databases، stats، textures، color variants. **الـ flowcharts = checklists** للموظفين الجدد أو اللي في الخارج.

- **لموسفولك:** ★★★ **الـ visual يطابق القوة الحقيقية**: التحديات من 2501 (mossy shells / stones / rot) لازم شكلها يقول صعوبتها بصدق؛ وإلا اللاعب يفتكر الليفل سهل ويفشل ويحس بظلم. قاعدة **90/10** للـ creature skins: variants (tint + shader + effect) على نفس الـ 9 أحجام لـ events/rival contests، مع 10–20% «signature» لحظات. ولو الـ base اتعدل يتعدل الكل (فكرة الـ variants؛ التنفيذ برمجة).

---

## 9. Quests (93m–98m) ★★★

- **Pipeline:** concept الـ quests (paper design) → approvals → إزاي بتشتغل **عبر multiple zones** → detail: 2D maps، world terrain، quest stories، cutscenes، NPC designs (كل واحد ليه pipeline). ثم **production**: implement، verify، التأكد من الـ rewards، test، play.
- **Quest concepting sub-chart = cheat sheet للـ designers:** who / what / where / when / how، وإزاي بتشتغل جوه الـ zones.
- **Develop:** quest givers، stories، targets/goals، **unique art يظهر للـ quest بس** (chest بيظهر للاعب ده أو لمدة معينة)، mobs/groups، bosses، scripting AI behaviors، audio.

**★★★ قصة «Kill 20 wolves»:**
- لو اللاعب قتل 10 والذئاب ما بترجعش → الـ quest بيقول 20 وباقي 10 بس في العالم → **عمره ما يخلص**.
- في الـ MMO **×3 تعقيد**: لاعب تاني ممكن يقتل الذئب.
- أمثلة سيئة: **spawner يطلّع ذئب كل دقيقة** → طابور لاعبين مستنيين دورهم **لساعات** («كان تصميم فظيع»، بس ده اللي كتير من MMOs عملوه) → «**بيدوسوا على بعض**».
- **الباترن:** لازم **تضمن إن اللاعب هيلاقي كل اللي محتاجه** لإنهاء الهدف.

- **لموسفولك:** ★★★ **مولد الليفلات + الـ side quests:** أي هدف (مثلاً «ادمج X مرة» أو «وصل لحجم Y») لازم يكون **قابل للتحقق بميزانية الإسقاطات وتوزيع القطع** (البوت يثبت إن الهدف قابل للتحقيق بنسبة معقولة) — مفيش «ذئب مش بيرجع». وفي **rival contests** لو في موارد مشتركة، تأكد إنها ماتبقاش مصدر «طابور» أو تنافس على نفس المورد.

---

## 10. Rigging / Animation / Cutscenes / Audio (98m–107m) ★★

**Rigging** ★:
- **الـ rigger** يبني skeleton يناسب الـ mesh ويلوي صح. تخصص حساس؛ مش كل animator يعرف rig.
- **نصيحته:** لو بتفكر تبقى animator **اتعلم rigging**. رأى animators ما بيعرفوش rig «وده بيضر شغلهم كثير»: بيعرفوا يخلوا الحركة طبيعية بس مايعرفوش الجانب التقني (character في T-pose، إدخال skeleton، constraints).
- **Constraints/range of motion:** الدراع يقدر يوصل هنا بس ما يلف ورا بشكل غريب؛ الـ animator بيحرك ضمن الحدود. الـ rigger الشاطر بيعرف **range of motion البشري**. الـ masters «قليلين ومبهرين»، وبيزيد التعقيد مع الوجه والإيدين والقماش.
- **Skinning:** ربط الـ skeleton بالـ mesh.
- **Animation:** أحيانًا تألّفها، وأحيانًا لازم دقيقة: لعبة **TNA wrestling** كل animation كانت **motion captured** وواقعية (قفزات وهجمات). hand animation أو mocap أو مزيج.

**Cutscenes:** pre-rendered أو in-game، قصيرة جوه quest أو طويلة بين regions. pipeline لزوايا الكاميرا واللقطات والتوقيت — «معقدة جدًا».

**★★★ Audio:**
- مش بس أصول — **مربوطة بالـ gameplay**: الـ chest لازم يعرف إمتى بيتفعّل. **Footsteps حسب الـ material**: عشب vs حجر vs معدن (clank) → لازم أعرف اللاعب ماشي على إيه.
- الصوت بين «nice to have» و**حاسم للـ mood/ambiance** (horror).
- **غلطة شائعة:** «هضيف الـ audio في الآخر زي الـ icing». اللعبة الممتازة بتفكر في الـ audio **من يوم 1**، حتى **dynamic audio** (FMOD) — موسيقى بتتغير حسب اللي بيحصل.
- **مثال Armor Command (~1992–93، DOS، تاني لعبة اشتغل عليها):** كلما قربت من الأعداء الموسيقى تعلى في الـ intensity، وفي القتال تتغير تمامًا لحاجة مثيرة، وبعد ما القتال ينتهي ترجع ambient هادي. **«خلّت المعارك أكثر إثارة بكتير».** مش pre-scripted بالكامل: قطع موسيقى كثيرة بتمتزج بسلاسة، ومهندسو الصوت لازم يعرفوا الانتقالات **زي DJ بيعمل beat match**.
- الـ audio pipeline: اتعمل، compressed صح، صوته كويس، بيمتزج. voice-over، SFX، background music.
- مهندسو الصوت بيشتغلوا في «black box» والباقي بيقولوا «شغال، مش صعب»، وده تقليل من تعقيدهم.

- **لموسفولك:** ★★ **Dynamic music في الـ jar:** الموسيقى تعلى كل ما الـ jar يقرب من خط الـ overflow وترجع هادية بعد merge كبير (Armor Command). **SFX الـ merge يتغير حسب الحجم والـ material** (mossy/stone/rot) زي الـ footsteps. والـ audio يتخطط من البداية مش في الآخر.

---

## 11. Integration / QA / Instances / Bosses / Mounts / Consumables (107m–114m) ★★

**Integration:**
- أقسام مختلفة بتنتج (animators، character artists، prop artists، AI programmers) ولازم يتجمعوا. أحيانًا فيه **tech artist** («jack-of-all-trades wizards») بيربط الـ artists غير التقنيين والـ engineers اللي مش فاهمين art.
- المشاكل: Maya → Unreal عبر FBX والـ textures مش تمام: «مين هيصلح؟ مين هيساعدني أدمجه؟».

**QA/Testing/Usability:** مش مفصل في الـ pipeline بس **لازم pipeline كامل ليه**. **Build servers** بتأتمت الـ validation: ماتكسرش حاجة. **مثال:** asset المفروض 1 MB طلع **1 GB** → الـ memory تنفجر واللعبة تـcrash عند التحميل. وقال إنه كراش Unreal 4 النهارده وهو بيجرب plugins اشتراها: «لسه شائع حتى في منتجات تجارية».

**Instances** (من غير تفاصيل تنفيذ):
- instance = نسخة من الأصل: **نسخة مطابقة تمامًا** (لو الأصل اتغير بتتغير) أو **variation مع override** (لو غيرت اللون/قلبت الحجم؛ لو الـ scale مش locked بيتغير بتغيير الأصل). بعض الخصائص **locked** وبعضها لأ.

**Bosses:**
- ممكن كل حاجة custom: الـ model، الـ AI، الـ animations، البيئة، الهجمات، الأسلحة. «صعبة ومتقنة جدًا» و**«ممكن تعمل أو تكسر لعبتك»** بسبب تعقيدها.

**Mounts (الخيل/المركبات):** برية أو طايرة. القيد: الشخصية لازم **تتسلق وتركب**. ربط اللاعب بالـ mount، والـ mount قابل للتخصيص، و**animations مشتركة**: اللاعب + الـ mount معًا = **model تقني تاني** له set animations خاص (ride animations).

**Consumables:** للـ crafting، pipeline مختلف شوية (بدأوا يعرّفوه).

**الختام:** الـ link للوثيقة الأصلية في الـ chat. **ده بيشتغل للعبته وفريقه وحاجاته بس**، الفايدة إنك تفهم إزاي لعبة من نوع معين اتعملت وإزاي عرّفوا الـ process عشان **كل الفريق على نفس الصفحة وماينساش حاجة**.

- **لموسفولك:**
  - **Build validation:** نفس مشكلة الـ 1 MB → 1 GB تنطبق على أي asset أو config غلط في الـ pipeline؛ ومولد الليفلات يطلع ليفل «شغال» بس **غلط** (مثلاً توزيع/ميزانية مش متسقة) — فاحتاجين فحص تلقائي قبل ما يدخل الـ build.
  - **ملاحظة:** لما نضيف مخلوق جديد، تخطيط الـ dependencies (art → animation → effect → audio) يتعمل مسبقًا.

---

## 12. الباترنز الجامعة للمصدر (للمراجعة السريعة) ★★★

1. **الـ pipeline = checklist ضد النسيان** (naming، directory، check-in، إشعار الخطوة التالية).
2. **Done = جوه اللعبة وقابل للعب.**
3. **القيود من يوم 1** (standards، caps، memory map) **قبل** ما أي قسم يبني بحرية.
4. **Reuse 80–95% + 5–20% signature** — والـ variants (tint + shader + effect) بتضاعف المحتوى.
5. **طبقة فوق المحتوى الموجود** (ghost goggles، zombie) بدل محتوى جديد من الصفر.
6. **Iteration:** 3–5 passes للـ focus test، والـ approval loop بيرجع للخلف لحد ما يتوافق.
7. **الـ source files = أغلى حاجة**: backup ثلاثي + control منفصل للـ raw.
8. **الـ visual لازم يطابق القوة الحقيقية** (armor level، mob level).
9. **ضمان إن الهدف قابل للتحقيق** (20 wolves).
10. **الـ audio والـ economy والـ performance من البداية** مش في الآخر.
11. **التفاصيل أهم كل ما الفريق أكبر/موزع/outsourced.**

**لموسفولك — أولويات التطبيق:** (1) definition-of-done + checklist للمحتوى، (2) physics/memory budget وcap على الـ variants، (3) طبقة replay فوق الـ 3000 ليفل للاعبين اللي خلّصوا، (4) التحقق إن كل هدف/quest قابل للتحقيق، (5) الـ visual language للتحديات من 2501 يطابق صعوبتها، (6) backup لمصادر الـ art الخام.