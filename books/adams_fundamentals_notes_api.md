# Adams — *Fundamentals of Game Design* (3rd Ed., 2014) — جزء 1 من 2 — نوتس مذاكرة

**اللي في الجزء ده (p.1–39 من الـ PDF):** غلاف + front matter + Contents + Introduction + **Chapter 4 كامل** (Understanding Your Player) + أول الـ Index (من Numbers لحد حرف I).

**ملحوظة مهمة:** الجزء قفز من الـ Introduction للفصل 4 مباشرة. فصول 1–3 و5–17 غير موجودة هنا، ومتجاهَلة لحد ما تيجي. لو جزء 2 مش فيه فصول 1–3 و5–6 يبقى لازم نطلبهم، خصوصًا 1 (تعريف الـ game) و3 (genres) و6 (monetization). ترقيم الفصول تحت هو ترقيم الكتاب نفسه. صفحة 16 فاضية، وفيه صفحة مكررة في الـ OCR (نص «Men and Women» اتكرر مرتين) اتحسبت مرة واحدة.

---

## Front Matter — عن الكتاب والمؤلف ★

- **المؤلف:** Ernest Adams. أسّس الـ IGDA سنة 1994 وكان أول رئيس لها. اشتغل 8 سنين في Electronic Arts، وكان audio/video producer على خط Madden NFL، وlead designer في Bullfrog Productions، وقبل كده software engineer (من IBM 360 mainframe لحد النهارده). دكتوراه من Teesside University في interactive storytelling. بيدرّس part-time في Uppsala Campus Gotland. عنده 5 كتب تانية وعمود «Designer's Notebook» على Gamasutra.
- **الطبعة الثالثة (2014، Pearson/New Riders).** المحرر التقني **Tobi Saulnier** (مؤسسة 1st Playable Productions، خبرتها في casual وألعاب الأطفال). اعتمد على MobyGames وGiant Bomb كل يوم في البحث.
- **شكر خاص لـ Jason VandenBerghe** (Creative Director في Ubisoft) على بحثه في player motivation. ده أساس أول قسم في الفصل 4.
- **الشكر شمل:** Raph Koster وSteve Meretzky وBrian Moriarty وChris Taylor وScott Kim وCarolyn Handler Miller وJesyca Durchin وآخرين. وكلهم ظهروا كمصادر فعلية في الفصل 4.

---

## Introduction (p.x–xv) ★★

**فلسفة الكتاب وتغييرات الطبعة:**
- **السبب المعلن للتحديث:** الصناعة اتغيرت أكتر من أي وقت. انفجار casual وfree-to-play وmobile، وUnity كـ middleware، وأدوات فن/أنيميشن/صوت مجانية، وaccelerometers في أغلب الـ input devices، وKinect على أعتاب جيله التاني (كان لسه «Project Natal» في الطبعة اللي قبلها).
- **4 فصول جديدة:** 3 (Genres)، 4 (Understanding Your Player)، 5 (Understanding Your Machine)، 6 (Making Money). فصول الـ genres القديمة اتحولت لـ e-books اسمها «Fundamentals of <genre> Design». القائمة: Shooter / Action & Arcade / Music-Dance-Exercise / Strategy / Role-Playing / Sports / Vehicle Simulation / Construction & Simulation / Adventure / **Puzzle & Casual**. أقرب واحد لنا هو الأخير.
- **ميزتين بيقول إنهم بيميزوه:**
  1. موجّه لتصميم لعبة تجارية كاملة، وبيغطي تجربة اللاعب كلها مش الـ mechanics بس.
  2. مفيش interviews مع مصممين مشاهير. المساحة دي بتتصرف على نصايح عملية.
- **اللي مش في الكتاب:** برمجة، فن، أنيميشن، موسيقى، audio engineering، كتابة، project management، budgeting، scheduling. بس بيشير ليهم لأن قرارات التصميم بتأثر عليهم. وبينصح المصمم يتعلم منهم كلهم: «أعظم المصممين Renaissance men and women مهتمين بكل حاجة».
- **افتراض الكتاب:** إنت بتصمم اللعبة كلها لوحدك. السبب إن تقسيم المسؤوليات بين فريق مصممين بيعتمد على نوع اللعبة ومهارات الأفراد، فمش هيقدر يقول غير generalities.
- **الـ prerequisites:** معرفة ألعاب (خصوصًا المشهورة)، كتابة مختصرة وواضحة («مهارة مطلوبة تمامًا للمصمم»)، وجبر وprobability ثانوي. الأخيرين مهمين لفصلي core mechanics وbalancing.
- **Design Practice Exercises vs Questions:** الـ exercises للمدرّس يكلف بيها. الـ **Questions أسئلة تسألها لنفسك عن لعبتك: «الإجابة عليها هي جوهر تصميم الألعاب»** ★.

**خريطة الفصول (من Intro + Contents)** — دي هتبقى مرجع الربط مع الجزء 2:
1. Games and Video Games (تعريف game وgameplay، عوامل الترفيه).
2. Designing and Developing Games (core mechanics + UI + storytelling engine، gameplay mode، مراحل التصميم، الـ design documents، أدوار الفريق، player-centric design).
3. Major Genres.
4. Understanding Your Player *(ده اللي اتذاكر تحت)*.
5. Understanding Your Machine (consoles/PC/portable).
6. Making Money (direct وindirect: freemium وad-supported، world markets).
7. Game Concepts.
8. Game Worlds (physical/temporal/environmental/emotional/ethical).
9. Creative & Expressive Play.
10. Character Development.
11. Storytelling.
12. Creating the User Experience.
13. Gameplay (hierarchy of challenges، skill/stress/absolute difficulty، save).
14. Core Mechanics (5 أنواع: physics وeconomics وtactical maneuvering وprogression وsocial، والتركيز على internal economy، وrandom numbers وbell curve).
15. Game Balancing (dominant strategies، chance، PvP/PvE fairness، difficulty، positive feedback، design to make tuning easy).
16. Level Design.
17. Online Gaming (persistent worlds، social problems).

**للاستوديو:**
- (1) **Mossfolk:** الفصول 13/14/15/16 هي الأقرب لمشاكلنا اليومية: challenge hierarchy، internal economy (ميزانية الإسقاطات)، positive feedback (الـ merge chain)، DDA، level design (3000 ليفل). فهتتذاكر بأعلى أولوية لما توصل.
- (2) **خط الإنتاج:** الـ Design Practice Questions هي template جاهزة لـ **idea intake form**. أي فكرة جديدة في الاستوديو تتجاوب عليها كتابيًا قبل أي بروتوتايب. الأسئلة الأربعة بتتفصل في آخر الفصل 4 تحت.

---

## Chapter 4: Understanding Your Player (p.81–102)

**الفكرة المحورية:** الـ player-centric approach «يتطلب فوق كل حاجة» إنك تفهم اللاعب كفرد له علاقة عاطفية باللعبة (وبالتبعية بيك)، مش كجزء من جمهور مستهلكين. وبيحذر: «بنفتكر إننا عارفين اللاعبين عايزين إيه، وأغلب المعرفة دي حدسية ومبنية على اللي إحنا عايزينه كلاعبين» ★★. الترتيب: motivations ← demographics (رجال/نساء/أولاد/بنات/dedicated/casual) ← تعريف جمهورك ← نوع اللعبة.

---

### 4.1 VandenBerghe's Five Domains of Play ★★★

- **المصدر:** Jason VandenBerghe (Creative Director، Ubisoft). محاضرة GDC 2012 «The 5 Domains of Play: Applying Psychology's Big 5 Motivation Domains to Games». بتطبقها كجزء من player-centric design بإنك تفكر في «representative player» بمصطلحاتها.
- **الأساس النفسي: Five Factor Model (Big Five) = OCEAN:**
  - **O**penness (للتجارب الجديدة) ← عكسها: مقاومة التجارب الجديدة.
  - **C**onscientiousness ← عكسها: غيابها.
  - **E**xtraversion ← عكسها: introversion.
  - **A**greeableness ← عكسها: disagreeableness.
  - **N**euroticism (ميل لتجربة المشاعر السلبية) ← عكسها: stability.
  - «بعد آلاف الـ surveys النموذج ثابت بشكل ملحوظ عبر الأعمار والثقافات».
- **فرضية VandenBerghe:** بنلعب عشان نشبع **نفس الدوافع اللي في الحياة الحقيقية، خصوصًا لو ما نقدرش نشبعها فيها**. اللعب = منفذ (outlet). ده الـ pattern ورا الأطر الخمسة.

**الدومينز الخمسة ← السمة المقابلة ← معناها:**

| Domain | الترابط | اللاعب العالي | اللاعب الواطي |
|---|---|---|---|
| **Novelty** ★ | Openness | تنوع وعناصر غير متوقعة | يفضل **familiarity** = تشابه مريح؛ مثال: *Words with Friends* بدل sci-fi extravaganza بعالم وقواعد غريبة |
| **Challenge** ★★ | Conscientiousness (وتحديدًا effort + control) | صعوبة ودقة للفوز، والدافع إنه يعمل كل حاجة ويكمّل كل اللعبة | **sandbox** وألعاب حرية العبث من غير إنجاز مطلوب |
| **Stimulation** | Extraversion (عبر social engagement) | party games والتفاعل مع لاعبين | ألعاب بيلعبها لوحده، وهو «الشخص الحقيقي الوحيد» في العالم |
| **Harmony** | Agreeableness | تعاوني → *Little Big Planet* | تنافسي بحت → *Street Fighter* = عكس الـ harmony أي conflict |
| **Threat** ★★ | Neuroticism | **عكس المتوقع**: اللي عنده ميل لمشاعر سلبية بيدور عليها فعلًا (survival horror) | — |

- **تنبيه:** الـ Harmony هنا = social harmony. مش نفس «harmony» بتاعة الفصل 1 (إحساس إن كل أجزاء اللعبة جزء من كل متماسك).
- **الـ facets:** كل domain ليه 6 facets (30 إجمالًا). Threat مثلًا = **tension, provocation, gloom, humiliation, addiction, danger**. الـ slides عند darklorde.com/2012/03/the-5-domains-of-play-slides.
- **ملحوظتين مهمين:**
  1. دي **continuums مش on/off**.
  2. **المزاج بيتغير**: ساعات عايز action عالي الطاقة وساعات adventure أبطأ فيه حاجات تتشاف. فالـ domain مش هوية دائمة للاعب.
- **نقطة VandenBerghe (وآدمز):** بنحدد كمصممين «إزاي هنسلي الناس: إيه التجارب اللي لعبتنا هتقدمها».
- مرجع إضافي: *Personality Traits* لـ Gerald Matthews وآخرين (2009).

#### الدومين السادس: Attitudes to Storytelling ★★
(VandenBerghe ما تكلمش فيه، آدمز بيضيفه.)
- **المعادي للـ story:** بيكره أي narrative (cut-scenes). اللعبة عنده system of rules للإتقان، والـ story «بتتدخل» في المتعة. بيفضل **tactical/strategic immersion** ومالوش اهتمام بـ narrative immersion. الـ NPCs عنده **رموز يتحكم فيها مش ناس**. بيفضل pure action/strategy أو multiplayer من غير قصة (نقطتها التفاعل مع اللاعبين). وفيه genres مناسبة للـ story أكتر من غيرها: sports games بتكسب قليل جدًا منها.
- **المحب المتطرف:** الـ story سبب اللعب الأساسي. بيصدّق الشخصيات وبيهتم بيها. ممكن يهتم بالـ story أكتر من الـ gameplay فيستخدم cheats وwalkthroughs عشان يشوف إيه اللي بيحصل من غير ما يتخطى الـ challenges.
- **الأغلبية:** حاجة في النص. «بعض الـ storytelling طالما **متسقة مع الـ gameplay ومش بتبطّأ اللاعب**». وعلى الأقل framing narrative بسيط لـ context: مين البطل وبيحاول يعمل إيه ولمَ.
- **القرار التصميمي:** جمهورك بيحب الـ story بشغف / بيكرهها تمامًا / عايز «رشة» storytelling. اختار وبعدها شوف فصل 11.

**الباترن ورا الفصل:** ثلاث شرائح: Motivation (Big 5) ← preference ← نوع لعبة. وبما إن المزاج بيتغير، الـ domain ده «طيف بيتحرك» مش تصنيف ثابت.

**للاستوديو:**
- (1) **Mossfolk:** merge puzzle بيخدم: Novelty (9 أحجام + mossy shells/stones/rot كتحديات جديدة من 2501) + Challenge (3000 ليفل بأهداف وميزانية) + Threat خفيف (rot/stones = facets من tension/danger) + Stimulation/Harmony (rival contests، وده بيحتاج نوع «conflict» مش «harmony» حسب التصنيف) + نقطة الـ story (Mossfolk فيها narrative خفيف؟ لو لأ، ده مناسب للأغلبية بتاعة «framing بسيط بس»). **حاجة تتفحص:** الـ Challenge عندنا للـ conscientious المكمّلين (bot_difficulty بيقيسها) — وفين الـ low-challenge/sandbox mode؟ ممكن الـ side-quest minigames هم اللي يغطوا ده؟
- (2) **خط الإنتاج:** أول سطر في كل **idea card**: «أي domains من الستة هتقدم وبأي شدة؟» — تمرين دقيقتين قبل البروتوتايب بيمنع فكرة «تتفتح لكل الناس». لو الفكرة نقطتها Threat عالي وجمهورنا الحالي من puzzle/casual، ده تحذير مبكر.

---

### 4.2 Demographic Categories

*(ملاحظة آدمز: الاختلافات بالسن والجنس «كبيرة» لكنه في كل قسم بيشدد: generalities مش قوانين.)*

#### أ) Men and Women ★★★

**أرقام ومعلومات:**
- في أمريكا (ESA 2013): **نساء بالغات 31% > مراهقين ذكور 19%** من لاعبي الفيديو جيمز ★★★. ضد الـ stereotype.
- الرجال والنساء مش مختلفين بقدر ما الـ pop psychology بتقول. Holly Devor (*Gender Blending*, 1989): **حتى 50% من النساء المغايرات** وصفن نفسهن كـ tomboys في الطفولة. الاهتمامات بتتداخل كتير.
- الخطأ الشائع: المصممين يعاملوا الجنسين «كأنواع مختلفة بقت».

**Gender Inclusiveness ★★★ (مصدر: Sheri Graner Ray، *Gender Inclusive Game Design* 2003):**
- مش لازم تعمل لعبة عن fashion/shopping عشان تجذب النساء، زي ما مش لازم monster truck rallies للرجال. **القاعدة: تجنّب محتوى بيطفّش مجموعة أو التانية**، مش «بنِي محتوى مخصوص».

**أكبر turnoffs للنساء:**
1. شخصيات (avatars وغيرها) **hypersexualized**.
2. لعب **متكرر ممل** (repetitive, monotonous).
3. لعب **بلا هدف ذي معنى**. «مجرد أعلى سكور مش كفاية» ★★.
4. الطبيعة الانفرادية للـ single-player (مفيش حاجة تتعمل لو لعبتك single-player، بس خد بالك).

- جهود الصناعة لبطلات مغامرات (Lara Croft، Jade من *Beyond Good and Evil*) قابلها backlash صاخب من أقلية رجال. آدمز: **تجاهلهم**. ادعاءهم إن الرجال مش هيلعبوا ببطلة «غير صحيح»، ولو اللعبة كويسة هيلعبوها.

**Generalities (لدى الغرب فقط؛ ممكن ما تنطبقش في اليابان/الصين/كوريا/الهند):** ★★
1. **التعلم:** النساء عايزين يعرفوا المتوقع منهم قبل ما يبدأوا بدل ما «يترموا في المية»: **learn-by-dying** (أركيد قديم، ولسه في ألعاب mobile كتير) غير محبوب عند كتير من اللاعبات ← حط tutorial levels في الأول.
2. **المخاطرة:** الرجال بيجرّبوا حتى لو خسروا كتير. النساء غالبًا **consolidate وبيحافظوا على اللي حققوه** عشان ما يخسروه تاني، حتى لو الاستراتيجية الأخطر تجيب مكسب أكبر.
3. **ناس > أشياء:** النساء بيحبوا يتواصلوا اجتماعيًا ضمن اللعب. ده سبب نجاح الـ online games أكتر من single-player. وألعاب Facebook (دعوة أصحاب، مشاركة موارد، مقارنة إنجازات) شهيرة جدًا عند النساء حتى من غير multiplayer حقيقي. (Note: النساء في الواقع بيشيلوا جزء كبير من مسؤولية نسيج المجتمع، والـ social networks وألعاب الأونلاين بقت جزء من ده.)
4. **حل النزاعات:** النساء بيفضلوا إن العنف يكون **له مبرر/سياق** (قصة). مش ضد العنف، بس الـ fighting for its own sake مالوش اهتمام. وبيحبوا **lateral thinking** لإيجاد بدائل لـ brute-force. fighting/war/shooters أشهر عند الرجال. بس RPGs مشهورة عند النساء رغم الـ combat الكتير **لأن الـ combat ليه غرض وجزء من هدف أكبر**.
5. **التحديات الذهنية والحلول الأنيقة:** النساء بيحبوها ← شعبية الـ puzzle games.
6. **Avatar customization:** الرجال غالبًا بيعاملوه كـ **puppet** يتحكموا فيه عشان يكسبوا. النساء بيتماهوا معاه أكتر ويستخدموه **self-expression** (نفسها أو نسخة fantasy منها). بتتفاوت حسب السن والـ genre (الرجال ممكن يضيّعوا وقت كبير في تعديل الشخصية في RPG لأن ده الـ point).
7. **الوقت والفلوس:** الرجال أكتر leisure time وفلوس: عادة بيدفعوا $60 يوم الإصدار الأول أسهل. النماذج الجديدة (casual) **شعبية جدًا عند النساء** لأنها ما بتطلبش مخاطرة بمبلغ كبير مقدمًا وبتسمح بدفع صغير على دفعات. الرجال بيخصصوا blocks طويلة. وقت النساء **مجزّأ** (خصوصًا مع الأطفال): **30 دقيقة لساعتين أكتر من 5 ساعات متواصلة**. بعضهن بيلعبن نفس إجمالي الأسبوع بس في قطع أصغر. ← خد بالك من **المسافة بين نقاط الـ save**. ألعاب social network بتسمح بالتوقف في أي نقطة من غير فقد تقدم.

**Design Rule ★★★: «Women Are a Market, Not a Genre»** — ما تحاولش تصمم «لعبة للنساء» بإضافة features من الـ generalities. صمم لعبة **ممتعة جوهريًا** وخلّي بالك من تأثير قراراتك على جمهورك. والاستثناءات كتير: لاعبات يشترين console games غالية، ولاعبين آباء ليهم وقت لـ puzzle رخيصة مرتين في اليوم. **الغرض من المعرفة دي: تعرف هل لعبتك هتجذب/تطفّش كتير من النساء أو الرجال، مش تعمل لعبة «لهن» أو «لهم».**

**Male/Female Players & Characters ★★:**
- قديمًا كان فيه قلق إن الرجال مش هيلعبوا بـ avatar أنثى. **Lara Croft** أثبتت إن مفيش مشكلة **طالما بتعمل أدوار الرجال مرتاحين معاها** (أنشطة مغامرات «ذكورية تقليديًا»). مش مرتاحين مع avatar بأنشطة «أنثوية» تقليديًا.
- النساء بيتوقع منهم يتماهوا مع بطل ذكر دايمًا، ودلوقتي مليّنوا. لكن مش مهتمين بـ **male-fantasy characters** زي **Rayne من BloodRayne**: متطرفة لدرجة تمنع التماهي. **Heather من Silent Hill 3** مثال أحسن: «شكلها زي إنسانة حقيقية مش إعلان lingerie ماشي».
- الرجال بياخدوا **default avatar** ويجروا بيه. النساء بيشوفوه امتداد لشخصيتهم (أو شخصية يهتموا بيها). **أحسن حاجة تجذب بيها النساء: تسمح بـ customize (ملابس، إكسسوارات، أسلحة)**. الـ RPGs (خصوصًا online) أقوى features customization.
- **اختيار avatar ذكر/أنثى:** ينفع، بس لازم رعاية: «**المرأة مش رجل بجسم مختلف**». اكتب الحوار من جديد عشان لما الـ avatar الأنثى تتكلم تبقى «امرأة بتتكلم» مش «امرأة بتقرأ سطور مكتوبة لرجل» ← أساليب التواصل مختلفة. (tip: صفحات Facebook/Pinterest «Heroic Women to Inspire Game Designers».)

**الباترن ورا القسم كله:** آدمز بيعمل **شغل statistical حذر**: فروق متوسطات + تداخل كبير + «avoid exclusion بدل ما تستهدف». ودي الفكرة اللي بتتحول لـ math في 4.4.

**للاستوديو:**
- (1) **Mossfolk:** المميز إن عندنا puzzle (ألعاب شعبية عند النساء) + **ميزانية إسقاطات** (= goal ذو معنى مش high score فقط ← turnoff رقم 3 مشطوب) + جلسات قصيرة. فحوصات: (أ) الـ **tutorial**: learn-by-dying مقبول على الـ mobile عادةً لكن آدمز بيقول بيطفّش، فهل أول ليفلات Mossfolk بتشرح المتوقع قبل الفشل؟ (ب) نقاط الـ save/الاستكمال: هل اللاعب يوقف في منتصف ليفل من غير فقد؟ (ج) **مدة الجلسة 30د–ساعتين**: كل ليفل لازم يخلص في دقايق، والـ progress يتحفظ تلقائي. (د) **Risk attitude**: لو بنعاقب على الفشل (rot، ميزانية) بشدة، ده بيفرّق مع اللاعبين اللي «بيحافظوا على اللي كسبوه» — يقاس بـ retention بعد أول فشل حسب segment. (هـ) **Customization للـ Mossfolk** (skins/ملابس للمخلوقات)؟ دي رافعة self-expression حقيقية، وبتتلاقى مع «girls like stuff» تحت.
- (2) **خط الإنتاج:** ★★ **«Exclusionary-material checklist»** تتحط كـ gate بسيط في art review لكل لعبة جديدة (قبل الإعلانات كمان): hypersexualized؟ تكرار ممل؟ مفيش هدف ذو معنى؟ — الـ 4 turnoffs قابلين للتحويل لـ checklist من 4 أسطر. وكمان: **الأرقام (31% vs 19%) أمريكية ومن 2013** — جمهورنا ممكن يبقى من أسواق تانية (آدمز نفسه بيحذر إن الـ generalities غربية فقط). لازم نقيس segments من الـ analytics بتاعنا (CPI test بحسب الـ demographic) بدل ما نصدّق الرقم.

---

#### ب) Boys and Girls

**الفئات العمرية:**
- Preschool/kindergarten: **3–6**
- Early elementary: **5–8**
- Upper elementary (tweens): **7–12**
- Middle/high school (teens): **13+**
- Late teens–mid-20s: «مش أطفال، لكن مخّهم لسه بيتطور».
- **Piaget وMontessori:** غلط تشوف الأطفال «كبار صغيرين أقل مهارة ومعرفة».
- **الغرب:** الأطفال بيطمحوا لعالم الكبار وبيتجنبوا أي حاجة لفئة أصغر منهم ← ترفيه الأطفال بيعرض شخصيات **أكبر** من اللاعبين. **عكسه في اليابان.**

**9 اعتبارات لتصميم ألعاب الأطفال ★★:**
1. **Hand-eye coordination:** ضعيفة في الأول، ذروتها في المراهقة وأوائل العشرينات، وبتقل بعدين.
2. **Logic development:** بتوصل لذروتها **بين 6 و7 سنين** (حسب الطفل). puzzles لسن أقل: **عدة مستويات صعوبة** (تتأكد منها بـ playtest)، و**عناصر أقل وسلسلة تفكير أقصر** لنفس مستوى الـ engagement.
3. **Systematic thinking:** بتبدأ **12–14** سنة. متضيفش أنظمة معقدة قبلها. «systems optimization problem بسيط عندك هو حاجة الطفل لسه بيبدأ يستكشفها».
4. **Immediate vs long-term goals:** الأطفال أكتر تركيزًا على **moment-to-moment** ومحتاجين feedback أكتر تكرارًا. بس مش لازم «Good job!» سكرية كل مرة.
5. **Visual design:** الأطفال أقل خبرة في تصفية التفاصيل غير المهمة ← UI بسيط ومركز، **deep rather than broad**.
6. **Linguistic complexity:** متتكلمش بتعالي، لكن جمل قصيرة وكلمات مختارة (مثال: *The Little Prince* بيعبر عن أفكار عميقة بجمل قصيرة).
7. **Experimentation:** عندهم طاقة تجريب لا نهائية، بيدوسوا على كل حاجة ← صمم عالم **يكافئ الاستكشاف**.
8. **Reading:** محدودة (حتى في سن المراهقة بعضهم مش بيحب القراءة) ← **voiceover** للمعلومات المهمة والخيال يكمّل تفاصيل القصة.
9. **Appropriate content:** كتير من الأمر هو ما **الأهل** عايزينه. الترفيه للأطفال لازم يخاطب اهتماماتهم؛ الجنس والمال العالي مش في عالمهم. *Harry Potter* المبكر عبقري لأنه بيعبّر عن مخاوفهم: الاغتراب، سوء فهم الأسرة، إحساس بإمكانية كامنة لم تُستغل. حتى التركيز على الأكل مقصود لأن الأكل اهتمام كبير للأطفال الصغار. طريقة التذكر: **اقرأ الأدب الشعبي لنفس السن**.

**Seven Kisses of Death (Carolyn Handler Miller، *Digital Storytelling* 2nd Ed. 2008) ★★★** — مفاهيم مغلوطة مبنية على «اللي الكبار عايزين الأطفال يحبوه»:
1. **«الأطفال بيحبوا أي حاجة حلوة»**: بيحبوا بعض الحاجات الحلوة بعض الوقت. الدليل **كرتونات Warner Bros**: Bugs Bunny الساخر، Sylvester ومحاولاته الأبدية يأكل Tweety، Wile E. Coyote وRoadrunner، Yosemite Sam القاتل، Elmer Fudd صائد الأرانب ← مفيهاش حاجة «حلوة»، وفيها «عبرة ماكرة» إن العنف بيرتد على العنيف.
2. **«أعطيهم اللي كويس ليهم»**: بيتقالهم كده طول الوقت (أكل، مدرسة، بيانو). مش في الترفيه: «تحب تاخد جرعة propaganda مع كل كتاب؟» لما يريحوا مش عايزين دواء.
3. **«لازم تسليهم بأي حاجة»**: عكس #2. بيفترض إنهم أقل تمييزًا. هم **ما يفرّقوش بين تمثيل كويس ورديء** وملهمش خبرة يميزوا الـ clichés، **بس مش هيتحملوا أي حاجة**. **Disney** فهم ده: أفلامها multilayered. «المحتوى ذو المعنى بيمسك انتباه الطفل أطول من التافه».
4. **«العب safe دايمًا»**: بتشيل أي حاجة تخوّف أو ترفع نبضهم = ترفيه باهت. أمثلة Disney: انفصال **Dumbo** عن أمه، هروب **Snow White** المرعوب في الغابة، **قتل أبو Simba** في *The Lion King*. حجة Gerard Jones (*Killing Monsters*, 2002): **التعامل مع مواقف مهددة جزء مهم من النضج**.
5. **«كل الأطفال سواء»**: مفيش «سوق أطفال واحد». لو مصممة لـ **6–10** والناشر عايز **8–12** ← **إعادة تصميم**. one-size-fits-all مش بيشتغل.
6. **«اشرح كل حاجة»**: الأطفال أسعد بـ trial-and-error من الكبار. عايزين يلعبوا على طول. **تجنب talking heads** والـ jabber. في عوالم الألعاب «ما يقدروش يأذوا نفسهم أو أي حاجة» فاختصر أي exposition أو تعليم.
7. **«تأكد الشخصيات wholesome»**: **wholesome = boring**. اعمل شخصيات حقيقية لها نقائص. *Sesame Street* قدمت شخصيات صُممت لتمثل مزاجات يعرفها الأطفال: طماع، متجهم، مساعد…

**الباترن ورا الـ Kisses:** كل 7 = **الكبار بيسقطوا رغباتهم على الطفل**. المصدر الحقيقي للصح هو ملاحظة الطفل نفسه (و playtest).

#### ج) Games for Girls ★★

**الخلفية والحقائق:**
- الصناعة سيطر عليها رجال بيض، ومصممين بيعملوا ما كانوا يحبوه كأولاد.
- **الفجوة بين الأولاد والبنات أوسع من الرجال والنساء** (متوسطات المنحنيين أبعد). في سن معين ممكن يرفضوا رموز الجنس الآخر (ملابس، لعب).
- **الدائرة المغلقة (catch-22):** تقترح لعبة للبنات ← «البنات مش بيلعبوا فيديو جيمز» ← مفيش لعب ← ماحدش يلعب. والبحث لاحقًا أثبت إنها صورة نمطية خاطئة: بنات كتير لعبوا، والناس ما اهتمتش باهتماماتهم.
- **منتصف التسعينات:** اكتشاف سوق غير مستغل. لكن **أغلب المحاولات المبكرة كانت رديئة جرافيك وأقل قيمة من الألعاب الأخرى**. «البنات عايزات ويستاهلوا ألعاب كويسة زي الأولاد».
- **أواخر الألفينات:** سلسلة **Ubisoft Imagine** (من النجاح المفاجئ لـ *Imagine: Fashion Designer*) غطّت مواضيع كتير. نجاحات: ألعاب مبنية على شخصيات لعب/كتب: **Barbie, Bratz, Nancy Drew**.
- **تحذير:** الجمهور **بنات مش نساء**. النساء أكتر تنوعًا، فما تفترضش إن اللي ينطبق على النساء ينطبق على البنات.

**Mattel's approach:** افحص إيه اللي بتشتريه وتقراه وتتفرج عليه الفتيات. Barbie نجحت بـ formula مجربة + سوق مستهدف: **core age 4–8**. بعدها الاهتمامات تتغير و«مفيش one-size-fits-all». «لا أجندة اجتماعية ولا ادعاء political correctness». Mattel بقت ما تنشرش سوفتوير بنفسها (بترخص الـ brands).

**Jesyca Durchin (Nena Media، وexecutive producer سابقة في Mattel؛ GDC 2000) ★★:**
- **تنوع الاهتمامات:** البنات **أكتر تفتتًا** من الأولاد، وبيتغيروا أسرع. لهن احتياجات لعب مختلفة **تقريبًا كل سنة** بين 4 و14.
- **ابنِ التفاعل على Proven Play Patterns** (طريقة طفل تقليدية وشبه غريزية للتعامل مع شيء للترفيه). البنات تقليديًا بيقدّروا 7: **Fashion، Glamour، Nurture، Action/twitch، Collection، Adventure، Communication/social**. بيحبوا يعيدوا إنتاج الحياة اليومية (Barbie = وسيلة لإسقاط أنشطة الكبار على عالم الطفل). **«متخافش من اللعب المفتوح غير الموجه بهدف»**.
- **Girls like stuff** ★★: stuff = حاجة تجمعها وتعرضها وتاخدها معاها. «من المهم جدًا إنها تحس إن فيه سبب تلعب». **جمع الأشياء بيحل محل السكور**: «جمع كل الأنواع من الأصداف أمتع من تحقيق سكور عالي لكن مجرد».
- **Environments:** واقعية (reality-based) لكن إما جميلة أو منطقية مع القصة. **التناظر (symmetry) وتماسك الألوان (color coherency) مهمين**. «مش لازم كل حاجة pink/purple/pretty»، بس كل بيئة تدّي إحساس «مكان آخر». الخيال عند البنات (والأولاد) بيبني story lines بديلة، فخيالها بيأثر على نظرتها لبيئتك.
- **Sensual interface** ★★: واجهات ملونة، مدفوعة بالصوت، «تحس حلوة»، سحرية، فيها «**brrrring factor**». **متديش البنات صف من أزرار رمادية متطابقة مهما كان منطقيًا**، اديهم أزرار ترن وتغيّر الشكل واللون.
- **امتداد من لعب/ميديا موجودة:** الـ branding بيزيد أهمية، **مضاعف في سوق البنات** لأنهن لسه بيشوفوا الكمبيوتر كأداة ترفيه.
- **«متتكسفش من شغلك»**: لو محرج هتبان. اعمله بكل قلبك أو متعملوش. البنات بيحسوا لو إنت محرج. لو مش مرتاح تقول «hair play» أو «relationship games» ما تتعبش.

**Kaye Elling's Five Cs (Blitz Games، سلسلة Bratz؛ Animex 2006 «Inclusive Games Design») ★★★:**
1. **Characterization:** البنات/النساء بيشوفوا الـ avatar «حد بيمثلهم» مش حد بيتحكموا فيه ← لازم يتماهوا معاه وملوش صفات منفّرة.
2. **Context:** البيئة مهمة؛ بيتنفروا من الـ ugly/hostile (ده بيوافق Durchin).
3. **Control:** تحس إنها هي اللي بتتحكم مش اللعبة. **risk-and-reward** بيجذبهن أقل. وبيكرهوا **mechanics اللي بتعاقب الفشل بشدة** لأنها بتثبط التجريب.
4. **Customization:** البنات بيخصصوا موبايلاتهم وإكسسواراتهم أكتر من الأولاد. مثال: **Bratz: Rock Angelz = 686 قطعة** (ملابس/مكياج/مجوهرات…)، **الأكثر جاذبية منها unlockable rewards** بتكسبها بإنهاء mini-games.
5. **Creativity:** *The Sims* ناجحة مع البنات والنساء للـ creative play. إظهار اللي عملته للغير. مش خاص بالبنات: حتى *Halo 2* فيه تصميم clan badges.

**Misconceptions الأربعة ★★:**
1. «البنات مش بيحبوا كمبيوتر لأنه تقني» ← **خطأ**. مش مهتمات بتفاصيله التقنية، لكن ده ما بيمنعهم يلعبوا زي ما مواصفات العربيات ما بتمنعش السواقة.
2. «البنات ما بيحبوش العنف» ← الحقيقي: **ما بيحبوش العنف المتواصل بلا معنى**. مش مقزز بقدر ما هو **ممل** («شفت انفجار شفتهم كلهم»). عند Elling: لما العنف يكون **عرضي أو سادي أو gory زيادة** يبقى **brutality** والبنات ما بيحبوهاش. لما يكون **دفاعي، مُستفَز، أو cartoony** يبقى مقبول.
3. «عايزين كل حاجة سعيدة وحلوة» ← **غلط**. كتب البنات فيها mystery وsuspense وحتى danger، **بس مع معنى** مش عشوائي.
4. «ما بيحبوش الخوف» ← **جزئيًا**. Durchin: **spooky ≠ scary**. Spooky = بيت مهجور، ملاهي بالليل (احتمال إنك تتفاجئ). Scary = شارع مظلم وقاتل طليق (احتمال تتأذى أو تموت). **spooky = إمكانية الانزعاج؛ scary = إمكانية الأذى/الموت.**

- **TIP (Puzzle Quest، Nintendo DS RPG):** ناجحة للأولاد والبنات. avatar ذكر/أنثى، **الـ combat متصوّر كـ puzzle-solving**، ولما تخسر المعركة الـ avatar **مش بيموت، بس بيهرب** وتحاول تاني بعدين.
- **ملاحظة ختامية:** دي generalities. بعض المطورين (ذكور وإناث) بيرفضوا فكرة ألعاب عن شعر/ملابس/مكياج لأنها بتكرس stereotype. آدمز: فيه ميزة في الحجة، لكن **عدد أكبر بكتير من الألعاب بيكرس stereotype أسوأ للذكورة: رجال (ولاعبين بيتكافأوا) عنيفين، طماعين، شهوانيين، monomaniacal**. فإدانة ألعاب البنات على أساس الـ stereotype = **double standard** ★.

**الباترن ورا القسم:** أغلب «ما تحبه البنات» هو **meaning + control + beauty + collection** مش «لون وردي». الـ pink مجرد skin، والجوهر هو الأربعة دول.

**للاستوديو:**
- (1) **Mossfolk:** الـ mossy folk creatures بـ **9 أحجام** = natural **collection** (ممكن تتعرض/تتفتح/تتجمع بدل ما تبقى مجرد أرقام ← جمع بدل سكور)، وهي نقطة Durchin الأقوى. وfeedback الـ merge (صوت/لون/شكل) = **brrrring factor**. وrot challenges: خليها **spooky** مش scary (rot ظاهر بس مش gore). **Control:** ميزانية الإسقاطات + إعادة المحاولة = لا عقوبة قاسية (ممتاز مع Elling #3). وتحذير: لو ضغطنا الـ rot/stones لدرجة إحباط (من 2501) فده بيمسّ Control.
- (2) **خط الإنتاج:** **Five Cs (Characterization/Context/Control/Customization/Creativity)** + **الـ 7 play patterns** كقائمة سريعة في idea intake: أي منها الفكرة بتخدمه؟ وكمان: Seven Kisses لما نستهدف أطفال (فيه ألعاب hyper-casual بتخاطب أطفال بالصدفة): لو الفكرة موجهة لـ 6–10 وجاء تسويق لـ 8–12 ← **إعادة تصميم** (Kiss #5). وأخيرًا **Kiss #6 + نقطة المرأة/learn-by-dying**: التيوتوريال لازم يكون صفر-شرح للأطفال لكن «يوضح المتوقع» للبالغات ← تعارض، حلّه: tutorial تفاعلي قصير جدًا (نفس خلاصة Extra Credits في exemplar).

---

### 4.3 Gamer Dedication ★★★

- **كان:** «Core Versus Casual» في الطبعة السابقة. المصطلحين بدأوا يفقدوا معناهم **مع ألعاب social networks** ← ما هو binary بل **continuum اسمه gamer dedication**.
- **المصدر:** Barry Ip + Adams، مقال **«From Casual to Core: A Statistical Mechanism for Studying Gamer Dedication»** (2002). بعضه مأخوذ من عرض **Scott Kim** GDC 2001 «Designing Web Games that Make Business Sense». «قديمة بس أساسية كفاية».

**الـ 15 صفة قابلة للقياس عند الـ dedicated gamers (كلها):**
1. **Technologically savvy:** عارف أحدث الإصدارات ومهتم بتقنيات جديدة.
2. **Latest high-end gear:** consoles/PC/mobile أحدث، ومُلاّك/كانوا ملّاك لمنصات قديمة متنوعة.
3. **Willingness to pay:** بينفقوا على الألعاب والمنتجات المرتبطة. الـ casual بيستنوا خصومات وعروض.
4. **Prefer violent/action games** (اقتراح Kim).
5. **Prefer depth & complexity:** يحتاجوا وقت أطول للإتقان بغض النظر عن الثيم.
6. **Play over many long sessions.**
7. **Hunger for gaming information:** أخبار/previews/reviews/مقابلات/strategy guides.
8. **Discuss games with friends online:** منتديات وغرف شات.
9. **Play for exhilaration of defeating/completing the game:** أكتر تسامحًا مع عيوب جمالية (تمثيل رديء، plot تافه).
10. **Much more tolerant of frustration:** الـ casual أسهل يتركوا اللعبة الصعبة ★.
11. **Engaged in competition** (مع نفسه/اللعبة/لاعبين): مثال: يلعب *Gran Turismo* لتقليل lap-time بجزء من الثانية، أو يتعلم كل combos في *Street Fighter*، أو سكور أعلى.
12. **Age first started:** بدأ صغير ومنتظم = أكتر خبرة. من بدأ متأخر نادرًا بيبقى dedicated.
13. **Comparative knowledge of the industry:** أحداث زي تسريحات واندماجات (الـ casual بيتابعوا الإصدارات والـ reviews بس).
14. **Early adoption:** midnight releases، gray-market imports.
15. **Desire to modify/extend games:** من skins بسيطة لـ **aim-bots** (برامج بتدّي ميزة غير عادلة). الـ casual بيلعبوا «as-is out of the box».

- **الوزن لك:** الهدف الأصلي للمقال: طرق قياس للبحث. **كمصمم محتاج تعرف بس إزاي الـ dedication بيظهر.** مثال عملي: لو الـ dedicated بيدوروا على معلومات اللعبة وهي لسه في التطوير ← **developer blogs وpress releases** توصلهم.
- **القاعدة:** لو صممت لطرف واحد من الـ continuum «غالبًا مش هتبيع كتير للطرف التاني». قليل من الألعاب بتجمع الاتنين:
  - **GoldenEye:** الـ core يضبط أعلى difficulty ويتجنن في تقليل 15 ثانية من وقت المهمة؛ الـ casual يضبط أسهل مستوى ويتسلى بـ **smooth controls وتفاصيل بصرية**.
  - **Rock Band** مثال تاني.

**الباترن:** **difficulty modes = الجسر العملي** بين طرفي الـ continuum من غير ما تعمل لعبتين.

**للاستوديو:**
- (1) **Mossfolk:** عندنا 3000 ليفل، والـ completionists (صفات 5/6/10/11) هم اللي هيوصلوا لـ 2501+. والـ bot_difficulty لازم يفرّق بين «صعب على الـ casual» و«صعب على الـ core». سؤال: هل فيه mode/مسار يخلي الـ casual يستمتع بـ **smooth feel + visuals** (نموذج GoldenEye) من غير ما يعلق في rot؟ الـ side quests (rival contests وminigames) ممكن تخدم الـ core (صفة 11) بينما التقدم الرئيسي يخدم الـ casual.
- (2) **خط الإنتاج:** في idea card: «**نقطة على الـ dedication continuum**» ← بتقرر تصميم الجلسة، المونيتايزيشن، والإعلانات (الـ casual = ads + قطع صغيرة؛ الـ dedicated = ممكن premium/IAP) — **استنتاج مني** مبني على صفة 3 (willingness to pay)، مش من نص آدمز. وكمان **صفة 7 (hunger for info)** تعني إن قنوات التسويق للـ dedicated مختلفة (blogs/devlogs) عن الـ casual (store listing + ads) ← ميزانية الـ UA تتقسم حسب نقطة اللعبة على الـ continuum.

---

### 4.4 The Dangers of Binary Thinking ★★★

- **التعريف:** binary thinking = تفترض إن «لو المجموعة A بتحب شيء، اللي برّاها مش هيحبوه». «تفكير غير سليم وممكن يخسّرك جزء من العملاء».
- **Reasoning statistically (مثال الـ 0–10):** اسأل مجموعة لاعبين: درجة اهتمامهم بلعبة معينة من 0 (لا اهتمام) لـ 10 (حماس متعصب). أغلبهم في النص.
  - **Figure 4.3 (hypothetical):** متوسط الرجال ≈ **5.5**، النساء ≈ **4.5**.
  - الرسم بيدعم «الرجال أكتر اهتمامًا» **لكن في تداخل كبير**: عدد النساء عند مستوى 6 ≈ **ثلثين** عدد الرجال عند نفس المستوى ← **خمسين حاجة 2/5 من كل اللي أجابوا 6 نساء** ★★★ («كتير جدًا لتتجاهله»).
  - ده مثال افتراضي. أحيانًا التداخل صغير ومفيش ثمن لمخاطبة جمهور مش موجود (لعبة لـ 5 سنين مش هتجذب 15 سنة).
  - **النقطة:** في أغلب الألعاب العادية فيه overlap. أفلام Disney بتحط محتوى متطور للكبار فقط ← جاذبية أوسع. «تتجاهل أو **الأسوأ تنفّر** أقلية بدون ما تعرف حجمها = **بتحرق فلوس**».
- **Strive for Inclusiveness, not Universality ★★★:**
  - **ما تجذبش الكل بـ hodgepodge** من features. مثال: kung fu + chess + Monopoly عشان تجذب action/strategy/management fans = «فوضى ما تجذب حد»؛ **«too many features and no harmony»**.
  - الصح: story line في fighting game **بشرط ما تتدخلش في الـ gameplay**: بتضيف عمق من غير ما تطفّش جمهورها، وممكن تجذب ناس عادةً مش بتهتم بالـ fighting. أمثلة: **Heavenly Sword وGod of War**.
  - **Exclusionary material:** محتوى/features بتطفّش لاعبين ممكن يحبوا اللعبة. أمثلة: نساء ضد تصويرهن «sex objects بلا عقل»؛ آباء ما يشتروش لعبة كلها دم وgore؛ **مجموعات عرقية** (وكتير من الأغلبية) ضد المحتوى العنصري؛ النساء أحساس أكتر لجماليات اللعبة وبيشتروا أقل لو الفن قبيح؛ ناس مالهاش اهتمام بـ narrative وبتتضايق لو اتجبروا يتفرجوا عليه في genre مش عادةً فيه.
  - **Design Rule ★★★: Keep Exclusionary Material Out of Your Game.** **اشتغل على تجنب تنفير ناس ممكن تتجذب، مش على إضافة features غير مرتبطة لجذب الجميع.** «الهدف: أفضل لعبة ممكنة عن موضوعك مع تجنب exclusionary material اللي بيأذي جاذبيتها من غير داعٍ».

**الباترن ورا القسم:** الـ **default = لا تُنفّر، ثم ركّز.** الجمع بين الاتنين بيحمي الـ harmony الداخلية للعبة (الفكرة اللي ظهرت في Harmony في 4.1 والـ coherence في 4.1/الـ story).

**للاستوديو:**
- (1) **Mossfolk:** أي إضافة من الـ side quests/rival contests/minigames لازم تسأل: هل هي «story-line في fighting game» (تضيف عمق من غير ما تقطع الـ core) ولا «kung fu + chess + Monopoly»؟ وفحص exclusionary: mossy shells/rot/stones — أي حاجة منها بتبان gore/مقرفة لشريحة (الـ rot بالذات)؟ الـ tester-bot ما يقيسش ده، لازم قراءة بشرية في art review.
- (2) **خط الإنتاج:** ★★★ **قاعدة قرار الـ CPI test**: متقتلش فكرة بس لأن الـ CPI/الـ retention بتتميل لجنس/سن واحد، **احسب الـ overlap**: نسبة الـ segment التاني عند نفس مستوى الاهتمام/retention. وكمان في كل الألعاب اليومية/الأسبوعية: **«inclusive مش universal»** = عدم حشر mechanics من genres مختلفة لأن تيست واحد قال «أضف كذا». ده يخدم السرعة: قاعدة واحدة تُسرّع رفض التعديلات العشوائية بعد التيست. وأخيرًا الإعلانات: creative الإعلان نفسه ممكن يكون exclusionary (hypersexualized thumbnails، أو gore) فيطفّش segment كامل **قبل** ما اللعبة تتفتح — ده امتداد منطقي مني، مش في النص.

---

### 4.5 Summary (p.101)
ملخص الفصل: 5 domains + سادس (storytelling)، ثم men/women وboys/girls (مع تركيز على ألعاب البنات)، ثم gamer dedication، ثم binary thinking، والتوصية **inclusiveness لا universality**. التالي: الفصل 5 (المنصات).

### 4.6 Design Practice Exercises (للمدرس/للتدريب الذاتي)
1. خد **Big Five test** (outofservice.com/bigfive) هو وأصحابك، وقارن نتايجكم بـ preferred domains of play، واكتب ورقة قصيرة: تأكد/تنفي/غير حاسم فرضية VandenBerghe.
2. افحص لعبة **AAA** شهيرة ووثّق **exclusionary material** (محتوى بيثبط demographic معين من شراءها).
3. افحص ألعاب مسوّقة لـ demographic محدد (بنات/أطفال صغار) ووثّق الـ design features المشتركة: **أنواع التحديات** (من Table 1.1 في الفصل 1) + **الجماليات**: color palettes وtypefaces وscreen layouts.

### 4.7 Design Practice Questions (للعبتك) ★★★
1. أي **domains of play** هتقدمها؟ وده بيقول إيه عن الجمهور اللي بتأمل تجذبه؟
2. **الفئة العمرية** المستهدفة؟ (بتأثر على التحديات والـ UI والـ pacing والجماليات.)
3. **gender inclusive** ولا بتستهدف جنس معين (وده ممكن يحد من جاذبيتها للتاني)؟ لو الثاني: إيه المحتوى/الـ features اللي هتجذب جمهورك المختار تحديدًا؟
4. **مدى dedication** الجمهور؟ مثلًا **اشتراط جلسات طويلة** هيستبعد ناس مالهمش وقت. راجع قائمة الـ 15 وقول هل بتتوقعها من لاعبك، وإزاي هتلبّي توقعاتهم؟

**للاستوديو (للقسمين 4.6 و4.7):**
- (1) **Mossfolk:** الأسئلة الأربعة تتجاوب كتابيًا مرة واحدة وتتحط في ملف الـ design (لو مش مكتوبة بالفعل). ده بيخلي الـ audit الدوري (زي «المعلومة وقت الحاجة» في exemplar) أسهل.
- (2) **خط الإنتاج:** ★★★ **الأسئلة الأربعة = idea-intake template** إجباري لكل فكرة جديدة (نص صفحة، 10 دقايق)، **قبل** أي بروتوتايب. بيوفر وقت لأنه بيطلّع التعارضات (مثلاً: «hyper-casual لكن session طويلة؟») قبل الكود. وتمرين 3 (مقارنة ألعاب مستهدفة demographic معين) = **competitor research مجاني** لكل genre: نفس المنهج (تحديات + color palette + typefaces + screen layouts) ممكن يتأتمت في checklist بسيط لتحليل الـ top charts قبل اختيار الفكرة.

---

## الـ Index (p.533 وما بعدها، A→I فقط في الجزء ده)

مجرد navigation، مفيهوش content تصميمي. لكنه خريطة لمواضع تتقرأ في الجزء 2 بحسب أولوية الاستوديو (أرقام صفحات الكتاب):
- **Absolute difficulty** (322–324, 329, 420–425)، **Difficulty / Dynamic difficulty adjustment** (418–428)، **Balance/Dominant strategy** (403–411, 413–416)، **Positive feedback** (429–433)، **Negative feedback** (432–433).
- **Challenges** (فصل 13: 323–339)، **Core mechanics** (351–402)، **Progression** (374–378, 452–453)، **Internal economy** (366–374).
- **Game concept** (125–136)، **Casual-related: freemium (118–119)، IAP (111, 118)، free-to-play (111, 119)، crippleware (118)، DLC (118)، advertising (119–120)**، **cheating/technical security** (482–484).
- مصطلحات الـ Glossary ظاهرة في الـ index (attract loop، atomic challenges، branch points…) هتتذاكر مع فصولها.

**للاستوديو:** فصل 15 (Balancing) + فصل 13 (Gameplay) هم أول مرشحين للقراءة بعمق لأنهم بيغطوا بالظبط المشاكل اللي بنقيسها بالـ tester-bot (absolute vs perceived difficulty، DDA، positive feedback في merge chains). وفصل 6 للـ monetization/ads. ومن الـ index: **perceived difficulty** و**in-game experience** مفاهيم محددة بتتعرّف في فصل 15، وهتفيد في تحويل bot_difficulty لـ metric قريب من تجربة اللاعب مش من الأرقام الخام.

---

## ملخص المستوى الأعلى للجزء (التحويل لقرارات) ★★★

1. **Idea intake template** من الأسئلة الأربعة + domain card (6 domains) + dedication point — يتطبق على كل لعبة جديدة قبل البروتوتايب.
2. **Exclusionary-material gate** (4 turnoffs للنساء + محتوى عرقي/gore/ugly art) في art review وفي creative الإعلانات.
3. **CPI test بعقلية overlap**: قارن الـ segments بالتوزيع مش بالمتوسط، وارفض «أضف features لإرضاء الكل».
4. **Reusable systems** مدعومة بالفصل: tutorial تفاعلي قصير، save/resume في أي نقطة (جلسات 30د–2س)، **collection + customization** كـ meta-layer لأي لعبة، **difficulty modes** (نموذج GoldenEye) لجسر casual↔core.
5. **تحذير منهجي:** أرقام الفصل (31% و19%) من ESA 2013 وغربية. آدمز نفسه بيحذر إن الـ generalities غربية وإن أسواق زي الهند والصين وكوريا واليابان ممكن تختلف. نقيس segments جمهورنا الفعلي من الـ analytics، والكتاب مصدر فرضيات مش حقايق عن جمهورنا.

**الباقي (الـ Front matter/Index/الغلاف الإعلاني):** تعريفات وإعلانات ناشر وتوثيق بلا محتوى تصميمي إضافي — متجاهل ما عدا اللي اتسجل فوق.

# Adams — Fundamentals of Game Design (الجزء 2 من 2) — نوتس مذاكرة

**تنبيه قبل أي حاجة:** الجزء ده **مفيهوش أي نص فصول**. هو الـ Index بس (من آخر حرف I لحد Z، صفحات 545–560 في الكتاب) من غير محتوى الفصول نفسها. مفيش هنا تاكتيك ولا رقم ولا مثال ولا شرح، وأنا مش هألف محتوى ممكن يكون مش في الكتاب. «بلا فقد» معناه إني ما أمثلش إني ذاكرت فصول ما شفتهاش.

اللي عملته: سجلت كل حاجة في الـ Index كـ **خريطة موضوعات بأرقام الصفحات**، ورتبتها حسب الأهمية للاستوديو. دي بتتحول لنوتس حقيقية أول ما المتن يتبعت.

**ترقيم الفصول:** مفيش سياق سابق عندي (الجزء 1 مش مرفق)، فمش هخمّن أرقام فصول. بستخدم **نطاقات الصفحات** اللي الـ Index بيثبتها، وهربط بأرقام الفصول لما الجزء 1 يوصل.

---

## 1. خريطة الأقسام الكبيرة (من نطاقات الصفحات) — ما هو مثبت في الـ Index

| النطاق | الموضوع |
|---|---|
| 69–78 | Genres: shooters (69–70)، action (71–72)، strategy (72–73)، RPG (73–74)، sports (74–75)، vehicle sims (75–76)، construction/management (76–77)، adventure (77)، puzzle (78) |
| 81–102 | فهم اللاعب: VandenBerghe's Five Domains of Play، ولاد/بنات، رجال/ستات، dedication |
| 103–124 | الـ Machines والفلوس: consoles / PCs / portable، direct/indirect payment، world markets |
| 125–135 | Game concept: المفهوم، الـ target audience، الـ unique selling points |
| 137–163 | Game world: physical/temporal/environmental/emotional/ethical dimensions |
| 167–205 | Characters: avatars، visual appearance، personality، voice |
| 207–253 | Storytelling: interactive stories، branching/foldback/emergent، dialogue trees، episodic |
| 255–312 | User Interface: camera models، visual/audio elements، input devices، navigation، accessibility |
| 315–347 | Gameplay: challenges، actions، saving |
| 351–400 | Core mechanics: internal economy، progression، tactical maneuvering، social mechanics |
| 403–436 | Balancing: fairness، dominant strategy، difficulty، feedback loops |
| 439–470 | Level design: layouts، pacing، tutorial levels، pitfalls |
| 471–500 | Online games: synchronous/asynchronous، persistent worlds، social problems |

---

## 2. مصطلحات وأرقام صفحات تخص الاستوديو مباشرة ★★★

دي المواضع اللي لازم يتسحب منها محتوى أول ما المتن يوصل. كل بند عليه صفحاته.

**Balancing وDifficulty (403–436) — أعلى أولوية:**
- **Perceived difficulty** (420–425)، و**Power provided** (420–423)، و**Native talent** و**Previous experience** (419–422)، و**Intrinsic skill required** (321–323). الكتاب بيفكك الصعوبة لعناصر.
- **Consistent range of difficulty** (405، 418، 425) و**Sawtooth difficulty progression** (424): منحنى صعوبة على شكل سن المنشار.
- **Positive feedback** (404، 429–433) و**Negative feedback** (432–433) و**Stalemates** (404–405، 417، 430) و**Stagnation** (433–434). دول بيربطوا مباشرة بالـ merge games اللي فيها snowball.
- **Dominant strategy:** PvP (406–410) وPvE (410–411) واختبار وجودها (411).
- **Transitive** (405–407) و**Intransitive** (408–409) relationships، و**Rock-paper-scissors** (408–409)، و**Shadow costs** (407، 409)، و**Orthogonal unit differentiation** (409).
- **Learn-by-dying designs** (417، 441–442)، و**Shot clock in basketball** (405) كمثال على كسر الـ stalemate، و**Avoiding trivialities** (434).
- **Tuning stage** (54، 435–436) و**Pseudo-random numbers** (396–398، 436) و**Monte Carlo simulation** (396–397).
- **Gaussian curve / Uniform / Nonuniform distribution** (395–399) للأرقام العشوائية.

**Level design (439–470):**
- **Pace** (441، 453–455)، و**Progression** (451–453، 467–468)، و**Atmosphere** (450–451)، و**Tutorial levels** (455–457).
- **Layouts** (445–449): linear / open / parallel / network / ring.
- **Level design process** (457–465): planning (459–462) وprototype (462–464) و**Level review** (463) و**Lock-down** (464) وtesting (465).
- **Pitfalls** (465–468): scope (465–466)، و**conceptual non sequiturs** (466–467)، و**Twinkie Denial Conditions** (468).
- **Genre-specific level design** (443–445) و**universal principles** (441–442).

**Core mechanics (351–400):**
- **Internal economy** (352، 366–372) بمصطلحات: source، drain، converter، trader، production mechanism، tangible/intangible resource، feedback loops، mutual dependency، deadlock، **Runaway profit problem** (369).
- **Static equilibrium** (373–374).
- **Progression mechanics** (353، 375–378).
- **Tactical maneuvering** (352، 378–383).
- **Social interaction mechanics** (352، 383–386).
- **Simplicity of core mechanics / generalizing** (389–390).
- **Machinations** (372) كأداة لنمذجة الاقتصاد.

**Gameplay / challenges (315–347):**
- **Atomic challenges** (simultaneous 319–321)، و**Intermediate challenges** (318)، و**Victory condition** (317–319).
- **Time pressure** (322–323، 325، 328–329)، **Pattern recognition** (330)، **Memory** (329)، **Logical/Mathematical** (326–328)، **Lateral thinking puzzles** (338–339).
- **Stealth learning** (27، 335)، **Perfect information** (334)، **Pure strategy** (334).
- **Saving:** save slot، quick-save (345)، level access codes (344)، save-affecting-story (344).

**Money (113–124) — لخط الإنتاج والإعلانات:**
- **Direct payment:** retail (113–115)، subscription (115–116، 119، 251)، time-based subscription على الموبايل (111).
- **Indirect payment:** **Pay-to-win** (118)، upgrades (118–119)، **sponsorships and advertising** (119–120)، **sponsored/commissioned games** (120).
- **Sportsmanship** (118) كمصطلح مرتبط بالـ pay-to-win.
- **World markets** (120–123): Islamic world market وMexico (123)، traditional markets (121–122)، language/localization (120–123، 286).

**Players (81–102):**
- **VandenBerghe's Five Domains of Play** (81–83)، و**OCEAN** (81).
- **"Seven Kisses of Death"** (90–92) للعب الأطفال، و**Piaget** (89–92).
- **Gamer dedication** (96–98)، و**Binary thinking** (98–100)، و**Reasoning statistically about player groups** (98–99)، و**Inclusiveness not universality** (100).
- **Nena Media** وMattel (93–94) للـ games for girls.
- **Representative player** (32–33، 47، 81–83): اختبار كل قرار تصميمي عليه.

**UI (255–312):**
- **Interaction models:** multipresent / omnipresent / party-based (269–270، 303–304).
- **Input devices:** 0D، 1D (297–299)، 2D (294–296)، 3D (292–294).
- **Navigation:** avatar-oriented وscreen-oriented steering (300–302)، point-and-click (139، 303–304)، waypoints (304).
- **Accessibility** (304–308): vision/hearing/mobility، Vischeck (305–306)، magnification، subtitles، vibration، speed. **Customizing UI** (308–309) و**restore defaults** (309).
- **Complexity management** (267–269)، **shell menus** (44، 266، 309)، **tooltips** (283)، **mini-maps** (284)، **fonts** (286–287)، **UI prototyping** بـ PowerPoint (264).

**Storytelling (207–253):**
- أنواع القصص: linear (221–222)، branching (222–226)، foldback (227)، multilinear، emergent narrative (228–230).
- **Storytelling engine** (219–221)، و**Granularity** (232)، و**Dramatic vs gameplay tension** (217–218)، و**Endings** (230–232)، و**Frustrated author syndrome** (247).
- **Episodic delivery:** limited series (250–251)، unlimited series (248)، serial (248–250).
- **Dialogue trees** (239–245) وأدواتها: Twine، Scrivener، Scapple (242).
- **Emotional limits of interactive stories** (235–237).

**Online (471–500):**
- **Synchronous vs asynchronous** (476–482)، و**Latency/Lag** (474)، و**Technical security** (482–484).
- **Persistent worlds** (484–494)، وسياسة **avatar death** (491–492)، و**Permanent death** (491).
- **Social problems** (494–499): chat moderation (495–496)، player-killing (496–499)، warning systems، profanity filters (495).

**Team وProcess (من الـ Index):**
- **Elaboration stage:** iterate (52–53)، irresolution (48).
- **Scrum وsprints** (53).
- **Design roles** (54–57)، **Treatment document** (58–59)، **Requirements specification** (209).

---

## 3. للاستوديو (قراءة الـ Index فقط — مش استنتاجات من المتن)

**(1) Mossfolk:**
- المصطلحات اللي في الكتاب (Positive feedback وStalemates وSawtooth وPerceived difficulty وRunaway profit) هي الأقرب لـ `bot_difficulty` وللـ snowballing في الـ merge.
- صفحات 419–425 و429–434 أول حاجة تتسحب لما المتن يوصل.
- **Twinkie Denial Conditions** (468) وLearn-by-dying (417، 441) بيلمّحوا لنقاش «الفشل غير العادل»، ولازم يتقرا في سياق ميزانية الإسقاطات.

**(2) خط الإنتاج السريع:**
- **Tuning stage** (435–436) وPseudo-random (436) وMonte Carlo (396–397): الكتاب بيعتبر المحاكاة العددية أداة موازنة، وده نفس فكرة التيستر-بوت.
- **Machinations** (372) أداة نمذجة اقتصاد تتقارن بالتيستر-بوت عندنا قبل البروتوتايب الكامل.
- **Pay-to-win** (118) وsponsorships وadvertising (119–120) وlocalization (286، 120–123) تتقرا في سياق الإعلانات والـ CPI.
- **Representative player** (32–33، 47، 81–83) كعدسة اختيار أفكار: كل قرار يتفحص على لاعب مرجعي.

---

## المطلوب عشان المذاكرة الفعلية تتم

ابعت **متن الفصول (صفحات 1–520 تقريبًا)**. لو كان الجزء 1 هو المتن، ابعته. ولو الاستخراج وقف عند الـ Index، يبقى محتاج يتعمل من تاني.

بالمتن هعمل نوتس لكل فصل بنفس الفورمات: التاكتيك والرقم والمثال والباترن وراه، وسطر «للاستوديو» بمستويين. وهرقّم الفصول من الجزء 1.

**اقتراح ترتيب** لو المتن كبير: 403–436 (Balancing) أولًا، وبعده 439–470 (Level design)، وبعده 351–400 (Core mechanics). دول أعلى قيمة للاستوديو.

# Adams — Fundamentals of Game Design (الجزء 2 من 2) — نوتس مذاكرة

**المصدر:** الجزء ده هو **الـ Index بتاع آخر الكتاب بس (من "Inspiration" لحد "Zero-dimensional characters"، صفحات 545–560)**. مفيش فيه نص أي فصل. الجزء 1 (حرف A–H في الـ index) مش في السياق، وأول سطر مقطوع من النص (`rview of 290–291`).

**اللي هعمله وإللي مش هعمله:**
- الـ index بيقول **فين** كل فكرة وبيقول **إيه الأفكار الموجودة**، لكنه مش بيقول الشرح. مش هألف محتوى فصول مقراتش نصها.
- هسجل كل مدخل تصميمي فيه مع أرقام الصفحات، مجمّعًا بالفصول اللي بتتحدد من نطاقات الصفحات.
- مفيش جزء 1 في السياق، فمش هكمل ترقيم فصول من حاجة مش قدامي. بدل كده بسمي كل مجموعة بنطاق صفحاتها (§A…§L).
- أي حاجة جاية من معرفتي العامة مش من النص هتتعلّم **[خارج المصدر]**.
- في الآخر قائمة سحب بالأولويات، عشان الفصول الفعلية تتسحب بنفس البايبلاين.

---

## §A — Balancing / Tuning (ص 395–436) ★★★ أهم مجموعة لينا

الـ index بيكشف إن الـ balance عند Adams هو الأكبر في المحتوى الرياضي والـ playability:

- **PvE vs PvP**: لكل واحد balancing خاص (404–405). الـ **dominant strategy** ليه مدخلين منفصلين: PvP (406–410) وPvE (410–411) + **"testing for dominant strategies" (411)** كخطوة تطبيقية.
- ★★ **العلاقات بين الوحدات**:
  - **Transitive (405–407)** = أقوى/أضعف خطي.
  - **Intransitive (408–409)** = حجر-ورقة-مقص (RPS، مذكور كمان باسم Rochambeau / scissors-paper-stone).
  - **Orthogonal unit differentiation (409)**.
  - **Shadow costs (407, 409)** = تكلفة مخفية بتوازن الوحدة. **[خارج المصدر: وحدة قوية بتتحاسب عليها تكلفة غير ظاهرة في التسعير]**.
- **Fairness (412–417)**: symmetric games (413–414)، **point assignment system (414–415)**، وPvE fairness (416–417) بمدخل **learn-by-dying (417, 441–442)**.
- ★★★ **Perceived difficulty vs relative difficulty (420–425)**:
  - العوامل المسماة: **native talent, previous experience, skill (404, 419), power provided (420–423)**.
  - **"consistent range of difficulty" (405, 418, 425)**.
  - **Sawtooth difficulty progression (424)** = منحنى سن المنشار.
  - Multiplayer difficulty modes (425).
- ★★★ **Feedback loops**: **Positive feedback (404, 429–433)** و**Negative feedback (432–433)** → **stagnation (433–434)** و**stalemates (404–405, 417, 430)**. مثال الـ stalemate المذكور: **shot clock في كرة السلة (405)**.
- **Trivialities, avoid (434)**: لازم يتفحص وجود قرارات تافهة.
- **Tuning stage (54, 435–436)**: مرحلة مستقلة في دورة التطوير.
- ★★ **الأرقام العشوائية (395–399)**: Gaussian curve، Uniform vs Nonuniform distribution (397–398)، **Pseudo-random numbers (396–398, 436)**، **Monte Carlo simulation (396–397)**.
- **Other**: Powerup (411)، Wildcard enemy، Runaway profit problem (369).
- **الباترن ورا المجموعة:** Adams بيتعامل مع الـ balance كـ**مجموعة أنماط مسماة بأعراض وعلاج** (dominance، stalemate، stagnation، runaway). ده اللي يخليها تتحول لـ checklist مش حدس.

**للاستوديو:**
1. **Mossfolk:**
   - منحنى الصعوبة: sawtooth (424) مقابل الخط المستقيم بتاعنا في 3000 ليفل.
   - الـ merge بطبيعته positive feedback (كبير يعمل أكبر)، فنراجع هل عندنا negative feedback مقابل (حد البرطمان / ميزانية الإسقاطات) ولا فيه runaway/stalemate.
   - الـ pseudo-random (396–398) هو موضوع RNG التوزيع بتاع القطع.
2. **خط الإنتاج:**
   - قائمة الأعراض (**dominant strategy، stalemate، stagnation، runaway، trivial decisions**) تتحول لـ **تقارير ثابتة من التيستر-بوت** لكل لعبة جديدة قبل الـ CPI test.
   - نكتب لكل لعبة جدول "ممكن تتكسر إزاي" في ساعة واحدة.

---

## §B — Core Mechanics (ص 351–395) ★★★

- **ترجمة القواعد لميكانيكا** (351–352) + **Physics as game mechanics (352)** (مهم لموسفولك).
- ★★ **تشريح الميكانيكا (362–366)**:
  - events & processes (354, 362)، conditions (364)، relationships بين الـ entities (362).
  - **Entities** بأنواعها: simple (359)، unique (361)، numeric/symbolic (364). و**Resources vs entities (358–359)**.
  - **Numeric vs symbolic relationships (364–366)**.
  - **Machinations (372)** = أداة/إطار لرسم الاقتصاد الداخلي.
- ★★ **Internal Economy (352, 366–372)**:
  - **Source (367)، Drain (367–368)، Production rate (367)، Production mechanism (369)، Trader (368–369)، Converting resources (368)**.
  - **Tangible vs Intangible resources (369–370)**.
  - **Mutual dependency، feedback loops، deadlocks (370–371)**.
  - **Runaway profit problem (369)**.
  - **Static equilibrium (373–374)**.
- **Progression mechanics (375–378)**: **One-way door (234, 375)**، locked doors (331, 375)، reversing time (376)، pause (376)، tracking time and progress (376–377)، triggers (377).
- **Tactical maneuvering (378–383)**: space control, regions (378)، grids (380)، obstacles (380)، landscape objects (381)، units attributes: maneuverability/observation range/range/range of fire (382–383).
- **Social interaction mechanics (383–386)**.
- ★★ **Simplicity of core mechanics (389)** و**Generalizing (389–390)**.
- ★★★ **"Test every mechanic" (395)**.
- **Turn-based vs real-time (355–356)** و**core mechanics detecting termination (355)** و**level design relation (356–357)**.
- **الباترن:** الميكانيكا عند Adams = **اقتصاد (مصادر/مصارف/محوّلات) + علاقات رقمية/رمزية بين كيانات** — مش "فيتشرات". وده اللي يخلي التحليل الكمي ممكن.

**للاستوديو:**
1. **Mossfolk:** نرسم الاقتصاد (**source = الإسقاطات، drain = امتلاء الجرة، converter = الدمج**) ونفحص هل فيه mutual dependency أو deadlock (ليفل يتقفل بدون حل).
2. **خط الإنتاج:** رسم Machinations-style من صفحة واحدة لكل فكرة قبل البروتوتايب. الفكرة اللي مفيهاش **source/drain/converter واضحين** غالبًا مش هتتحمّل إيقاع الإنتاج السريع. الميكانيكا اللي تعدي الفحص دي تتحول لموديولات reusable.

---

## §C — Challenges & Actions (ص 315–347) ★★★

- **Victory condition (317–319)**، **Atomic challenges (simultaneous 319–321)**، **Intermediate challenges (318)**، **Tutorial levels بتقابل الـ atomic challenges (317)**، **"information about challenges" (317)**.
- ★★ **Intrinsic skill & stress & time pressure (321–323)**.
- **التصنيف حسب النوع:**
  - **Physical coordination** (17, 324–326): speed/reaction (324)، precision/accuracy (324–325)، rhythm/timing (325).
  - **Time pressure** (17, 322–323, 325, 328–329): races.
  - **Logical/Mathematical (89, 326–328)**، formal logic puzzles، **Lateral thinking puzzles (338–339)**.
  - **Memory (17, 329)** و**Pattern recognition (17, 330)** و**Spatial awareness (330–331)**.
  - **Exploration (331–332)**: mazes، traps، locked doors، unmarked switches، teleporters (332)، **hidden objects (332–333)**.
  - **Strategic/tactical (334)**: perfect information (334)، pure strategy (334)، situational analysis (334).
  - **Logistics (335)**، **reducing enemy forces (335)**، **survival (335, 378)**، **stealth learning (27, 335)**.
- **Actions (340–343)**: participation، self-expression، social، **sightseeing (342)**، **unstructured play (342)**.
- ★★ **Saving (343–347)**: level access codes (344)، **quick-save (345)**، save slot (345)، وتأثير الحفظ على القصة (344).

**الباترن:** Adams بيجمع التحديات حسب **القدرة الذهنية/الجسدية المختبَرة**، فيسهل نحدد أي قدرة لعبتنا بتختبرها وهل فيه تنوع.

**للاستوديو:**
1. **Mossfolk:** اللعبة أصلًا **spatial + precision (الإسقاط) + planning**. التحديات بعد 2501 (shells/stones/rot) نصنفها بالجدول ده ونشوف هل بتضيف **نوع تحدي جديد** (pattern/memory/logistics) ولا مجرد رقم أصعب.
2. **خط الإنتاج:** نصنف كل فكرة جديدة بنوع التحدي. لو آخر 5 ألعاب كلها "precision + time"، نختار الفكرة السادسة من نوع تاني. ده فلتر تنويع رخيص قبل البروتوتايب.

---

## §D — Level Design (ص 439–470) ★★★

- **الأساسيات الكونية (441–442)**: **Pace (441)**، **Risk/reward (441–442)**، **Resources (441)**، **Learn-by-dying (417, 441–442)**، tutorial levels (441).
- **Genre-specific (443–445)**: shooter, RPG, puzzle, simulation, sports, vehicle, strategy، وكل جنر ليه مدخل خاص.
- ★★ **Layouts (445–449)**: **Linear (445–446)**، **Open (445)**، **Parallel (446–447)**، **Network (447–448)**، **Ring (447)**.
- **Atmosphere (450–451)**: lighting، weather، music، visual effects.
- **Progression (451–453)** وعلاقتها بـ **perceived difficulty (422–425, 452)**.
- ★★ **Pacing (453–455)**، **Tutorial levels (455–457)**.
- ★★★ **Level design process (457–465)**:
  - **Planning phase (459–462)**: layouts, props, NPCs, landmarks (460)، save points (460)، spawn points (460)، resources (460).
  - **Prototype (462–464)**: textures, rigging (462, 464), performance (461).
  - **Level review (463)**، **Lock-down (464)**، **Testing (465)**.
- ★★ **Pitfalls (465–468)**: **Scope (465–466)**، **conceptual non sequiturs (466–467)**، progression pitfalls (467–468)، **"Twinkie Denial Conditions" (468)**. التعريف مش في الـ index، فيتسحب من الصفحة.
- **Level designer role (55, 439–440, 458)**.

**الباترن:** Adams بيدي الـ level design **عملية بمراحل وبوابات** (plan → prototype → review → lock-down → test). ده الفرق عن "ارسم الليفل واجرّبه".

**للاستوديو:**
1. **Mossfolk:** الـ 3000 ليفل محتاجين **pacing curve** مكتوب (مش sawtooth عشوائي)، وLock-down واضح قبل أي تغيير في أهداف الليفل (علشان بيانات البوت تفضل قابلة للمقارنة).
2. **خط الإنتاج:** نسخة مصغرة من بوابات Adams لكل لعبة: **Plan (ساعة) → Prototype → Review → Lock**، وتتحدد أيام لكل بوابة بدل ما الميزان يبقى "لما نحس إنها كويسة". وكمان تمنع **scope creep (465–466)**.

---

## §E — Player Understanding (ص 81–102) + Player-centric (32–36) ★★

- **Representative player (32–33, 47, 520)**: كل قرار تصميم يتفحص ضده.
- **Player-centric vs self-centered (33–34)**، **Market-driven vs technology-driven (35–36)**، **Professionalism (33–34)**.
- ★★ **Five Factor Model / OCEAN (81–83)** + **VandenBerghe's Five Domains of Play**، والمجالات المذكورة: **Stimulation, Threat, Novelty (82)**، وفيه Narrative/Strategic immersion (83).
- **الفروق بين الجنسين وأعمار اللاعبين:**
  - رجال/نساء (84–88)، **binary thinking (98–100)**، و**"strive for inclusiveness, not universality" (100)**.
  - البنات (92–96): Nena Media (93–94)، Mattel (94)، أنواع قصص البنات (95).
  - الأطفال: **Piaget (89–92)**، **"Seven Kisses of Death" (90–92)**، القراءة (90)، visual design (90)، voiceover (90)، trial and error (91).
- **Gamer dedication (96–98)**، **walkthrough mode (25, 83)**.
- نقطة "النساء بيحبوا تحديات ذهنية/اجتماعية وبيتعلموا بالتيوتوريال" (85–86).

**الباترن:** Adams بيحذر من **التفكير الثنائي في فئات اللاعبين** ويفضّل الكلام بالإحصاء ("reasoning statistically").

**للاستوديو:**
1. **Mossfolk:** جمهور الـ hybrid-casual ميل لـ puzzle/mental challenges (ص 86)، فنراجع الـ onboarding حسب فئات الصبر.
2. **خط الإنتاج:** نحدد **representative player واحد مكتوب لكل لعبة** قبل أي تصميم، ونستخدمه كمرجع في مراجعات الـ CPI بدل رأي الفريق.

---

## §F — User Interface (ص 255–312) ★★

- **مبادئ UI (257–262)**: short-term memory (258)، shortcuts (258)، physical stress (258)، وبيشرح اللاعب محتاج إيه (حسب الكيان: objects/NPCs/numbers/orders/options (261–262))، و**risk/reward (260)** و**progression (260)**.
- **UI process (263–266)**: **PowerPoint prototype (264)**، screen layout (265)، mapping input to actions (266)، shell menus (44, 266).
- ★★ **Complexity (267–269)**: simplification (267–269)، menus (268–269).
- **Interaction models (39, 269–270)**: **Avatar-based, Multipresent (303–304), Omnipresent (270), Party-based (237, 303–304)**.
- **Camera (271)**: pan, tilt, roll, truck. **Perspectives (272–279)**: first-person, third-person, aerial, isometric (143, 276–277)، top-down (276)، side-scrolling (279)، top-scrolling، **context-sensitive (278)**.
- **Visual elements (280–287)**: main view، overlays/transparency (280–281)، windowed views، indicators (symbolic 282–283، numeric 282, 284–285)، tooltips (283)، mini-maps/radar (284)، screen buttons (285)، **fonts (286–287)**: serif/sans/monospaced.
- **Audio (287–290)**: sound effects, positional audio (288)، **pitch variation للأصوات المتكررة (288)**، rumble (288, 306)، music (289)، voiceover/dialogue (290)، تكرار (290).
- **Input devices (290–299)**: 0D (zero-dimension)، 1D (297–299)، 2D (294–296)، 3D (292–294)؛ Wii Remote (292–294)، Nunchuck (293)، Wii Motion Plus (293)، Kinect (298–299)، joystick/trackball/touch (295–296)، pressure-sensitive buttons (298).
- **Navigation (300–304)**: steering (screen-oriented 300–301، avatar-oriented 301–302)، point-and-click (139, 303–304)، waypoints (304)، pathfinding (303).
- ★★ **Accessibility (304–308)**: vision (magnification 305, Vischeck 305–306)، color blindness، hearing (subtitles 307, visual cues 306)، mobility (speed 307, 423)، older players (307)، volume (306).
- **Customization (308–309)**: **Restore defaults (309)**.

**الباترن:** الـ UI عند Adams = **وسيط بين الـ core mechanics واللاعب** (37)، وبيتبني بروتوتايب مبكر بأرخص أداة.

**للاستوديو:**
1. **Mossfolk:** تحقق من color-blind (Vischeck) على ألوان المخلوقات الـ 9 (مهم جدًا في الدمج)، وpitch variation لصوت الدمج المتكرر، والـ haptic.
2. **خط الإنتاج:** **قالب UI/accessibility checklist** reusable بين الألعاب: color-blind، حجم الخط، صوت، vibration، restore defaults. ده أرخص نظام مشترك.

---

## §G — Storytelling & Narrative (ص 207–253) ★ (أقل أولوية لـ hyper-casual، مهم للـ side quests)

- **أسباب وجود قصة (207–209)**، **Requirements specification (209)**، طول القصة (208, 210)، **ما تريد تحقيقه (209–210)**.
- **Interactive story (212–214)**، **Narrative events (213–214, 232)**، **Player events (212–214)**.
- **Tension: dramatic vs gameplay (217–218)**، randomness وrepetition وأثرهم (218).
- **Storytelling engine (219–221)**.
- ★ **أنواع الهيكل**:
  - **Linear (221–222)**
  - **Branching (222–226)** + cumulative influence (223)
  - **Foldback (227)**
  - **Multilinear (227)**
  - **Emergent narrative (228–230)**
  - Journey (233–235)
  - **Endings (230–232)** وpremature endings (231, 236)
- **Granularity (232)**، **Emotional limits (235–237)**.
- **Scripted conversations / dialogue trees (237–246)**، أدوات: **Scapple, Scrivener, Twine (242)**.
- **Episodic delivery (248–251)**: **Unlimited series (248)**، **Serial (249)**، **Limited series (250–251)**.
- **Frustrated author syndrome (247)**، **متى تكتب القصة (246–247)**.

**للاستوديو:** هايبر-كاجوال غالبًا من غير قصة، لكن **Episodic/Serial (248–251)** مناسبة جدًا للـ side quests في Mossfolk (rival contests كحلقات). **Foldback (227)** أرخص هيكل متفرع للتنفيذ السريع.

---

## §H — Characters & Avatars (ص 183–204) ★

- **Avatar**: specific / nonspecific / partially-specified (184–186)، علاقة اللاعب بالـ avatar (182–186)، **photorealistic response (185)**.
- **Visual (186–195)**: **nonhumanoid (186–187)**، animals/machines/mermaids/monsters، **body types (187–191)**: tough (188)، hypersexualized (190–191)، **clothing/weapons/jewelry/names (191–193)**، **Model sheet (192–193)**، **color palette (194)**، **sidekicks (194)**، superheroes (194)، Sculptris (195)، story-driven (195).
- **Personality (196–202)**: **roles & values (196–198)**، **status attributes (169, 198)**، **dimensionality 0D→3D (199–200)**، **archetypes (201–202)**.
- **Voice (203–204)**: vocabulary، sentence construction، **vocal quirks (204)**، avoid stereotypes (204).

**للاستوديو:**
- **Mossfolk:** مخلوقات الـ 9 أحجام = شخصيات nonhumanoid. **Model sheet (192–193)** وcolor palette (194) هما أداة للـ consistency بين الأحجام وألوان قابلة للتمييز.
- **خط الإنتاج:** **Model sheet template** ثابت وpalette rules لكل لعبة جديدة يوفر وقت الـ art.

---

## §I — Game World & Creative Play (ص 137–179) ★★

- **Magic circle (3–7, 137–138)**، pretending (1, 3–5)، sports games من غير world (137).
- **Physical dimension (139–146)**: spatial (139–142)، **scale (142–144)**، relative size، perspective، vertical، speed distortion (144)، boundaries (144)، locations (144–146).
- **Temporal (146–148)**: **variable time (146–147)**، verisimilitude (148).
- **Environmental (150–155)**: physical aspects (150–151)، mood/tone (151)، sound، **visual style (14, 152–153)**، **inspiration (153–155)**، **overused settings (153–154)**.
- **Emotional dimension (156–158)** و**Ethical (157, 159–161)**: moral decision-making، violence (161–162).
- **Realism (37–38, 51, 162–163)**، make-believe، "unclear line between fantasy and real" (162).
- ★★ **Creative play**: **Self-defining play (167–171)** (personality expression 167–168، avatar sex 171)، **Constrained creative play (172–174)** (physical standards 172–174)، **Sandbox (175)**، **Storytelling play (177)**، **Mods (177–178)**، **Level editors (178–179)**، **Sharing creations (171)**، **IP rights (127, 178)**.

**للاستوديو:** **Level editor/sharing (171, 178–179)** فكرة UGC ممكن تتحول لـ reusable system بين الألعاب. **Constrained creative play (172–174)** يناسب الـ minigames.

---

## §J — Business & Markets (ص 113–124, 126–132) ★★ (للـ CPI والإعلانات)

- **Direct payment (113–117)**: **Retail (113–115)** (manufacturing, marketing, royalties 114، conservatism of publishers 114–115)، **Subscription (115–116)**.
- ★★ **Indirect (117–120)**: **Pay-to-win (118)**، **upgrades (118–119)**، **sponsorships/advertising (119–120)**، **sponsored (commissioned) games (120)**، sportsmanship (118)، sponsorship في sports/vehicle (120).
- **World markets (120–123)**: **language (120–123)**، **traditional (121–122)**، **dating sim (122)**، **Islamic world (123)**، **Mexico (123)**، body types of characters by culture (189).
- **Platforms (103–113)**: consoles + **licenses/NDAs (105)**، PCs (105–109)، **mobile (109–111)**: **time-based subscription (111)**، **3D on low-end (272)**، screen layout (265)، wireless; portable (109–111)، **phablet (109)**، smartphones (298)، microconsoles/Ouya (106)، **networked play (105–106, 109)**.
- **Concept stage**: **quantity of ideas in brainstorming (128)**، ideas from other media (126–127)، poetry، **game concept document**: actions/role (131–132)، **target audience (130, 133–134)**، **unique selling points (130)**، storyline، monetization (130).

**للاستوديو:** **"Quantity of ideas, brainstorming" (128)** هو نفس منطق خط الإنتاج. **Pay-to-win (118)** مذكور كنموذج منفصل، وده يربط بمبدأ "مفيش طاقة تمنع اللعب". **Localization (286, 514)** مرتبط بالـ fonts واللغة. **ملحوظة:** كل أرقام الأسواق من 2012–2014 تقريبًا، فتتراجع قبل الاعتماد.

---

## §K — Process, Team & Documents (ص 32–65) ★★

- **المراحل**: Concept (47)، **Elaboration (48–53)**: **irresolution (48)**، **iterate (52–53)**، paper prototypes (49–50, 62)، physical prototypes (50)، software prototypes (49)، **Tuning (54, 435–436)**، **Scrum + sprints (53)**.
- **الفريق (54–57)**: lead designer، **level designer (55)**، **mechanics designer (55)**، UI designer (55)، world builder (55)، writers (56, 64)، producer/project manager (56)، lead programmer (56).
- **الوثائق (56–62)**: **treatment (58–59)**، **moveset (59–60)**، **world design (60)**، **UI design (60)**، **on-screen text & audio script (61–62)**، **story and level progression (56)**، storyboards (55–56)، **requirements specification (209)**.
- **Research (64)**.

**للاستوديو:** **Elaboration مبنية على iterate (52–53)** وتعتمد على **paper prototypes (49–50)** لتقليل تكلفة التجارب. **Treatment document** قالب قصير لكل فكرة.

---

## §L — Online & Persistent Worlds (ص 471–500) ★

- **مزايا (471–473)** وعيوب (473–476) اللعب أونلاين: **latency (474)**، **P2P (474)**، **packets (475, 483)**، monetization (475)، **suspension of disbelief (475)**.
- **Synchronous (476–481)**: **arriving (476–477)**، **disappearing (477–479)**، real-time vs turn-based (479–480). **Asynchronous (481–482)** و**single-player cooperative (482)**.
- **Security (482–484)**: serial numbers (483)، secure protocol (483)، sensitive data (483–484).
- **Persistent worlds (484–494)**: vs ordinary (485–487)، MUDs (485, 488)، types of players (488)، **avatar creation/autobiography (488–489)**، **world models (490–491)**: **scavenger (490)**، PvP، **social model (490)**، **avatar death (491–492)**، permanent death (491)، resurrection (2, 491)، **time (492–493)**، **economies (493)**، meditation (493)، secrets (494).
- **Social problems (494–499)**: chat (494–496)، **moderated chat (496)**، **profanity filters (495)**، **warning systems (495)**، **player-killing (496–499)**، shards (497)، **switch (498)**، **safe games (498)**، faction-based (498)، **managing expectations (498)**.

**للاستوديو:** **Rival contests (Mossfolk)** يستفيد من **asynchronous (481–482)** بدل real-time (يلغي latency/security). الـ MMOG تفصيل بعيد عن الـ hyper-casual.

---

## ملاحظات على الجزء ده نفسه

- **مفيش محتوى فصل متسجل فيه.** الـ index بيثبت وجود المفاهيم وصفحاتها بس.
- **قائمة السحب بالأولوية** (ترتيب الفصول الفعلية): **1) Balancing 395–436** ← **2) Core mechanics 351–395** ← **3) Challenges 315–347** ← **4) Level design 439–470** ← **5) UI/accessibility 255–312** ← **6) Players 81–102** ← **7) باقي الفصول**.
- مصطلحات محتاجة تعريف من الصفحة نفسها قبل الاعتماد: **Twinkie Denial Conditions (468)، Shadow costs (407, 409)، Orthogonal unit differentiation (409)، Learn-by-dying (417, 441–442)، Sawtooth difficulty progression (424)**.
- لو بعت لي نص الفصول (حتى صفحات الـ Balancing لوحدها)، أكتب النوتس بالتفصيل بالأرقام والأمثلة والباترن ورا كل تاكتيك بنفس الفورمات.

