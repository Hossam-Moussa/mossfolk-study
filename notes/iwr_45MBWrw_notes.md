# Game Pipeline Walkthrough: محاضرة عن pipeline مستند إنتاج لاستوديو Globex (الصين) — نوتس مذاكرة

**المصدر:** محاضرة بث مباشر (iwr_45MBWrw)، المدة حوالي 115 دقيقة. العنوان الرسمي مش مذكور في الترانسكريبت، والمحاضر بيشتغل على flow chart بيقارب 30 صفحة اتعمل قبل حوالي 10 سنين لاستوديو اسمه Globex في الصين.

**الملاحظة الأهم من أول المحاضرة:** الـ pipeline ده ليه سياق معين. المحاضر بيقول بنفسه إن المستوى ده من التفصيل «مش طبيعي» ومش هتلاقيه في معظم الشركات. السبب إن فريقه كان حوالي 250 واحد في الصين بيعملوا MMORPG ضخمة، والغالبية منهم junior، وفيه حواجز لغة، وكان فيه 8 مترجمين in-house بدوام كامل. فالمستند اتعمل عشان يعوض الغموض والحواجز.

---

## 1. ليه الـ pipeline المكتوب أهم من الموهبة (المقدمة + الـ checklist)

- ★★★ **الفكرة الأم: الـ pipeline = checklist مكتوب، مش خريطة للإلهام بس.** الهدف إن الـ junior وأي حد مش متأكد يمشي خطوة بخطوة: «كيف تعمل كل asset؟ كيف تعمل character؟ كيف تعمل level؟ إزاي تدمج الحاجات ببعض؟ مين مسؤول عن كل خطوة ومين بيقرر؟»
- **الأخطاء الغبية هي اللي بتكسر الإنتاج** (مش الأخطاء المعقدة): naming conventions (إزاي تسمي الـ asset)، الـ directory الصح، هل الـ asset اتعمل له check-in في source control، إنك تبلغ الشخص اللي بعدك إن الشغل جاهز ليه. المحاضر بيقول «مش متخيل كام واحد مش عارف يعمل الحاجات دي».
- **الباترن ورا الأخطاء دي:** الواحد بيخلص شغله ويحفظ ويروح للتاسك اللي بعده، وينسى إنه يرجع الـ asset للعبة ويبلغ صاحب الخطوة اللي بعده. النتيجة: حد تاني بيضيع ساعات يدور على الـ asset.
- **فكرة الـ checklist بتتطبق على أي حد، حتى الـ producer:** الـ checklist بيقولك إنت فين في الـ pipeline، إيه المطلوب منك، وإمتى، وإيه الـ dependencies.
- **ملاحظة قابلة للتطبيق:** لو الشغل مع outsource أو فريق بعيد، الـ pipeline المكتوب بيبقى ضروري. المحاضر بيقول إن الشركة الخارجية مش عارفة الـ engine بتاعك ومش موجودة معاك، فكل ما تكون أدق في الوصف كل ما تطلع نتايج أحسن.

---

## 2. الـ Estimation والـ Resource Spreadsheet

- كل خطوة في الـ flow chart ليها **spreadsheet مرتبط** بيوضح: مين المشارك (مثلاً artist واحد، أو artist وart director)، الوقت التقريبي (ساعات)، والأدوات المستخدمة.
- ★★ **الـ producers بيستخدموا الأرقام دي للـ scheduling، وفي بداية كل مشروع بيتحققوا منها:** «هل ده فعلاً هياخد 38 ساعة؟ وإحنا قربنا من التقدير ولا لأ؟» والأرقام بتتعدل مع الوقت عشان الجدولة تبقى أدق.
- **تحذير من المحاضر:** الأرقام دي خاصة بمشروعه ومش هتشتغل عند غيره. اللي يفيد هو **المنهج** مش الرقم.
- الـ pre-production هي المرحلة اللي فيها بتحاول تعمل «guesstimate» لأقصى حاجة تقدر تعملها، وتحدد فين تحفظ وقت وموارد.

---

## 3. قراءة الـ Flow Chart (الـ legend)

- **الأشكال:** فيه عناوين، خطوات، وخطوات فرعية. الأشكال المعينة (ما يعني decision) مخصصة للـ **approvals** أو الحاجات اللي لازم تتتحقق منها. لو فشلت بترجع لخطوة قبلها، وبتفضل في loop لحد ما تتعتمد.
- **الخطوط المتقطعة = optional.**
- **الترقيم والحروف** مجرد reference للربط مع الـ spreadsheet، مش مهمة في حد ذاتها.
- ★ **الـ cross-links:** المستند كان فيه حاجات بتيجي من pipeline تاني وبتروح لـ pipeline تاني، لأن الشغل كان موزع على صفحات مختلفة. ده بيعني إن كل pipeline فرعي له دخول وخروج واضحين.
- **المستند كان تفاعلي:** كل مربع كان ممكن يبقى زرار يوديك للصفحة التفصيلية. ده بيسهل التنقل بين مستويات التفصيل.

---

## 4. الـ Game Universe (المرحلة الأولى: الكون)

- **الترتيب المنطقي:** ابدأ بالكون قبل أي حاجة. الـ IP والـ world building هو الأساس.
- **Zone = level أو area أو جزء من عالم.** في الـ MMORPG الـ zones مش بالضرورة levels، والمصطلحات دي بتختلف حسب نوع اللعبة (open world أو MMO أو لعبة صغيرة). **المحاضر بيحذر تستخدم المصطلح الصح لمشروعك.**
- **خطوات المرحلة:**
  1. **Creating a text summary:** المصمم بيكتب كل حاجة نصياً: مين عايش هنا، مين موجود في الـ level، الأعداء، الـ NPCs، والـ flow charts اللي بتوصف الكون (هل فيه regions؟ هل فيه map؟ إزاي اللاعب هيتقدم؟).
  2. **High-level story overview لكل الـ zones:** الـ 10,000 foot view. المصمم بيشتغل على القصة الكبيرة.
  3. **Visual inspirational concepts:** الـ concept art.
  4. **Approval** قبل ما ينتقل للخطوة اللي بعدها.
- ★★ **تحديد الـ standards بدري جداً:** لأن كل الـ assets كانت المفروض تتعاد استخدامها بكثافة. فكانوا بيحددوا من الأول: كم character؟ كم body type؟ كم skeletal type؟ هل الـ characters modular؟ هل الـ vehicles والـ enemies modular؟
- **الباترن ورا ده:** التحديد المبكر بيحدد «قد إيه مسموح نعمل جديد أو أصيل»، وبيخلي الشغل مقيد بشكل صحي. المحاضر بيقول بالحرف إن **حتى 200 واحد مكانوا مش كفاية** عشان يعملوا كل حاجة يبغوها في يوم واحد لعبة بحجم World of Warcraft.
- **قيود اللعبة الخاصة:** لعبة time travel، بتنقل بين universes، فيها science fiction وfantasy وmodern day مع بعض. فكان لازم يحدد **categories** واضحة: أنواع المباني (modern/fantasy/sci-fi)، أنواع البيئات (desert، forest، fantasy world)، الـ props، الـ enemies، الـ creatures، والـ textures والـ animations والـ LODs والـ AI. كل حاجة اتحطت في spreadsheets.
- **Universal assets:** أصول تتعاد استخدامها عبر كل الـ worlds والـ regions (زي الأسلحة والشطرنج وأي حاجة مشتركة). الهدف مزدوج: **consistency** بين كل الـ levels، و**uniqueness** لكل level.
- **الـ Object Pipeline** بيتبني على الـ universal assets دي (هنعرض تفاصيله تحت).

---

## 5. الـ Zone Construction وترتيب الـ Dependencies

- ★★ **Zone object pipeline:** الـ zone objects زي الشجر والمباني والـ props. كل object ليه: 3D model، textures، LODs، وأحياناً concept art. دي «الـ Lego bricks» ومعظمها شغل artist.
- **الشغل بيحصل بالتوازي لما يكون مفيش dependency:** مثال، الـ objects والـ NPCs ممكن يتعملوا في نفس الوقت (فريقين مختلفين).
- **الـ dependencies الصريحة:**
  - **Skeleton + skinning بيعتمدوا على الـ base mesh.** مينفعش تعمل skeleton قبل ما الـ mesh يبقى موجود، ولا تعمل animation قبل الـ skeleton.
  - **Special effects بتعتمد على الـ objects:** مثال الـ fire pit: بتتعمل الأول، وبعدين الـ effect بتتربط بيها. نفس الكلام على الـ torches والسيوف المشتعلة.
  - **Audio:** مثال الصندوق (chest) بيفتح ويصدر صوت «كريك». ومثال تاني: الـ footsteps بتختلف حسب الـ material اللي اللاعب ماشي عليه (عشب، حجر، معدن «clank clank»). يعني الصوت لازم يعرف الـ trigger والـ material.
  - **Animation + effect + audio في نفس اللحظة:** مثال الصندوق: بيفتح (animation) + sparkle زي Zelda (effect) + صوت مكافأة صغير (audio). ممكن تتعمل بالتوازي بس بتتربط بالتسلسل عشان تطلع أحسن.
- **Performance validation (من أهم الحاجات في المستند):**
  - الفكرة: مشاريع كبيرة بتعمل levels مبهرة وبتكتشف إن الـ game بيشتغل بـ **5 frames per second** لما تحط عليه شخصيتين. السبب: الـ zone كانت ثقيلة بالـ polygons والـ memory، ومفيش مكان للـ AI والـ gameplay. المحاضر بيقول إن الحالة دي كلفت **سنة كاملة** في بعض الفرق.
  - **الحل: memory map** بتتعمل مسبقاً، بيعرف الكل قد إيه مسموح للـ level وقد إيه فاضل للحاجات التانية.
  - **مثال Munch's Oddysee:** الـ character الأول (default) كان حوالي **10 MB** (model + texture + skeleton + animation + AI). الـ instance بعدها ~100 KB بس. المشكلة إن كل level فيه حوالي 10 characters، فيعني حوالي **100 MB** والـ Xbox كان فيه **64 MB** بس. الحل: قللوا الـ levels لـ **4 characters لكل level** وأعادوا تصميم الـ levels عشانها تشتغل.
  - ★ **الباترن:** الـ performance مش بس مشكلة art. الـ memory budget لازم يتحسب من الأول لكل حاجة (art، characters، AI، music، sound). الـ performance validation بيكون ليها خطوة في الـ pipeline، مش بعد ما تخلص.
- **Music وSound effects:** ممكن تتحط على مستوى الـ level كلها، أو تتحط حسب الـ area (مثال: قريب من base العدو تسمع موسيقى من مكبرات صوت)، أو تتربط بـ object (الصندوق بيعمل صوت لما يتفتح). المصمم بيضيفها ويعمل localization.
- **Focus testing والـ validation:** نادراً الـ level تطلع صح من أول مرة. المحاضر بيقول غالباً **3 لـ 5 passes**. مش شرط تغير الموسيقى كل مرة، بس ممكن تحتاج تعدلها حسب إعادة بناء الـ level.
- **Final polish:** إضافة art أحسن أو تفاصيل صغيرة، وبعدين bug testing للـ zone.

---

## 6. Source Control والـ Backup (فصل الـ raw files عن الـ game files)

- ★★ **المشكلة الشائعة:** الـ artist بيشتغل في Maya وPhotoshop. الـ raw files (`.ma` / `.psd`) بتتحفظ محلياً على جهازه بس. بيعمل export لـ FBX للمحرك، وبيفكر إن ده كفاية.
- **النتيجة:** لو الجهاز اتعطل، معندكش غير الـ FBX. ومش هتقدر ترجع تعدل الـ model أو الـ textures الأصلية بسهولة (لو اتعمل بالعكس تبقى شبه مستحيلة).
- **الحل المعمول:** فيه نظامين source control: واحد للـ **raw files**، وواحد للـ **game files**. وكمان **triple redundancy**: الجهاز المحلي + سيرفرين مختلفين + الـ SVN source safe server. ومفيش asset بيتمسح أو بيضيع.
- **تعليق المحاضر:** الـ artist بيكون الأسهل يتلام هنا، لأنه غالباً الأكتر إهمالاً للـ raw files.
- **ملاحظة تقنية:** تفاصيل FBX وتكوين الـ SVN والـ import settings → **الباقي برمجة — متجاهل.** الدرس التصميمي والعملي هو: احفظ الـ source، وامتلك أكثر من نسخة.

---

## 7. الـ Concept للزون وخطوات تصميم الـ Gameplay

- **الـ concept للـ level** بيتعتمد من الـ lead (level lead أو chief creative officer أو creative director). لازم تعرف مين بيعتمد إيه وإمتى.
- **White box:** نسخة رمادية بدائية تقدر تجري فيها، بتوضح الـ gameplay بس مش شكلها النهائي.
- **الـ concept art** بيبدأ بعد ما المصممين يحددوا الـ zone (عشان الـ concept artists يعرفوا يرسموا إيه).
- **الـ enemies في الزون:** فيه **universal enemies** (موجودين في أي مكان) و**zone-specific enemies** (زي الـ civilians أو اللي شغالين في مخبز أو حداد بيبيع armor). كل نوع له pipeline وترجمة واعتماد.
- **الـ gameplay pipeline (الأساس):**
  1. **Scripts والـ mobs:** المصمم بيحط الـ mobs، وهم مجموعات أصغر من الـ enemies بتتقاتل بالجملة. بيتعمل لهم scripting، AI behaviors، ومسارات:
     - هل بيمشوا على patrol path ثابت؟
     - ولا عندهم منطقة بيتحركوا فيها عشوائياً؟
     - ولا واقفين؟
     - ولا عدوانيين أو defensive؟
  2. **Quests:** المصمم لازم يعرف الأعداء فين، والـ quest هتمر فين، ومش هتمر على منطقة قاتلة. المثال: quest بين A وB لو خط مستقيم ممكن يعدي من منطقة الموت، فتتعمل route تاني.
  3. **NPCs:** كل الشخصيات اللي مش أعداء، سواء تفاعلية أو لأ (عربيات، خيول، ماشيين في الشارع).
  4. **Vendors، crafting، trainers:** NPCs بتدي قيمة للاعب (quests، equipment، تدريب).
  5. **Items والـ economics:** أسعار، أماكن، regions، ومنطقة الـ vendor. ★★ **الـ costs لازم تتبنى على bell curve:** تبدأ رخيصة وتزيد exponentially، عشان تدخل اللاعب تدريجياً. والـ trainers والـ vendors لازم يكونوا متاحين بدري والتكلفة منخفضة، عشان الـ newbie ميتأخرش.
     - ★ **مثال strategy:** لو فيه zerg rush، لازم تعرف من الأول إن التكتيك ده ممكن يخسر بشكل كبير، والـ economics بتحدد ده.
  6. **Cutscenes، bosses، resources:** مثال portal gateways: teleport بين الـ regions. ومثال **special events**: معركة بين فصيلين بتحصل في منطقة، واللاعب يقدر يتجنبها أو يشارك، أو يتعمل لها scripting مخصص.
  7. **Hazards:** مصايد، spike pits، lava، acid pools (أي حاجة بتأذي اللاعب).
  8. **Construction approvals** من الـ lead.
  9. **تربيط الـ zones ببعض والـ secondary gameplay** (في الـ MMO ده مهم جداً).

---

## 8. الـ MMO Endgame: مثال Ghost Goggles

- **المشكلة:** في MMO اللاعبين بيوصلوا للـ level cap (في المثال: **60**، وWoW بدأت بـ 60 وبعدين رفعت لـ 100 ومن بعدها لحد حوالي 180). لو كل المحتوى مخلص، اللاعب بيحتاج يرجع يلعب نفس الـ levels.
- ★★ **الـ in-game mode (endgame) ممكن يبقى أربح mode**، لأن اللي وصل للنهاية غالباً متعلق باللعبة، وده بيخلي فيه **whales** كتير. المحاضر بيحذر إنه منزلق: لازم تديهم محتوى بدون ما تكسر اللعبة.
- **الحل الذكي (Ghost Goggles):** لما اللاعب يوصل لـ level 60 أو يركب نظارة (goggles) بتخليه يشوف عالم الأشباح. الـ enemies بتتكرر كـ **ghosts** بنفس الـ models تقريباً:
  - **Visual:** transparency + blur + effect (شكل شبح). ده شغل effect بسيط.
  - **Stats مختلفة:** لأن الـ ghost model ليه اسم وstats منفصلة، فالـ ghost ممكن يكون level 50 أو 60 وأقوى بكتير، وممكن كمان يضرب بـ psionics (مهارات سحرية).
  - **أسلحة مخصوصة:** لازم سلاح يقدر يقاتل الـ ghosts، عشان الـ gameplay يبقى مرتبط بالمحتوى الجديد.
  - **Doors ومحتوى إضافي:** اتضافوا بنفس الفكرة.
- **النتيجة:** الـ level designers ما اتعبوش (تقريباً ما عدلوا حاجة)، وكل الـ art اتعاد استخدامه، واللاعبين بيقدروا يضاعفوا أو يطلعوا x3 من وقت اللعب.
- **الباترن ورا الحل:** المحاضر بيقول إن الحل الإبداعي ده نتيجة **القيود** (ميزانية، جدول، ذاكرة، art محدود). كل حاجة تقدر تتعاد استخدامها، والقيد نفسه بيقود للـ design الذكي. ومثال آخر: الـ enemies بتتحول لـ zombies بعد ما تموت (تقاتلهم مرتين)، أو zombie أقوى بقدرات سحرية.

---

## 9. الـ Terrain والـ Roads (Zone Terrain Artwork)

- ★★ **الـ terrain pipeline:**
  1. **Sculpt الـ terrain** (نحت الأرض).
  2. **Lay out الـ roads:** الـ roads عندها نوع خاص في معظم الـ engines، لأنها لازم تتبع الـ terrain وتلف حوالين الحاجات، وممكن تربط regions ببعض، ولازم تبان مميزة.
     - الـ roads اللي حوافها حادة جداً بتبان مزيفة. لازم تتعدل.
     - الـ roads الحقيقية مش بتقعد على الأرض مستوية: ممكن تنزل شوية، أو تحتاج **bridges** (مثال: الطريق بيعدي على وادي بجسر مش بينزل لقاعه).
     - الـ roads والـ rivers والحاجات الطويلة اللي بتتلوى على الأرض **من أصعب الحاجات**، والـ engines الحديثة بقت أحسن فيها.
     - ★ **Roads ممكن يبقى ليها AI بيشتغل عليها** (AI عارف إنها طريق وإنه يقدر يتحرك عليها بعربية مثلاً).
  3. **التخطيط للمدينة والمباني:** تحديد أماكن المباني، أو clear لمساحة مستوية أو white box.
  4. **Rough terrain textures:** رسم الـ texture الأولي للأرض كلها.
- **مشكلة الـ cliffs (وحل modular tiles):** لما تعمل جرف عمودي على الـ terrain، الـ texture الواحدة اللي بتتعمل **projection** من فوق بتتقطع (tearing) على الوجه العمودي. الحل المعمول: **3D models للصخور والـ cliffs** بيتحطوا جنب بعض عشان الوجه يبان كأنه صخور حقيقية. المحاضر بيقول إنك على الأغلب شفت الشكل ده في ألعاب كتير ومعجبكش.
- **Terrain tools حديثة:** فيها أدوات ممكن تعمل دا كله تلقائياً. مثال: تقدر تستورد بيانات **USGS** وبيانات حقيقية وتعمل map لأماكن حقيقية. وممكن تحدد قواعد **بالارتفاع والـ slope**: مثال:
  - عند sea level (صفر): texture رمل/desert
  - لفوق: تتحول لـ dense forest
  - بعدين chaparral وrocky
  - في القمة: snowy mountains
  - والـ slope ممكن يغير الـ texture كمان.
- **الباترن ورا ده:** المصمم مش مضطر يعمل كل حاجة يدوياً، والنظام يبقى **semi-intelligent**. ★ **المحاضر بيقول إن الـ process بيتغير مع التطور، فبص لمستقبل الـ tools بتاعتك مش للـ workflow القديم.**

---

## 10. الوقت واللايتنج والطقس والـ Animations (Zone Finishing)

- ★★ **الـ 24-hour clock في الـ MMO:** لازم يبقى فيه **consistency**. مش لازم اللاعبين كلهم يشوفوا نفس الوقت بالظبط بس لازم الـ world يبقى منطقي. في single player تقدر تتحكم، لكن في MMO فيه ممكن 100 أو مليون لاعب في نفس الـ level، ولازم لو لاعب خرج ورجع الوقت يكون متسق (مش يبقى ليل فجأة).
- **Hyper-accelerated clock:** المحاضر بيحكي إن 24 ساعة في اللعبة ممكن تكون حوالي **4 ساعات حقيقية**. مثال: لو الساعة 12 الضهر دلوقتي، بعد ساعتين الشاشة بتبقى سودا (منتصف الليل)، وبعد ساعتين تانيين الضهر تاني. وكمان فيه dusk وdawn.
- ★ **الوقت مش بس للـ visuals:** ممكن يأثر على الـ gameplay (مثال: NPCs أو أعداء بيطلعوا بالليل بس). يعني الـ time system بيربط بالـ gameplay.
- **Weather والـ effects والـ animations:** كل حاجة في الـ level بتتحط: الطقس، الـ effects، الـ animations (مثال: waterfall، أو rock slide قابل للـ trigger). وممكن تكون one-off (تحصل مرة وتتغير permanent) أو تتعمل reset. وفيه rules لكل ده.
- **Collision مع الـ performance validation:**
  - ★ **Invisible walls:** بتتحط عشان تمنع اللاعب من حاجة (مثال: فجوة صغيرة في الجدار، اللاعب يدخلها والكاميرا تتلخبط ويتعلق). الـ collision بيتعمل manual عشان يحل bugs أو يمنع السقوط من حافة معينة.
  - **الحاجة المهمة:** الـ collision للـ player والـ NPCs ممكن يكون مختلف عن الـ geometry الظاهرة، ودي مشكلة قديمة.
- **Zone bug testing:** فحص أولي (first level of bug testing) وتأكد إن مفيش حاجة شكلها غلط. وتذكير بعمل backup.

---

## 11. الـ Objects (Generation، LODs، Concept Sketches، Stats)

- ★★ **الـ objects في MMO ممكن تتطور (upgradeable).** لازم تحدد قواعد التطور: هل نفس الـ base object بيتغير (لون، tint)؟ هل الاسم بيتغير؟ إيه اللي بيحصل لو الـ object اتطور؟
- **Validation للـ design** قبل الـ modeling. وتحديد الـ requirements وعدد الـ LODs.
- ★★ **LODs (Level of Detail):** نسخ من الـ object بدقة أقل كل ما يبعد. مثال: object بـ 10,000 polygon ممكن يبقى له نسخ بـ 5000، 2500، ... لـ 50. وعلى مسافة بعيدة جداً ممكن يكون مجرد texture أو silhouette.
  - **Popping:** لو الانتقال بين LOD والتاني سريع أو حاد، بيحصل **pop** (الـ object يقفز فجأة). ده أسوأ حاجة، والـ LODs لازم تتعمل بعناية.
  - **مثال الـ hands:** في LOD بعيد الـ hands بتبقى مجرد كتلة بدون animation. في متوسط، الصوابع بتبان بس مش بتتحرك كويس. قريب جداً، الـ hands بتتحرك كاملة، والـ facial animation بتتفعل. لما تبعد الـ facial animation بتتحول لـ texture.
  - المحاضر بيقول إن الـ LODs كانت أكتر ضرورة زمان، والـ consoles الحديثة (PS5) قللت الحاجة، بس **موبايل** وغيره لسه محتاجينها.
- **Concept art بالـ orthographic views:** الـ concept art العادي بيكون بزاوية منظور وصعب تعرف الحجم. فالـ artist لازم يعمل **side view، top view، back view** من زاوية مستقيمة (مش منظور)، عشان الـ modeler يقدر يستخدمها كـ blueprint بدقة. بيوفر وقت كبير.
- **الـ flow:** concept، validation، sketch تفصيلي، ثم modeling، textures، variants، LODs.
- **Naming وأماكن الـ files:** تأكد إنك حطيت كل asset في المكان الصح وسميته صح، وإنك عديت الـ polygon count وحجم الـ texture.
- ★★★ **قصة Die Hard (الدرس الأهم في المحاضرة):**
  - لعبة FPS فيها performance مشكلة، والفريق حاول أسابيع يعرف السبب.
  - المحاضر طار للمطور، وقعد معاه، وفي **30 ثانية** شاف موديل واحد وسأل: كام polygon في سلة المهملات دي؟ الـ artist قال حوالي **10 مليون**. المحاضر ضحك وقال إنها كان المفروض تبقى حوالي **100 polygon**.
  - المشكلة: جنيور عمل الـ asset، ومكانش عارف الـ limitations. وحط منه مئات في الـ level، فكان فيه **مئات الملايين** من polygons بيتم رسمها، وفي الوقت اللي المفروض فيه **مليون أو اتنين** بس. يعني حوالي **100x** فوق الـ budget.
  - **الدرس:** الـ asset الصغير ممكن يقتل الـ game. لازم حدود (polygon limits، texture sizes، عدد الـ models).
- ★★ **قصة 122 Characters:** في اللعبة كان المفروض **4 body types، 4 skeletal meshes، 4 مجموعات animations** (~100 animation لكل مجموعة، يعني ~400 animation بس للعبة كلها). لما المحاضر رجع من الولايات المتحدة لقى الفريق عمل **122 model و122 skeleton** وكل واحد فيه 100 animation، يعني حوالي **12,000 animation**، والـ memory بقت أكتر بحوالي **25x** أو أكتر. ده ضيّع **شهور** شغل. والسبب: الفريق ماكانش فاهم أو نسي الـ limitation.

---

## 12. الـ Characters (Player Characters: CAP و الـ Armor)

- ★★ **الـ player characters بتتعامل بطريقة مختلفة عن الـ hero الفردي:** مثال Kratos في God of War: شخصية واحدة، أسلحة وأزياء خاصة بيه. لكن في اللعبة دي الـ armor والـ weapons كانت **shared** بين الـ characters. يعني معظم الـ art (حوالي **90 لـ 95%**) كان بيتعاد استخدامه.
- **الـ CAP system (Create A Player):** اللاعب يقدر يعمل شخصيته: يغير الوش (أوسع، أنحف)، لون البشرة، الشعر، العيون، نوع الجسم. ولازم قواعد تضمن إن كل قطعة armor تتركب على كل الـ characters.
  - اللعبة فيها **60 level** تقريباً، وكل 5 أو 10 levels فيه armor sets جديدة، ولكل class armor مختلف. يعني **آلاف** القطع اللي لازم تتركب على نفس الـ characters.
  - ★★ **الاختبار المبكر للـ CAP:** لازم يتعمل تستينج كويس من بدري عشان يتأكد إن كل الأجزاء بتشتغل مع بعض. ده نظام معقد وصعب.
- **الـ reuse الذكي للـ armor:** مثال: black armor وred armor، والاتنين نفس الـ model بس فرق **tint** (لون) وshader وeffect (مثلاً red = fire armor وفيها شوية نار). لو الـ base model اتغير، كل النسخ بتتحدث أوتوماتيك.
- **الـ rules اللي لازم تتحدد:**
  - مين يقدر يلبس إيه؟ (هل مرتبط بـ class؟)
  - الـ armor مرتبط بالـ level؟ ★★ **مثال المشكلة:** level 10 لابس armor level 50 بيبقى مربك، والعكس: level 50 لابس armor level 10 هيفتكر إنه قوي وهيتفاجئ إنه اتقتل بسهولة. يعني **الـ visual يقول مستوى الـ armor**، واللاعبين بيفهموا منه القوة.
  - الـ names والـ stats والـ variations.
- **الـ animation للـ armor:** ثابت (shield/helmet ثابت) ولا متحرك (ريشة في الخوذة بتتحرك مع الهوا)؟ ولو متحرك، إزاي يتعمل؟ ممكن يبقى system منفصل (skull system).
- **الـ NPCs والـ players بيستخدموا نفس الحاجات تقريباً**، فلازم يتفهموا مع بعض.

---

## 13. الـ NPCs والـ Monsters

- **الـ NPCs** بيتعملوا بنفس الـ pipeline تقريباً:
  - ★ **الأدوار:** vendor، عدو، تاجر، trainer، named character مهم في cutscene، أو generic (مثل Peasant 1، Peasant 2).
  - **الـ customization:** لازم يكون فيه شوية unique، والمحاضر بيقول: **80 لـ 90%** reuse، و**10 لـ 20%** unique عشان الـ game يبقى memorable، وعشان اللاعب يقول «آه، ده جديد».
  - **Randomize ولا ثابت:** هل الـ NPC بيتغير كل مرة ولا نفس الشخص في كل مكان؟ لازم قرار واضح.
  - **الـ levels والـ stats:** ★ لو عدو level 20 مقابل 50 enemies، ممكن فيه multiplier. ولازم يتحدد أثر ده على الـ weapons والـ armor.
- **الـ Monsters:** non-humanoids، ليهم شوية reuse (categories وclasses) بس عندهم AI وattacks وanimations خاصة بيهم.
  - **Skeletal types:** quadrupeds (زي الحصان والكلب)، birds، snakes، spiders، fish، وغيرهم.
  - **بتتصمم عادة أبسط** وأقل complexity عشان يكون فيه عدد أكبر منها (زي الحياة البرية الطبيعية، مش بالضرورة أعداء).
- **الـ Rigging (تركيب الـ skeleton):** ★★ شغل متخصص اسمه **rigger**. المحاضر بيقول: **لو انت animator، اتعلم rig**. عنده animators ممتازين بيعرفوا يخلوا الشخصية تتحرك طبيعي، بس مش عارفين يعملوا T-pose وskeleton وسقوف الحركة (range of motion). ★ **الـ rigger الكويس بيحدد الـ restraints:** مثال الذراع ممكن تتحرك لحد معين بس، ولو اتعدت هتبان غريبة. والـ animator بيحرك في الحدود دي.
- **Skinning:** ربط الـ skeleton بالـ mesh بحيث الـ mesh يتحرك مع الـ skeleton.
- **Animations:** ممكن تتعمل باليد، أو motion capture، أو مزيج. مثال: لعبة **TNA Wrestling** كل الـ animations كانت mocap وواقعية جداً، والـ jump والـ attack لازم يكونوا دقيقين.

---

## 14. الـ Quests (Concepting، Detailing، Implementation)

- **المراحل:** concepting (paper design + approvals + تحديد الـ quest عبر zones)، ثم detailing (الـ 2D maps، الـ world terrain، القصة، الـ cutscenes، تصميم الـ NPCs)، ثم implementation (إزاي تتبنى فعلاً، وإيه الأدوات، وإزاي تتتحقق من الـ rewards والـ testing).
- ★★ **Quest concept cheat sheet:** الـ quest designers بيسألوا نفسهم دايماً: **who، what، where، when، how**. ده بيخليهم متأكدين إنهم فاهمين كل quest قبل ما يبنوها.
- **أمثلة للـ quest elements:**
  - Quest giver ومتابعة القصة.
  - Targets والـ goals.
  - Unique art: مثلاً صندوق بيظهر للاعب ده بس (أو لفترة زمنية).
  - Mobs وBosses (groups).
- ★★★ **مشكلة الـ Wolves (من أهم الأمثلة في المحاضرة):** quest بتقول «اقتل 20 ذئب». لو اللاعب قتل 10 قبل ما يبدأ الـ quest، والـ spawner مش بيعيد، فمفيش 20 ذئب في العالم. الـ quest تتعطل. وفي **MMO**، لاعب تاني ممكن يقتل الذئب، والـ spawner بيعيد كل دقيقة، فالناس بتقف في **طابور** مستنيين الذئب ساعات. «Horrible game design» بس دي كانت طريقة كتير من الـ MMOs.
  - **الدرس:** لازم تتأكد إن اللاعب قادر يخلص الـ quest، وإن الـ resources (الـ spawns) تكفي في MMO.
- **الـ scripting والـ AI behaviors والـ audio** لكل quest: خطوة بخطوة.

---

## 15. الـ Cutscenes والـ Special Effects

- **الـ cutscenes** ممكن تكون: مُعدة مسبقاً (pre-rendered)، داخل اللعبة، قصيرة (جزء من quest)، أو **interstitials** كبيرة بين regions. كل نوع له pipeline بتاع camera angles والـ timing.
- **الـ special effects:** تتحط في اللعبة وتتعمل لها pipeline أساسي. الـ effects ممكن تكون standalone (ألعاب نارية في السما) أو مربوطة بـ object (نار على bonfire مثلاً، أو سيف مشتعل، أو سيف سحري).

---

## 16. الـ Audio كـ Pipeline مستقل

- ★★ **الصوت أهم من ما بنتخيل:** المحاضر بيقول إن معظم المطورين بيعتبروه **icing على الكيكة** وبيضيفوه في الآخر. لكن في الألعاب الجيدة الصوت بيتفكر فيه **من اليوم الأول**، خصوصاً في الـ horror.
- **الـ dynamic audio:** الموسيقى بتتغير حسب اللي بيحصل في العالم. مثال: قرب الأعداء الموسيقى بتزيد حدتها، ولما تدخل القتال بتتغير لموسيقى حماسية، ولما تبعد بتهدى تاني.
  - **مثال Armor Command (حوالي 1992-93، DOS):** المحاضر كان شغال عليها، وده كان **نظام dynamic audio من بدري جداً**، والموسيقى كانت بتتبلند كأنها DJ بيعمل beat matching.
  - ★ **FMOD وأدوات زي دي** بتخلي الموسيقى ديناميكية، وده pipeline خاص لوحده.
- **الـ footsteps مثال:** الصوت بيعتمد على الـ **material** اللي تحت اللاعب. ده بيحتاج design وربط بالـ gameplay.
- **Voice over**، الـ compression (ضغط الملفات)، وإنها تتدمج بسلاسة.
- **الـ audio engineers غالباً بيشتغلوا في "black box" منفصل**، والباقي بيشوفوا النتيجة بس ومش بيقدروا الشغل المعقد. المحاضر بيحذر من ده.

---

## 17. الـ Integration والـ Tech Artist

- ★★ **المشكلة:** كل قسم بيعمل حاجة (animators، character artists، prop artists، ai programmers، engineers) ولازم كل حاجة تتجمع في الآخر.
- **الحل:** في الفرق دي بيكون فيه **tech artist** أو "in-betweener"، شخص يفهم الـ art والـ tech مع بعض، لأن الـ artists مش دايماً technical، والـ engineers مش دايماً بيفهموا الـ art.
- **مثال المشكلة:** النقل من Maya لـ Unreal عن طريق FBX وأي file format تاني، وبيحصل إن الـ textures تبوظ، والكل بيسأل مين هيصلحها. ده تحدي كبير.
- ★ **Bugs بتحصل من الـ integration:** مثال: asset المفروض يكون 1 MB اتعمل بالغلط 1 GB، فالـ memory بتتملي والـ game يضرب. ومثال تاني: المحاضر نفسه كان بيشتغل على UE4 وعمل crash بسبب plugin اشتراه.

---

## 18. QA، Build Servers، والـ Validation

- الـ pipeline لازم يبقى فيه process كامل للـ QA والـ testing والـ usability focus testing.
- **Build servers:** بتعمل automation لبعض الـ checks، وبتتأكد إن كل حاجة شغالة وإن مفيش حاجة كسرت اللعبة.
- ★ **الـ validation مستمر:** كل ما تتدمج حاجة لازم تتأكد إنها مكسرتش حاجة تانية.

---

## 19. الـ Instances (النسخ والـ variants)

- **Instance = نسخة من الـ original.** ممكن تكون:
  - **نسخة 100% مطابقة:** أي تغيير على الـ original بيتعكس على الـ instance تلقائياً.
  - **نسخة بتغييرات:** مثلاً نفس الـ object بس لونه مختلف، أو مرفوع مثلاً، أو scaled. الـ instance ممكن **تتفك** عن الـ original في حاجات معينة (locked vs unlocked).
  - مثال: لو الـ instance اتكبر بعد ما تتعمل ومش locked، هيفضل بيكبر لوحده، ولو locked مش هيتأثر.
- ★ **الدرس:** تحديد أي خصائص (stats، scale، color) **locked** وأي خصائص **free** عشان مش يحصل تغيير غير مقصود.

---

## 20. الـ Bosses، الـ Mounts، والـ Consumables

- **Bosses:** ممكن تكون custom بالكامل: الـ model، الـ AI، الـ animations، الـ environment، الـ attacks، الأسلحة. ★★ **المحاضر بيقول إنهم ممكن يعملوا النجاح أو الفشل للعبة**، وبيحتاجوا حذر كبير.
- **Mounts (الركوب):** في اللعبة دي كانت خيول. كانت لازم تتربط بالـ character عشان الـ character يقدر يركب، والـ mount ممكن يكون customized. ولما اللاعب يركب، بيتكون **model جديد** ليه animations خاصة (ride animations) والحصان والـ player بيتحركوا مع بعض.
- **Consumables (الاستهلاكيات):** بيتعملوا في crafting، ولهم pipeline مختلف في الإنشاء والاستخدام.

---

## 21. الخلاصة التصميمية (مجمعة)

- ★★★ **الـ pipeline الواضح يوفر وقت وفلوس** أكتر من الموهبة الفردية، خصوصاً في الفرق الكبيرة والمتعددة الجنسيات والـ outsource.
- ★★★ **القيود مش عدو** (زي: 4 body types، 4 characters في الـ level، الـ ghost goggles، الـ polygon budget). كل قيد بيخلي الـ design أذكى.
- ★★ **الـ performance budget** يتحسب من الأول: polygons، textures، memory، characters، animations، audio.
- ★★ **الـ assets الصغيرة ممكن تكسر اللعبة** (الـ trash can في Die Hard).
- ★★ **الـ naming والـ directories والـ source control** مش تفاصيل صغيرة.
- ★★ **الـ dependencies لازم تتوثق** (skeleton بعد mesh، effect بعد object، audio بعد trigger).
- ★★ **الـ quests لازم تتأكد إن اللاعب قادر يخلصها** حتى مع spawn محدود والـ MMO.
- ★ **Rigging مهارة مستقلة** والـ animators لازم يتعلموها.

---

**لموسفولك:**
- **Naming conventions وmanifest للـ assets:** Mossfolk محتاجة قائمة واضحة للـ assets (اسم، directory، source control check-in، إشعار للتاسك اللي بعده). ده حاجة بسيطة بس بتوفر ساعات.
- **Memory/performance budget لكل level:** الـ Unity physics والـ merge puzzle فيها عدد كبير من الـ creatures والـ jars، فلازم تحدد budget للـ rigidbodies، والـ particles، والـ audio، ومحدش يزود عدد الأحجام أو الـ creatures من غير ما يتحسب الأداء.
- **Mossy shells/stones/rot challenges:** الـ challenges من 2501 لازم تتبنى على قيود واضحة (زي Die Hard)، ولازم قيود الـ materials والـ textures تتحدد من الأول، مش بعد ما تتعمل الـ levels.
- **Tester-bot وbot_difficulty:** الـ bot ممكن يتعامل كـ "QA automation" زي الـ build servers، يتأكد إن كل ليفل ينفع يتحل ومفيش quest/challenge مستحيل الخلاص (زي مشكلة الذئاب)، وإن الـ resources (الـ shells والـ stones) تكفي.
- **Side quests والـ rival contests:** لو الـ rival contest بيعتمد على spawns أو موارد محدودة، لازم نعمل نفس فحص الـ wolves: هل اللاعب يقدر يكمل حتى لو لاعبين تانيين؟ (في Mossfolk offline أغلب الوقت، بس لو فيه leaderboard أو contests مشتركة، فالفحص ده مهم).
- **Miniجيمز:** الـ dependencies بين الـ mini-games والـ main loop (زي الـ audio والـ effects) لازم تتوثق عشان ماتتكسرش مع التحديثات.
- **Checklist للـ 3000 level:** اعمل checklist بسيط لكل ليفل جديد (goal، budget، approvals، testing)، زي الـ flow chart، وده بيخلي فريقك (حتى لو صغير) يشتغل بنفس الطريقة.