# Tom Lehmann (مصمم Race for the Galaxy): تصميم ألعاب كروت استراتيجية (JcyyeAww2wc، ~61 دقيقة) — نوتس مذاكرة

ملاحظات قبل ما نبدأ:
- المحاضرة على الأرجح من GDC (فيه تقييمات جمهور وQ&A). مفيش عنوان رسمي في الترانسكريبت.
- هدف Tom المعلن: **أفكار تخلّي لعبتك أكتر strategic**. اللعبة كروت طاولة، فكل تطبيق على موبايل ده نقل مبدأ مش نسخ.
- **الـ takeaways slide اتعرضت بس ما اتقرتش** في الترانسكريبت، فمفيش منها حاجة هنا. أسماء الأشخاص مكتوبة زي ما ظهرت في الترانسكريبت وبعضها مشوّه.
- الباقي مفيهوش برمجة أصلًا.

---

## 0. الخلفية والـ Race Franchise (حقايق)

- **Tom Lehmann**: أول لعبة منشورة 1992، full-time freelance من 2008، اشتغل على board/dice/card/wood. **Matt Leacock جابه يعمل pandemic expansions**، فاشتغل co-ops كمان.
- **Race for the Galaxy**: card game طاولة، Rio Grande Games، **2007**، 2–4 لاعبين، 20–40 دقيقة.
- **المنظومة حواليها** ★★: 5 expansions وواحدة greenlit للسنة الجاية، و3 spin-offs:
  - **Roll for the Galaxy**: نسخة dice، ليها expansionين وRivalry جاية في يونيو، وكان lead designer فيها Wei (الترانسكريبت: «way wahoo»).
  - **Jump Drive**: نسخة introductory أبسط.
  - **New Frontiers**: board game، آخر الصيف.
- **المنصات**: Board Game Arena (**+5 مليون لعبة**)، نسخة PC open-source بدأت كـ **AI project** لـ Kelvin Jones (Tom بيرشحها لمهتمي AI/neural networks)، موبايل من Temple Gate Games (AI + online)، ونسخة Steam بـ UI حلو.
- **الباترن**: لعبة واحدة بـ rule-skeleton قوي طلّعت 4 منتجات لجماهير مختلفة (core / dice / intro / board).

---

## 1. Overview: هيكل اللعبة (عشان نعلّق عليه التصميم)

- **نوعين كروت**: action cards (بتختار بيها الـ phases) وgame cards (اللي بتبني بيها الإمبراطورية).
- **البداية**: 4 كروت في الإيد من اختيار 6، وstart world واحد على الترابيزة.
- ★★★ **اختيار الأكشن secret وsimultaneous**: 5 phases، **اللي اتختار بس هو اللي بيحصل في الراوند**. أي phase بيحصل **الكل بيعمله** والـ caller بياخد **bonus**.
  - مثال 3 لاعبين: A وC اختاروا develop يبقى develop بيحصل **مرة واحدة**، الكل يضع development وA وC بياخدوا bonus. بعدها الكل يعمل settle وB بياخد bonus.
  - النتيجة: كل راوند مختلف (مثلًا R1 develop+settle، R2 explore+consume، R3 explore+settle+produce).
- **الـ phases**:
  - **Explore**: تجيب كروت.
  - **Develop**: بتحط الكروت اللي بالـ diamond.
  - **Settle**: بتحط الـ worlds (الدايرة).
  - **Produce**: بتعمل goods.
  - **Consume**: بتحوّل goods لـ VP chips وكروت.
- **الـ worlds**:
  - Gray worlds زي الـ developments، بتدي powers بس.
  - Colored worlds (4 ألوان) ممكن يتحط عليها good، وهو كارت وش لتحت من الـ draw pile. النوع بيتحدد بلون الـ world.
- **الـ consume powers**: كل power بيتستخدم على good واحد بس. مثال: power بيحوّل أي good لـ VP chip واحد، والتاني أي good لـ VP chip + draw كارت. التاني أحسن، فلو معاك goodين تاخد 2 VP + كارت واحد.
- **النهاية** (شرطين): أي لاعب يوصل **12 كارت أو أكتر** في إمبراطوريته، أو الـ communal VP pool يخلص (بيضيفوا chips بـ10 نقط عشان الكل ياخد حقه). في الحالتين بيكملوا الراوند وبعدين score.
- **الـ scoring**: VP chips من consume + قيمة VP للكروت في الإمبراطورية (**الكروت في الإيد مش بتتحسب**) + bonuses الـ **six-cost developments**. مثال: Alien Tech Institute بيدفع على كل الـ yellow worlds + أي كارت بـ alien tag (منهم نفسه).

---

## 2. التصميم: Pace والنهايتين = Strategy تلقائي

1. **من غير عدد turns ثابت = استراتيجية فورية عن السرعة** ★★★:
   - **Tableau rush**: كروت keep worlds/developments كتير ورخيصة عشان تنهي اللعبة بسرعة.
   - **أو** كروت أغلى وأكتر كثافة في VP.
   - على جانب produce/consume: شوية production worlds بـ consumption تشغّلها على VP فورًا، **أو** production worlds وبعدين consume powers حلوة عشان VP أكتر.
2. ★★★ **شرطين نهاية = strategic tension**: تستثمر في VP engine ولا في discounts لبناء الإمبراطورية ولا hybrid؟
   - **Thought experiment**: Hearthstone أو Magic لو فيهم برج لو وصل level 10 يكسب فورًا غير إن الخصم يوصل 0 health.
   - الأسئلة اللي هتتفتح: minions تهاجم ولا تبني البرج؟ defenders لصحتي ولا لـ builders البرج؟
   - لو ارتفاع البرج تفاعل مع الكروت (level 5: archers بتضرب كل turn بدل أول دخول، level 8: ballistas، dragons بتطير من فوق البرج) هتطلع interactions كتير.
   - **قول Tom**: «مش بقول اللعبة أحسن لو فيها شرطين فوز، لكن ده **أسهل طريقة أعرفها لإدخال/تعليم tension**».

---

## 3. كروت = عملة (Card Sifting) والـ Opportunity Cost ★★★

- **بتدفع بكروت تانية بتتقلّب (discard)**. مفيش mana. مثال: Terraforming Robot تكلفتها 3 فبتـdiscard 3 من إيدك (6 كروت). لو call develop بتوفّر واحدة (discount 1).
- **كل كارت في إيدك = opportunity**: تحطه ولا لأ.
- **تعريف الـ opportunity cost**: التكلفة مش بس الموارد المصروفة، لكن **اللي كان ممكن تعمله بدلها**. أمثلة من الحياة:
  - **Electives** في الكلية.
  - الـ seminar: وقتك دلوقتي كان ممكن تقعده في أوضة تانية.
  - Job offers والاستثمارات.
- **الفرق عن الـ mana**: مع 4 mana وكارتين بـ4: بتحط واحد ودور جاي تحط التاني. فبتـ**postpone** الفرصة بس. لكن في الـ discard بتـ**التخلى عنها نهائيًا**.
  - **الباترن**: الـ mana بيصغّر الـ opportunity cost (تأجيل)، والـ card-as-currency بيكبّره (تضحية). والتضحية هي اللي بتصنع القرار.
- **Richard Garfield في Magic**: كان فاكر إن zero-cost cards هتكسّر اللعبة. لما فهم إن فيه opportunity cost (لما بتسحب **Ornithopter** ده كارت سحبته بدل كارت تاني أفيد)، عرف إن zero cost مقبولة. فالـ slot في الدك له تكلفة على الأقل زي zero-to-flying artifact creature.
- **الأرقام** ★★★: اللاعب بيسحب **30–50 كارت** في اللعبة ويبني **8–12 بس**. الـ base game **114 كارت، 91 unique** = استراتيجيات كتير، لأن اللي مش مناسب لاستراتيجيتك بترميه وتدفع بيه.
- **بدائل التنويع وعيوبها**:
  - **Constructed**: لازم دك قبل اللعب، يعني استثمار وقت.
  - **Drafting**: لو متقسم على راوندات زي 7 Wonders (play-draft-play) بيطلّع الناس من اللعبة، ولو قبل اللعب بياخد وقت.
  - **Deck building** زي Dominion: variety كبيرة من Kingdom cards بس بتلعب subset.
  - **Card sifting** بيدمج التنويع **جوه اللعب نفسه**.
- **فايدة ثانية**: بيضيف فئة قرارات جديدة = **hand management**:
  - تحط كل الإيد في شراء كبير وبعدين تتعطل راوندات لحد ما تعيد ملء الإيد.
  - الكروت اللي بتخبيها للـ endgame ليها تكلفة، فهي **boat anchor** لأنك مش بتصرفها.
- **الانتقادات**:
  - بعض اللاعبين يتوتروا (angsty): رميت كارت وبعد دورين اكتشفت إني كنت محتاجه.
  - الخبير عنده technology advantage لأنه عارف الدك وهيستنى combos.
  - Tom مش قلقان من التاني لأنه موجود في كل الألعاب (co-op وcompetitive).

---

## 4. التاريخ: من Puerto Rico → San Juan → Race ★★

- **Puerto Rico** (Andreas Seyfarth): popular. **Stefan Brück** (رئيس Alea الناشر) عايز card game بسرعة يستغل نجاحها. نموذج Seyfarth ماكانش شغّال، فكلّم عدة designers منهم Tom كـ **backup**.
- **Tom اشتغل 3 شهور وعمل 3 major iterations**. **ضغط (collapse) الـ cost structure** من 1–10 لـ (الترانسكريبت مشوّش، وغالبًا 1–6). وكتشف حاجات كتير عن card sifting. لعبوها أسبوع في Gathering of Friends وعدّلوا حاجات صغيرة.
- **القرار**: Stefan قال لو الأمر ليه كان عرض عقد، بس Andreas مشارك. Andreas قال «ده بيحل مشاكلي بس أنا لسه عايز أعمل prototype بتاعي».
- **النتيجة**: Brück دمج prototype Seyfarth + cost structure بتاع Tom + أفكاره في market slips = **San Juan**. Tom بياخد royalty بس كان محبط إن لعبته ما اتنشرتش.
- **ليه Tom كمّل لـ Race**: San Juan لعبة كويسة بس **ما دفعتش «variety button»**: **29 كارت unique من 110** بس. وعنده CCG مش منشور اسمه **Duel from the Stars** يصلح كـ setting، وطوّر أفكار action selection جديدة في سنة ونص. أخد إذن Alea (مع first right of refusal).
- **الباترن** ★★: **Race لعبة اتبنت على تراكم 3 iterations لعبة قريبة**. قال في الآخر: «Race ما اتغيرتش كتير بين أول prototype والنسخة المنتجة».

---

## 5. Simultaneous Action Selection: ليه وإزاي ★★★

- **المشكلة في Puerto Rico**: اللعب clockwise مش simultaneous، وكل لاعب بيـ**block** اللي بعده (لما تختار role محدش تاني يختاره في الراوند). المصطلح: **left-right binding** (Casey Laurence حسب الترانسكريبت). كل لاعب بيأثر في اللي downstream منه أكتر من غيره.
- **تجارب Tom**:
  - في 5-player games كان فيه لاعب upstream **يطحنه** وهو نفسه ما بيكسبش. وموقفه «ده طريقة اللعب».
  - في ألعاب 4 خبرة + 1 مبتدئ، **اللاعب downstream من المبتدئ كان دايمًا بيكسب**.
- **الحل**: اختيار simultaneous، وفوايده:
  1. **agency** أكبر: لو عايز أكشن، تختاره بس.
  2. **يلغي left-right binding**.
  3. **اللعبة تروح اتجاهات أكتر**، لأن الكل ممكن يختار نفس الـ role.
- **السلسلة اللي نتجت**:
  - **Build tempo من 0–2** بدل 0–1 (develop + settle). ده بيخلي الـ Empire يكبر أسرع.
  - **Consume bonus = double VP** بدل +1 VP للـ captain في PR.
- ★★★ **شرط ملزم**: لازم **كل الأكشنز viable في early/mid/late**. أي أكشن مش هيتنادى إلا في أخر اللعبة بيقتل الـ bluffing.

### تشريح الـ 5 phases (إزاي حل كل واحد مشكلة الـ viability)

- **Explore**: سهل. دايمًا بتدور على كروت تتماشى مع بعض، وحتى آخر turn عندك **Hail Mary** (explore وتتمنى الكارت اللي هيكسّبك).
- **Develop** ★★:
  - مشكلة الـ mid-game: في PR/San Juan المباني اللي بتدي bonuses مفيهاش powers، بتبقى للـ scoring بس.
  - **الحل: حط powers عليها** = سبب تبنيها قبل النهاية.
  - مثال: لو yellow/alien strategy، power بتديك discount 2، ومع 3–4 yellow worlds تطلع **profit**.
- **Settle** ★★:
  - مبكر: عشان card flow، تحط worlds ومعاها goods وتبيعهم.
  - وسط: VP engines.
  - **ليه حد يـsettle متأخر؟** من Duel from the Stars: طريقتين نحط world: **peaceful أو military conquest**.
  - مثال military: start world بـ 2 military + development بـ 3 + تغلب defense كارت يديك +2 = تحط كارت بـ 7 قيمته VP كبيرة.
  - **الباترن**: big military ما بيدفعش كروت لـ worlds العسكرية. فمش عايز يـcall settle في النص عشان ما يساعدش اللي بيبني VP engines. بيخزّن worlds وبيحطهم دفعة في الـ endgame.
  - الـ worlds non-military بتتحط زي developments (discard بالتكلفة)، والفرق إن الـ bonus **draw كارت بدل discount**.
- **Produce** ★★★:
  - المشكلة في PR/San Juan: **«who bells the cat»**، اللي بينادي produce اللي بعده هو اللي بياخد first crack في البيع. فالكل عايز غيره يناديها.
  - الحل 1: **Produce في آخر الراوند**، فلو ناديت produce الراوند الجاي ممكن أنادي أكشن بيستفيد منها (وغيري كمان).
  - الحل 2: **Windfall worlds** (الدايرة بـ halo): بتاخد good **وقت الـ settle** مش وقت produce. تـsettle windfall world وتبيع الـ alien good بكروت كتير من غير ما تنادي produce.
  - **Two-edged sword**: windfall worlds ماتاخدش goods وقت produce، فمحتاجة power أو اللاعب ينادي produce عشان bonus (تعمل good على windfall world). أخدت طريق تهرب من produce **وحافز تناديها** في نفس الوقت.
  - **النتيجة**: produce بتتنادى طول اللعبة ومش dominant زي PR.
- **Consume** ★★★:
  - double VP حلو في الـ late بس مين هيضاعف VP في البداية؟ المبدأ (Engine building): ابنِ engine وبعدين score.
  - **Consume-trade** (الـ bonus اللي بيبيع goods بكروت) **بيشتغل للـ caller بس** (عكس باقي الـ phases اللي الكل بيستفيد منها).
  - **ليه** (سببين): (1) عشان يتنادى بدري. (2) ★★★ **حل rich-gets-richer**: لو alien production world بتـproduce أوتوماتيك وتبيع أوتوماتيك لما أي حد ينادي trade، اللعبة تبقى «مين يحط الـ world الكبير أول».
  - **أربع حلول لنفس المشكلة، كل واحد على شخصية لعبته** ★★★:
    - **Puerto Rico**: trading house وبيعك ممكن يتمنع (لو حد باع coffee قدامك، أو لو coffee لسه في الـ trading house من phase سابقة).
    - **San Juan**: sale prices أقل (market slips) + compensation buildings زي **poorhouse** (لو عندك كروت قليلة تاخد زيادة). ده «casual euro approach».
    - **Roll**: returns أقل لو حسبت تكلفة producer/shipper dice، وخلّوا **explore محسّنة جدًا** كبديل لحد إن بعض الناس ما بيتاجروش أصلًا.
    - **Race**: **أكبر return بس محتاجة action من اللاعب**.
  - **Explore ليها action cards بـ bonuses مختلفة**: +1 كارت زيادة، أو تنزل عميق في الدك تدور على كارت بعينه.

---

## 6. التفاعل في الـ Simultaneous ★★★

- **Bluffing** (double-think): عندي alien good وإيدي 10 كروت. شايف واحد هيعمل develop وواحد settle، فأنادي trade عشان أملأ إيدي بعد ما أحط development وworld. لكن اللاعبين ممكن يفكروا «Tom عنده alien good وإيد مليانة، هيـ call consume-trade يبيع ويـdiscard لأن overhand limit» فيتجنبوا.
- **Gambling**: في الـ final turn محتاج develop وsettle الاتنين، فتخمّن مين هيدعي إيه.
- **Leaking** (مثال Bank): لو حطيت Bank، كل مرة حد ينادي develop **أنا بآخد حصتي**.
- **Blunting**: لو حد هينادي produce عشان يـrefill alien windfall، أحط **Lost Species world**: بتديني gains good (قريب من alien) و2 كروت زيادة وقت produce. اللاعب اللي كان عايز ينادي produce غالبًا مش هينادي تاني. فـ**بُهت ميزته**.
- **Pressuring** (build tempo): لو إيدي قليلة والخصوم ناديوا develop وsettle: أحط كارتين ضعاف ولا واحد قوي وواحد ضعيف وأوفّر؟
  - **كل missed build = opportunity cost** لأن لو اللعبة خلصت على الـ tableau وماكملتش كروتي كل slot فاضي = VP ضايع (شرط الـ 12 كارت).
- **انتقاد «multiplayer solitaire»** ★: Tom بيقول **self-fulfilling prophecy**: لو لعبت heads down ومش بتبص لـ tableau الباقي ولا بتتوقع، هتحس كده. مفيش forced interaction، لكن ألعاب الاستراتيجية بتشتغل لما **كل اللاعبين يحاولوا يكسبوا فعلًا**، واللي بيدّي انتباه بيكسب أكتر.

---

## 7. Simultaneous Play (مش بس selection) ★★

- **بيسرّع** اللعب: Race في 4 لاعبين أطول بـ **~5 دقايق بس** من 2 لاعبين.
- **المشكلة**: أوقات لازم تعمل serialize (لما حد لو عمل حاجة اللعبة ممكن تخلص واللي بعده محتاج الـ info دي).
- **الفلسفة**: «بطّئ اللعب لما **تحتاج** بس».
- **أداتين**:
  1. ★★ **اخفي المعلومات غير الأساسية**: الـ discards وش لتحت عشان محدش يستنى يشوف إيه اللي بترميه قبل ما يقرر.
  2. ★★ **قلّل synchronization points**: Race عندها نقطة واحدة رئيسية = action selection/revelation. ممكن لاعب يكمل turn بينما التاني لسه بيعمل explore. لو عندك نقط كتير ما هتستفيد من simultaneous.

---

## 8. تصميم الكروت: Powers، Cognitive Load، Icons

### Multiple powers
- الكروت متعددة الـ powers (مثال Terraforming Robot: power في settle + consume power) بتخلي الكارت يشتغل مع produce/consume أو empire building = **التنويع** اللي عايزه.
- ★★★ **الثمن**: **cognitive load** عالي. Tom بيقول إن ناس بتسمي Race «مش learning curve، لا learning **spike** اللاعب بيتـimpale عليه». ولما بيقولوا الـ icons هي المشكلة، **كتير من الحمل ده فعلًا بسبب الـ multiple powers**.
- **تأثير على الجرافيك**: أضافوا **swooshes** ورا الأيقونات عشان اللاعب يبص عبر كروت الإمبراطورية ويشوف الـ powers بسهولة.

### Big combos vs. gaining an edge ★★★
- **Spectrum**: powers كبيرة (اللعبة عن تجميع combo) ↔ powers صغيرة تدريجية (اللعبة عن اكتساب ميزة تدريجية).
  - **Edge side**: meta-strategy = قرارات صغيرة كتير لحد ما تكسب تدريجيًا.
  - **Combo side**: meta-strategy = «تأجل الهزيمة لحد ما الـ combo يوصل وبعدين تقتل». مثال Hearthstone: تدافع بـ defender عالي، ولما الـ combo يجي: double defense، double defense، attack = defense، **Wham**.
- **Tom بيحب اللعب اللي فيها قرارات صعبة وstrategic tension**، فهو في طرف الـ edge. بس مفيش حاجة في card sifting بتفرض ده: **Glory to Rome** بتستخدم big combos وdiscard pile لتجميعها ومشهورة بـ «التأرجح على الحافة لحد ما حد يحط combo ويكسب».
- **سبب تاني للـ powers الصغيرة: تقليل cognitive load.**
- **قوايم Race**: كارت زيادة وexplore، military بسيطة، كارت وسط الـ phases، إضافة consume power.
- **3 powers بس بيكسروا القواعد** (ويستاهلوا):
  1. دفع military worlds (بيربط military بـ non-military).
  2. كسر قاعدة «consume trade bonus» لحد معين بعد ما اتبنت بحرص.
  3. صرف كروت مباشرة مقابل VP chips (كسر «VP من الإمبراطورية بس»).

### Icons vs. Text ★★★
- **المزيج**: بعض الـ powers من غير نص، والمعقدة عليها نص. **اللي ما توقعوش**: لو فيه powers بدون نص، لاعيبة كتير **افترضوا إن مفيش نص خالص** حتى لو النص قدام عينهم.
- **موديل الأيقونات**: زي **road signs**: كام شكل أساسي + رقم.
- ★★★ **قرار عكسي عن العادي**: عادة ده **خطأ كبير** (أي لعبة لازم تكون accessible، لأن لو محدش لعب فالـ replay value تافهة). لكن في playtesting كان فيه ناس بيلعبوا **مئات وآلاف المرات** قبل النشر، فـ **تراجعوا عن accessibility** عشان **سهولة اللعب المتكرر**.
  - اللي يقدر على الجرافيك بتـ«click» معاه بعد كام لعبة ويلعب أسرع وأسهل.
- **الـ spin-offs للجمهور الكاجوال**: أيقونات معقدة + نص (Roll وNew Frontiers). **Jump Drive** (powers بسيطة): كلمات مساعدة قليلة جوه الـ power.
- **الأيقونات بتدفع على الموبايل**: بتبان كويس على الشاشة، والـ implementer أضاف **expanded mode** وكل حاجة فيه عليها نص.
- **تكامل بصري**: card design مر بـ iterations كتير (prototype أصلي → نهائي)، وتصميمات Wei قبل ما يبدأوا الشغل، وتصميمات بعد ما فريق الفن دخل.

---

## 9. الفريق والـ Theme

- **Wei** (الترانسكريبت «way wahoo»): prototype icons، card design، مساعدة في التطوير، lead designer لـ Roll.
- **Jay Tummelson** (الترانسكريبت «K Tumbleson»): رئيس Rio Grande، fan خيال علمي. **في 2007 الناشرين الألمان كانوا مقتنعين إن SF games مش هتتباع** فهو دعم المشروع ودفع في فن كتير.
- **فريق الفن** (أسماء الترانسكريبت: Claus، Martin، Mirko Suzuki): أغلفة، card art، بعض الـ 3D modeling، logos، rules layout، templates، إعادة عمل كل الأيقونات، وكل الـ production. **بيشتغلوا مع بعض 13 سنة** بشكل collegial.
- **Roll**: الفن اقترح ذكيًا dice عايمة في الفضاء ورموز Race طالعة منها بضوء أحمر (مقابل أصفر في الـ branding للتمييز).
- ★★ **الـ theme**: كل الكروت متصممة thematically، بس **Tom مش بيقول للفنان**.
  - مثال **Distant World**: موديله الداخلي **Iceland**. سكان معزولين وعليهم دراسات جينية كتير، ولذلك بتـproduce «gains good». ولديهم أعلى معدلات ملكية كتب وثقافة في العالم، ولذلك bonus ضخم لـ novelty goods.
  - **لا بيتوقع** اللاعب يلاحظ ده، **ولا بيشرح** للفنان. بيدّي بس العنوان.
  - **الباترن**: الفنان يفضل «fresh» ويجيب أفكاره هو.
- **الإلهام**: **Fred Pohl — Heechee Saga** (حضارة غريبة اختفت من زمان ولسه مفيش غير artifacts)، و**David Brin — Uplift** (أجناس فضائية بتوصّل أجناس تانية للوعي). مش مستخدم منهم حاجة مباشرة.

---

## 10. أفكار من Optimization Theory ★★★

### 1) Mind the Gap
- **المثال**: New Sparta عايز يحط military world. عنده كارت military مؤقت «one-shot» رخيص بس يخسّره tempo، أو واحد تاني أغلى من المطلوب. اللي عايزه فعلًا كارت ثالث ما سحبوش. فلازم يقرر: **military استراتيجية جدية ولا one-shot؟**
- **القاعدة**: لو وفّرت **كل combinations الـ power/cost**، اللعب هيبقى tactical (بس «إيه المطلوب دلوقتي»). لو حطيت **فجوات (gaps)**، **تفرض choices استراتيجية**.
- **تنبيه**: الـ random draws في card games بتقلل المشكلة لأنك ممكن ما تسحبش الكارت الوسيط. لكن **CCGs وdrafting وboard games** لازم تحذر لو عايز strategic.
- **التطبيق في Race**: **قليل جدًا من الـ 5-cost developments** عشان يبقى فيه **خطوة كبيرة (step up)** تكون strategic move.

### 2) Switching Costs
- **الصورة**: strategy hills، اللاعب بيتسلق تل (alien / big military / novelty). لو كروتك الأولى بتقول alien وبعدين ما سحبتش حاجة منها وبقت تقول military، عندك **switching cost** (six-cost الـ military هيسجّل أقل لأن عندك military أقل في الـ tableau).
- **المبدأ**: «لا تخلي اللاعب يحس إنه محبوس بسبب إيده الأولى» ★★★، فلازم **تعويض (compensation)** لما بيبدّل.
- **الحل في Race**: **six-cost devs** فيها power **و**VP bonus. التكلفة **أقل من القيمة الكلية** لما تحسب الاتنين، لكن **أغلى بكتير** لو حسبت الـ power لوحده (مثال: development بتدي 2 military بتكلفها زيادة جدًا). ده **تعويض من غير كروت قوية في تأثيرها في اللعب**.

### 3) Player Types (Mark Rosewater)
- **Spike**: يقدّر efficiency وبيكسب بنسبة عالية.
- **Johnny**: بيحب يكسب بطريقة مبدعة (مثال: **Pilgrimage World**: لو معندكش consume power تاني تاخد كل الـ goods وتستهلكها دفعة واحدة).
- **Timmy**: بيحب big effects (**Big Military**).
- ★ لما صمّم الكروت حط الـ 3 أنواع.

---

## 11. اللي ما اشتغلش (What Didn't Work) ★★★

- **حجم الدك**: كان تمام في الـ base لكن بقى مشكلة بعد **~180 كارت** مع الـ expansions. **Sample variance problem**: variance الدك ثابت لكن الـ sample (الـ 30–50 كارت اللي اللاعب بيشوفها) بقت تتفاوت أكتر من اللازم. **الحل**: قسّموا الـ expansions لـ **arcs منفصلة**: base + 3 expansions، وبعدين تبدّل وتلعب base مع غيرها. ده كمان بيخلّي Tom يحكي **قصص مختلفة**.
- **بعض الكروت متخصصة زيادة.**
- ★★★ **Colorblind issue** (browns وgreens): في Jump Drive حطوا **dots** عشان يحلوا. **Play tester كان extremely colorblind لكن expert bridge player حفظ الكروت**، فما اتكشفتش المشكلة («لو Larry يقدر يلعب، فالمشكلة إيه؟»). **الـ 2nd edition** (عند المطبعة): dots في blue/green/brown worlds. مش حل كامل، **~90% solution**.
- **Rules gender-neutral**: كان في 2 «he/he's» و12 «his» وبقوا «they».
- **إضافات الـ 2nd edition**: sample rounds للاعبين الجداد، **6 promo worlds** من الـ app مع start world choice اختياري، **تعديل 5 كروت ضعيفة** وهتتاح كـ promos منفصلة (BGG store).

---

## 12. Q&A (كل سؤال وجوابه) ★★

1. **Balancing strategies / inevitability** (مشكلة Magic: مفيش طريقة تكسب ضد استراتيجية معينة):
   - Magic في المستويات العالية لعبة big effects وcombos. Race بـ small effects تتخلص من كتير من المشكلة بس مش كلها.
   - في 2-player بخبرة، **strong develop-develop strategy** ممكن تعمل مشكلة.
   - **المعتمد على طول اللعبة**: لو بتخلص في 10 دقايق المشكلة مش كبيرة.
2. **Cost crunch في San Juan**: السبب أساسًا **ergonomics**: لو التكلفة 1–10 وبتدفع 9–10 كروت يبقى إيد ضخمة، ولو عايز تحتفظ بكروت تبقى 15 كارت في الإيد. وده بيتطلب دك أكبر من 110. **فكتير منه مدفوع بعوامل خارجية.**
3. **ليه Roll أسهل في القراءة**: Roll بيتجنب **multi-phase powers**. التايلز اللي فيها بتحصل نفس الـ power مرتين فنص واحد يكفي، وأغلب التايلز power واحد. **Tom نفسه متوقع إن الـ multi-phase powers هي سبب صعوبة Race**، وملتزم بيها في Race. لكن New Frontiers وRoll وJump Drive بيتجنبوها (**الـ spin-offs موجودة لتنويع الجمهور**).
4. **ازاي وازن أرقام التكلفة**:
   - **Mind the gap** (قليل 5-cost عشان الخطوة تبقى strategic).
   - **حدد الاستراتيجيات الأول** (مثال **Novelty** = blue worlds رخيصة كتير) = **anchor points** والباقي بـ interpolation.
   - حط **كروت هي استراتيجية كاملة**: مثال **Consumer Markets** (سحبتها تقول «يمكن أروح novelty»)، تكلفتها 5 لأن بزيادة 1 تعمل six-dev. فكانت **قوية جدًا**.
   - بعدين test وrevise.
5. **تصميم الـ sixes**: لو الاستراتيجيات معرّفة كويس في كروت تانية الـ six بيبقى **capstone وغالبًا scoring**. لو مش واضحة، الـ power لازم تكون أقوى والـ VP أقل. مثال: **Galactic Economy** و**Rebel vs Imperium** (حسب الترانسكريبت) بتشتغل مع كل الألوان = power قوي جدًا، فقلّلوا تكلفة الـ VP bonus للتعويض.
6. **ازاي بيتصور الكروت قبل playtest** ★★★: بيقعد في **tea shop** ويكتب **أسماء كروت محتملة**، ويجمعها في categories، **من غير أرقام**. بعدين يحدد الاستراتيجيات ويدور عليها بدايرة (مثال: Novelty = keep worlds، Alien = density). وبعدين يوزع على التكاليف. **«Race ما اتغيرتش كتير من أول prototype»** بفضل تجربة الـ 3 iterations بتاعة Puerto Rico card game. وقال «أسابيع في tea shop» (الترانسكريبت: «three wheats»). وحذّر إن ده طريقته هو بس.

---

**للاستوديو:**

**(1) Mossfolk (اللعبة الحالية):**
- ★★★ **Mind the Gap على مستوى الميزانية**: إسقاطات الـ drop budget لازم تعمل «فجوات» تفرض قرارات استراتيجية (حتة نفضّل نندمج الحجم 5 ولا نحتفظ بمساحة؟) بدل ما كل قرار tactical مؤكد. **الـ bot يقيس عدد الاستراتيجيات الفائزة المختلفة لكل ليفل**، مش بس win rate. ليفل بحل واحد = tactical بحت.
- ★★★ **Opportunity cost = ميزانية الإسقاط**: كل drop تضحية، مش mana بيتجدد. افحص: هل في ليفلات الميزانية بتصنع **قرار فعلي** (تتخلى عن إيه؟) ولا مجرد counter؟
- ★★ **الـ Two end-conditions**: الليفل بـ هدف + ميزانية. الـ rival contests ممكن تزود شرط تاني (race ضد خصم) = tension. بس لو ضفنا حاجة تانية، شوف أنهي واحدة بتبقى dominant في البوت.
- ★★★ **Switching cost وcompensation**: لو توزيع القطع العشوائي حبّسك في وضع سيء، هل في تعويض؟ (مثال: القطع النادرة تدّي bonus). اللاعب ما يحسش إنه محبوس بسبب «إيده الأولى» (= أول كام drop). افحص بالـ bot: هل فيه ليفلات الـ drops الأولى بتحدد الفوز تقريبًا؟
- ★★ **Rich-gets-richer**: في merge ألعاب snowball طبيعي (المخلوق الكبير بياخد مساحة). Race حلّته 4 طرق بتتناسب مع شخصية اللعبة. حدد أي ليفل الـ snowball بيقتل التنوع والمشكلة.
- ★★★ **Cognitive load والـ learning spike**: Tom بيقول الحمل كان من الـ multiple powers مش الأيقونات. تحديات 2501+ (mossy shells / stones / rot): ندخلهم **واحد واحد**، ومنقدّمش اتنين يتفاعلوا قبل ما كل واحد يتعلّم لوحده.
- ★★ **Colorblind والـ bot tester**: الـ playtester اللي حفظ الكروت خبّى المشكلة. **التيستر-بوت مش بيشوف accessibility أبدًا**. كل أحجام المخلوقات (9) لازم تتميّز بالشكل مش بس اللون، ولازم **cold user** (مش حافظ اللعبة) يختبر.
- ★★ **Sample variance**: التسلسل العشوائي للقطع في ليفل قصير = sample صغير ممكن يتفاوت جدًا. استخدم رانات البوت (عدد كافي) عشان تقيس تفاوت النتيجة بسبب الحظ مش المهارة، وراجع الليفلات اللي variance فيها عالي.

**(2) خط الإنتاج السريع (أهم):**
- ★★★ **Rule-skeleton واحد → منتجات متعددة**: Race → Roll (dice) → Jump Drive (intro أبسط، كلمات مساعدة) → New Frontiers (board). كل واحد لجمهور مختلف **وبمستوى accessibility مختلف**. ده نموذج حرفي لـ «النظام القابل لإعادة الاستخدام»: نبني core system مرة (merge/drop physics + level generator + bot) ونطلّع منه نسخ hyper (قواعد 1–2) وhybrid (طبقات meta). وما نتعلمش tutorial جديد كل مرة.
- ★★★ **Accessibility vs. replay**: Tom تراجع عن accessibility **لأن لاعبينه بيلعبوا مئات المرات**. في hyper-casual اختبار CPI بيعمل العكس: اللاعب عنده ثواني. القاعدة للاستوديو: **حدد الـ audience أولًا**: hyper = accessibility أول، hybrid بعدين = depth مسموح. ما نخلّطش الاتنين في نفس اللعبة.
- ★★★ **الـ prototype بالأسماء والاستراتيجيات الأول**: Tom بيكتب **أسماء** كروت، يجمّعها، يحدد الاستراتيجيات، **وبعدين** يحط الأرقام. للاستوديو: لما نختار فكرة لعبة جديدة، نكتب في ساعة قائمة «مخلوقات/عناصر/تحديات + استراتيجيات واضحة» **قبل أي tuning**، وبعدين anchor points + interpolation. وده يوفّر iterations.
- ★★★ **Race ما اتغيرتش بين أول prototype والنهائي** لأنه اتبنى على 3 iterations من لعبة قريبة. **النقل لينا**: كل لعبة جديدة بتبدأ من مكتبة الـ iterations والـ levels والـ bot configs بتاعة اللي قبلها، مش من صفحة بيضا. وبما إننا بنطلّع لعبة كل يوم/أسبوعين، التراكم ده هو الميزة التنافسية.
- ★★ **Gap/choice test للـ CPI**: قبل ما نطلّع فكرة، نسأل: في أول 30 ثانية، هل اللاعب بياخد **قرار فيه تضحية** (opportunity cost) ولا بس بيضغط؟ الألعاب اللي كلها tactical بتتشبّع بسرعة.
- ★★ **Sample variance كـ فلتر للأفكار**: لو الفكرة بتعتمد على عشوائية كبيرة في جلسة قصيرة (30–50 ثانية)، النتيجة هتتفاوت بحظ مش بمهارة. شغّل البوت N مرة وقيس الـ variance **قبل** ما نصرف على art.
- ★★ **Rules breaking بحساب**: Tom حدد **3 استثناءات بس** تستاهل تكسر القواعد. في الألعاب السريعة: قاعدة core واحدة + استثناء واحد كحد أقصى، وأي حاجة زيادة تتشال.
- ★ **Left-right binding / who bells the cat**: لو اللعبة فيها خصم (rival contest) تأكد إن مفيش حد «بيضحي» لصالح التاني بشكل بيخلي كل لاعب يستنى التاني. وده كمان تحذير للـ ads: ما نبنيش لحظة بيستنى فيها اللاعب عشان غيره يتحرك.