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

**لموسفولك:**
- **Unity مش UE**، بس المبدأ واحد: **الـ creatures في الـ jar** بتتقسم لـ 9 تعريفات أحجام مشتركة (ScriptableObject فيها sprite/mesh/material/physics material)، وكل creature instance بيشيل بس position وvelocity وindex الحجم. ده بيوفر ميموري كبيرة على موبايل، وده بالظبط الـ intrinsic/extrinsic.
- **الديكور اللي بيتكرر** (mossy shells، stones، rot tiles على خلفية الـ jar) مرشح قوي لـ **GPU instancing** (Unity's equivalent للـ ISM). ده بيقلل الـ draw calls وده مهم جدًا في hyper-casual.
- **الـ particles** (تأثيرات الـ merge وانفجار الـ moss) = نفس مثال Refactoring Guru بالظبط: شيل التعريف المشترك في شيء واحد وخلي كل particle يشيل بس موقعه وسرعته.
- **حذار:** لو كل creature عنده material أو tint مختلف، الـ sharing بيتكسر. فقرر من البداية: هل التنوع البصري بييجي من **tint بيتعدّل per-instance** (property block) ولا من **material منفصل**؟
- **للـ tester bot:** لو بتشغّل آلاف simulations بالتوازي، الـ level definitions والـ creature types لازم تبقى shared read-only، والـ runs بتشيل بس الـ state بتاعها. ده بيخلي الـ bot_difficulty runs أخف بكتير.