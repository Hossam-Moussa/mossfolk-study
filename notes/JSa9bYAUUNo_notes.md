# Homa Games — Home Hangar Live: "Puzzles — Reimagine the Genres" (JSa9bYAUUNo، ~73 دقيقة) — نوتس مذاكرة

**المصدر:** لايف أسبوعي من Homa Games (publisher هايبر كاجوال). Kevin هو المقدم، وGeorge هو "ideation expert". الحلقة تكملة لحلقة FPS من أسابيع فاتت، وبتتسجل في أسبوع إعلان Unity عن رسوم per-install. **مفيش برمجة خالص**، الحلقة كلها ماركت وتصميم. ملاحظة تقنية: الترجمة الآلية بتلخبط في أسماء كتير (هنعلّم عليها فين لزم).

---

## 0. السياق والإعلانات (★ خلفية بس)

- **Unity:** Homa وقّعت مع collective من publishers (**Voodoo, Azur, Say Games, Crazy Labs** وغيرهم) ضد قرار رسوم التحميل. في خطاب جماعي منشور على mobilegamer.biz، وبيان رسمي من Homa على LinkedIn وDiscord.
- **Godot** شاف أعلى spike users في تاريخه في الأيام دي. Kevin حوّل سؤال "رأيك في الـ commission" للـ Discord.
- **استبيان AI** من دقيقة واحدة على homagames.com. الحلقة الجاية: الجزء 2 من Arcade Idle Playbook، موضوعه **trigger points for monetization**.
- **للاستوديو:** اعتمادنا على Unity معناه إن أي تغيير في تسعير الـ engine يدخل في حساب تكلفة كل لعبة. ده بيزيد أهمية قياس الـ CPI قبل أي استثمار في اللعبة.

---

## 1. تعريف الـ puzzle ★★

- التعريف من القاموس: مشكلة/لعبة مصممة **تختبر Ingenuity أو Knowledge**.
  - **Ingenuity** = جودة إنك ذكي ومبتكر وأصلي.
  - **Knowledge** = اللاعب **يكتسب المهارة بالتجربة** (مش بنص ولا شرح).
- هدف Kevin من البداية بالتعريف: **تفضل واقف على الهدف الأساسي ومتبعدش عن الجنر**. بتسأل نفسك وإنت بتصمم: "أنا لسه صادق للتعريف اللي الناس متخيلاه؟"
- **الباترن:** الـ puzzle وعد للاعب إنه هيحس إنه "ذكي". أي ميكانيك بتسرق الإحساس ده (RNG، سرعة، grind) بتكسر العقد مع الجمهور.

---

## 2. السوق: الأرقام ★★

- **تحميلات الـ puzzle عالميًا** (iOS + Android، 2019–2022): **4.5 مليار تحميل**، رجعت لمستوى ما قبل الجائحة. 2019 هو الـ benchmark، وسنوات اللوك داون spike غير طبيعي. 2023 لسه مش كاملة.
- **US iOS، أعلى 100 free overall (اتسحبت يوم الإثنين اللي قبل الحلقة):**
  - **28 من 100 puzzle**، يعني تقريبًا الثلث.
  - **12 من الـ28 دول** كمان في أعلى 100 **grossing**.
  - الأمثلة المذكورة: **Happy Match Cafe** (جديدة نسبيًا و"بتكسّر الدنيا")، **Chrome Valley Customs** (Match-3 حوالين العربيات من Space Ape، الترجمة كاتباها "super sale company" وغالبًا Supercell)، و**Angry Birds 2** (لسه موجودة).
- **الباترن:** الجنر قديم ومزدحم، ومع ذلك أغلبه في القمة. يعني الطلب حقيقي، والمنافسة على **الابتكار والـ theme** مش على إثبات إن الجنر شغال.

---

## 3. مين اللاعب؟ ★★★ (يتحكم في كل قرار)

- **أغلبية إناث فوق 35.**
- **دوافعهم:** تقليل التوتر، قتل الوقت، **إحساس الإنجاز والرضا**.
- **مش بيعرّفوا نفسهم كـ gamers**، ومش hardcore. بيلعبوا **بين الحاجات التانية**، وده ألعاب "snackable" حتى لو casual.
- **الجلسة:** حوالي 3 دقايق استرخاء وفصل. السؤال المحوري: **"أقدر أنجز حاجة (أوصل الليفل الجاي) في 3 دقايق؟"** مش عايزين يلتزموا ببلوك 20 دقيقة. ممكن يلعبوا أطول، بس لازم الإنجاز متاح في القصير.
- **عايزين يحسوا الميكانيك بتتطور:** الـ puzzles ميكانيكها متكرر، فالحل **إضافة ميكانيكس/tweaks جديدة طول التقدم**.
- **Live ops وbattle passes:** انتشارهم بقى mainstream وبيحلوا الحتة دي (الإحساس بالتقدم والتغيير) كويس.
- **الباترن ورا التاكتيك:** الجمهور بيشتري **استرخاء + إنجاز مضمون في وقت قصير**، مش تحدي. ده سبب إن الـ themes الناجحة بتميل أنثوية (cafe، home، decoration).

---

## 4. العناصر الثلاثة لتصميم الـ puzzle ★★★

1. **Rules & limitations:** القواعد والحدود هي اللي **بتخلق pinch points/revelations**، يعني لحظة "آها فهمتها". مش لازم تتعقد، يكفي "الإحساس الصغير إنك ذكي". مثال: الشطرنج، كل قطعة محدودة بحركة: الفيل قطري بس (بيروح لآخر اللوحة بس قطريًا)، والحصان/الـ knight ليه حركة "L" (Kevin قالها غلط "up three and over one"). **الحد هو اللي بيعمل اللغز.**
2. **Intuitive/tight controls:** في الـ puzzle بالذات (swap, slide, swipe) أي **jank** = إحباط فوري. ★★ "كنترول تايت" شرط مش ميزة.
3. **Clear completion goal:** اللاعب يعرف المطلوب **أول ما يدخل الليفل**. تركيزه يبقى على "إزاي" مش "إيه".
- **الباترن:** الـ 3 دول عبارة عن فحص قابل للتطبيق على أي بروتوتايب خلال دقايق. هل في حد مؤثر؟ هل الإيد مرتاحة؟ هل الهدف ظاهر من ثانية صفر؟

---

## 5. تصنيف ميكانيكس الـ puzzle الأعلى ربحًا ★★★

الأنواع اللي طلعت في الـ top grossing:
- **Matching:** Match-3 عادي، أو **match & collect** (نقط تربطها بخطوط).
- **Word games:** word search وcrosswords.
- **Bubble shooters.**
- **Sorting.**
- **Tap & blast** (زي Toon Blast).

**الأمثلة بالاسم:**
- **Triple Match:** ابتكار على الـ match. أكل كتير على الشاشة، والميكانيك **collect مش swap**.
- **Wordscapes:** "crossword معكوس". الجدول متملي مسبقًا، وإنت بتكوّن الكلمات اللي تملاه.
- **Bubble Pop** من BitMango: Bubble Shooter كلاسيك.
- **Water Sort Puzzle:** نجاح ضخم، و"كمية هائلة" من المشابهين مش clones بالضبط. وهي logic محض.
- **Toon Blast:** juicy جدًا، إحساس Match-3، وهي tap & blast.

**الـ taxonomy slide** (ميكانيكس × كنترولز × sub-genres). Kevin بيقول: "مش exhaustive، بس خد screenshot".
- **الكنترولز:** tap, hold, swipe/cut (زي Cut the Rope). **لازم الكنترول يتجوز مع الميكانيك:** مش هتحط swipe على match-3 لأن إحساسها هيبقى غريب (Kevin مش متأكد).
- **التصنيفات:** physics-based / non-physics / **1v1 battles** / multiplayer conquering.
- ★★★ **تاكتيك الـ ideation:** **امسك ميكانيكين مشهورين وادمجهم.** مثال: "folding + match-3؟" والـ slide موجود عشان يسهّل الدمج لما تبص عليه.
- ★★ **Fake versus:** "تقدر تاخد لعبة single-player وتحط فيها AI مزيف يخليها تحس versus؟"
- **الباترن:** الابتكار في السوق ده غالبًا **combinatorial**، مش اختراع من الصفر.

---

## 6. Sequential Puzzles — صيغة George ★★★

**التعريف:** sub-genre من الـ logic puzzles. هو الأكثر hyper-casual، وأكتر واحد عنده **نجاح مستمر** لأن عناوين كتير بتمشي على نفس الإطار. اتشهر على إيد **Popcorn** (Parking Jam وغيرها).

**الخصائص العامة:**
- **أهم قاعدة ★★★:** الألعاب دي **بسيطة لأنها بتعتمد على الـ marketability والـ theme.** ده لازم تفكر فيه **قبل ما تفكر في الميكانيك** لأن **الـ CPI بيتحرك بالـ theme**، والميكانيك غالبًا نفسها بين ألعابك.
- **التحدي الحقيقي:** إنك **تحافظ على الـ logic fresh.** بتسأل: "هشيل حاجات وأكشف اللي تحتها؟ ولا أديها twist بـ gravity أو gimmick؟"
- **الكاميرا:** top-down أو مواجهة مباشرة.
- **الكنترول:** **tap قرب 100%** دلوقتي، وفي slide وdrag قليل.
- **الآرت:** cartoonish ومينيمال، **contrast عالي**، ومباشر في إيه اللي بيحصل.
- **الأصول:** بسيطة.
- **البنية:** تسلسل حركات يوصل لنتيجة واضحة. ★ **غالبًا constraint واحد كفاية** (ممكن أكتر).
- **Consumables:** ما فيش في الأغلب. لعبة كبيرة واحدة بس عندها consumable، ودي ممكن تكون فكرة تدخلها في لعبة جديدة.

**الـ 4 parameters لتحليل أي sequential puzzle ★★★:**
1. **Core mechanics**
2. **Game constraint**
3. **Main objective**
4. **Consumables**

### الأمثلة بالاسم (تفصيل لكل واحدة)

| اللعبة | الكنترول | الميكانيك | الـ constraint | الهدف | Consumables |
|---|---|---|---|---|---|
| **Tangle Snakes** (Popcorn، حديثة) | tap | شيل الثعابين المتراكبة/اللي قدام غيرها، وتفادى الـ traps | ما تتحركش لو في ثعبان فوقك/قدامك | امسح كل الثعابين | لا |
| **Parking Jam 3D** | slide | العربية تروح لأقرب lane، وإنت تشيل العربيات اللي بتسد | عربية قدامها عربية ما تتحركش | فضّي الباركينج | لا |
| **Tap Away** | tap + دوران الكاميرا 3D | بلوك بسهم يتحرك في اتجاه السهم، ولو قدامه بلوك ما يتحركش | نفس القيد | امسح كل البلوكات | **أيوه: Dynamite** |
| **Pull the Pin** | tap | شيل الـ pin، الـ gravity بتخلي الكور تقابل بعض، وتتجمع في الكوب | الـ pin بيسد + **ما تجمعش الكور الرمادي** (constraint تاني) | اجمع الكور الملونة | لا |
| **Open the Box** (Homa، "Moma and mammal Studios" بالترجمة) | tap to unfold + دوران | تفتح القطع لو مفيش حاجة فوقها، **tear strips** زي شرايط أمازون، ثم الفوم يغطي الهدف فتضغط تكشفه | ما تفتحش لو في sticker/tear strip فوق | اكشف كل الأوبجكتس + meta: اجمعها وزيّن الأوض | لا |

**تفاصيل الأمثلة:**
- ★★ **Tangle Snakes:** الـ constraint بيتوصل **بصريًا**: لو في ثعبان فوقك بيبقى في **ظل** عليك، وبتشوف إنك لو ضغطت مش هتروح لأي حتة. وفي **timing**: لو ثعبان خبط في تاني وهو هارب، **الأنيميشن بيتلغي**. **ضاف الـ overlapping** على Parking Jam، وبدونه كانت هتبقى "Parking Jam بثيم ثعابين".
- **Parking Jam:** لازم تعمل **time exit** عشان تتجنب التصادم.
- **Tap Away:** "يستعير نفس ميكانيكس الاتنين" وبيضيف **rotation + theme جديد = "بوم، puzzle جديد تقريبًا"**. الـ Dynamite بيفتح بلوكات وبيسهّل ليفلات، لكن **مش في الـ core loop**، وتقدر تلعب طويل من غيره. بيتعامل معاه George كمسألة progression.
- **Pull the Pin:** هي اللعبة الوحيدة اللي فيها gravity. ملاحظة: George سماها "color selection/collection". تسلسل الـ logic: 3-4 خطوات.
- **Open the Box:**
  - بتاخد الـ rotation من Tap Away، لكن بدل الحركة **unfold لجسم ثابت**. George مصنفها مستوحاة من هايبر كاجوال زي "followed 3D" من Good Job Games (الاسم غير واضح من الترجمة).
  - بتخلي اللاعب يفكر: "أي قطعة أفتحها الأول؟ في قطع مخفية ورا زاوية تانية؟" يعني **تدور على الزاوية اللي تبدأ منها**.
  - الـ **sticker/tear strip** تفاصيل **مش واضحة في الأول، وبتظهر أكتر مع التقدم** عشان تزود التحدي تدريجيًا.
  - **ممكن تضيف consumable** (زي x-acto cutter يسهّل حركة واحدة) لكن "مش هيضيف كتير". George: "نظريًا ممكن".

### ★★★ الباترن ورا الفئة كلها

- **القاعدة:** كل لعبة بتحافظ على **نفس الأساس: إزالة عائق تتيح لعنصر تاني يتحرك**، وبتضيف **ميكانيك أو constraint واحد-اتنين** يخلي الـ theme يلمع (gravity + color collection، rotation + overlapping).
- **Open the Box = Tap Away rotation + Tangle Snakes overlapping + ثيم unboxing relatable.** ده مثال حي على الـ combinatorial ideation: ناخد عناصر موجودة من ألعاب ناجحة ونحطها على ثيم جديد.
- **اختيار الـ theme:** لازم يكون **relatable** ("الكل يعرفه أول ما يشوفه")، وسهل الفهم حتى لو مجرد (ثعابين، عربيات، بلوكات، كور ملونة).
- **كل لعبة ليها شخصية/theme مختلفة** → ده اللي بيساعد في CPI والـ marketability غالبًا.

---

## 7. Meta وprogression وmonetization في الفئة ★★★

**Progression/Challenges:**
- أنواع تحديات: **time-based، memory-based، difficulty levels من normal لـ extreme.** مثال: في Tap Away في ليفل **1000 بلوك في time limit**.
- **Map system أو decoration system** (زي Open the Box) للـ long-term play والـ collection.

**Meta خفيفة:**
- Customization بسيط: الخلفية، الـ core toy، الأنيميشن، الـ hand.
- تجمع **puzzle pieces** من الليفلات وتفتح premium features.
- كلها **cosmetics** بتتفتح بـ **in-game currency**. الـ coins هي العملة الوحيدة المحتملة (George مش متأكد إن في IAP أصلًا).
- التحديات level-based بتتفتح بالـ coins.

**Monetization:**
- ★★ **اللعبة بتحط إعلانات كتير زي الهايبر كاجوال العادي، رغم غياب consumables وIAP، وده شغال.** George بيفسر: الـ puzzle فيه **عنصر ثابت (مش moving target)** ودوران وأفعال صغيرة.
- أدوات الـ monetization: playable skins، accessories، backgrounds، "barely IAP".
- **الـ theme بيحدد قد إيه تقدر تـ monetize بالـ cosmetics والـ skins.**
- الـ cosmetics بتحتاج تنويع: الأنيميشن، الأصول نفسها.

**"أيه اللي تركز عليه في لعبتك الجاية" (الـ last slide):**
- **Sticky core mechanic:** إزالة عنصر (single action) يخلي غيره يتحرك أو يعمل حاجة؛ **مسح الليفل يكون مُرضي**، أو **كشف حاجة في الآخر** بعد unwrap.
- **اعتبارات design:**
  - **Challenges كـ progression** (ليفلات أصعب، تتفتح بـ daily missions أو تقدم عادي).
  - **Level races** (تخلص الليفلات قبل لاعبين تانيين).
  - **Leaderboards**، و**fake/async PVP**.
  - **Gadget machines بمكافآت عشوائية** (coins، tickets، ball machines، skins) وموجودة في ألعاب Popcorn كتير.
  - **World-building maps:** بيت تزينه، أوض، مواقع تفتحها، أقسام خريطة جديدة.

---

## 8. أسئلة الشات والإجابات (Q&A) ★★★ (كلها مفيدة للتطبيق)

### أ. أسلوب Popcorn المينيمال: كويس للـ CPI والـ retention؟ ★★★
- **George:** كويس للـ CPI. حتى لو بسيط، لسه ملون وبيشد الانتباه. **الكرييتيف مش لازم يعكس الـ gameplay النهائي** (مثال: Open the Box، الاسم في الترجمة "Tupperware"، بتغيّر شكل الأسهم في الكرييتيف). **الـ core loop والآرت النظيف الـ contrasty مهم عشان اللاعب ما يتعبش**. الحفاظ على نفس الـ fidelity في كل ألعابهم قرار ذكي: "ده Popcorn game، فعارف إنها هتبقى puzzle كويسة".
- **Kevin:** Popcorn في موقع فريد بـ **Pull the Pin كـ outlier** و**بنت brand منه**. الخلفيات والـ UI "carbon copy" ("insert new puzzle here"). **مفيش سبب ما تعيدش استخدام الأصول، وبيبني brand.**
- ★★ **ملاحظة Kevin:** "سمّي لعبة casual مفيهاش pull the pin minigame دلوقتي"، يعني الـ **creative** اتنسخ في الإعلانات (Save the King from the dragon، drop the coal on the fire to warm the woman up). و**Homescapes نسخت Pull the Pin** وPull the Pin كانت قبلها "trendsetter".

### ب. تردد الإعلانات: "بعد كل ليفل = Bonkers" (Julie) ★★★
- **George:** لازم تكون كتيرة عشان ما فيش IAP/consumables، وإلا اللعبة ما تعيشش. **لا تكسر الـ gameplay** (الليفل 30 ثانية–دقيقة) بإعلان. **بعد الليفل** أقبل بكتير، و**mid-game** (في بعض upper-casual) أكتر إزعاج.
- **Kevin:** الـ **match-3 الكبار (زي Royal Match) مفيهمش interstitials**، وغالبًا مفيش حتى rewarded، بيتربحوا من **IAP وشراء الوقت/الـ moves**. الألعاب الأبسط لازم تعرض إعلانات كتير "عشان في النهاية عايزينك تدفع **$1.99 تشيلها**". الإعلانات "شر لازم".
- **الباترن:** غياب الـ monetization الثانوي بيجبر الـ ads → نظام **remove-ads IAP** هو الإيراد الحقيقي.

### ج. شكل الآرت: لازم هايبر كاجوال بالكامل؟ ★★
- **Kevin:** أكبر الـ puzzle games ليها **مظهر "creamy cartoony" شبه Pixar**، **soft وunbusy**، **ما يشتتش عن اللغز**. استثناء: hidden object (ممكن ينفع تفاصيل كتير).
- **George:** مثال **Scavenger Hunt**: مظهر **أقل polish، 2D flat بأصول سميكة**، منطقي لأن في عالم كبير بأصول كتير، و**3D hyper-casual assets مع شخصيات كتير هتتعب الأداء**. لازم **تكيّف الآرت مع نوع اللغز**.
- **Kevin:** **Portal** puzzle كلاسيك بجرافيك واقعي، يعني لازم **تتطابق مع الـ vibe**.
- ★ **Realistic graphics + puzzle** (Johan): **Triple Match 3D، Match 3D، Goods Sort** ليهم textures وphysics واقعية وجذبوا نفس الجمهور. "ليه لأ".

### د. CPI والـ publisher thresholds ★★
- CPI لـ Open the Box: مش متاح، وهيتشارك على Discord. **الحلقة "ideation" وعمدًا ما اتكلموش عن الـ CPI، التركيز على game design.**
- **Carla:** الـ publishers عندهم متطلبات **أقل من 70** للـ puzzle. **Kevin:** "حاول تخلي الـ CPI أقل ما يمكن، وكل ما قل **أنت على حاجة**". **اعمل ألعاب، اختبرها، حسّن كل مرة. ما تقلقش من الـ thresholds، لأن لو لعبتك مش بتحققها يبقى الموضوع moot.**

### هـ. Popcorn: 100 موظف و"hit واحد في السنة"؟ (YG Studio)
- الإجابة: الشركات الكبيرة **بتختبر باستمرار** (prototypes كتير، وقليل بيعدي الـ KPI filters). في الشات: "Popcorn دايمًا في الـ top charts، وParking Jam ثابتة، والـ live team".
- ★★ **جملة جامعة (شات + Kevin):** "كل الألعاب مبنية على **motivation رئيسي + إضافة constraints وpower-ups وعمق** عشان تبقى ممتعة."

### و. Twisted Tangle (Rollic) على نفس blueprint؟ ★★
- **أيوه sequential** وبنفس الفيتشرز، **لكن بتلعب بـ grid** (الباقي free movement). **Tangling بدل overlapping/front-facing**، وبتشيل جزء من الحبل عشان التاني يتحرك.
- **أكتر hybrid** (IAP أكتر)، وهي **تطور** لـ **Tangle Master 3D** (ترجمة تقريبية للاسم). حبال وgrids أكتر، **playtime أطول**، "أخدوا اللعبة القديمة وضافوا عمق ضخم".
- **Kevin:** العمق ده **بيوسع monetization loops.** اقتراح: pop-up "استخدم تذكرة لتشيل 5 حبال". (نفس الشركة الأم مع Popcorn حسب الترجمة، والاسم غير واضح.)

### ز. هل أحط IAP/rewarded في الـ test؟ ★★★
- **George:** لأ، **مش في أول خطوة (ideation)**، بعد ما الـ test ينجح.
- **Kevin:** ما نحبش نشوف ads، فاقفل الـ pop-ups أو **اديهم الأزرار ببلاش.** **الهدف: نشوف الناس بتلعب لأنها ممتعة**، يعني الـ test بيقيس الـ core loop بس.

### ح. أفكار فيديوهات/كرييتيف للـ puzzle (frantic/Ray)
- نفس **قواعد الـ CPI العادية.** ارجع لـ "your first five seconds count" وCPI section في الـ Academy.
- **الناس بتعمل ألعاب من كرييتيفات الشركات الكبيرة** (Homescapes ads).

### ط. ألعاب موسمية/Halloween ★★
- **George:** risky. **Kevin:** spike مرة في السنة (مثال: Santa Tracker بتاع صاحبه Simon، بيرتفع في ديسمبر وبس). الأفضل: **live event جوه اللعبة** مش لعبة موسمية كاملة.

### ي. أصعب حاجة في الـ puzzle: difficulty curve ولا CPI؟ ★★★
- **George:** **CPI الأول:** "صعب جدًا تلاقي theme قابل للتسويق". الـ **balance** صعب برضه. الـ level design في sequential أبسط، لكن **الـ theme والـ long-term balancing** هما الاتنين الرئيسيين.
- **Kevin:** للـ balancing لازم **data**: **analytics مظبوطة**، سجّل **فين اللاعبين بيسقطوا في الليفلات** (مثال: لو الكل بيقع في ليفل 5 يبقى فيه مشكلة). "خلي الداتا تقودك شوية" و"كل puzzle مختلف".

### ك. هل Homa بتدور على puzzle games؟ ★★★
- **أيوه.** لكن: **"ما تسألش 'عايزين puzzle ولا كذا؟'، اختبر لعبتك."** السوق هو اللي بيقول. ★★★ **لو شفت لعبة بتنجح فهي نجحت في الـ testing، ولو الكل بيقلدها فأنت أصلًا متأخر. اديهم حاجة وهنختبرها.**

### ل. Horror و non-level-based
- **Horror:** Five Nights at Freddy's "كسرت الدنيا"، و"youtubable"، لكن **سوق نيش صعب**. Kevin اعترف بصراحة: "**مش عارف**"، وهيحولها للـ publishing team (غالبًا هيقولوا لأ).
- **Non-level puzzle:** Kevin مش متخيل ازاي بيشتغل. اقتراح من الشات: **World of Goo**، و"ممكن reboot".

---

## 9. مصادر الإلهام ★★★ (قابلة للتطبيق مباشرة)

1. **Google: "success leaves clues"** ★★. اكتب "top puzzle games 2011 iOS" (غيّر السنة والمنصة) فتلاقي قوائم تفتح كل لعبة بـ wiki وdownload. من أول بحث لقى **Snauticals**: لعبة physics شبه Angry Birds، **one-touch**، juicy، landscape. Kevin ما يقولش "اعملها"، لكن "مثال تقدر تجرب عليه".
2. **Steam:** تقسيم الـ categories بتاع الـ puzzle كويس. مثال: **Merge Beasts** (tower defense شكلها match-3).
3. **itch / Epic / Unreal store / Kongregate.**
4. ★★★ **Apple Arcade:** **45 puzzle game** وقت التسجيل، ومعظم الناس مش بتبص عليه.
5. ★★★ **Paid games القديمة:** كتير منها **مش متاحة أو تحميلاتها قليلة بسبب الـ paywall.** السؤال: **"تقدر تحوّل puzzle مدفوعة (حالية أو قديمة من top paid charts) لـ free-to-play؟"**

---

## للاستوديو:

### (1) Mossfolk
- **الجمهور (★★★):** أنثى 35+، جلسة ~3 دقايق، "إنجاز في الجلسة القصيرة". نراجع: هل الليفل (هدف + ميزانية إسقاطات) بيتحل في ~3 دقايق على أغلب الليفلات؟ والتيستر-بوت يقدر يطلّع متوسط زمن الليفل ويشوف كام ليفل خارج الحد.
- **العناصر الثلاثة:** القواعد والحدود = البرطمان + ميزانية الإسقاطات + 9 أحجام. والـ **mossy shells/stones/rot** من 2501 هي **pinch points** الجديدة، يعني مصدر "آها". الكنترول (الإسقاط في الـ physics) لازم يكون deterministic ومحسوس عشان مفيش jank. والهدف لازم يظهر من أول ثانية.
- **Merge مش مذكور** صراحة في قائمة الميكانيكس اللي اتقرت (matching/word/bubble/sorting/tap-blast)، وسلايد الـ taxonomy ما اتقراش بالكامل. فمش هنقول إن السوق "أثبت merge" من الحلقة دي.
- **Meta:** الحلقة بتأكد على **decoration/world-building map** وlevel races وfake PVP وgadget machines. الـ **rival contests** عندنا جاهزة (fake PVP)، ونقدر نقيّم **map/decoration meta** كطبقة تقدّم (بدون أي طاقة تمنع اللعب).
- **الإعلانات:** نفس قاعدتهم: لا إعلان وسط الليفل، فقط بعده. وIAP "remove ads" هو الإيراد الحقيقي لو الاقتصاد ضعيف.

### (2) خط الإنتاج السريع ★★★

1. **"Sequential puzzle" = ماكينة أفكار جاهزة لإيقاع لعبة/يوم-أسبوع:** الصيغة ثابتة: **تحليل بالـ 4 parameters (mechanic / constraint / objective / consumables) + theme relatable + twist واحد.** ننتج سبريدشيت combinatorial: [ميكانيك أساسي] × [كنترول] × [twist: gravity/rotation/overlap/fold] × [theme]. وده بالظبط اللي عمله Popcorn وHoma (Open the Box = Tap Away + Tangle Snakes + unboxing).
2. **الـ theme هو اللي بيحرك الـ CPI** (George)، فخلّي اختيار الـ theme **القرار رقم 1 في الـ intake**، وجرب كذا theme على نفس الميكانيك بكرييتيفات قبل بناء كامل. الاختبار ده أرخص من بناء لعبة.
3. **اختبار الـ CPI من غير monetization:** البروتوتايب بيتقاس على "هل بيلعبوا لأنها ممتعة"، **الـ ads والـ IAP والـ pop-ups تتقفل أو تتدّي بلاش** في الـ test.
4. **أنظمة قابلة لإعادة الاستخدام بين الألعاب:**
   - قالب UI/خلفيات واحد ("insert new puzzle here") عشان brand واحد.
   - ad-after-level module.
   - coins + cosmetics shop.
   - daily missions.
   - level race / fake-async PVP.
   - gadget machine (random rewards).
   - decoration map.
   - analytics لـ level drop-off.
   
   **تحذير:** ده تكلفة بناء مرة واحدة، لكن مش مضمون إن كل لعبة محتاجة كل الأنظمة. نحط كل نظام وراء feature flag.
5. **التيستر-بوت:** في الـ sequential puzzle نقدر نحسب **solvability وعدد حلول صالحة** (dependency graph للعوائق) ونقيس difficulty قبل ما نبعت لبشر. ده بيحل "أصعب حاجة: difficulty curve" ويقلل ليفلات مستحيلة أو تافهة. بعد الـ soft launch نربط ده بـ analytics الحقيقية (فين بيسقطوا).
6. **فلتر الأفكار:** "لو لعبة نجحت والكل بيقلدها فأنت متأخر" (Kevin). يعني **نتجنب نسخ ترند اليوم**، ونعمل **recombination** (ميكانيكس معروفة × theme/twist لسه ماحدش عمله). مصادر الـ ideation الجاهزة: Google "top puzzle games [year] [platform]" + Steam categories + **Apple Arcade** + **top paid charts القديمة (paid → F2P)**.
7. **معدل النجاح منخفض حتى للكبار** (Popcorn: 100 موظف و~hit في السنة). هنكتب في خطتنا نسبة تعدي متوقعة منخفضة، ونعتمد على **حجم البروتوتايبات** مش على توقع كل لعبة تنجح.
8. **الأنظمة الموسمية:** الأفضل **live event** جوه اللعبة مش لعبة موسمية كاملة (spike مرة في السنة).

**نقطة تحذير للدقة:** الحلقة ما اتكلمتش عن CPI فعلي (متعمد)، ولا عن أرقام retention. فكل الكلام عن "ينجح في CPI" هو رأي publisher مش داتا معروضة.