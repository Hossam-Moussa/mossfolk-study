```markdown
---
name: adams-fundamentals
description: >
  قواعد تشغيلية من Ernest Adams — Fundamentals of Game Design (3rd Ed., 2014):
  player-centric design (Ch.4 كامل: 5+1 domains، demographics، أطفال/بنات، gamer dedication،
  binary thinking)، وخريطة مرجعية بأرقام الصفحات للـ genres والـ gameplay/challenges والـ UI
  والـ balancing والـ level design. استخدمها في: idea intake قبل أي بروتوتايب، art/ad review،
  قراءة نتايج الـ CPI test، audit دوري لـ Mossfolk، وتصميم تقارير التيستر-بوت.
---
```

# adams-fundamentals — SKILL.md

## 0. اقرا ده الأول: حدود التغطية (مهم قبل ما تنفذ أي حاجة)

| الجزء | الحالة | ينفع تنفذ منه؟ |
|---|---|---|
| Front matter + Introduction | متذاكر من المتن | أيوه (سياق ومنهج) |
| **Ch.4 Understanding Your Player (p.81–102)** | **متذاكر كامل من المتن** | **أيوه: قواعد وجداول وتشيك ليستات كاملة** |
| Genres (Ch.3)، Gameplay/Challenges (Ch.13)، Core Mechanics (Ch.14)، Balancing (Ch.15)، Level Design (Ch.16)، UI (Ch.12)، الباقي | **Index بس**: أسماء مفاهيم + أرقام صفحات، من غير شرح | **كتصنيف وخريطة سحب فقط.** ممنوع تتعامل مع التعريفات على إنها من آدمز لحد ما المتن يتسحب |

**علامات المستند:**
- ★★★ = بيخدم خط الإنتاج (لعبة جديدة كل يوم/أسبوع): اختيار أفكار، بروتوتايب، CPI، تيستر، إعلانات.
- **[index]** = المفهوم والصفحة موجودين في الـ Index، والشرح لسه ما اتقراش.
- **[استنتاج]** = امتداد من النوتس للاستوديو، مش نص آدمز.
- **[خارج المصدر]** = معرفة عامة مش من النوتس.

> **قاعدة صفر:** لما سؤال يخص balance أو UI أو level design، ارجع لقسم 7 (قائمة السحب) واطلب الصفحات قبل ما تحكم. ما تألّفش تعريف وتنسبه لآدمز.

---

## 1. تعارضات بين المصادر (متسمّية)

المصادر: **N1** = `adams_fundamentals_notes_api.md` (جزء 1: Intro + Ch.4 + Index Numbers→I). **N2a** = نوتس الجزء 2 النسخة الأولى (Index، خريطة نطاقات). **N2b** = نوتس الجزء 2 النسخة التانية (Index من "Inspiration" لـ Z، مقسّم §A–§L).

| # | النقطة | N1 | N2a | N2b | التصرف |
|---|---|---|---|---|---|
| 1 | نطاق Core mechanics | 351–402 | 351–400 | 351–395 | خريطة فصول N1 (Ch.14) بتقول إن random numbers وbell curve جزء من Core Mechanics، فـ395–399 غالبًا آخر Ch.14. يتحسم من المتن |
| 2 | نطاق Balancing | Balance/Dominant 403–411، 413–416 | 403–436 | 395–436 (حاطط الـ random numbers جوّه) | اعتمد 403–436 للـ Balancing، و395–399 كـ"على الحدود" |
| 3 | نطاق Challenges | "فصل 13: 323–339" | Gameplay 315–347 | 315–347 | 315–347 = الفصل كله (فيه saving 343–347)، و323–339 = قلب التحديات |
| 4 | Internal economy | 366–374 | 352، 366–372 + static equilibrium 373–374 | زي N2a | نفس المحتوى، تقسيم مختلف |
| 5 | Representative player | — | 32–33، 47، 81–83 | 32–33، 47، 520 | اسحب الاتنين (81–83 و520) |
| 6 | اسم نوع الصعوبة المقابل لـ perceived | "Absolute difficulty" (322–324، 329، 420–425)؛ وخريطة Ch.13: skill/stress/absolute | — | "Perceived vs **relative** difficulty (420–425)" | المصطلحين محتاجين تعريف من 420–425 |
| 7 | الـ domains في الـ Index | المتن فيه الخمسة كاملين | — | Index بيذكر Stimulation/Threat/Novelty (82) بس | مش تعارض. الـ index جزئي، والمتن (N1) هو المرجع |
| 8 | هل الجزء 1 موجود؟ | موجود | "الجزء 1 مش مرفق" | "A–H مش في السياق" | N1 موجود فعلًا. نوتس الجزء 2 اتكتبت من غيره |
| 9 | Learn-by-dying | Women: بيطفّش ← tutorial في الأول. وKiss #6: الأطفال أسعد بـ trial-and-error | 417، 441–442 | 417، 441–442 | تعارض جوه آدمز نفسه (شرائح مختلفة). الحل في R-09 |
| 10 | منحنى صعوبة Mossfolk | مش مذكور | — | بيفترض "الخط المستقيم بتاعنا في 3000 ليفل" | **افتراض N2b غير متحقق.** يتقاس من بيانات bot_difficulty قبل أي قرار |
| 11 | "مفيش طاقة تمنع اللعب" | — | — | ذكره N2b كمبدأ مرتبط بـ pay-to-win | مبدأ استوديو، مش آدمز |

---

## 2. السياق والمنهج (Front matter + Intro)

- **المؤلف:** Ernest Adams. أسس الـ IGDA سنة 1994 وكان أول رئيس لها. اشتغل 8 سنين في Electronic Arts (audio/video producer على Madden NFL)، وكان lead designer في Bullfrog Productions، وقبلها software engineer (من IBM 360 mainframe لحد دلوقتي). دكتوراه في interactive storytelling من Teesside University. بيدرّس part-time في Uppsala Campus Gotland. عنده 5 كتب تانية وعمود «Designer's Notebook» على Gamasutra.
- **الطبعة:** 3rd، سنة 2014، Pearson/New Riders. المحرر التقني Tobi Saulnier (مؤسسة 1st Playable Productions، خبرتها casual وألعاب أطفال). البحث اليومي كان على MobyGames وGiant Bomb.
- **أساس Ch.4:** بحث Jason VandenBerghe (Creative Director في Ubisoft). الشكر شمل Raph Koster وSteve Meretzky وBrian Moriarty وChris Taylor وScott Kim وCarolyn Handler Miller وJesyca Durchin، وكلهم مصادر فعلية في Ch.4.
- **سبب التحديث:** انفجار casual وF2P وmobile، وUnity كـ middleware، وأدوات فن/أنيميشن/صوت مجانية، وaccelerometers، وKinect على أعتاب جيله التاني (كان «Project Natal» في الطبعة اللي قبلها).
- **4 فصول جديدة:** 3 Genres، 4 Understanding Your Player، 5 Understanding Your Machine، 6 Making Money. فصول الـ genres القديمة اتحولت لـ e-books «Fundamentals of <genre> Design»: Shooter / Action & Arcade / Music-Dance-Exercise / Strategy / Role-Playing / Sports / Vehicle Simulation / Construction & Simulation / Adventure / **Puzzle & Casual** (الأقرب لينا).
- **مميزات الكتاب حسب آدمز:** بيغطي تجربة اللاعب كلها في لعبة تجارية كاملة مش الـ mechanics بس، ومفيهوش interviews مع مشاهير، والمساحة رايحة لنصايح عملية.
- **مش في الكتاب:** برمجة، فن، أنيميشن، موسيقى، audio engineering، كتابة، project management، budgeting، scheduling. بيشاور عليهم بس. «أعظم المصممين Renaissance men and women».
- **افتراضه:** إنك بتصمم اللعبة كلها لوحدك.
- **الـ prerequisites:** معرفة ألعاب، كتابة مختصرة وواضحة («مهارة مطلوبة تمامًا»)، جبر، probability ثانوي (الأخيرين لـ core mechanics وbalancing).
- ★★★ **Questions ≠ Exercises:** الـ Exercises للمدرّس. الـ Questions تسألها لنفسك عن لعبتك، و«الإجابة عليها هي جوهر تصميم الألعاب». **دي أساس الـ idea intake (Checklist C1).**

**خريطة الفصول:** 1 Games & Video Games · 2 Designing & Developing (core mechanics + UI + storytelling engine، **gameplay mode**، مراحل، documents، أدوار، player-centric) · 3 Major Genres · 4 Understanding Your Player · 5 Machine (consoles/PC/portable) · 6 Making Money (direct/indirect: freemium، ad-supported، world markets) · 7 Game Concepts · 8 Game Worlds · 9 Creative & Expressive Play · 10 Character Development · 11 Storytelling · 12 User Experience · 13 Gameplay (hierarchy of challenges، skill/stress/absolute difficulty، save) · 14 Core Mechanics (5 أنواع: physics، economics، tactical maneuvering، progression، social + internal economy + random numbers/bell curve) · 15 Balancing (dominant strategies، chance، PvP/PvE fairness، difficulty، positive feedback، design to make tuning easy) · 16 Level Design · 17 Online Gaming.

---

## 3. القواعد التشغيلية — Player-Centric (من المتن، Ch.4)

### R-01 ★★★ فهم اللاعب كفرد، مش كسوق
الـ player-centric approach «يتطلب فوق كل حاجة» إنك تفهم اللاعب كفرد له علاقة عاطفية باللعبة (وبيك). **تحذير آدمز:** «بنفتكر إننا عارفين اللاعبين عايزين إيه، وأغلب المعرفة دي حدسية ومبنية على اللي إحنا عايزينه كلاعبين».
**التنفيذ:** كل قرار تصميم يتختبر على **representative player** مكتوب (Index: 32–33، 47، 81–83 / 520)، مش على ذوق الفريق.

### R-02 ★★★ حدّد الـ domains قبل أي بروتوتايب
فرضية VandenBerghe (GDC 2012، «The 5 Domains of Play: Applying Psychology's Big 5 Motivation Domains to Games»): بنلعب عشان نشبع **نفس دوافع الحياة الحقيقية، خصوصًا اللي ما نقدرش نشبعها فيها**. اللعب منفذ.
- الأساس: Five Factor Model (Big Five = OCEAN). «بعد آلاف الـ surveys ثابت بشكل ملحوظ عبر الأعمار والثقافات».
- كل domain ليه 6 facets، يعني 30 إجمالًا. Threat = tension, provocation, gloom, humiliation, addiction, danger. الـ slides: darklorde.com/2012/03/the-5-domains-of-play-slides. مرجع إضافي: *Personality Traits* (Gerald Matthews وآخرين، 2009).
- **الـ domains continuums مش on/off، والمزاج بيتغير** (ساعات action عالي الطاقة وساعات adventure أبطأ). الـ domain مش هوية دائمة للاعب.
- آدمز وVandenBerghe: المصمم بيحدد «إزاي هنسلي الناس: إيه التجارب اللي لعبتنا هتقدمها».

**جدول قرار D1 — الـ Domains (5 + السادس بتاع آدمز):**

| Domain | Trait (OCEAN) | اللاعب العالي عايز | اللاعب الواطي عايز |
|---|---|---|---|
| **Novelty** | Openness | تنوع، عناصر غير متوقعة | **familiarity** = تشابه مريح (*Words with Friends* بدل sci-fi extravaganza بقواعد غريبة) |
| **Challenge** | Conscientiousness (effort + control) | صعوبة ودقة، يعمل كل حاجة ويكمّل اللعبة | **sandbox**، حرية من غير إنجاز مطلوب |
| **Stimulation** | Extraversion (social engagement) | party games، تفاعل مع لاعبين | لعب فردي، هو «الشخص الحقيقي الوحيد» في العالم |
| **Harmony** | Agreeableness | تعاوني (*Little Big Planet*) | تنافسي بحت/conflict (*Street Fighter*) |
| **Threat** | Neuroticism | **عكس المتوقع:** اللي عنده ميل لمشاعر سلبية بيدوّر عليها (survival horror) | — |
| **Storytelling** (إضافة آدمز) | — | المحب المتطرف: الـ story سبب اللعب، وممكن يستخدم cheats وwalkthroughs عشان يشوف الأحداث | المعادي: بيكره cut-scenes، اللعبة system of rules، الـ NPCs رموز، وعايز tactical/strategic immersion. الـ sports games بتكسب قليل جدًا من الـ story |

- **الأغلبية في الـ storytelling:** «بعض الـ storytelling طالما متسقة مع الـ gameplay ومش بتبطّأ اللاعب»، وأقلها framing narrative (مين البطل، بيعمل إيه، وليه). **القرار:** شغف / كره تام / «رشة»، وبعدها روح Ch.11.
- **تنبيه:** Harmony هنا = social harmony. مش «harmony» بتاعة Ch.1 (كل أجزاء اللعبة جزء من كل متماسك).

### R-03 ★★★ «Women Are a Market, Not a Genre»
ما تصممش «لعبة للنساء» بإضافة features من الـ generalities. صمم لعبة **ممتعة جوهريًا** وراقب تأثير قراراتك على جمهورك. والاستثناءات كتير: لاعبات يشترين console games غالية، وآباء ليهم وقت لـ puzzle رخيصة مرتين في اليوم.
**الغرض:** تعرف هل لعبتك هتجذب أو تطفّش كتير من النساء أو الرجال، مش تعمل لعبة «لهن» أو «لهم».

**أرقام (أمريكا، ESA 2013):** ★★★ نساء بالغات **31%** أكبر من مراهقين ذكور **19%** من اللاعبين. Holly Devor (*Gender Blending*، 1989): حتى **50%** من النساء المغايرات وصفن نفسهن tomboys في الطفولة، فالاهتمامات متداخلة جدًا. الخطأ الشائع إنك تعامل الجنسين «كأنواع مختلفة».

### R-04 ★★★ تجنّب المحتوى المنفّر بدل ما تبني محتوى مخصوص
Sheri Graner Ray (*Gender Inclusive Game Design*، 2003): مش لازم fashion/shopping عشان النساء، ولا monster truck rallies عشان الرجال. **القاعدة: تجنب اللي يطفّش.**
**أكبر 4 turnoffs للنساء:** (1) شخصيات hypersexualized. (2) لعب متكرر ممل. (3) لعب بلا هدف ذي معنى، و«مجرد أعلى سكور مش كفاية». (4) الطبيعة الانفرادية للـ single-player (مفيش حاجة تتعمل فيها، بس خد بالك).
- بطلات زي Lara Croft وJade (*Beyond Good and Evil*) قابلهم backlash صاخب من أقلية رجال. آدمز: **تجاهلهم**. لو اللعبة كويسة هيلعبوها.

### R-05 ★★ Generalities الجنسين (غربية فقط، ممكن ما تنطبقش في اليابان/الصين/كوريا/الهند)

**جدول D2:**

| المحور | رجال (متوسط) | نساء (متوسط) | القرار التصميمي |
|---|---|---|---|
| التعلم | بيترموا في المية | عايزين يعرفوا المتوقع قبل البداية. learn-by-dying (أركيد قديم وموبايل كتير) مش محبوب | tutorial levels في الأول |
| المخاطرة | بيجربوا حتى لو خسروا | consolidate وبيحافظوا على المكسب حتى لو الخطر يجيب أكتر | ما تعاقبش الفشل بقسوة |
| ناس vs أشياء | — | تواصل اجتماعي ضمن اللعب (سبب نجاح online)؛ ألعاب Facebook (دعوة، مشاركة موارد، مقارنة إنجازات) حتى من غير multiplayer حقيقي | social layer خفيف |
| العنف | fighting/war/shooters | عنف **بمبرر/سياق**، وlateral thinking بدل brute-force. RPGs ناجحة لأن الـ combat ليه غرض في هدف أكبر | اربط أي صراع بهدف |
| التحدي الذهني | — | تحديات ذهنية وحلول أنيقة (شعبية الـ puzzle) | — |
| Avatar | **puppet** يتحكموا فيه عشان يكسبوا (ممكن يضيعوا وقت في تعديل RPG لأن ده الـ point) | تماهي و**self-expression** | customization |
| وقت وفلوس | leisure وفلوس أكتر، بيدفعوا $60 يوم الإصدار، blocks طويلة | casual شعبي لأنه من غير مخاطرة مقدمًا ودفع صغير على دفعات. وقت **مجزّأ**: **30 دقيقة لساعتين أكتر من 5 ساعات متواصلة** (نفس إجمالي الأسبوع في قطع أصغر) | **مسافة قصيرة بين نقاط الـ save**، والتوقف في أي نقطة من غير فقد (زي ألعاب social network) |

(ملحوظة آدمز: النساء في الواقع بيشيلوا جزء كبير من مسؤولية نسيج المجتمع، والـ social networks وألعاب الأونلاين بقت جزء من ده.)

### R-06 ★★ الـ Avatar والجنس
- **Lara Croft** أثبتت إن الرجال بيلعبوا بـ avatar أنثى **طالما بتعمل أدوار مرتاحين معاها** (مغامرات «ذكورية تقليديًا»)، مش أنشطة «أنثوية» تقليديًا.
- النساء مش مهتمين بـ male-fantasy characters زي **Rayne (BloodRayne)**. **Heather (Silent Hill 3)** أحسن: «شكلها زي إنسانة حقيقية مش إعلان lingerie ماشي».
- الرجال بياخدوا الـ default ويجروا. النساء بيشوفوه امتداد لهم. **أحسن رافعة لجذب النساء: customize** (ملابس، إكسسوارات، أسلحة). الـ RPGs (خصوصًا online) أقوى في ده.
- **اختيار ذكر/أنثى: «المرأة مش رجل بجسم مختلف».** اكتب الحوار من جديد. (tip: صفحات Facebook/Pinterest «Heroic Women to Inspire Game Designers».)

### R-07 ★★ الأطفال: الفئة العمرية بتغيّر التصميم
الفئات: Preschool/kindergarten **3–6** · Early elementary **5–8** · Upper elementary/tweens **7–12** · Teens **13+** · Late teens لحد mid-20s («مخهم لسه بيتطور»). Piaget وMontessori: غلط تشوف الأطفال «كبار صغيرين». **الغرب:** الطفل بيطمح لعالم الكبار، فاعرض شخصيات **أكبر** منه. **عكسه في اليابان.**

**جدول D3 — 9 اعتبارات:**

| # | الاعتبار | القاعدة |
|---|---|---|
| 1 | Hand-eye coordination | ضعيفة في الأول، ذروتها في المراهقة وأوائل العشرينات، وتقل بعدها |
| 2 | Logic | ذروتها **6–7 سنين**. للأصغر: عدة مستويات صعوبة (تتأكد بـ playtest)، وعناصر أقل وسلسلة تفكير أقصر |
| 3 | Systematic thinking | بيبدأ **12–14**. ما تضيفش أنظمة معقدة قبلها |
| 4 | Goals | moment-to-moment، feedback أكتر تكرارًا، من غير «Good job!» سكرية كل مرة |
| 5 | Visual | UI بسيط ومركز، **deep rather than broad** |
| 6 | اللغة | من غير تعالي، جمل قصيرة (*The Little Prince*) |
| 7 | التجريب | طاقة لا نهائية، فصمم عالم **يكافئ الاستكشاف** |
| 8 | القراءة | محدودة، فاستخدم **voiceover** للمهم |
| 9 | المحتوى | كتير منه = اللي الأهل عايزينه. الجنس والمال العالي مش في عالمهم. *Harry Potter* المبكر: الاغتراب، سوء فهم الأسرة، إمكانية كامنة، والأكل. **اقرا الأدب الشعبي لنفس السن** |

### R-08 ★★★ Seven Kisses of Death (Carolyn Handler Miller، *Digital Storytelling* 2nd Ed. 2008)
كلهم = الكبار بيسقطوا رغباتهم على الطفل. المرجع الصح هو ملاحظة الطفل نفسه وplaytest. → **Checklist C3.**

### R-09 ★★★ حل تعارض learn-by-dying
آدمز (شريحة النساء): وضّح المتوقع قبل الفشل. Miller (Kiss #6): الأطفال عايزين يلعبوا على طول وtrial-and-error. **الحل المقترح في N1:** tutorial **تفاعلي قصير جدًا**، صفر talking heads، والمتوقع بيتوضح بالفعل مش بالكلام. (N1 بتنسب نفس الخلاصة لـ Extra Credits في exemplar، **[خارج المصدر]** بالنسبة لآدمز.)

### R-10 ★★ ألعاب البنات: meaning + control + beauty + collection
- **الفجوة بين الأولاد والبنات أوسع من الرجال والنساء**، وفي سن معين بيرفضوا رموز الجنس الآخر.
- **Catch-22 تاريخي:** «البنات مش بيلعبوا» ← مفيش ألعاب ← مفيش لعب. البحث أثبت إنها stereotype. منتصف التسعينات اتكشف سوق غير مستغل، لكن أغلب المحاولات كانت رديئة جرافيك وقيمة. «البنات عايزات ويستاهلوا ألعاب كويسة».
- **أواخر الألفينات:** Ubisoft Imagine (بعد *Imagine: Fashion Designer*)، ونجاحات Barbie وBratz وNancy Drew.
- **الجمهور بنات مش نساء**، والنساء أكتر تنوعًا.
- **Mattel:** افحص اللي البنات بيشتروه ويقروه ويتفرجوا عليه. Barbie = formula مجربة + **core age 4–8**، وبعدها مفيش one-size-fits-all. «لا أجندة اجتماعية ولا political correctness». Mattel بقت بترخص الـ brands وما بتنشرش بنفسها.
- **Jesyca Durchin** (Nena Media، كانت executive producer في Mattel؛ GDC 2000):
  - البنات أكتر تفتتًا ويتغيروا أسرع، واحتياجات مختلفة **تقريبًا كل سنة بين 4 و14**.
  - ابنِ على **Proven Play Patterns (7):** Fashion · Glamour · Nurture · Action/twitch · Collection · Adventure · Communication/social. إعادة إنتاج الحياة اليومية. «متخافش من اللعب المفتوح».
  - ★★ **Girls like stuff:** جمع وعرض وحمل. «لازم تحس إن فيه سبب تلعب». **الجمع بيحل محل السكور** («جمع كل أنواع الأصداف أمتع من سكور عالي مجرد»).
  - **Environments:** reality-based، جميلة أو منطقية مع القصة، **symmetry + color coherency**. مش لازم كلها pink/purple، بس لازم إحساس «مكان آخر».
  - ★★ **Sensual interface:** ملونة، مدفوعة بالصوت، «brrrring factor». **ما تديش صف أزرار رمادية متطابقة.**
  - الـ branding وامتداد لعب/ميديا موجودة: **مضاعف في سوق البنات**.
  - «ما تتكسفش من شغلك». لو محرج من «hair play» أو «relationship games» ما تعملوش.
- **Spooky ≠ Scary (Durchin):** spooky = إمكانية الانزعاج (بيت مهجور، ملاهي بالليل). scary = إمكانية الأذى/الموت (شارع مظلم وقاتل طليق).
- **TIP — Puzzle Quest (DS):** avatar ذكر/أنثى، الـ combat متصوّر كـ puzzle، ولما تخسر الـ avatar **بيهرب مش بيموت**.
- **Double standard:** فيه مطورين بيرفضوا ألعاب الشعر/الملابس لأنها بتكرس stereotype. آدمز: ألعاب أكتر بكتير بتكرس stereotype أسوأ للذكورة (عنيف، طماع، شهواني، monomaniacal).

### R-11 ★★★ Gamer Dedication = continuum مش core/casual
المصدر: Barry Ip + Adams، «From Casual to Core: A Statistical Mechanism for Studying Gamer Dedication» (2002)، وجزء من Scott Kim (GDC 2001، «Designing Web Games that Make Business Sense»). المصطلحين core/casual فقدوا معناهم مع ألعاب الـ social networks.
- **القاعدة:** لو صممت لطرف واحد «غالبًا مش هتبيع كتير للطرف التاني». والجسر هو **difficulty modes**:
  - **GoldenEye:** الـ core على أعلى difficulty يقلل 15 ثانية من وقت المهمة، والـ casual على أسهل مستوى يتسلى بالـ smooth controls والتفاصيل البصرية.
  - **Rock Band** مثال تاني.
- كمصمم، محتاج تعرف إزاي الـ dedication بيظهر (مش القياس البحثي). مثال: الـ dedicated بيدوّر على معلومات اللعبة وهي في التطوير، فـ developer blogs وpress releases بتوصله.

**الـ 15 صفة (Checklist C4).**

### R-12 ★★★ Inclusiveness, not Universality + ما تفكرش binary
- **Binary thinking** = «لو A بتحب حاجة، اللي برّاها مش هيحبها». غلط وبيخسّرك عملاء.
- **Figure 4.3 (افتراضي):** مقياس 0–10. متوسط الرجال ≈ **5.5** والنساء ≈ **4.5**، لكن عدد النساء عند 6 ≈ **ثلثين** عدد الرجال، يعني ≈ **2/5** من اللي جاوبوا 6 نساء. «كتير جدًا لتتجاهله». تتجاهل أو **تنفّر** أقلية من غير ما تعرف حجمها = **بتحرق فلوس**.
- **الاستثناء:** أحيانًا التداخل صغير (لعبة لـ 5 سنين مش هتجذب 15 سنة). وDisney بتحط محتوى للكبار فتوسّع الجاذبية.
- **Hodgepodge ممنوع:** kung fu + chess + Monopoly = «فوضى ما تجذب حد». «too many features and no harmony».
- **الصح:** story line في fighting game **من غير ما تتدخل في الـ gameplay** (Heavenly Sword، God of War).
- **Design Rule: Keep Exclusionary Material Out of Your Game.** «أفضل لعبة ممكنة عن موضوعك مع تجنب exclusionary material».

---

## 4. Genres — خريطة [index + Intro]

| Genre | صفحة (N2a) | e-book |
|---|---|---|
| Shooters | 69–70 | Shooter |
| Action | 71–72 | Action & Arcade |
| Strategy | 72–73 | Strategy |
| RPG | 73–74 | Role-Playing |
| Sports | 74–75 | Sports |
| Vehicle sims | 75–76 | Vehicle Simulation |
| Construction/management | 76–77 | Construction & Simulation |
| Adventure | 77 | Adventure |
| **Puzzle** | **78** | **Puzzle & Casual** |
| (Music/Dance/Exercise) | — | Music-Dance-Exercise |

- Genre-specific level design: 443–445 (shooter، RPG، puzzle، simulation، sports، vehicle، strategy).
- **من المتن (Ch.4):** fighting/war/shooters أشهر عند الرجال، وRPGs ناجحة عند النساء رغم الـ combat، والـ puzzle شعبي عند النساء، وsports بتكسب قليل من الـ story.
- **Studio:** «Puzzle & Casual» (ص 78 + 443–445) أول صفحات تتسحب من الـ genres.

---

## 5. Gameplay Modes + Challenges — [index]

**Gameplay mode:** خريطة الفصول (N1) بتقول إن Ch.2 بيعرّفه، والتعريف نفسه مش في النوتس. **[خارج المصدر]** آدمز بيعرّف الـ gameplay mode كتركيبة: الـ gameplay المتاح في اللحظة (challenges + actions) + **camera model/perspective** + **interaction model**. يتأكد من Ch.2.
مكوناته في الـ index: Interaction models (39، 269–270): Avatar-based، Multipresent (303–304)، Omnipresent (270)، Party-based (237، 303–304). Perspectives (272–279): first-person، third-person، aerial، isometric (143، 276–277)، top-down (276)، side-scrolling (279)، top-scrolling، context-sensitive (278). Camera (271): pan، tilt، roll، truck.

**Challenges (315–347):** Victory condition (317–319) · Atomic challenges (simultaneous 319–321) · Intermediate (318) · Tutorial levels بتقابل الـ atomic challenges (317) · Information about challenges (317) · Intrinsic skill/stress/time pressure (321–323).

**جدول D4 ★★★ — تصنيف التحديات (فلتر تنويع، أسماء من الـ index):**

| النوع | صفحات |
|---|---|
| Physical coordination: speed/reaction · precision/accuracy · rhythm/timing | 17، 324–326 (324، 324–325، 325) |
| Time pressure / races | 17، 322–323، 325، 328–329 |
| Logical/Mathematical · formal logic | 89، 326–328 |
| Lateral thinking | 338–339 |
| Memory | 17، 329 |
| Pattern recognition | 17، 330 |
| Spatial awareness | 330–331 |
| Exploration: mazes، traps، locked doors، unmarked switches، teleporters (332)، hidden objects (332–333) | 331–333 |
| Strategic/tactical: perfect information، pure strategy، situational analysis | 334 |
| Logistics · reducing enemy forces · survival · stealth learning | 335 (survival 378، stealth 27) |

**Actions (340–343):** participation، self-expression، social، sightseeing (342)، unstructured play (342). **Saving (343–347):** level access codes (344)، save يأثر على القصة (344)، quick-save، save slot (345).

**Studio [استنتاج]:** صنّف كل فكرة جديدة بالجدول. لو آخر 5 ألعاب «precision + time»، الفكرة السادسة تبقى من نوع تاني. Mossfolk = spatial + precision (الإسقاط) + planning. تحديات 2501+ (shells/stones/rot) لازم تضيف **نوع** جديد مش رقم أصعب بس.

---

## 6. UI — [index] + قواعد من Ch.4

**من المتن:** البنات عايزين sensual interface و«brrrring factor» من غير صفوف أزرار رمادية (Durchin). الأطفال عايزين UI deep not broad وvoiceover (R-07).
**مواضع الـ index:**
- مبادئ (257–262): short-term memory، shortcuts، physical stress (258)، معلومات اللاعب (objects/NPCs/numbers/orders/options 261–262)، risk/reward وprogression (260). الـ UI وسيط بين الـ core mechanics واللاعب (37).
- Process (263–266): **PowerPoint prototype (264)**، screen layout (265، و265 للموبايل)، mapping input (266)، shell menus (44، 266، 309).
- Complexity (267–269): simplification، menus.
- Visual (280–287): overlays/transparency (280–281)، indicators (symbolic 282–283، numeric 282، 284–285)، tooltips (283)، mini-maps (284)، screen buttons (285)، fonts serif/sans/mono (286–287).
- Audio (287–290): positional (288)، **pitch variation للأصوات المتكررة (288)**، rumble (288، 306)، music (289)، voiceover وتكرار (290)، و«rview of 290–291».
- Input (290–299): 0D، 1D (297–299)، 2D (294–296)، 3D (292–294)؛ Wii Remote (292–294)، Nunchuck/Motion Plus (293)، Kinect (298–299)، touch/joystick/trackball (295–296)، pressure-sensitive (298)، smartphones (298).
- Navigation (300–304): screen-oriented (300–301)، avatar-oriented (301–302)، point-and-click (139، 303–304)، pathfinding (303)، waypoints (304).
- Accessibility (304–308) وCustomization/Restore defaults (308–309): انظر C6.

---

## 7. Balancing / Core Mechanics / Level Design — [index] + قائمة السحب

### 7.1 Balancing (403–436)
- PvE vs PvP balancing (404–405). Dominant strategy: PvP (406–410)، PvE (410–411)، **testing for dominant strategies (411)**.
- Transitive (405–407)، Intransitive/RPS/Rochambeau (408–409)، Orthogonal unit differentiation (409)، Shadow costs (407، 409). **[خارج المصدر]** shadow cost = تكلفة مخفية مش ظاهرة في التسعير.
- Fairness (412–417): symmetric (413–414)، point assignment (414–415)، PvE fairness (416–417)، learn-by-dying (417، 441–442).
- Difficulty: skill (404، 419)، native talent وprevious experience (419–422)، **power provided (420–423)**، **perceived difficulty (420–425، 452)**، consistent range of difficulty (405، 418، 425)، **Sawtooth progression (424)**، multiplayer difficulty modes (425)، DDA (418–428)، speed (307، 423).
- Feedback: **Positive (404، 429–433)**، Negative (432–433)، Stalemates (404–405، 417، 430؛ مثال shot clock في السلة 405)، Stagnation (433–434)، Avoid trivialities (434)، Runaway profit (369).
- Tuning stage (54، 435–436)، Pseudo-random (396–398، 436)، Monte Carlo (396–397)، Gaussian/Uniform/Nonuniform (395–399؛ 397–398). وكمان Powerup (411) وWildcard enemy.

### 7.2 Core Mechanics (351–395/402، انظر التعارض #1)
Physics as mechanics (352) · events/processes (354، 362) · conditions (364) · entities: simple (359)، unique (361)، numeric/symbolic (364) · Resources vs entities (358–359) · numeric vs symbolic relationships (364–366) · **Internal economy (352، 366–372):** source (367)، drain (367–368)، production rate (367)، production mechanism (369)، trader (368–369)، converting (368)، tangible/intangible (369–370)، mutual dependency/feedback/deadlock (370–371) · Machinations (372) · Static equilibrium (373–374) · Progression (353، 375–378): one-way door (234، 375)، locked doors (331، 375)، reversing time/pause (376)، tracking (376–377)، triggers (377) · Tactical maneuvering (352، 378–383) · Social (352، 383–386) · Simplicity (389)، Generalizing (389–390) · **Test every mechanic (395)** · Turn-based vs real-time (355–356)، detecting termination (355)، علاقة بالـ level design (356–357).

### 7.3 Level Design (439–470)
Universal (441–442): pace، risk/reward، resources، learn-by-dying، tutorial · Layouts (445–449): linear (445–446)، open (445)، parallel (446–447)، network (447–448)، ring (447) · Atmosphere (450–451) · Progression (451–453، 467–468) · Pacing (453–455) · Tutorial levels (455–457) · **Process (457–465):** planning (459–462: landmarks، save/spawn points، resources 460، performance 461) ← prototype (462–464) ← **level review (463)** ← **lock-down (464)** ← testing (465) · Pitfalls (465–468): scope (465–466)، conceptual non sequiturs (466–467)، **Twinkie Denial Conditions (468)** · Level designer (55، 439–440، 458).

### 7.4 ★★★ قائمة السحب بالأولوية
1. **Balancing 395/403–436**، وجواها 419–425 و429–434 أولًا.
2. Core mechanics 351–395/402.
3. Challenges 315–347.
4. Level design 439–470.
5. UI/accessibility 255–312.
6. Money 113–124 (freemium 118–119، IAP 111/118، F2P 111/119، crippleware 118، DLC 118، advertising 119–120، pay-to-win 118، sponsored games 120، world markets 120–123: Islamic 123، Mexico 123).
7. الباقي.

**مصطلحات ممنوع تستخدمها كقاعدة قبل تعريفها من الصفحة:** Twinkie Denial Conditions (468)، Shadow costs (407/409)، Orthogonal unit differentiation (409)، Learn-by-dying (417/441–442)، Sawtooth (424)، Perceived/Absolute/Relative difficulty (420–425).

---

## 8. التشيك ليستات

### C1 ★★★ Idea Intake (إجباري قبل أي بروتوتايب؛ نص صفحة و10 دقايق)
- [ ] **Q1 Domains:** أنهي من الستة (Novelty/Challenge/Stimulation/Harmony/Threat/Storytelling) وبأي شدة (continuum)؟ وده بيقول إيه عن الجمهور؟
- [ ] **Q2 Age:** الفئة العمرية (بتأثر على التحديات والـ UI والـ pacing والجماليات). لو أطفال، يبقى C3.
- [ ] **Q3 Gender:** inclusive ولا مستهدف؟ لو مستهدف: إيه المحتوى/الـ features اللي بتجذب جمهورك تحديدًا؟ وإيه اللي هيقل عند التاني؟
- [ ] **Q4 Dedication:** النقطة على الـ continuum، وأنهي من الـ 15 صفة متوقعة، وإزاي هتلبّيها؟ (مثال: جلسات طويلة بتستبعد اللي مالهمش وقت.)
- [ ] Representative player مكتوب في سطر.
- [ ] أنهي من الـ 7 play patterns وأنهي من الـ Five Cs الفكرة بتخدم؟
- [ ] نوع التحدي (D4)، ومش متكرر مع آخر الألعاب. **[استنتاج]**
- [ ] تعارضات بانت؟ (مثال: «hyper-casual بس session طويلة».)
- [ ] تحذير: Threat عالي مع جمهور puzzle/casual = علم أحمر مبكر.

### C2 ★★★ Exclusionary-Material Gate (art review + ad creative)
- [ ] hypersexualized؟
- [ ] تكرار ممل؟
- [ ] مفيش هدف ذو معنى (سكور بس)؟
- [ ] gore/دم يخلّي الآباء ما يشتروش؟
- [ ] محتوى عنصري؟
- [ ] فن قبيح (النساء أحساس أكتر للجماليات وبيشتروا أقل)؟
- [ ] narrative إجباري في genre مش متوقع فيه؟
- [ ] عنف عرضي/سادي/gory زيادة = brutality؟ (مقبول: دفاعي، مُستفَز، cartoony — Elling.)
- [ ] spooky مش scary؟
- [ ] **الإعلان نفسه** (thumbnail) مش بيطفّش segment قبل التحميل؟ **[استنتاج من N1]**
- [ ] قراءة **بشرية**. التيستر-بوت ما بيقيسش ده.

### C3 Kids Gate — Seven Kisses of Death
- [ ] (1) «بيحبوا أي حاجة حلوة»؟ لأ: كرتونات Warner Bros (Bugs Bunny الساخر، Sylvester وTweety، Wile E. Coyote وRoadrunner، Yosemite Sam، Elmer Fudd) مفيهاش حاجة «حلوة»، وفيها عبرة إن العنف بيرتد على العنيف.
- [ ] (2) «إديهم اللي كويس ليهم»؟ لأ: «جرعة propaganda مع كل كتاب؟» لما يريحوا مش عايزين دواء.
- [ ] (3) «سلّيهم بأي حاجة»؟ لأ: ما بيفرّقوش التمثيل الكويس من الرديء ولا بيميّزوا الـ clichés، بس مش هيتحملوا أي حاجة. Disney multilayered، والمحتوى ذو المعنى بيمسك أطول.
- [ ] (4) «العب safe»؟ لأ: Dumbo بيتفصل عن أمه، Snow White بتهرب في الغابة، أبو Simba بيموت. Gerard Jones (*Killing Monsters*، 2002): التعامل مع التهديد جزء من النضج.
- [ ] (5) «كل الأطفال سواء»؟ لأ: مصممة لـ **6–10** والناشر عايز **8–12** = **إعادة تصميم**.
- [ ] (6) «اشرح كل حاجة»؟ لأ: trial-and-error، من غير talking heads، اختصر الـ exposition.
- [ ] (7) «شخصيات wholesome»؟ wholesome = boring. شخصيات بنقائص (Sesame Street: طماع، متجهم، مساعد).
- [ ] مراجعة الـ 9 اعتبارات (D3).

### C4 Dedication — الـ 15 صفة (dedicated)
1. Technologically savvy. 2. Latest high-end gear وملكية منصات قديمة. 3. Willingness to pay (الـ casual بيستنى الخصومات). 4. بيفضّل violent/action (Kim). 5. Depth & complexity. 6. جلسات طويلة كتير. 7. جوع للمعلومات (أخبار/previews/reviews/مقابلات/guides). 8. نقاش أونلاين. 9. بيلعب عشان يهزم/يكمّل، ومتسامح مع العيوب الجمالية. 10. **متسامح جدًا مع الإحباط** (الـ casual بيسيب الصعب). 11. منافسة (Gran Turismo lap-time، كل combos Street Fighter، سكور). 12. بدأ صغير ومنتظم (اللي بدأ متأخر نادرًا يبقى dedicated). 13. معرفة بالصناعة (تسريحات واندماجات). 14. Early adoption (midnight releases، gray-market imports). 15. Modding (من skins لـ aim-bots). الـ casual بيلعب as-is.

### C5 Five Cs — Kaye Elling (Blitz Games، Bratz؛ Animex 2006 «Inclusive Games Design»)
- [ ] **Characterization:** الـ avatar «حد بيمثلني»، من غير صفات منفّرة.
- [ ] **Context:** البيئة مش ugly/hostile.
- [ ] **Control:** اللاعب هو اللي بيتحكم. risk-and-reward بيجذب أقل، و**ما فيش عقاب قاسي للفشل** (بيقتل التجريب).
- [ ] **Customization:** Bratz: Rock Angelz = **686 قطعة**، والأكثر جاذبية منها unlockable من mini-games.
- [ ] **Creativity:** The Sims، وإظهار اللي عملته. مش خاص بالبنات (Halo 2 clan badges).
- **Misconceptions الأربعة:** «تقني فمش بيحبوه» (غلط، زي مواصفات العربيات والسواقة) · «ما بيحبوش العنف» (ما بيحبوش العنف المتواصل بلا معنى، ممل: «شفت انفجار شفتهم كلهم») · «كل حاجة سعيدة» (غلط، mystery وsuspense وdanger بمعنى) · «ما بيحبوش الخوف» (جزئيًا: spooky ≠ scary).

### C6 UI/Accessibility template — [index، التفاصيل لسه]
- [ ] Color blindness عن طريق Vischeck (305–306).
- [ ] Magnification (305) وحجم/نوع الخط (286–287).
- [ ] Subtitles (307) وvisual cues للصوت (306) والـ volume (306).
- [ ] Vibration/rumble (288، 306).
- [ ] Mobility/speed (307، 423) واللاعبين الكبار (307).
- [ ] Pitch variation للأصوات المتكررة (288).
- [ ] Customizing UI + **Restore defaults** (308–309).

### C7 Mossfolk Audit (من «للاستوديو» في N1/N2؛ كل البنود **[استنتاج]**)
- [ ] Domains: Novelty (9 أحجام + mossy shells/stones/rot من 2501) + Challenge (3000 ليفل بأهداف وميزانية) + Threat خفيف (rot/stones = tension/danger) + rival contests (conflict مش harmony). **فين الـ low-challenge/sandbox؟** (الـ side-quest minigames؟)
- [ ] Story: framing بسيط ولا مفيش؟
- [ ] أول ليفلات بتوضح المتوقع قبل الفشل؟ (R-05/R-09)
- [ ] Save/resume في نص الليفل، والليفل بيخلص في دقايق، والـ progress بيتحفظ تلقائي (30د–2س).
- [ ] Retention بعد أول فشل حسب segment (risk attitude).
- [ ] الـ 9 أحجام كـ **collection** تتعرض وتتفتح بدل أرقام. Skins للمخلوقات = customization.
- [ ] Merge feedback (صوت/لون/شكل) = brrrring.
- [ ] Rot = spooky مش gore. وضغط rot/stones بعد 2501 ما يكسرش Control.
- [ ] Vischeck على ألوان المخلوقات الـ 9، وpitch variation لصوت الدمج، وhaptic.
- [ ] الاقتصاد: source = الإسقاطات، drain = امتلاء الجرة، converter = الدمج. فيه deadlock؟ Positive feedback (merge snowball) قصاده negative (حد البرطمان/الميزانية)؟ وفيه runaway/stalemate؟
- [ ] منحنى الصعوبة: sawtooth (424) ولا شكل تاني؟ **قيسه بـ bot_difficulty** (التعارض #10).
- [ ] bot_difficulty بيفرّق بين «صعب على الـ casual» و«صعب على الـ core»؟ وفيه مسار GoldenEye (feel + visuals) للـ casual؟
- [ ] Lock-down لأهداف الليفلات قبل التعديل عشان بيانات البوت تفضل قابلة للمقارنة.
- [ ] Rival contests: asynchronous (481–482) بدل real-time؟ وممكن serial/episodic (248–251)؟
- [ ] الأسئلة الأربعة (C1) مكتوبة في ملف الـ design.

---

## 9. ★★★ قواعد خط الإنتاج (تجميع)

| # | القاعدة | الأساس |
|---|---|---|
| P1 | C1 إجباري قبل الكود | Questions = جوهر التصميم (Intro + 4.7) |
| P2 | C2 في الـ art review **وفي الإعلانات** | Keep Exclusionary Material Out (4.4) |
| P3 | **CPI بعقلية overlap:** ما تقتلش فكرة عشان الـ CPI/retention مايل لجنس/سن واحد. احسب نسبة الـ segment التاني عند نفس المستوى (التوزيع مش المتوسط) | Figure 4.3 (4.4) |
| P4 | ارفض «ضيف feature X» بعد تيست لو بتعمل hodgepodge | kung fu + chess + Monopoly (4.4) |
| P5 | Reusable systems: tutorial تفاعلي قصير، save/resume في أي نقطة، collection + customization كـ meta-layer، difficulty modes | N1 ملخص |
| P6 | Dedication point بيحدد الجلسة والمونيتايز والقنوات: casual = ads + قطع صغيرة + store listing؛ dedicated = premium/IAP + devlogs | **[استنتاج]** من صفات 3 و7 |
| P7 | أرقام الكتاب (31%/19%، ESA 2013) غربية وقديمة. **قِس segments جمهورك** | تحذير آدمز نفسه |
| P8 | Competitor research: لكل genre حلّل الـ top charts (أنواع التحديات + color palette + typefaces + screen layouts) | Exercise 3 (4.6) |
| P9 | تقرير البوت الثابت لكل لعبة قبل الـ CPI: dominant strategy، stalemate، stagnation، runaway، trivial decisions + جدول «ممكن تتكسر إزاي» في ساعة | [index] 7.1 + **[استنتاج]** |
| P10 | رسم Machinations-style صفحة واحدة: من غير source/drain/converter واضحين، الفكرة غالبًا مش هتستحمل الإيقاع | [index] 372 + **[استنتاج]** |
| P11 | بوابات مصغّرة: Plan (ساعة) ← Prototype ← Review ← Lock بأيام محددة. بتمنع scope creep (465–466) | [index] 457–465 |
| P12 | Brainstorming بالكمية (128) + treatment document قصير (58–59) + paper prototypes (49–50) + iterate (52–53) + PowerPoint UI prototype (264) | [index] |
| P13 | Model sheet (192–193) وpalette rules (194) template ثابت لكل لعبة | [index] + **[استنتاج]** |
| P14 | Tuning stage (435–436) + Monte Carlo (396–397) = نفس فكرة التيستر-بوت | [index] |

---

## 10. Anti-Patterns

1. **«عارفين اللاعب عايز إيه»** من ذوقنا كلاعبين.
2. **لعبة للنساء/للبنات** بإضافة features من الـ generalities (= genre مش market). وتعميم اللي ينطبق على النساء على البنات.
3. **«مجرد high score»** كهدف وحيد.
4. **Hodgepodge** لإرضاء الكل (too many features, no harmony).
5. **Binary thinking:** قتل فكرة بالمتوسط وتجاهل الـ overlap (≈2/5).
6. **عقاب قاسي للفشل** وlearn-by-dying من غير توضيح المتوقع، أو بالعكس talking heads للأطفال.
7. **جلسات طويلة إجبارية** ونقاط save بعيدة.
8. **أي Kiss من الـ Seven** (حلوة، تعليمية، safe، كل الأطفال سواء، شرح كل حاجة، wholesome، أي حاجة وخلاص).
9. **صف أزرار رمادية متطابقة** في لعبة بنات/أطفال.
10. **Scary بدل spooky،** وعنف عرضي/سادي/gore = brutality.
11. **«المرأة رجل بجسم مختلف»:** نفس الحوار للـ avatar الأنثى.
12. **Male-fantasy avatars** (Rayne) بدل إنسانة حقيقية (Heather).
13. **Avatar أنثى في أنشطة «أنثوية»** والمتوقع إن الرجال يرتاحوا.
14. **«ما تعملش بطلات عشان الـ backlash»:** تجاهل الأقلية الصاخبة.
15. **الإحراج من شغلك** («hair play»): يبان.
16. **إدانة ألعاب البنات بالـ stereotype** مع تجاهل stereotypes الذكورة (double standard).
17. **تصميم لطرف واحد من الـ dedication** وتوقّع بيع للطرف التاني من غير difficulty modes.
18. **أنظمة معقدة قبل 12–14** أو سلاسل منطق طويلة تحت 6–7.
19. **تعامل الـ domain كهوية دائمة** (المزاج بيتغير).
20. **تصديق أرقام 2013 الغربية** على سوقنا من غير analytics.
21. **تأليف تعريف لمفهوم في الـ index** (Twinkie Denial، shadow costs…) ونسبه لآدمز.
22. **Story بتقطع الـ gameplay** أو بتبطّأ اللاعب.

---

## 11. Exercises (4.6) — للتدريب الذاتي
1. Big Five test (outofservice.com/bigfive) ليك ولأصحابك، وقارن بالـ preferred domains، واكتب ورقة: تأكيد/نفي/غير حاسم لفرضية VandenBerghe.
2. وثّق exclusionary material في لعبة AAA شهيرة.
3. ألعاب لـ demographic محدد (بنات/أطفال صغار): وثّق أنواع التحديات (Table 1.1، Ch.1) + color palettes + typefaces + screen layouts. ★★★ (= P8)

---

## 12. Cheatsheet ختامي

```
PLAYER (Ch.4 — مُذاكَر)
 Domains: Novelty/Openness · Challenge/Conscientiousness · Stimulation/Extraversion
          Harmony/Agreeableness · Threat/Neuroticism(بيدوّر عليه!) · +Storytelling(آدمز)
          continuum · 6 facets ×5 = 30 · المزاج بيتغير
 ESA 2013 US: نساء 31% > مراهقين ذكور 19% · Devor 1989: حتى 50% tomboys
 Women = Market not Genre · 4 turnoffs: hypersexual / repetitive / no goal / solo
 وقت النساء: 30د–2س > 5س متواصلة · $60 يوم الإصدار (رجال)
 Kids: 3–6 / 5–8 / 7–12 / 13+ · logic peak 6–7 · systems 12–14 · غرب: شخصيات أكبر (اليابان عكس)
 7 Kisses (Miller 2008): cute / good-for-them / anything / safe / all-same(6–10≠8–12) / explain / wholesome
 Durchin (GDC 2000): 4–14 تتغير كل سنة · 7 patterns: Fashion Glamour Nurture Action Collection Adventure Social
          girls like stuff (collection > score) · brrrring · spooky≠scary
 Barbie core 4–8 · Elling 5Cs (Animex 2006): Character Context Control Customization Creativity · Bratz 686
 Dedication (Ip+Adams 2002، Kim GDC 2001): 15 صفة · جسر = difficulty modes (GoldenEye، Rock Band)
 Fig 4.3: 5.5 vs 4.5 · عند 6 النساء ≈2/3 الرجال ≈ 2/5 · Inclusive ≠ Universal
 Keep Exclusionary Material Out

★★★ PIPELINE: C1 intake (4 Qs) → C2 gate (art+ads) → CPI بالـ overlap → لا hodgepodge
               → bot report (dominant/stalemate/stagnation/runaway/trivial) → Plan/Proto/Review/Lock

INDEX ONLY — اسحب قبل ما تحكم:
 Balancing 403–436 (perceived 420–425 · sawtooth 424 · pos fb 429–433 · neg 432–433 · tuning 435–436)
 Random 395–399 · Core mech 351–395/402 · Economy 366–374 · Machinations 372 · Test every mechanic 395
 Challenges 315–347 · Saving 343–347 · Level design 439–470 (Twinkie Denial 468)
 UI 255–312 · Accessibility 304–308 · Genres 69–78 (Puzzle 78) · Money 113–124
```
````