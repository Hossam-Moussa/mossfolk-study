# Flyweight Design Pattern في Unreal Engine — نوتس مذاكرة

**المصدر:** فيديو معرّفه zBuqYKjeIEk، المدة ~7 دقايق (تقدير من الترانسكريبت، والعنوان مش موجود في الملف).

**ملاحظة على الترانسكريبت:** فيه أخطاء ASR واضحة، وصححتها هنا: "flywheat" و"flyweight design pencils" = Flyweight design patterns، و"innocent static mesh" = **Instanced Static Mesh (ISM)**، و"game programming design patterns" = كتاب Robert Nystrom *Game Programming Patterns*، و"Class A Grass" اتصحح بعدين في الفيديو نفسه إنه مش grass، ده **Foliage Type** asset.

**تصنيف الفيديو:** فيديو برمجة/باترنز بيشرح مفهوم وبعدين workflow في الإنجن. الجزء التقني (خطوات الـ Blueprint وضغطات الـ UI) متجاهل حسب القاعدة. الدروس التصميمية اتسجلت كاملة.

---

## 1. تعريف الباترن — Flyweight (★★★)

- **الباترن:** Flyweight design pattern، **structural pattern** (تصنيف GoF)، هدفه **تقليل استهلاك الميموري** عن طريق **مشاركة الداتا** بين الـ objects المتشابهة.
- **المشكلة اللي بيحلها:** تخيّل 1000–2000 instance من class في الـ scene، وكل instance شايل معلومات وattributes كتير. كل واحد بياخد ميموري لوحده، فالجهاز بيتخنق.
- **الحل:** بدل ما كل instance يحمل كل الداتا، بتعمل **class واحد بيشيل الداتا المشتركة**، وكل الـ instances بتكلمه وتاخد منه المعلومة اللي محتاجاها بس. النتيجة: ميموري أقل بكتير.

**الباترن ورا التاكتيك (من برا الفيديو):** الفيديو ما سماش التقسيم بالاسم، بس الفكرة الأساسية في Flyweight هي فصل الـ state لنوعين:
- **Intrinsic state (مشترك):** الداتا اللي بتتكرر ومش بتتغير من instance للتاني (الشكل، الماتيريال، الـ collision).
- **Extrinsic state (خاص بكل instance):** الداتا اللي فريدة لكل واحد (المكان، الاتجاه، الحجم، الحالة).

الفيديو بيقولها بالعامية: "الـ attributes المشتركة في الـ flyweight، والمعلومات الضرورية لكل واحد بتتاخد وقت الحاجة".

---

## 2. أمثلة من الإنجن (UE4/UE5)

### أ. الـ Foliage (★★★)
- الـ foliage tool بيسمح تحط **عدد كبير جدًا من الـ instances** لأي حاجة: شجر، صخور، أو أي مِش (mesh) تختاره، مش محدود بخيارات معينة.
- كل الـ instances دي **بتشترك في نفس الشكل، والماتيريال، والـ collision** = Flyweight.

### ب. الـ Instanced Static Mesh (★★★)
- ده **component جاهز** من الإنجن، بتحطه في أي Blueprint وتعمل منه instances.
- **قاعدة مهمة:** الـ ISM الواحد بيمثل **شكل واحد**، وكل الـ instances بتبقى نفس الشكل. عايز شكلين؟ تحتاج اتنين ISM.
- **الـ demo في الفيديو:** ضيف الـ ISM على Blueprint، ضيف instances من قائمة الـ instances، وحرّك كل واحد في الـ scene. كلهم بيتشاركوا الماتيريال والـ collision والشكل.
- **المكسب المعلن:** الـ instances دي كلها **بتعمل draw call واحد على الـ CPU**، فبتوفر CPU وميموري في نفس الوقت.

---

## 3. أمثلة من كتب ومراجع الباترن

### أ. Game Programming Patterns (Nystrom) — الشجر (★★)
- مثال الشجر: بدل ما كل شجرة تحمل كل معلوماتها، كلها بتكلم **class واحد اسمه "model"** وتاخد منه الداتا اللي محتاجاها.
- ده **نفس المنطق**: الـ model هو الـ flyweight، والشجرات هي الـ instances الخفيفة.

### ب. Refactoring Guru — الـ Particles (★★)
- كل particle ليها **coordinates، وvector speed، وcolor، وsprite**.
- الشيء المشترك هنا هو **الـ particle type / الـ sprite**. الـ position والـ speed هما الـ unique لكل particle.
- **المثال ده أوضح مثال للتقسيم intrinsic/extrinsic** اللي فوق.

---

## 4. الـ Workflow داخل الإنجن (★)
الفيديو بيوريك خطوات عملية، بس **الأهم منها المنطق**:
- الـ foliage مش موجود في المشروع؟ تعمل **Foliage Type** جديد من **Static Mesh**.
- تختار شكل، تحفظ، وترجع للـ Foliage mode وتبدأ **تـ paint** instances بسرعة.
- كل اللي اتعمل بالـ paint بيدخل تحت نفس الباترن (مشاركة الشكل والماتيريال والـ collision).

*(باقي الضغطات والـ Blueprint steps = برمجة/implementation — متجاهل.)*

---

## 5. الخلاصة
- Flyweight = **فصل الداتا المشتركة عن الداتا الخاصة** عشان توفر ميموري وCPU.
- في UE: **Foliage** و**Instanced Static Mesh** هم تطبيقات الباترن الأساسية.
- الفيديو مختصر جدًا ومش بيغطي حدود الباترن (مثلاً: لو كل instance محتاج ماتيريال مختلف بيبوظ الـ sharing). دي نقطة لازم تبقى في دماغنا.

**المراجع اللي الفيديو ذكرها:** موقع Game Programming Patterns، وRefactoring Guru (Flyweight).

---

**للاستوديو:**
- **الفكرة:** Flyweight معناه إنك تفصل الحالة المشتركة (intrinsic) عن الحالة الفريدة (extrinsic)، وتخزن المشتركة مرة واحدة وتشاركها بين آلاف الـ instances. في Unreal ده بيتحقق بـ UDataAsset/UPrimaryDataAsset كـ definition read-only، والـ Actor أو الـ Component يشيل بس الـ transform وأي state خاص بيه. ينفع يتطبق على أي لعبة فيها كيانات كتير متشابهة: أعداء، مقذوفات، tiles، VFX، عناصر UI.
- **اختيار الفكرة:** قبل ما تبدأ أي كونسبت جديد، اسأل: هل الكونسبت فيه كيانات كتير (مئات أو آلاف) بنفس الشكل؟ لو أيوه، الـ architecture دي لازم تتحط من أول الـ prototype مش بعد ما الفكرة تتقبل. ده بيخلي الـ prototype أخف، وبيتعاد استخدامه بين الألعاب.
- **الـ Data Assets:** كل نوع كيان يبقى DataAsset واحد فيه mesh وmaterial وphysics material وstats. الـ instances تعمل reference ليه بـ TObjectPtr أو TSoftObjectPtr ومتكررش الداتا جواها. (مثال على اللعبة الحالية Mossfolk: الـ creatures في الـ jar تتقسم لـ 9 أحجام مشتركة، وكل creature instance يشيل بس position وvelocity وindex الحجم، وده بيوفر ميموري كبيرة على موبايل.)
- **Instancing للديكور:** أي ديكور متكرر مرشح قوي لـ Instanced Static Mesh أو HISM بدل Actors منفصلة، وده بيقلل الـ draw calls وده مهم جدًا في hyper-casual على الموبايل. (مثال على اللعبة الحالية Mossfolk: mossy shells وstones وrot tiles على خلفية الـ jar.)
- **الـ VFX:** الـ particles تبقى Niagara system واحد مشترك، والـ spawn بيمرر بس الـ parameters الفريدة زي الموقع والسرعة. (مثال على اللعبة الحالية Mossfolk: تأثيرات الـ merge وانفجار الـ moss، نفس مثال Refactoring Guru بالظبط.)
- **حذار من كسر الـ sharing:** لو كل instance عنده material أو tint مختلف، الـ sharing بيتكسر. قرر من البداية: التنوع البصري هيجي من per-instance data (Custom Primitive Data أو Material Parameter Collection)، ولا من Material Instance Dynamic منفصل لكل واحد؟ الـ MID لكل instance بيكلف draw calls وميموري، فالأفضل الـ Custom Primitive Data غالبًا. (مثال على اللعبة الحالية Mossfolk: لون كل creature أو لمسة الـ moss.)
- **الـ hot path:** الـ spawn والـ update لآلاف الكيانات يتكتبوا في C++، والـ Blueprints تتحط بس للـ setup والتصميم، لأن الـ Blueprint overhead بيبان بسرعة مع الأعداد الكبيرة.
- **الـ tester bot:** لو بتشغّل آلاف simulations بالتوازي (headless build)، الـ level definitions والـ creature types لازم تبقى shared read-only، والـ runs تشيل بس الـ state بتاعها. ده بيخلي الـ bot_difficulty runs أخف بكتير ومايحتاجش يحمّل الداتا تاني في كل run. (مثال على اللعبة الحالية Mossfolk: الـ jar configs وتعريفات الـ creatures.)
- **الإعلانات والـ creatives:** نفس المبدأ ينفع في خط الإنتاج: template واحد مشترك لكل فورمات الإعلان، وكل variant يشيل بس الـ parameters الفريدة زي النص أو اللون أو الـ hook. ده بيسرّع إنتاج الـ A/B tests من غير ما كل نسخة تبقى مشروع لوحدها.
