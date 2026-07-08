"""One-time: write the 14 LinkedIn posts as markdown files in posts/."""
import os, textwrap

POSTS = [
    {
        "slug": "ley-de-brooks",
        "title": "La Ley de Brooks",
        "date": "abr 2026",
        "order": 1,
        "excerpt": "Tu instinto dice: mete más gente. Probablemente eso lo va a empeorar.",
        "body": """Tienes un problema grave con un cliente? Un bug que nadie puede resolver?

Tu instinto te dice: mete más gente. Más manos = más rápido, no?

Déjame decirte que probablemente eso lo va a empeorar.

Esto se llama la Ley de Brooks: "agregar personas a un proyecto atrasado lo atrasa más."

Porque cada persona nueva necesita onboarding, alguien tiene que parar de producir para explicarle todo, se multiplican las reuniones, y para cuando entiende el problema... el deadline ya pasó.

La solución casi nunca es más gente. Es reducir el scope, mover el deadline, o quitar obstáculos al equipo que ya tienes.

Pero claro, es más fácil decir "ya metí refuerzos" que admitir que el plan no funcionaba 😅

Cuál ha sido tu peor experiencia con esto?"""
    },
    {
        "slug": "ai-companero-de-trabajo",
        "title": "AI ya no es una herramienta. Es tu compañero de trabajo",
        "date": "abr 2026",
        "order": 2,
        "excerpt": "Lo que más me interesa no es la tecnología. Es lo que viene después.",
        "body": """AI ya no es una herramienta más en tu lista de apps.

Es tu compañero de trabajo.

Hace un año la conversación era "deberías probar ChatGPT".

Hoy las empresas están diciendo "tienes que usar AI. No es opcional."

Y no como un ayudante que te corrige un email. Como un ejecutor. Que hace tareas, toma decisiones y entrega resultados.

Yo lo vivo todos los días. En Darwin AI trabajo rodeada de esto.

Pero lo que más me interesa no es la tecnología. Es lo que viene después:

→ Más AI = más productividad por persona = menos necesidad de contratar equipos grandes. Un equipo de 5 va a hacer lo que antes hacía uno de 20.

→ Más AI = menos barreras de entrada = más emprendedores. Ya no necesitas levantar plata para armar un equipo de devs. Yo hice una herramienta entera para mi empresa sin escribir código.

→ Más AI = menos tareas repetitivas = más tiempo para pensar. Y pensar es lo que todavía no se puede automatizar.

→ Más AI = menos especialistas haciendo una sola cosa = más generalistas que entienden el problema completo.

Las empresas van a buscar gente con capacidad de ejecución, pensamiento crítico y visión transversal. No gente que solo sabe usar una herramienta.

Nos vamos a quedar sin trabajo? No lo creo.

Pero el perfil que se busca va a ser muy diferente. Menos "sé hacer esto" y más "entiendo por qué hay que hacerlo y lo resuelvo con lo que tenga."

Los que hoy aprenden a trabajar con AI van a tener una ventaja absurda. No porque sean más inteligentes. Porque van a saber usar el multiplicador.

Ya estás usando AI en tu día a día? O todavía lo ves como algo opcional?"""
    },
    {
        "slug": "la-mandala-de-la-comunicacion",
        "title": "La mandala de la comunicación",
        "date": "abr 2026",
        "order": 3,
        "excerpt": "Con 10 personas tienes 45 canales de comunicación posibles. Con 90? Más de 4,000.",
        "body": """Cuando entré a la startup donde trabajo éramos menos de 10 personas.

La comunicación era fácil. Todos sabían todo. Si necesitabas algo, "girabas la silla" y preguntabas. No hacía falta proceso, ni canal de Slack, ni documento.

Hoy somos casi 90.

Y hay un concepto que me parece genial para visualizar lo que pasa: la mandala de la comunicación.

Con 10 personas tienes 45 canales de comunicación posibles.
Con 50 personas tienes 1,225.
Con 90? Más de 4,000.

Cada persona nueva no suma un canal sino que multiplica la complejidad. Y lo peor es que nadie lo nota hasta que un día llegas a una reunión y te das cuenta de que 3 personas estaban trabajando en lo mismo sin saberlo.

Es la trampa del crecimiento rápido: todo el mundo está enfocado en escalar el producto, los clientes, el equipo... pero nadie escala la comunicación al mismo ritmo.

Y ahí es donde todo empieza a romperse. Pero eso da para otro post 👀

Te pasó algo parecido en tu empresa? De repente sentir que ya no te enteras de todo?"""
    },
    {
        "slug": "las-metodologias-no-te-van-a-salvar",
        "title": "Las metodologías no te van a salvar",
        "date": "mar 2026",
        "order": 4,
        "excerpt": "Las metodologías son herramientas, no religiones.",
        "body": """Las metodologías no te van a salvar.

He visto de todo: equipos que implementan EOS, OKRs, Scrum, SAFe... etc.

Y sí, las metodologías sirven. Te dan estructura, foco, un lenguaje común. Pero hay algo que para mi cada vez es más evidente: seguirlas al pie de la letra puede ser tan peligroso como no tener ninguna.

Lo veo mucho en startups:
Definen objetivos para el trimestre. El equipo se enfoca. Todo va bien. Pero a las 3 semanas el mercado se mueve, sale algo nuevo, un cliente pide algo que no estaba en el plan... y la respuesta es "no podemos, estamos enfocados en los objetivos del Q."

Técnicamente correcto. Pero en un ambiente donde las cosas cambian cada semana, atarte 100% al plan del trimestre es como seguir un mapa de hace 3 meses en una ciudad que se reconstruye todos los días.

Lo que fui aprendiendo hablando con founders y líderes de operaciones:

→ Las metodologías son herramientas, no religiones. El día que la sigues sin cuestionar, dejó de servirte.

→ Lo que funciona con 10 personas te puede matar con 50. Y lo que funciona en SaaS tradicional puede no servir en AI donde todo se mueve el doble de rápido.

→ El framework perfecto no existe. Lo que sí existe es un equipo con criterio para saber cuándo seguir el proceso y cuándo romperlo.

Los mejores equipos que conozco agarran pedazos de cada metodología, arman algo propio, y no les da culpa saltearse una regla si el contexto lo pide.

La metodología que mejor funciona es la que tu equipo puede adaptar sin sentir que está haciendo trampa.

Tu empresa sigue alguna metodología al pie de la letra o la fueron adaptando? Me da curiosidad"""
    },
    {
        "slug": "omitir-intro",
        "title": "Trabajar remoto te enseña a omitir intro",
        "date": "mar 2026",
        "order": 5,
        "excerpt": "Remote no es frío. Frío es trabajar en una oficina rodeada de gente y no conocer a nadie.",
        "body": """Trabajar en una empresa remota te enseña a "omitir intro".

No hay pasillo. No hay cafetería. No hay "ey qué tal el finde" antes de la reunión.

Abres el Slack y vas directo al punto.

Y al principio se siente raro. Frío. Como que falta algo.

Pero después te das cuenta de que lo que falta no es la intro. Lo que falta es ser intencional con la conexión.

En remoto nadie se va a conectar contigo por accidente. No hay encuentros casuales en el ascensor.

Si quieres conocer a tu equipo, tienes que buscarlo activamente.

Algunas cosas que aprendí:

1. Los 1:1 no son solo para hablar de tareas. Son para hablar de personas.
2. Un "cómo estás de verdad" en un DM vale más que 100 emojis en un canal.
3. Las calls sin agenda a veces son las más productivas.
4. Si solo hablas de trabajo, vas a trabajar con desconocidos.

Remote no es frío. Frío es trabajar en una oficina rodeada de gente y no conocer a nadie.

Trabajas remoto? Qué haces para conectar con tu equipo? 👇"""
    },
    {
        "slug": "la-ai-me-usa-a-mi",
        "title": "Últimamente siento que la AI me usa a mí",
        "date": "mar 2026",
        "order": 6,
        "excerpt": "Mi valor ya no es saber hacer. Es saber qué hacer.",
        "body": """Últimamente siento que la AI me usa a mí. No al revés.

Hace poco hice una herramienta de PTO para mi empresa. Sin escribir código. Con Claude.

Yo le describía el problema. La AI proponía la solución. Yo decía "dale". La AI lo ejecutaba.

Y no solo eso. Sus ideas eran mejores que las mías. Por lejos.

En algún momento pasé de ser la que dirige a ser la que aprueba.

Y es raro. Porque el producto salió. Funciona. Mejor de lo que hubiera hecho sola.

Pero hay una vocecita que dice: "y tu qué aportaste realmente?"

No sé si es síndrome del impostor 2.0 o si es una señal de que algo está cambiando en cómo trabajamos.

Lo que sí sé:
→ Mi valor ya no es saber hacer. Es saber qué hacer.
→ La AI ejecuta. Yo decido qué vale la pena ejecutar.
→ El trabajo no desaparece. Se mueve. Del "cómo" al "qué" y al "para qué".

Si tu valor ya no está en lo que sabes hacer... en qué está?"""
    },
    {
        "slug": "let-them",
        "title": "Let them",
        "date": "mar 2026",
        "order": 7,
        "excerpt": "Cuantas decisiones has dejado de tomar por miedo a lo que van a pensar los demás?",
        "body": """Cuantas decisiones has dejado de tomar por miedo a lo que van a pensar los demás?

Yo muchas. Más de las que me gustaría admitir

No aplicar a ese rol porque "van a pensar que no estoy lista"

No dar mi opinión en una reunión porque "van a pensar que no sé suficiente"

No publicar en LinkedIn porque "van a pensar que quién me creo"

Mel Robbins tiene un concepto que es tan simple pero a la vez tan poderoso: "Let them"

Déjalos.

Déjalos que piensen lo que quieran. Déjalos que opinen. Déjalos que critiquen

Porque la realidad es que van a pensar lo que quieran de todas formas. Hagas lo que hagas

Entonces la pregunta no es "qué van a pensar?"

La pregunta es "qué voy a dejar de hacer por preocuparme por lo que piensan?"

Desde que aplico esto, tomo decisiones más rápido. Y me equivoco igual que antes. Pero al menos son MIS errores

Que decisión estás postergando por miedo a la reacción de otros?"""
    },
    {
        "slug": "carrera-zigzag",
        "title": "Operations → Product → Operations → Chief of Staff",
        "date": "mar 2026",
        "order": 8,
        "excerpt": "Si tu carrera tampoco tiene sentido lineal, tal vez no es un bug. Es una feature.",
        "body": """Operations → Product → Operations → Chief of Staff

Mi carrera no tiene ningún sentido si la ves desde afuera.

A los 17 entré a mi primer trabajo en tech. No tenía idea de qué quería hacer, solo sabía que quería trabajar.

Empecé en operations. Hacía de todo: soporte, procesos, lo que hiciera falta.
Después me pasé a product. Pensé "esto es lo mío". Estuve un tiempo ahí, aprendí muchísimo.

Y luego volví a operations. Sí, volví. La gente me preguntaba si era un paso atrás. No lo era.

La verdad es que cada rol me enseñó algo diferente:

→ Operations me enseñó a ver el negocio completo, no solo una parte

→ Product me enseñó a priorizar y a decir que no

→ Volver a operations me enseñó que no hay camino lineal

Y ahora soy Chief of Staff. Un rol que básicamente combina todo lo anterior.
No fue un plan. Fue ir conectando los puntos.

Si tu carrera tampoco tiene "sentido lineal", tal vez no es un bug. Es una feature.

Tu carrera ha sido lineal o un zigzag como la mía?"""
    },
    {
        "slug": "el-foco-real",
        "title": "El foco real es saber qué ignorar",
        "date": "feb 2026",
        "order": 9,
        "excerpt": "Como haces foco cuando todo es urgente? Plot twist: no lo haces.",
        "body": """Como haces foco cuando todo es urgente?

Plot twist: no lo haces. Al menos no como te imaginas.

Llevo 7 años trabajando en startups y si algo aprendí es que el foco no es "hacer una cosa a la vez". Eso no existe en este mundo.

El foco real es saber qué ignorar.

Esto es lo que me funciona:

→ La regla de los 2 minutos. Si algo toma menos de 2 min, lo hago ya. Si no, va a la lista y lo priorizo después.

→ Identificar qué es realmente urgente vs qué solo se siente urgente. Spoiler: el 80% solo se siente urgente.

→ Decir que no (o "ahora no"). Suena obvio pero es lo más dificil. Cada sí que das es un no a otra cosa.

→ No revisar Slack/email cada 5 minutos. Es un agujero negro de tiempo.

→ Aceptar que van a haber días donde todo se va al carajo. Y está bien. Mañana es otro día.

La gente que parece tener todo bajo control no es porque hacen más. Es porque son muy buenos eligiendo qué no hacer.

Como manejas el foco? Tienes algun truco?"""
    },
    {
        "slug": "el-superpoder-del-chief-of-staff",
        "title": "El Chief of Staff no tiene poder",
        "date": "feb 2026",
        "order": 10,
        "excerpt": "Nadie te reporta. Pero tienes que lograr que toda la empresa se mueva.",
        "body": """El Chief of Staff no tiene poder.

Y ese es exactamente su superpoder.

Nadie te reporta. No eres el CEO. No eres el CPO. No eres el COO.

Pero tienes que lograr que toda la empresa se mueva.

Hace unos meses escribí sobre qué carajo hace un Chief of Staff. Ese post llegó a 48K personas.

Pero hubo una pregunta que se repitió mucho:
"Cómo logras que las cosas pasen si no mandas a nadie?"

Esto es lo que aprendí:

→ El CEO quiere velocidad. El dev quiere contexto. Finanzas quiere números. Si les hablas a todos igual, no le hablas a nadie.

→ Aparece antes de necesitar algo. La credibilidad no se exige, se construye.

→ "Es que el CEO dijo que..." Cuidado. El día que abusas de ese nombre, perdiste.

→ Tu trabajo no es dar órdenes. Es traducir. Conectar el "por qué" del CEO con el "cómo" de cada área.

Este rol es 80% soft skills, 20% ejecución.

Y el día que entiendes que tu trabajo es hacer que otros brillen, todo cambia.
Trabajas con equipos donde no tienes autoridad directa? Cómo lo manejas?"""
    },
    {
        "slug": "trabajar-y-estudiar",
        "title": "Trabajar full time y estudiar: DOs y DON'Ts",
        "date": "nov 2025",
        "order": 11,
        "excerpt": "No hay carrera que ganar. Solo un camino que recorrer.",
        "body": """Trabajar full time y estudiar: los DOs y DON'Ts de esa vida (en mi experiencia personal)

No es para todos, pero muchos no tenemos otra opción. Y aunque a veces parece una locura, se puede.

Es muy tentador soltar y quedarse solo con el trabajo, sobre todo cuando te está yendo muy bien y creces rápidamente sin ese título universitario.

Pero la universidad es un complemento importante. No solo por el título, sino por lo que te da: aprendizaje, resiliencia y una forma distinta de ver el mundo.

Tuve muchas crisis y dudas en el medio.

Recuerdo una charla con un familiar, en la que nos hicimos una pregunta: si se llama 'carrera universitaria', de verdad es una carrera? el que llega primero gana?

Desde mi punto de vista, no. Cada persona tiene sus ritmos y tiempos, y terminar antes o después del "ideal" no garantiza nada.

Después de varios años combinando ambos mundos, estos son mis DOs y DON'Ts:

DOs:
1. Organizarse es fundamental: bloquearse tiempos de estudio, anotarse desde el día uno todas las fechas de entregas y evaluaciones, registrar y anotar todo, etc.

2. Respetar los tiempos del trabajo y de la universidad: personalmente, se me hace mucho más tentador quedarme trabajando hasta tarde que estudiar, así que poner límites fue clave.

3. Conectar, escuchar y enfocarse: llegar cansada a clase luego de 8 horas (o más) intensas de trabajo y después tener que prestar atención 4 horas más de clase no es fácil, pero ahí está la diferencia entre sobrevivir y realmente aprender.

4. Busca apoyo: hablar con profesores o con tu equipo de trabajo cuando estás sobrepasado no te hace débil. Te hace responsable. Nadie puede adivinar que estás al límite si no lo dices.

DON'Ts
1. Una nota no define quién eres: queremos que nos vaya bien, sí, pero lo importante es el proceso de aprendizaje.

2. No dejes todo para último momento: parece obvio, pero no lo es. Hacer un poquito todos los días vale más que una maratón de estudio toda la noche.

3. No somos superhéroes: al principio creía que podía con todo: 8 horas de trabajo + 5 materias + hobbies + compartir con familia y amigos. Spoiler: no. Ir a tu ritmo y con equilibrio es mucho más sostenible.

4. No te compares: cada persona vive esa etapa con contextos distintos. Compararte con quien "ya se recibió" o "ya fue ascendido" solo te roba energía que podrías usar en avanzar a tu ritmo.

Me tomó tiempo entender que no hay carrera que ganar. Solo un camino que recorrer y mientras más lo disfrutes, mejor te va a ir.

Alguna vez trabajaste y estudiaste al mismo tiempo? Qué aprendiste de esa experiencia?"""
    },
    {
        "slug": "demos-en-vivo",
        "title": "Demo del producto LIVE o nada",
        "date": "oct 2025",
        "order": 12,
        "excerpt": "Me encantan las demos en vivo, incluso si fallan.",
        "body": """Demo del producto LIVE y en producción… o nada 😉

La semana pasada mi cuenta de X (Twitter) estaba invadida por el fail de la demo en vivo de Zuckerberg con los nuevos Meta Ray-Ban.

Lo que más me sorprendió no fue el fallo, sino la reacción: gente burlándose, tirando para abajo el producto (que btw me parece increíble y muy probable que termine usándolo)

Y yo me pregunto: de verdad esperaban perfección? eso existe? o qué pretendían?

A mí me encantan las demos en vivo, incluso si fallan. Porque una demo en vivo demuestra tres cosas clave:
1️⃣ Confianza en el equipo
2️⃣ Confianza en el producto
3️⃣ Valentía de mostrarte sin filtro frente a millones de personas (en este caso 😅)

No hay nada que perder, no hay nada que temer, y hay muchísimo por ganar y aprender

Alguien por aquí que haya visto la demo?"""
    },
    {
        "slug": "que-carajo-hace-un-chief-of-staff",
        "title": "Qué carajo hace un Chief of Staff?",
        "date": "sep 2025",
        "order": 13,
        "excerpt": "Eres la persona que resuelve lo que nadie más puede (o quiere) resolver.",
        "body": """Qué carajo hace un Chief of Staff? 🤨

Hace casi un año que ocupo este rol por primera vez en mi carrera profesional y la verdad, yo no tenía ni idea de qué significaba ser Chief of Staff. Pero me gustan los desafíos 😂

Las primeras preguntas que me hice (y que también me hacen todo el tiempo) fueron:
"Eso qué es? Asistente? Project manager? Mini-COO? is that a real job?"

La realidad: un Chief of Staff es todo eso y a veces nada de eso ( y si, si es un trabajo real)

Long story short: eres la persona que resuelve lo que nadie más puede (o quiere) resolver

En mi día a día eso significa:

- Organizar prioridades de distintas áreas o equipos

- Apoyar al CEO en tareas estratégicas (PR, investors, planificación, expansión, etc)

- Preparar información clave para decisiones importantes

- Apagar incendios de último minuto

- Y básicamente lo que aparezca ese día en la agenda sorpresa del caos

No existe un manual (o al menos yo no lo he visto todavía). Cada empresa le da el "job description" que le parece o necesita

Es un rol que se adapta al contexto y funciona como multiplicador: quita obstáculos, conecta puntos y asegura que la visión de la compañía avance sin fricciones

Por eso creo que cada vez más startups lo van a necesitar.

tú cómo lo ves? el Chief of Staff es un rol estratégico o simplemente un parche temporal?"""
    },
    {
        "slug": "empezar-a-trabajar-joven",
        "title": "La mejor carrera universitaria es empezar a trabajar",
        "date": "sep 2025",
        "order": 14,
        "excerpt": "Me gradué del colegio a los 16 en Caracas y a los pocos meses ya estaba en Buenos Aires.",
        "body": """La mejor carrera universitaria es empezar a trabajar a los 18 (o antes 👀)

Me gradué del colegio a los 16 en Caracas y a los pocos meses, ya estaba en Buenos Aires.

No tenía un plan brillante, ni un mapa claro de lo que venía. Tenía miedo, pero también muchas ganas de crecer y establecerme en este nuevo país

Entrar a trabajar en startups de tecnología no fue parte de una estrategia, al contrario, fue una coincidencia que terminó cambiándome la vida

No me malinterpreten, no soy anti-estudios y la universidad es un complemento muy importante. Pero la ventaja de haber trabajado antes y durante la universidad no tiene comparación

Estos son 5 aprendizajes que me tocaron a la fuerza (y que muchos descubren demasiado tarde):

1️⃣ La velocidad importa más que la perfección 🏃‍♀️
En las startups se actúa, se prueba y se aprende. "There's no time to overthink"

2️⃣ La resiliencia es la clave 🌳
Caerse es normal. Lo que cambia tu camino es qué tan rápido te levantas

3️⃣ Aprender a aprender 🤓
No se trata sólo de adaptarse: también de ser humilde, estar abierto a investigar, a escuchar
El conocimiento no termina nunca. Siempre hay algo nuevo por descubrir

4️⃣ La teoría sin práctica se queda corta 📚
Los libros son útiles, pero la presión real te enseña más rápido

5️⃣ Las personas con las que te rodeas importan 👀
Mentores, colegas, jefes: la gente que tienes cerca puede acelerar (o frenar) tu crecimiento

Hoy, a mis 23, miro hacia atrás y pienso que trabajar temprano fue sin darme cuenta, la mejor universidad que pude haber tenido

Qué pesa más para ti: un título universitario o la experiencia real?"""
    },
]

os.makedirs("posts", exist_ok=True)
for p in POSTS:
    md = f"""---
slug: {p['slug']}
title: {p['title']}
date: {p['date']}
order: {p['order']}
excerpt: {p['excerpt']}
---

{p['body']}
"""
    with open(f"posts/{p['slug']}.md", "w") as f:
        f.write(md)
    print("wrote", p['slug'])
print(f"{len(POSTS)} posts")
