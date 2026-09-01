# -*- coding: utf-8 -*-
"""
Genera es/index.html (home en castellà) a partir de index.html + la taula PARELLES.
Executa:  python genera_home_es.py
Si la home CA canvia, torna a executar: reporta les cadenes que ja no troba
perquè actualitzis la taula. La marca ("escola de dansa cristina colomé") NO es tradueix.
"""
import io
import os
import urllib.parse

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(ARREL, "index.html")
DESTI = os.path.join(ARREL, "es", "index.html")

q = urllib.parse.quote

PARELLES = [
    # ── head ──
    ('<html lang="ca">', '<html lang="es">'),
    ('<title>escola de dansa cristina colomé · Sant Gervasi, Barcelona</title>',
     '<title>escola de dansa cristina colomé · escuela de danza en Barcelona</title>'),
    ('<meta name="description" content="Escola de dansa a Sant Gervasi (Barcelona) amb més de 25 anys d\'història: clàssic, contemporani, jazz, hip-hop, claqué i més. 1a classe de prova gratuïta.">',
     '<meta name="description" content="Escuela de danza en Sant Gervasi (Barcelona) con más de 25 años de historia: clásico, contemporáneo, jazz, hip-hop, claqué y más. 1ª clase de prueba gratuita.">'),
    ('<link rel="canonical" href="https://escoladansa.com/">',
     '<link rel="canonical" href="https://escoladansa.com/es/">\n<link rel="alternate" hreflang="ca" href="https://escoladansa.com/">\n<link rel="alternate" hreflang="es" href="https://escoladansa.com/es/">\n<link rel="alternate" hreflang="x-default" href="https://escoladansa.com/">'),
    ('<meta property="og:title" content="escola de dansa cristina colomé · Sant Gervasi, Barcelona">',
     '<meta property="og:title" content="escola de dansa cristina colomé · escuela de danza en Barcelona">'),
    ('<meta property="og:description" content="Més de 25 anys movent Barcelona. Clàssic, contemporani, jazz, hip-hop, claqué i més, per a totes les edats i nivells. La primera classe de prova és gratuïta.">',
     '<meta property="og:description" content="Más de 25 años moviendo Barcelona. Clásico, contemporáneo, jazz, hip-hop, claqué y más, para todas las edades y niveles. La primera clase de prueba es gratuita.">'),
    ('<meta property="og:url" content="https://escoladansa.com/">',
     '<meta property="og:url" content="https://escoladansa.com/es/">'),
    ('<meta property="og:locale" content="ca_ES">', '<meta property="og:locale" content="es_ES">'),
    ('<meta name="twitter:title" content="escola de dansa cristina colomé · Sant Gervasi, Barcelona">',
     '<meta name="twitter:title" content="escola de dansa cristina colomé · escuela de danza en Barcelona">'),
    ('<meta name="twitter:description" content="Més de 25 anys movent Barcelona. La primera classe de prova és gratuïta.">',
     '<meta name="twitter:description" content="Más de 25 años moviendo Barcelona. La primera clase de prueba es gratuita.">'),

    # ── JSON-LD (LocalBusiness + FAQPage) ──
    ('"description": "Escola de dansa al barri de Sant Gervasi de Barcelona amb més de 25 anys d\'història. Classes de clàssic, contemporani, jazz, hip-hop, claqué, ball espanyol i dansa oriental per a totes les edats i nivells. Primera classe de prova gratuïta.",',
     '"description": "Escuela de danza en el barrio de Sant Gervasi de Barcelona con más de 25 años de historia. Clases de clásico, contemporáneo, jazz, hip-hop, claqué, baile español y danza oriental para todas las edades y niveles. Primera clase de prueba gratuita.",'),
    ('"@id": "https://escoladansa.com/#preguntes"', '"@id": "https://escoladansa.com/es/#preguntes"'),
    ('"name": "A quina edat es pot començar a ballar?"', '"name": "¿A qué edad se puede empezar a bailar?"'),
    ('"text": "Des de ben petits i sense límit d\'edat: tenim grups d\'iniciació a la dansa, infantils, juvenils i d\'adults, sempre organitzats per edats i nivells. De 0 a 99!"',
     '"text": "Desde bien pequeños y sin límite de edad: tenemos grupos de iniciación a la danza, infantiles, juveniles y de adultos, siempre organizados por edades y niveles. ¡De 0 a 99!"'),
    ('"name": "Cal tenir experiència prèvia?"', '"name": "¿Hace falta experiencia previa?"'),
    ('"text": "No. Hi ha grups des d\'iniciació fins a avançat en gairebé totes les disciplines, i t\'ajudarem a trobar el nivell on et sentis còmode."',
     '"text": "No. Hay grupos desde iniciación hasta avanzado en casi todas las disciplinas, y te ayudaremos a encontrar el nivel donde te sientas cómodo."'),
    ('"name": "Com puc provar una classe?"', '"name": "¿Cómo puedo probar una clase?"'),
    ('"text": "La primera classe de prova és gratuïta. Truca\'ns al 934 17 98 86 o passa\'t per l\'escola i et reservem plaça al grup que t\'encaixi."',
     '"text": "La primera clase de prueba es gratuita. Llámanos al 934 17 98 86 o pásate por la escuela y te reservamos plaza en el grupo que te encaje."'),
    ('"name": "Quant costen les classes?"', '"name": "¿Cuánto cuestan las clases?"'),
    ('"text": "Les quotes mensuals van dels 56 € (infantil, 1 dia per setmana) als 104 € (adults, 4 dies), amb opció de pagament trimestral. La primera classe de prova és gratuïta."',
     '"text": "Las cuotas mensuales van de los 56 € (infantil, 1 día por semana) a los 104 € (adultos, 4 días), con opción de pago trimestral. La primera clase de prueba es gratuita."'),
    ('"name": "On és l\'escola i com s\'hi arriba?"', '"name": "¿Dónde está la escuela y cómo se llega?"'),
    ('"text": "Som al carrer de Craywinckel, 25, al barri de Sant Gervasi – la Bonanova de Barcelona, a dos minuts de l\'estació d\'FGC Av. Tibidabo."',
     '"text": "Estamos en la calle Craywinckel, 25, en el barrio de Sant Gervasi – la Bonanova de Barcelona, a dos minutos de la estación de FGC Av. Tibidabo."'),
    ('"name": "Llogueu sales o feu celebracions?"', '"name": "¿Alquiláis salas o hacéis celebraciones?"'),
    ('"text": "Sí: disposem de 3 sales condicionades i insonoritzades per llogar, i organitzem aniversaris, balls de núvis i comiats, sobretot els divendres al vespre."',
     '"text": "Sí: disponemos de 3 salas acondicionadas e insonorizadas para alquilar, y organizamos cumpleaños, bailes de novios y despedidas, sobre todo los viernes por la noche."'),

    # ── nav ──
    ('hreflang="ca" class="actiu">Català</a>', 'hreflang="ca">Català</a>'),
    ('hreflang="es">Castellano</a>', 'hreflang="es" class="actiu">Castellano</a>'),
    ('<a href="/" class="actiu">cat</a>', '<a href="/">cat</a>'),
    ('<span>/</span><a href="/es/">es</a>', '<span>/</span><a href="/es/" class="actiu">es</a>'),
    (">l'escola</a>", '>la escuela</a>'),
    ('>activitats</a>', '>actividades</a>'),
    ('<a href="/horaris/">horaris</a>', '<a href="/es/horarios/">horarios</a>'),
    ('<a href="/preus/">preus</a>', '<a href="/es/precios/">precios</a>'),
    ('<a href="/blog/">blog</a>', '<a href="/es/blog/">blog</a>'),
    ('>contacte</a>', '>contacto</a>'),

    # ── hero ──
    ('aria-hidden="true">dansa</span>', 'aria-hidden="true">danza</span>'),
    ("const MOTS_ROTATIUS = ['dansa','ballet','jazz','hip-hop','claqué','k-pop','música','zumba','ioga','dansa'];",
     "const MOTS_ROTATIUS = ['danza','ballet','jazz','hip-hop','claqué','k-pop','música','zumba','yoga','danza'];"),
    ('<p class="hero-sub">més de 25 anys movent Barcelona. clàssic, contemporani, jazz, hip-hop, claqué, espanyol, dansa oriental… per a totes les edats i nivells.</p>',
     '<p class="hero-sub">más de 25 años moviendo Barcelona. clásico, contemporáneo, jazz, hip-hop, claqué, español, danza oriental… para todas las edades y niveles.</p>'),
    ('>classe de prova gratuïta</a>', '>clase de prueba gratuita</a>'),
    ('<a class="boto boto-buit" href="/horaris/">veure horaris</a>',
     '<a class="boto boto-buit" href="/es/horarios/">ver horarios</a>'),

    # ── marquesina ──
    ('>ballet clàssic</span>', '>ballet clásico</span>'),
    ('>contemporani</span>', '>contemporáneo</span>'),
    ('>espanyol</span>', '>español</span>'),
    ('>dansa oriental</span>', '>danza oriental</span>'),
    ('>ioga</span>', '>yoga</span>'),
    ('>puntes</span>', '>puntas</span>'),

    # ── cita ──
    ('«la dansa ens ajuda a <span class="destacat">sentir-nos a gust</span> en el nostre propi cos, a tenir-ne consciència, a saber utilitzar-lo per <span class="destacat">expressar allò que sentim</span> i imaginem»',
     '«la danza nos ayuda a <span class="destacat">sentirnos a gusto</span> en nuestro propio cuerpo, a tener conciencia de él, a saber utilizarlo para <span class="destacat">expresar lo que sentimos</span> e imaginamos»'),
    ('aria-hidden="true">passió</span>', 'aria-hidden="true">pasión</span>'),
    ('aria-hidden="true">ballar</span>', 'aria-hidden="true">bailar</span>'),
    ("aria-hidden=\"true\">moure's</span>", 'aria-hidden="true">moverse</span>'),
    ('aria-hidden="true">vine!</span>', 'aria-hidden="true">¡ven!</span>'),
    ('aria-hidden="true">dubtes</span>', 'aria-hidden="true">dudas</span>'),
    ('aria-hidden="true">novetats</span>', 'aria-hidden="true">novedades</span>'),
    ('aria-hidden="true">família</span>', 'aria-hidden="true">familia</span>'),

    # ── l'escola ──
    ('<div class="etiqueta reveal">l\'escola</div>', '<div class="etiqueta reveal">la escuela</div>'),
    ('ballar és un plaer, i més encara si es fa entre amics', 'bailar es un placer, y más aún si se hace entre amigos'),
    ("Som un centre de referència al barri de Sant Gervasi, a Barcelona. Un espai pensat per aprendre, formar-se, interactuar i gaudir, amb propostes per a totes les edats i tots els nivells: des de la iniciació a la dansa fins a la preparació d'exàmens oficials.",
     'Somos un centro de referencia en el barrio de Sant Gervasi, en Barcelona. Un espacio pensado para aprender, formarse, interactuar y disfrutar, con propuestas para todas las edades y todos los niveles: desde la iniciación a la danza hasta la preparación de exámenes oficiales.'),
    ("<small>anys d'història</small>", '<small>años de historia</small>'),
    ('<small>sales insonoritzades</small>', '<small>salas insonorizadas</small>'),
    ('<small>disciplines</small>', '<small>disciplinas</small>'),
    ('<small>totes les edats</small>', '<small>todas las edades</small>'),

    # ── activitats ──
    ('<div class="etiqueta reveal">activitats</div>', '<div class="etiqueta reveal">actividades</div>'),
    ("troba la teva manera de moure't", 'encuentra tu manera de moverte'),
    ("Cada estil és una porta d'entrada diferent a la dansa. Totes les classes s'organitzen per edats i nivells.",
     'Cada estilo es una puerta de entrada diferente a la danza. Todas las clases se organizan por edades y niveles.'),
    ('<h3>ballet clàssic</h3>', '<h3>ballet clásico</h3>'),
    ('<p>iniciació, infantil, juvenil i adults · puntes · preparació RAD</p>',
     '<p>iniciación, infantil, juvenil y adultos · puntas · preparación RAD</p>'),
    ('<p>moviment lliure i orgànic, tècnica i creació</p>', '<p>movimiento libre y orgánico, técnica y creación</p>'),
    ('<p>energia, ritme i coreografia per a totes les edats</p>', '<p>energía, ritmo y coreografía para todas las edades</p>'),
    ("<p>estils urbans des d'infantil fins a adults avançat</p>", '<p>estilos urbanos desde infantil hasta adultos avanzado</p>'),
    ('<p>el ritme als peus, de juvenil a adults</p>', '<p>el ritmo en los pies, de juvenil a adultos</p>'),
    ('<h3>ball espanyol</h3>', '<h3>baile español</h3>'),
    ('<p>tradició, caràcter i tècnica espanyola</p>', '<p>tradición, carácter y técnica española</p>'),
    ('<h3>dansa oriental</h3>', '<h3>danza oriental</h3>'),
    ('<p>dansa del ventre, expressió i feminitat</p>', '<p>danza del vientre, expresión y feminidad</p>'),
    ('<p>les coreos del moment i actitud sobre talons</p>', '<p>las coreos del momento y actitud sobre tacones</p>'),
    ('<h3>musical &amp; interpretació</h3>', '<h3>musical &amp; interpretación</h3>'),
    ('<p>dansa-teatre: ballar, cantar i actuar</p>', '<p>danza-teatro: bailar, cantar y actuar</p>'),
    ('<h3>formació escènica</h3>', '<h3>formación escénica</h3>'),
    ('<p>divendres a la tarda: jazz, hip-hop, claqué, cant i interpretació</p>',
     '<p>viernes por la tarde: jazz, hip-hop, claqué, canto e interpretación</p>'),
    ('<h3>cos &amp; benestar</h3>', '<h3>cuerpo &amp; bienestar</h3>'),
    ('<p>ioga, barre i zumba per cuidar-se ballant</p>', '<p>yoga, barre y zumba para cuidarse bailando</p>'),
    ('<p>suor, força i empoderament en grup</p>', '<p>sudor, fuerza y empoderamiento en grupo</p>'),
    ('Busques classe per al teu fill o filla? Mira la guia de <a href="/dansa-infantil/">dansa per a nens i nenes</a>. I si és per a tu, la de <a href="/dansa-adults/">dansa per a adults</a>.',
     '¿Buscas clase para tu hijo o hija? Mira la guía de <a href="/es/danza-infantil/">danza para niños y niñas</a>. Y si es para ti, la de <a href="/es/danza-adultos/">danza para adultos</a>.'),
    ('També fem <strong>classes particulars</strong>, balls de saló, coreografies per a <strong>casaments i celebracions</strong>, tallers de cap de setmana i cursos intensius de vacances. <a href="#contacte">explica\'ns què busques →</a>',
     'También hacemos <strong>clases particulares</strong>, bailes de salón, coreografías para <strong>bodas y celebraciones</strong>, talleres de fin de semana y cursos intensivos de vacaciones. <a href="#contacte">cuéntanos qué buscas →</a>'),

    # ── bandes horaris/preus ──
    ('<div class="etiqueta reveal">curs 2026–27</div>', '<div class="etiqueta reveal">curso 2026–27</div>'),
    ('<h2 class="reveal" data-lletres>horaris</h2>', '<h2 class="reveal" data-lletres>horarios</h2>'),
    ('De dilluns a divendres, tardes per a infantils i juvenils, vespres per a adults, i matins de barre. Consulta la graella completa per sala i nivell.',
     'De lunes a viernes, tardes para infantiles y juveniles, noches para adultos y mañanas de barre. Consulta la parrilla completa por sala y nivel.'),
    ('<a class="boto boto-ple reveal" href="/horaris/">veure els horaris</a>',
     '<a class="boto boto-ple reveal" href="/es/horarios/">ver los horarios</a>'),
    ('<div class="etiqueta reveal">tarifes</div>', '<div class="etiqueta reveal">tarifas</div>'),
    ('<h2 class="reveal" data-lletres>preus</h2>', '<h2 class="reveal" data-lletres>precios</h2>'),
    ('Quotes mensuals des de 56 €. Paga per mes o per trimestre, amb 1, 2, 3 o 4 dies de classe a la setmana. La primera classe de prova és gratuïta.',
     'Cuotas mensuales desde 56 €. Paga por mes o por trimestre, con 1, 2, 3 o 4 días de clase a la semana. La primera clase de prueba es gratuita.'),
    ('<a class="boto boto-buit reveal" href="/preus/">veure les tarifes</a>',
     '<a class="boto boto-buit reveal" href="/es/precios/">ver las tarifas</a>'),

    # ── opinions (a la versió ES: cites en castellà ORIGINAL de Google) ──
    ('<div class="etiqueta reveal">opinions</div>', '<div class="etiqueta reveal">opiniones</div>'),
    ('les famílies ho diuen millor que nosaltres', 'las familias lo dicen mejor que nosotros'),
    ('<strong>4,8</strong> a Google · 21 opinions', '<strong>4,8</strong> en Google · 21 opiniones'),
    ('«Una escola increïble! Professors immillorables, ambient sa, familiar i proper. Un gran nivell amb uns professionals exemplars.»',
     '«Una escuela increíble! Profesores inmejorables, ambiente sano, familiar y cercano. Un gran nivel con unos profesionales ejemplares.»'),
    ('«Escola fantàstica per a totes les edats! Ambient espectacularment agradable i familiar. Et permet aprendre totes les disciplines i amb diferents nivells.»',
     '«¡Escuela fantástica para todas las edades! Ambiente espectacularmente agradable y familiar. Te permite aprender todas las disciplinas y con diferentes niveles.»'),
    ("«L'ambient familiar i de bon rotllo que es respira a l'escola és un punt a destacar. Els professors són molt professionals […] fan que et sentis estimat i part de l'escola. Molt recomanable!»",
     '«El ambiente familiar y de buen rollo que se respira en la escuela es un punto a destacar. Los profesores son muy profesionales […] hacen que te sientas querido y parte de la escuela. ¡Muy recomendable!»'),
    ('<small>· ressenya a Google</small>', '<small>· reseña en Google</small>'),
    ('Ressenyes traduïdes del castellà original. Llegeix-les totes tal com es van escriure o <a',
     'Léelas todas en Google o <a'),
    ('rel="noopener">deixa-hi la teva →</a>', 'rel="noopener">deja la tuya →</a>'),

    # ── FAQ visibles ──
    ('<div class="etiqueta reveal">preguntes freqüents</div>', '<div class="etiqueta reveal">preguntas frecuentes</div>'),
    ('abans de venir, el que tothom ens pregunta', 'antes de venir, lo que todo el mundo nos pregunta'),
    ('<summary>A quina edat es pot començar a ballar?</summary>', '<summary>¿A qué edad se puede empezar a bailar?</summary>'),
    ("Des de ben petits i sense límit d'edat: tenim grups d'iniciació a la dansa, infantils, juvenils i d'adults, sempre organitzats per edats i nivells. De 0 a 99!",
     'Desde bien pequeños y sin límite de edad: tenemos grupos de iniciación a la danza, infantiles, juveniles y de adultos, siempre organizados por edades y niveles. ¡De 0 a 99!'),
    ('<summary>Cal tenir experiència prèvia?</summary>', '<summary>¿Hace falta experiencia previa?</summary>'),
    ("No. Hi ha grups des d'iniciació fins a avançat en gairebé totes les disciplines, i t'ajudarem a trobar el nivell on et sentis còmode.",
     'No. Hay grupos desde iniciación hasta avanzado en casi todas las disciplinas, y te ayudaremos a encontrar el nivel donde te sientas cómodo.'),
    ('<summary>Com puc provar una classe?</summary>', '<summary>¿Cómo puedo probar una clase?</summary>'),
    ('La primera classe de prova és gratuïta. Truca\'ns al <a href="tel:+34934179886">934 17 98 86</a> o passa\'t per l\'escola i et reservem plaça al grup que t\'encaixi.',
     'La primera clase de prueba es gratuita. Llámanos al <a href="tel:+34934179886">934 17 98 86</a> o pásate por la escuela y te reservamos plaza en el grupo que te encaje.'),
    ('<summary>Quant costen les classes?</summary>', '<summary>¿Cuánto cuestan las clases?</summary>'),
    ('Les quotes mensuals van dels 56 € (infantil, 1 dia per setmana) als 104 € (adults, 4 dies), amb opció de pagament trimestral. Consulta <a href="/preus/">totes les tarifes</a>.',
     'Las cuotas mensuales van de los 56 € (infantil, 1 día por semana) a los 104 € (adultos, 4 días), con opción de pago trimestral. Consulta <a href="/es/precios/">todas las tarifas</a>.'),
    ("<summary>On és l'escola i com s'hi arriba?</summary>", '<summary>¿Dónde está la escuela y cómo se llega?</summary>'),
    ('Som al carrer de Craywinckel, 25, al barri de Sant Gervasi – la Bonanova, a dos minuts de l\'estació d\'FGC Av. Tibidabo.',
     'Estamos en la calle Craywinckel, 25, en el barrio de Sant Gervasi – la Bonanova, a dos minutos de la estación de FGC Av. Tibidabo.'),
    ('<summary>Llogueu sales o feu celebracions?</summary>', '<summary>¿Alquiláis salas o hacéis celebraciones?</summary>'),
    ('Sí: disposem de 3 sales condicionades i insonoritzades per llogar, i organitzem aniversaris, balls de núvis i comiats, sobretot els divendres al vespre.',
     'Sí: disponemos de 3 salas acondicionadas e insonorizadas para alquilar, y organizamos cumpleaños, bailes de novios y despedidas, sobre todo los viernes por la noche.'),

    # ── newsletter ──
    ("no et perdis res del que passa a l'escola", 'no te pierdas nada de lo que pasa en la escuela'),
    ("Tallers, cursos intensius, el festival de fi de curs i les novetats de cada temporada, directament a la teva safata. Res d'spam: només el que importa.",
     'Talleres, cursos intensivos, el festival de fin de curso y las novedades de cada temporada, directamente en tu bandeja. Nada de spam: solo lo que importa.'),
    ('placeholder="el teu nom"', 'placeholder="tu nombre"'),
    ('placeholder="el teu email"', 'placeholder="tu email"'),
    (">apunta-m'hi</button>", '>apúntame</button>'),
    ("accepto rebre comunicacions de l'escola segons la", 'acepto recibir comunicaciones de la escuela según la'),
    ('>política de privacitat</button>', '>política de privacidad</button>'),

    # ── contacte ──
    ('<div class="etiqueta reveal">contacte</div>', '<div class="etiqueta reveal">contacto</div>'),
    ('vine a provar-ho. la primera classe és gratis.', 'ven a probarlo. la primera clase es gratis.'),
    ("Som a Sant Gervasi, a dos minuts de l'FGC Av. Tibidabo. Truca'ns o passa't per l'escola i t'ajudarem a trobar la classe perfecta per a tu. També pots llogar les nostres sales.",
     'Estamos en Sant Gervasi, a dos minutos del FGC Av. Tibidabo. Llámanos o pásate por la escuela y te ayudaremos a encontrar la clase perfecta para ti. También puedes alquilar nuestras salas.'),
    ("<strong>truca'ns</strong>", '<strong>llámanos</strong>'),
    ('<small>resposta al moment</small>', '<small>respuesta al momento</small>'),
    ("<strong>formulari</strong><small>explica'ns què busques</small>", '<strong>formulario</strong><small>cuéntanos qué buscas</small>'),
    ('<strong>com arribar?</strong>', '<strong>¿cómo llegar?</strong>'),
    ('<small>adreça</small>', '<small>dirección</small>'),
    ('<small>lloguer de sales</small>', '<small>alquiler de salas</small>'),
    ('<span>3 sales condicionades i insonoritzades</span>', '<span>3 salas acondicionadas e insonorizadas</span>'),
    ('<small>celebracions</small>', '<small>celebraciones</small>'),
    ('<span>aniversaris · balls de núvis · comiats</span>', '<span>cumpleaños · bailes de novios · despedidas</span>'),
    ('comparteix-nos', 'compártenos'),
    ('text=Mira%20l%27escola%20de%20dansa%20Cristina%20Colom%C3%A9%2C%20a%20Sant%20Gervasi%20La%20primera%20classe%20de%20prova%20%C3%A9s%20gratu%C3%AFta!%0Ahttps%3A%2F%2Fescoladansa.com',
     'text=' + q("Mira la escuela de danza Cristina Colomé, en Sant Gervasi. ¡La primera clase de prueba es gratuita!\nhttps://escoladansa.com/es/")),

    # ── nl-card + layers ──
    ('<strong>no et perdis res 💃</strong>', '<strong>no te pierdas nada 💃</strong>'),
    ('<p>tallers, intensius i el festival de fi de curs, directament a la teva safata.</p>',
     '<p>talleres, intensivos y el festival de fin de curso, directamente en tu bandeja.</p>'),
    (">apunta-t'hi</a>", '>apúntate</a>'),
    ('<div class="etiqueta">contacte</div>', '<div class="etiqueta">contacto</div>'),
    ('<h2>escriu-nos</h2>', '<h2>escríbenos</h2>'),
    ("<p class=\"sota\">explica'ns què busques i et respondrem molt aviat</p>",
     '<p class="sota">cuéntanos qué buscas y te responderemos muy pronto</p>'),
    ('placeholder="email o telèfon"', 'placeholder="email o teléfono"'),
    ('placeholder="explica\'ns què busques: estil, edat, horaris..."', 'placeholder="cuéntanos qué buscas: estilo, edad, horarios..."'),
    ('>envia el missatge</button>', '>envía el mensaje</button>'),
    ('en enviar el missatge acceptes la <button type="button" class="news-privacitat" data-obre="layerPrivacitat">política de privacidad</button> — només farem servir les dades per respondre\'t',
     'al enviar el mensaje aceptas la <button type="button" class="news-privacitat" data-obre="layerPrivacitat">política de privacidad</button> — solo usaremos los datos para responderte'),
    ('<div class="etiqueta">protecció de dades</div>', '<div class="etiqueta">protección de datos</div>'),
    ('<h2>política de privacitat</h2>', '<h2>política de privacidad</h2>'),
    ('<p class="sota">informació bàsica sobre el tractament de les teves dades (RGPD)</p>',
     '<p class="sota">información básica sobre el tratamiento de tus datos (RGPD)</p>'),
    ('<h3>responsable</h3>', '<h3>responsable</h3>'),
    ('<h3>finalitat</h3>', '<h3>finalidad</h3>'),
    ('Enviar-te per correu electrònic informació sobre les activitats de l\'escola (novetats del curs, tallers, cursos intensius i el festival de fi de curs) i, si ens escrius pel formulari de contacte, respondre la teva consulta.',
     'Enviarte por correo electrónico información sobre las actividades de la escuela (novedades del curso, talleres, cursos intensivos y el festival de fin de curso) y, si nos escribes por el formulario de contacto, responder tu consulta.'),
    ('<h3>legitimació</h3>', '<h3>legitimación</h3>'),
    ('El teu consentiment, que dónes en marcar la casella i apuntar-te al butlletí. El pots retirar quan vulguis.',
     'Tu consentimiento, que das al marcar la casilla y apuntarte al boletín. Puedes retirarlo cuando quieras.'),
    ('<h3>destinataris</h3>', '<h3>destinatarios</h3>'),
    ('Les dades es desen a Mailchimp (The Rocket Science Group LLC), la plataforma que fem servir per enviar els correus, acollida a marcs de protecció de dades UE–EUA. No cedim les teves dades a ningú més.',
     'Los datos se guardan en Mailchimp (The Rocket Science Group LLC), la plataforma que usamos para enviar los correos, acogida a marcos de protección de datos UE–EE. UU. No cedemos tus datos a nadie más.'),
    ('<h3>drets</h3>', '<h3>derechos</h3>'),
    ('Pots accedir, rectificar o suprimir les teves dades, o oposar-te al tractament, escrivint-nos o trucant-nos a l\'escola. També pots donar-te de baixa directament des de l\'enllaç que trobaràs al peu de cada correu.',
     'Puedes acceder, rectificar o suprimir tus datos, u oponerte al tratamiento, escribiéndonos o llamándonos a la escuela. También puedes darte de baja directamente desde el enlace que encontrarás al pie de cada correo.'),

    # ── JS: missatges del formulari i newsletter ──
    ("'gairebé fet! revisa el teu correu (i l\\'spam) i clica l\\'enllaç de confirmació 💌'",
     "'¡casi listo! revisa tu correo (y el spam) y haz clic en el enlace de confirmación 💌'"),
    ("'fet! ja ets dins. ens veiem aviat a l\\'escola 💃'", "'¡hecho! ya estás dentro. nos vemos pronto en la escuela 💃'"),
    ("'aquest email ja està apuntat al butlletí!'", "'¡este email ya está apuntado al boletín!'"),
    ("'no s\\'ha pogut enviar. torna-ho a provar d\\'aquí a un moment o truca\\'ns al 934 17 98 86.'",
     "'no se ha podido enviar. vuelve a intentarlo en un momento o llámanos al 934 17 98 86.'"),
    ("'el butlletí encara no està connectat — truca\\'ns al 934 17 98 86 i t\\'hi apuntem!'",
     "'el boletín aún no está conectado — ¡llámanos al 934 17 98 86 y te apuntamos!'"),
    ("'escriu el teu nom, si us plau'", "'escribe tu nombre, por favor'"),
    ("'revisa l\\'email — sembla que no és complet'", "'revisa el email — parece que no está completo'"),
    ("'marca la casella de la política de privacitat per continuar'", "'marca la casilla de la política de privacidad para continuar'"),
    ("'deixa\\'ns un email o un telèfon per poder respondre\\'t'", "'déjanos un email o un teléfono para poder responderte'"),
    ("'explica\\'ns en dues línies què busques'", "'cuéntanos en dos líneas qué buscas'"),
    ("'rebut! et respondrem molt aviat 💌'", "'¡recibido! te responderemos muy pronto 💌'"),
    ("'no s\\'ha pogut enviar — truca\\'ns al 934 17 98 86 i ho solucionem'",
     "'no se ha podido enviar — llámanos al 934 17 98 86 y lo solucionamos'"),
    ("'enviant…'", "'enviando…'"),
]

# el WhatsApp de contacte: prefix del missatge pre-omplert
_WA_CA = "Hola!%20M%27agradaria%20informaci%C3%B3%20sobre%20les%20classes"
_WA_ES = "%C2%A1Hola!%20Me%20gustar%C3%ADa%20informaci%C3%B3n%20sobre%20las%20clases"
PARELLES.append((_WA_CA, _WA_ES))

PARELLES += [
    ("🍪 Fem servir galetes d'anàlisi (Google Analytics) per entendre com s'utilitza la web i millorar-la.",
     '🍪 Usamos cookies de análisis (Google Analytics) para entender cómo se utiliza la web y mejorarla.'),
    (">d'acord</button>", '>de acuerdo</button>'),
    ('>no, gràcies</button>', '>no, gracias</button>'),
    ('<h3>galetes</h3>', '<h3>cookies</h3>'),
    ("Només amb el teu consentiment (banner de galetes), fem servir Google Analytics per obtenir estadístiques anònimes d'ús de la web. Si les rebutges, no es carrega cap galeta d'anàlisi. Pots canviar d'opinió esborrant les galetes del teu navegador.",
     'Solo con tu consentimiento (banner de cookies), usamos Google Analytics para obtener estadísticas anónimas de uso de la web. Si las rechazas, no se carga ninguna cookie de análisis. Puedes cambiar de opinión borrando las cookies de tu navegador.'),
]

# rutes relatives d'assets: des de /es/ s'han de fer absolutes
# ── mòdul del blog a la home: cadenes fixes + parelles DINÀMIQUES dels 3 posts
# més nous (les targetes les injecta genera_blog.py; executa'l abans que aquest)
import html as _html  # noqa: E402
from blog_posts import POSTS as _POSTS  # noqa: E402

_e = lambda t: _html.escape(t, quote=True)  # les targetes porten el text escapat
PARELLES += [
    ('<h2 class="reveal" data-lletres>consells de dansa i vida d\'escola</h2>',
     '<h2 class="reveal" data-lletres>consejos de danza y vida de escuela</h2>'),
    ('<span class="mot-fons" aria-hidden="true">consells</span>',
     '<span class="mot-fons" aria-hidden="true">consejos</span>'),
    ('Un article nou cada setmana: <a href="/blog/">visita el blog</a>.',
     'Un artículo nuevo cada semana: <a href="/es/blog/">visita el blog</a>.'),
]
for _p in sorted(_POSTS, key=lambda x: x["data"], reverse=True)[:3]:
    for _pa in [
        (f'href="/blog/{_p["slug"]}/"', f'href="/es/blog/{_p["slug_es"]}/"'),
        (f'<span class="cat-post">{_e(_p["categoria"])}</span>',
         f'<span class="cat-post">{_e(_p["categoria_es"])}</span>'),
        (f'<h3>{_e(_p["h1"])}</h3>', f'<h3>{_e(_p["h1_es"])}</h3>'),
        (f'<p>{_e(_p["excerpt"])}</p>', f'<p>{_e(_p["excerpt_es"])}</p>'),
        (f'<span class="peu-card">{_e(_p["data_ca"])}</span>',
         f'<span class="peu-card">{_e(_p["data_es"])}</span>'),
    ]:
        if _pa not in PARELLES:  # dues targetes poden compartir categoria/data
            PARELLES.append(_pa)

PARELLES += [
    ('"assets/', '"/assets/'),
    ("'assets/", "'/assets/"),
    ('url(assets/', 'url(/assets/'),
]


def main():
    h = io.open(ORIGEN, encoding="utf-8").read()
    fetes, perdudes = 0, []
    for ca, es in PARELLES:
        if ca in h:
            h = h.replace(ca, es)
            fetes += 1
        else:
            perdudes.append(ca[:70])
    os.makedirs(os.path.dirname(DESTI), exist_ok=True)
    io.open(DESTI, "w", encoding="utf-8", newline="\n").write(h)
    print(f"es/index.html generada · {fetes}/{len(PARELLES)} substitucions")
    if perdudes:
        print("NO TROBADES (revisa la taula):")
        for p in perdudes:
            print("  -", p.encode("ascii", "backslashreplace").decode())


if __name__ == "__main__":
    main()
