# Homa Games: Hybrid Casual + AI Ideation (بث مباشر، ~69 دقيقة) — نوتس مذاكرة

معرف الفيديو: DFpS92E8wY4. الترانسكريبت مفيهوش عنوان رسمي، فالعنوان ده وصفي. البث فيه 3 أجزاء: **Jules** (Publishing Manager) عن الـ Hybrid Casual العميق، و**George** (Ideation Expert) عن الأفكار بالـ AI، وكيفين مقدّم البث. ملاحظة: أسماء زي "Tugaystan" و"Augustine" و"Georgie" و"Quanti" و"Nervisha" جايين من الـ transcription وممكن يكونوا غلط في الكتابة.

---

## 0. افتتاح + سؤال الألوان (Quanti) ★

- سؤال: "إزاي أحسّن الـ color palettes وعدد الـ assets عشان تبقى جذابة؟" الجواب: **high contrast vivid colors**. الحل العملي: ابص على **Top Charts** وشوف الألعاب اللي فوق دلوقتي واتعلم منها الـ palettes، وده بيتعمل في Unity بسهولة.
- الباترن: الألوان مش ذوق عشوائي، دي **market validation بصري** — اللي شغال في الشارت بيبقى شغال في الـ thumbnail والـ creatives.
- المنصة: Homa Labs بتقبل الـ prototypes، وفيه Academy فيها تدريبات وجلسات أعمق، وDiscord.

---

## 1. تعريف الـ Hybrid Casual (Jules) ★★★

- **التعريف الجامع:** لعبة واقفة **في النص بين Hyper Casual و Casual**:
  - **Hyper Casual:** snackable، جمهور واسع، إعلانات بس، والـ core metric = **CPI** (تكلفة الاكتساب).
  - **Casual:** جمهور واسع برضه، بس بيستهدف **LTV** والـ **retention** كـ core metric، ومحتوى أطول.
  - **Hybrid:** بيجمع الاتنين: **إعلانات + In-App Purchases**، وبيستهدف الاتنين.
- **الباترن:** Homa بيقسّم الـ hybrid حسب **المدة اللي اللاعب بيفضل فيها**، ومن كده بيتحدد الـ budget والفريق والمدة. النوع اللي بيعيش 7 أيام مش نفس اللي بيعيش 30 يوم.

### نوعين Hybrid عند Homa:
1. **Light Hybrid (أقرب للـ Hyper Casual):**
   - أمثلة: **Zombie Defense، Farmland، Aquariumland، Fight for America** (وقال إنها في التوب 10 دلوقتي).
   - بيستهدف **D7** وممكن **D30** بس اللاعب عادةً بيلعب 7 أيام.
   - الهدف المالي الأدنى: **5 مليون دولار سنويًا مع 20% من الـ IAP**. الأربعة ألعاب دي كلها بتتجاوزه بكتير.
   - عملية الإنتاج أقصر، وبتتعامل بنفس منطق الـ Hyper Casual.
2. **Deep Hybrid (أقرب للـ Casual):**
   - لاعبين بيلعبوا **30 يوم أو أكتر**.
   - الهدف: **ROI إيجابي على الإعلانات بعد 20-30 يوم** من الاكتساب، مش بعد يومين.
   - نسبة الـ **IAP في الإيراد أعلى**.
   - محتاج **محتوى بـ 30 يوم**، وخبرة في **progression systems** و**economy balancing**.
   - بيتعمل مع **Hybrid Studios** بس، مش أي استوديو (معايير مذكورة لاحقًا).

---

## 2. الـ Prototype والـ KPIs: الماتريكس بتاع الـ Cumulative Play Time ★★★

- **الـ Prototype:** حوالي **40 دقيقة gameplay** + creatives + فكرة مختلفة.
- **بيتقاس على:** **Cumulative Play Time Day 3** — متوسط وقت اللعب التراكمي عبر أيام 0-1-2-3 (ملاحظة: الشرح في البث متلخبط شوية في التعريف، بس الفكرة إنه مقياس بيجمع **play time + retention**).
- **الماتريكس (بيحط الـ prototype على محورين: Play Time × CPI):**
  - **Play time متوسط/منخفض + CPI عالي → اعمل scratch وابدأ فكرة جديدة.** ده الـ kill decision.
  - **Play time متوسط/منخفض + CPI مقبول/عالي → ممكن تعيد الاختبار على CPI أقل** (الحركة لليمين في الماتريكس).
  - **CPI مقبول + play time ضعيف → iterate على المحتوى وضيف progression** (بس مش دلوقتي، لأنه لسه prototype، فالأولوية للـ core mechanic).
  - **Outlier في play time (بغض النظر عن CPI) → نجاح:** يدخل **Deep Hybrid process** لو الاستوديو hybrid. ولو الاستوديو صغير، يدخل **Light Hybrid iteration** (شبه الـ Hyper Casual، بس أطول لأنه محتاج محتوى وIAP).
- **الباترن:** القرار بيتاخد **قبل** ما تبني محتوى كتير. الـ prototype بيتقاس بالأرقام، والقرار بيكون "كمّل / عدّل / ارمي" بدل الحدس.

---

## 3. الـ Genres اللي Homa بيشتغل عليها ★★

- **Arcade Idle:** Aquariumland، Farmland.
- **Shoot 'em up:** Zombie Defense.
- **Arcade Tower Defense:** Fight for America (مزيج shoot 'em up + tower defense + arcade).
- **Draw Defense:** City Defense (الرسم كـ core mechanic + tower defense كـ genre).
- **تحت الاستثمار:** **Puzzle، Idle، Sniper**.
- **الباترن:** Homa بيدوّر على **fusion** لـ genres، مش genre واحد. الأفكار الهجين (merge genres + mechanic مبتكر) هي اللي بتبرز في السوق المزدحم.

---

## 4. خط إنتاج الـ Deep Hybrid (من الـ Prototype لـ الإطلاق) ★★★

- **المدة الكلية:** حوالي **10 شهور** من الـ prototype للـ launch.
- **المراحل:**
  1. **Prototyping:** بدعم من PM (ترندات، أفكار، تحليل داتا، feedback على البيلد). الهدف: إثبات الـ core gameplay بالـ KPIs.
  2. **Vertical Slice / Iteration:** بناء **7 أيام محتوى** للفكرة المثبتة، بناءً على:
     - **Player persona** مبني على **surveys مكثفة** للجمهور: بتسأل إيه الألعاب اللي بيلعبوها؟ بيحبوا إيه (customization، management، action)؟
     - **Hypotheses:** إيه اللي هيخلي اللاعب يلعب في يوم 7 و يوم 30؟ وإزاي هتتحول الـ engagement لفلوس؟
     - بيتبنوا الـ features في **3 شهور**، وبيتقاس تأثيرها.
     - بيتدخل **Game Economist** يوازن الاقتصاد وكل مراحل اللعبة والـ monetization.
  3. **Validation (معايير نجاح الـ slice):**
     - **D7 retention**
     - **Revenue per paying user**
     - **Conversion**
     - **Repeat spend** (أهم حاجة: الناس بتشتري تاني؟)
  4. **Production:** محتوى كامل، ومش فيه unknowns كبيرة لأن الفرضيات اتثبتت، والشغل بقى حجم.
  5. **Soft Launch:** بمساعدة فريق الداتا وUA وCreative والماركتينج، وبناء community حوالين اللعبة.
  6. **Live Ops:** لسه بيستكشفوه لأنهم لسه ما عملوش launch لأي لعبة deep.
- **الباترن:** كل مرحلة بتشتري **تقليل unknowns**. الفرق المكلفة (production) بتيجي بعد ما الفرضيات تتثبت، مش قبلها.

---

## 5. KPIs الإطلاق والأهداف ★★

- **حد أدنى للإطلاق:** **30 ألف دولار daily spend في الـ US، بـ ROAS 30%**. (الـ US بس، مش عالمي.)
- **الهدف بعد الإطلاق:** على الأقل **10 مليون دولار إيراد** و**40% ROI** (ربح بعد الإطلاق).

---

## 6. معايير الاستوديوهات اللي Homa بيدوّر عليها ★★

1. **خبرة Hyper Casual:** يعرفوا يعملوا prototype بسرعة، ويعرفوا "أكواد" الـ hyper casual (juiciness، simplicity، الوصول للـ core gameplay).
2. **فريق أكبر:** الألعاب deep فيها محتوى وfeatures كتير، فالـ solo dev أو الفريق الصغير صعب يخلّص.
3. **خبرة بالـ deep games:** فريق اشتغل على أنظمة معقدة و online systems، وعارف يتعامل مع **8-15 شخص بيكمّلوا على نفس الـ branch** من غير ما المشروع يتفكك. (الهدف: إن اللعبة متتفككش بعد 5 شهور تطوير.)
- **الباترن:** المعيار الأهم هو **الـ workflow management** مش المهارة الفردية. اللعبة الكبيرة بتفشل لأسباب تنظيمية.

---

## 7. Q&A: الفرق الصغيرة و Homa Labs ★★

- **Light Hybrid مع فرق صغيرة:** Homa نشر ألعاب من فرق صغيرة قبل كده. **Zombie Defense اتعملت بـ 5 أشخاص.** لازم تضبط التوقعات: الـ light hybrid محتاج شغل أكتر من Hyper Casual عادي.
- **Deep مع فرق صغيرة:** صعب جدًا، بس **الـ prototype** نفسه ممكن بـ **3-4-5 أشخاص** (الفرق اللي Jules بيشتغل معاها بتعمل prototypes بـ 3-5 أشخاص). لو الـ prototype طلع outlier، هيتدعم الفريق بموارد أكتر.
- **الفكرة:** Homa Labs هي **فرصة**: لو لقوا لعبة صغيرة مبهرة، بيتواصلوا ويدّوا موارد عشان تتطور.
- **الباترن:** الـ prototype الرخيص هو **فلتر** — بتدفع وقت صغير عشان تكتشف فكرة كبيرة، بدل ما تبني مشروع 10 شهور وتكتشف إنه مش شغال.

---

## 8. نصايح Jules للأفكار ★★

- **Light Hybrid:** لازم تكون **trendy**، وتحقق **CPI عالي**. الـ loop لازم يبقى hybrid (فيه عمق وprogression): زي **build your base / tycoon loops** أو **RPG-style evolve your character**. بس لسه معتمد على الترند والـ CPI.
- **Deep Hybrid:** ابحث عن **twist على لعبة hybrid موجودة** تديها عمق وplayability طويل المدى.

---

## 9. Idle & Puzzle + Clickers ★★

- **الـ Idle:** من أكتر الـ genres **اقتصادية** على الموبايل: تقدر تعمل لعبة كبيرة بفريق صغير، لأنك **محتاج systems قوية مش محتوى كتير**.
- **Golden Goblin** (مثال Jules): من أعلى 100 لعبة في الـ grossing، حوالي **50 مليون في الـ IAP سنويًا** (تقريبًا)، والـ **ads حوالي 50% من الإيراد**. فريقها **6-7 أشخاص**، بس كانوا خبرة طويلة في الـ idle وفيهم data scientists.
- **الباترن:** الفريق الصغير ينفع **لو** خبرة الـ genre عالية. الـ idle مش "سهل" — هو "محتاج systems دقيقة".
- **Clickers:** ترند في السنة دي، وفيه pipeline عند Homa. وفيه إمكانية **hybridize** (تهجين) الـ clickers مع genres تانية.

---

## 10. George: عملية الـ Ideation (ذكاء اصطناعي + بحث سوق) ★★★

**المراحل بالترتيب:**
1. **Market research (لازم، مش هتتخطاه):** Top charts، demographics، competitor analysis، prototyping trends.
2. **Reference check:** تتأكد إن الفكرة اتعملت قبل كده. لو فيه trend بيتعمل prototype الأسبوع ده، تشوف إذا ستوديوهات تانية عملته بطرق كتير، عشان ما تعملش نفس المنتج.
   - هنا بيستخدم ChatGPT أو Ludo أو أدوات تانية لأنها بتطلع thames و genres بسرعة.
3. **Brainstorm (ساعة):**
   - **أول 30 دقيقة:** remix لأفكار جاهزة (من trends أو فيديوهات social viral). بيرسموا mock-up بسيط، ويعدّلوا، ويدمجوا genres.
   - **آخر 30 دقيقة:** أفكار من الصفر، بيرسموا live ويناقشوا ويدمجوا. **"هنا السحر بيحصل"** (كلامه)، وده المكان اللي الـ AI يساعد فيه أكتر لو عملت الـ reference check.
4. **Validation:** تجمع الأفكار وتشوف هل تتكيف مع السوق؟ هل اتعملت prototype في الـ stores؟ هل فيه twist ممكن؟ **الفكرة اللي اتعملت خلاص بتتقتل** ومتأخدش فرصة.

**الباترن:** الـ AI **مش مصدر الأفكار**، ده **مصدر للتنوع والاقتراحات**. الحكم والـ twist والقرار النهائي بيتاخدوا في النقاش البشري.

---

## 11. AI: الـ DOs ★★★

1. **علّم الـ AI بالـ structure الأول:** متقولهوش "اعملي runner"، وريه إيه هو الـ runner، وريه الـ process والـ structure بتاعك، وبعدين اطلب الناتج. النتيجة بتبقى قابلة للاستخراج.
2. **وسّع قائمة الـ themes:** اسأله عن themes في الحياة الحقيقية أو الخيال، واختار من قائمة 100 أو أكتر. الـ bot عنده خيال كبير، فاطلب منه يكون creative قد ما يقدر.
3. **حدد العناصر الناقصة في الـ core loop** (ده أهم استخدام):
   - مثال George: عنده **سمكة** و**صنارة**، ومحتاج تفاعل بينهم. سأل الـ bot: "إيه العناصر اللي ممكن تتفاعل بين الصنارة والسمكة؟" فجاوبه: **fishing line durability** (متانة الخيط). الفكرة طلعت بمنظور جديد ودفعت الـ mechanic لقدام.
   - الباترن: الـ AI ممتاز في **ملء الفراغات بين عنصرين موجودين**.
4. **اعمل investigation للـ core loops في الحياة الحقيقية أو الطبيعة أو المهن** وطبقها على فكرتك.

---

## 12. AI: الـ DON'Ts ★★★

1. **متطلبش "فكرة لعبة موبايل" بشكل عام:** الناتج "نادرًا ما بيكون جيد". (مثال: مزج **Sky Roller** مع **Z Escape** → طلع: "Sky Roller بس مطاردة من الفضائيين".)
2. **متطلبش تدمج لعبتين موجودتين:** الـ AI بيرجع يديك نفس اللعبة بثيم مختلف.
3. **متطلبش تغيّر فكرة موجودة في الـ skin بس:** هيدّيك **نفس الـ core loop بشخصية مختلفة**. Homa بيتجنب ده بقصد، ويركز على تجارب جديدة و iterations و twists.
4. **متطلبش دمج ألعاب حديثة:** ChatGPT's knowledge مش بيغطي الحديث (في البث قالوا "حتى 2021"). مثال: مش عارف **Attack Hole** (لعبة Homa نفسها)، فبيجيب لعبة قديمة بنفس الاسم وبيعمل خلط.
- **الباترن:** الـ AI بيعيد **أقرب شكل معروف** للمدخلات. ولو المدخل قريب من اللعبة الموجودة، الناتج هيكون نسخة منها.

---

## 13. الأدوات ومقارنتها ★★

- **ChatGPT:** للـ structure والـ themes والـ exploration والـ research. مجاني، والنسخة المدفوعة **20$/شهر** أسرع.
- **Ludo AI:** بيعمل **game ideas + image generation** في نفس الوقت، وبيعرف يقرأ ألعاب معروفة زي Attack Hole ويدمجها. بيدي genre selection (مثل Hyper Casual) وstyle (3D أحسن نتيجة). **Free trial 200 credit، والنسخة المجانية 20 credit شهريًا.** عيبه: مش بتتكلم معاه وتعدّل الفكرة مباشرة.
- **Notion AI:** مش قوي زي ChatGPT، بس لو ده الخيار الوحيد ممكن يكون موثوق في حالات معينة.
- **Image generators (للـ mockups والـ art style والـ screenshots):**
  - **Midjourney:** أفضل نتيجة من الثلاثة.
  - **Ludo AI:** نتايج كويسة.
  - **DALL-E:** الأفضل في الـ **realistic**، بس **مش موصى بيه للـ Unity 3D style**.

---

## 14. شكل الناتج المثالي من الـ AI (Output Structure) ★★

- **Pitch:** سطر واحد.
- **Screen composition:** العناصر وأماكنها على الشاشة.
- **Art style.**
- **Core mechanics:** الكنترولز، الاتجاهات، progression.
- **Core loop:** دورة اللعب (الأهداف، المكافآت، التحديات). **التمييز:** الـ mechanics = "إيه اللي بتعمله بإيدك"، والـ loop = "الدورة الكاملة اللي بتخليك ترجع".
- **Satisfaction & focus:** عناصر الإحساس البصري والتفاصيل المهمة.
- **Meta features:** achievements، loops بديلة.
- **References:** من 2 لـ 4 ألعاب/صور، عشان تبين للاستوديو الشكل المطلوب بالظبط.

---

## 15. الـ Live Demo: Level-Up Runner ★★★

**الفكرة الأساسية:** George كان عايز runner، بس فكرة الـ subgenre دي اتعملت كتير. فحاول يدوّر على theme جديد.

**التسلسل (ومعاه الدرس في كل خطوة):**
1. **السؤال الأول:** "اعطيني 20 شيء ممكن يتطور، ووصف تطورهم" بالـ structure. **النتيجة:** coins، power-ups، enemies → **عامة جدًا**. **القرار:** وقّف الـ generation لما يبقى غير مفيد.
2. **تغيير الصياغة:** بدل "things that can evolve" → "**30 things that go through evolution**". **النتيجة:** fish، dinosaurs، insects، birds، plants، monkeys، dogs. **الدرس:** تغيير كلمة واحدة بيغيّر الناتج. الـ AI بيتجاوب مع الألفاظ بطريقة مختلفة.
3. **اختار Plants:** لأنه ملقاش كتير من plant runners.
4. **الـ structure:** "Could you build a level up game in this structure?" + الـ output بتاع الـ slides.
5. **إضافة قيد:** "لازم تكون 3D وthird-person camera". **النتيجة:** sapling بيمتص الماء والمغذيات من التربة وأشعة الشمس، وبيكبر وبيمتص نباتات أقل منه في المستوى.
6. **التقييم:**
   - Screen composition: أحيانًا positions عشوائية، والتكرار بيحلها.
   - Core mechanics: واضحة (sapling، امتصاص من الأقل منه).
   - Core loop: حركة في الـ map + امتصاص + نمو بإنك تاكل من النباتات الكبيرة.
   - **تعديل George:** بدل map runner → **platform** (بيفضله).
   - **Satisfaction:** الحركة الواقعية للـ saplings، البيئة الغنية، 3D immersive.

**الباترن:** الإطار (Structure) + القيد (3D، camera) + التغيير اللفظي = تحكم في الناتج. ولو الناتج مش كويس، **ابدأ chat جديد أو عدّل الـ prompt**، ماتكملش في نفس السلسلة.

---

## 16. Ludo AI Demo ★★

- ادخل **Attack Hole** (من Homa) وادمجها مع **plants** (نفس الـ theme).
- **Genre:** اختار Hyper Casual عشان الفكرة تبقى موجهة. **Style:** 3D أحسن نتيجة.
- **النتيجة:** plants مسلحة بالأسلحة وبتشيل كل حاجة، وده "fresh" وغير متوقع.
- **الميزة:** بيطلع **صورة توضيحية مع الفكرة**، والصورة بتبيّن الشكل بسرعة (وده بيساعد في الـ brainstorm والـ pitch).
- **الدرس:** Ludo بيعطي **out-of-the-box** وغير متوقعة أكتر، بس مش بتتكلم معاه بالتفاعل.

---

## 17. الذكاء الاصطناعي والـ solo devs (مستقبل) ★

- الـ AI هيبقى **أسهل وأكثر intuitive** (prompts أبسط، control أكتر على الصور).
- **Solo devs:** الـ ideation والـ art والـ sound والـ coding ممكن ينخفض جهدهم جدًا. ممكن يزيد عدد الـ prototypes، حتى لو الجودة مختلفة.
- **Unity + ChatGPT:** George شاف أمثلة إن الـ coding ممكن يتعمل بالـ prompts.

---

## 18. Q&A: هل الـ Hyper Casual مشبّع في 2023؟ ★★

- **الإجابة (كيفين):** نعم فيه oversaturation، خصوصًا آخر 18 شهر. بقى أصعب بكتير.
- **بس:** Hyper Casual "موجود من أول الـ App Store"، ولسه فيه appetite للـ snackable games.
- **القاعدة:** لو عملت نفس الحاجة اللي اتعملت قبل كده، **هتفشل**. المطلوب فكرة جديدة + تطبيق الأساسيات.
- **مثال:** **Attack Hole** (Homa) اكتسحت الشارت طول السنة: **دمج فكرتين قديمتين مع twist جديد**.

---

## 19. الـ Takeaways النهائية (George) ★★★

1. **الـ wording مهم جدًا:** كن محدد ودقيق في الطلب، و**بسيط** في الأسلوب.
2. **استخدم الـ AI كمصدر للـ themes وتقاطعات الـ themes والـ genres**، مش كمصدر للفكرة النهائية.
3. **ماتتخلاش عن الـ market research** (أول مرحلة في الـ slides) — دي اللي بتتأكد إن الفكرة اتثبتت في السوق.
4. **الـ brainstorm هو المكان اللي الحاجة الحلوة بتتولد**: اعمل homework في الـ AI وربطه بالـ market research.

---

## 20. الدروس اللي البث بيقولها بين السطور ★★

- **الـ Pipeline = Filter:** prototype رخيص + قياس صارم = قرار سريع، ومفيش وقت ضايع على أفكار ميتة.
- **الباترن الكبير:** القرار مبني على **أرقام مش حدس** (Cumulative play time × CPI)، والـ AI بيوسع **مساحة الأفكار** بس الحكم بيفضل للداتا والبشر.
- **الـ twist > الـ clone:** النجاح في السوق المشبع = دمج + twist، مش نسخ.

---

## **للاستوديو:**

**(1) تطبيق على Mossfolk (اللعبة الحالية):**
- **Cumulative Play Time × CPI matrix:** لو Mossfolk هتتجرب كـ prototype لأي شبكة إعلانات، حط البلاي تايم اليومي للـ 4 أيام الأولى مع الـ CPI، وقرر "كمّل / عدّل / ارمي" بالأرقام.
- **الـ 7 أيام محتوى (Vertical Slice):** لو 3000 ليفل بيتعمل على مراحل، اختبر أول 7 أيام كمحتوى مثبت قبل ما تكمل الباقي. ولازم **persona واضح**: مين اللي بيحب merge + physics؟ وإيه اللي بيخليه يرجع يوم 7 و30؟
- **Idle/Puzzle opportunity:** Mossfolk puzzle، وHoma بيستثمر في puzzle، يعني الـ merge puzzle مع **progression systems** (زي الـ rival contests والـ side quests) ممكن يبقى deep hybrid لو الـ D30 اتثبت.
- **الـ core loop audit بطريقة George:** الجرة والمخلوقات والـ merge. **إيه العناصر اللي ناقصة في التفاعل؟** (زي fishing line عند George: عنصر تالت بيخلق تفاعل جديد؟ مثلًا: حجم الجرة، ميزانية الإسقاطات، أو تأثير الـ mossy shells على الـ merge).
- **تيستر-البوت:** الـ bot_difficulty يتقاس بالـ cumulative play time والـ retention للبوت قبل ما يتعرض لبشر، عشان تطابق القرار ده مع الـ matrix.
- **الـ Repeat spend:** لو فيه IAP في Mossfolk (زي Hints أو boosts)، مقياس الـ repeat spend هو اللي بيحدد هل الناس بتدفع تاني.

**(2) خط إنتاج الاستوديو السريع (لعبة جديدة كل يوم/أسبوع):**
- **اختيار الأفكار (Idea Pipeline):** روتين ثابت: market research (top charts + reference check)، brainstorm من جزئين (remix + from scratch)، وvalidation يقتل الأفكار المتكررة قبل الـ prototype.
- **Prompt template موحد:** احفظ الـ structure اللي George بيستخدمه (pitch، screen composition، core mechanic، core loop، satisfaction، meta، references) واعمله template ثابت لكل فكرة جديدة. ده بيخلي الإنتاج اليومي أسرع بكتير.
- **Prototype بـ 40 دقيقة gameplay + creatives:** نفس الحجم اللي Homa بيستخدمه. كل لعبة جديدة تعدي على نفس الـ gate: play time D3 × CPI، وأي حاجة تفشل تتقتل بسرعة.
- **أنظمة قابلة لإعادة الاستخدام بين الألعاب:** الـ economy وprogression وmerge logic وtutorial system وshop واللعب بالـ save/load. كل لعبة جديدة تركّب من مكتبة systems، مش تبني من الصفر.
- **Bot tester كجزء من الـ pipeline:** قبل الـ CPI test، البوت يجرب الـ prototype ويقيس الـ difficulty curve والـ fail points، عشان تقلل الوقت اللي بيتصرف على اللاعبين الحقيقيين في الـ prototypes الفاشلة.
- **Creatives بالـ AI (Ludo/Midjourney):** الصور التوضيحية والـ thumbnails بتتعمل بسرعة بالـ AI، وبتتقاس بالـ CTR مع الـ CPI. ده بيوفر وقت في الـ prototype.
- **Market validation بالـ Top Charts:** قبل ما تبدأ أي prototype، شوف الألوان والـ genres الفايزة (زي سؤال Quanti) عشان تقلل المخاطرة.
- **Kill rule واضحة:** لو الـ prototype ماوصلش لحد معين في الـ matrix خلال أسبوع، يتقتل ومايتعدّلش كتير. ده بيحافظ على سرعة الإنتاج.
- **الـ Studio hub:** بدل ما تبني فريق كبير، حافظ على الفكرة الأساسية لـ Homa: **فرق صغيرة للـ prototypes، وفريق أكبر للـ deep games اللي تجتاز الماتريكس**.