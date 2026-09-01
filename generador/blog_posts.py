# -*- coding: utf-8 -*-
"""
Contingut del blog d'escoladansa.com — un diccionari per article, CA + ES.
Per publicar un post nou: afegeix-lo aquí i executa genera_blog.py.
El cos és HTML (p, h2, ul/li, a) i es renderitza dins de <section class="article">.
"""

POSTS = [
    {
        "slug": "a-quina-edat-comencar-dansa",
        "slug_es": "a-que-edad-empezar-danza",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-09-01",
        "data_ca": "1 de setembre de 2026",
        "data_es": "1 de septiembre de 2026",
        "minuts": 5,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-edat-infants.jpg",
        "img": "blog-edat-infants.jpg",
        "img_alt": "Unes sabatilles de ballet petites a terra d'una sala de dansa, amb puntes penjades a la barra al fons",
        "img_alt_es": "Unas zapatillas de ballet pequeñas en el suelo de una sala de danza, con puntas colgadas en la barra al fondo",
        "related_pagines": ["dansa-infantil", "ballet-classic", "hip-hop", "horaris"],
        "related_posts": ["comencar-dansa-adults"],

        "title": "a quina edat pot començar el meu fill a fer dansa? · escola de dansa cristina colomé",
        "desc": "La pregunta que més ens fan les famílies: a quina edat es pot començar a fer dansa? Guia per franges d'edat (dels 3 anys a l'adolescència), senyals que el teu fill està a punt i com és la primera classe.",
        "h1": "a quina edat pot començar el meu fill a fer dansa?",
        "intro": "És la pregunta que més escoltem a recepció. La resposta curta: abans del que et penses. La llarga — amb franges d'edat, senyals i consells de més de 25 anys d'escola — la tens aquí.",
        "excerpt": "Dels 3 anys a l'adolescència: la guia per franges d'edat que responem cada setembre a recepció, amb els senyals que indiquen que el teu fill està a punt.",
        "cos": """
<p>Cada setembre passa el mateix: una mare o un pare entra per la porta de Craywinckel amb una criatura de la mà i ens pregunta, una mica insegur, si «encara és massa petit» o si «ja fa tard». Després de més de 25 anys fent classes a nens i nenes de Sant Gervasi, la resposta gairebé sempre és la mateixa: <strong>ni una cosa ni l'altra</strong>. Cada edat té la seva porta d'entrada a la dansa — només cal saber quina és.</p>

<h2>als 3-4 anys: la dansa és un joc</h2>
<p>A aquesta edat no parlem de tècnica, parlem de <strong>psicomotricitat, música i imaginació</strong>. A les classes d'iniciació a la dansa, els més petits aprenen a escoltar el ritme, a controlar el cos, a esperar el seu torn i a compartir espai amb altres nens. Tot es fa jugant: som papallones, som gegants, som gotes de pluja. Sense adonar-se'n, estan construint la base de tot el que vindrà: equilibri, coordinació, lateralitat i — potser el més important — <strong>l'associació de ballar amb passar-s'ho bé</strong>.</p>

<h2>dels 5 als 7: la primera tècnica (sense presses)</h2>
<p>Aquí el joc comença a tenir estructura. Apareixen les primeres posicions, les primeres coreografies curtes, la memòria del moviment. És una edat fantàstica per començar <a href="/ballet-classic/">ballet clàssic</a>, perquè el cos és flexible, el cap és una esponja i encara no hi ha vergonya. Però compte: la clau en aquesta franja és que la tècnica arribi <strong>sense treure la il·lusió</strong>. Un nen de 6 anys que surt de classe content tornarà tota la vida; un que s'avorreix amb exercicis massa rígids, no.</p>

<h2>dels 8 als 12: l'edat d'or per triar estil</h2>
<p>Entre els 8 i els 12 anys els nens ja tenen prou control corporal per aprendre de debò, i prou personalitat per saber què els agrada. És el moment de <strong>provar estils</strong>: n'hi ha que s'enamoren de la disciplina del clàssic, d'altres que vibren amb l'energia del <a href="/hip-hop/">hip-hop</a> o del jazz, i d'altres que descobreixen que el que els agrada és actuar, cantar i ballar alhora. Si comença de zero a aquesta edat, cap problema: els grups estan pensats per edat <strong>i</strong> per nivell, així que mai no se sentirà fora de lloc.</p>

<h2>adolescents: no, no fan tard</h2>
<p>Ho diem ben clar perquè és el dubte que més frena: <strong>un adolescent que comença de zero no fa tard</strong>. Fa tard qui vol ser primera ballarina d'una companyia professional — i aquest no és el cas del 99% de les famílies que ens ho pregunten. Per a tota la resta (ballar bé, fer exercici, guanyar confiança, tenir un grup, pujar a un escenari), els 13, 14 o 15 anys són una edat magnífica. De fet, els adolescents aprenen rapidíssim: en un curs fan el camí que un nen petit fa en tres.</p>

<h2>els senyals que està a punt</h2>
<p>Més que l'edat, mira això:</p>
<ul>
<li><strong>Balla a casa.</strong> Quan sona música i el cos se'n va sol, el missatge és clar.</li>
<li><strong>Aguanta una activitat dirigida.</strong> Si ja segueix una classe (o el ritme de l'escola bressol) sense frustrar-se, pot seguir una classe de dansa.</li>
<li><strong>En té ganes.</strong> El millor predictor de tots. La dansa proposada funciona; la dansa imposada, no.</li>
</ul>

<h2>com ho fem a l'escola</h2>
<p>A l'escola tenim grups des dels 3 anys fins a l'adolescència, organitzats per edat i nivell, amb un recorregut que va de la <a href="/dansa-infantil/">iniciació a la dansa</a> fins a les puntes i els exàmens oficials. I la manera de saber si el teu fill o filla està a punt no és cap test: és <strong>venir a provar una classe</strong>. La primera és gratuïta, precisament per això — perquè la resposta a «quina és la bona edat?» la dona el nen quan surt de la sala amb un somriure. Mira la <a href="/horaris/">graella d'horaris</a> i busca el seu grup: segur que n'hi ha un que li va com anell al dit.</p>
""",
        "faqs": [
            ("quina és la millor edat per començar dansa?",
             "No n'hi ha una de sola: als 3-4 anys es comença jugant amb la iniciació a la dansa, dels 5 als 7 arriba la primera tècnica, dels 8 als 12 és l'edat ideal per triar estil, i els adolescents que comencen de zero aprenen rapidíssim. La millor edat és quan el nen en té ganes."),
            ("el meu fill és molt mogut (o molt tímid): la dansa li anirà bé?",
             "En tots dos casos, sí. Als nens moguts la dansa els dona una estructura on canalitzar l'energia; als tímids, un llenguatge per expressar-se sense paraules i un grup estable on guanyar confiança. Ho veiem cada curs."),
            ("què necessita per a la primera classe de prova?",
             "Roba còmoda que li permeti moure's i mitjons o sabatilles. Res més: la primera classe és gratuïta i sense compromís, i si després s'hi apunta ja us orientem sobre el vestuari de cada disciplina."),
        ],

        "title_es": "¿a qué edad puede empezar mi hijo a hacer danza? · escola de dansa cristina colomé",
        "desc_es": "La pregunta que más nos hacen las familias: ¿a qué edad se puede empezar danza? Guía por franjas de edad (de los 3 años a la adolescencia), señales de que tu hijo está a punto y cómo es la primera clase.",
        "h1_es": "¿a qué edad puede empezar mi hijo a hacer danza?",
        "intro_es": "Es la pregunta que más escuchamos en recepción. La respuesta corta: antes de lo que crees. La larga — con franjas de edad, señales y consejos de más de 25 años de escuela — la tienes aquí.",
        "excerpt_es": "De los 3 años a la adolescencia: la guía por franjas de edad que respondemos cada septiembre en recepción, con las señales de que tu hijo está a punto.",
        "cos_es": """
<p>Cada septiembre pasa lo mismo: una madre o un padre entra por la puerta de Craywinckel con una criatura de la mano y nos pregunta, algo inseguro, si «todavía es demasiado pequeño» o si «ya llega tarde». Después de más de 25 años dando clases a niños y niñas de Sant Gervasi, la respuesta casi siempre es la misma: <strong>ni una cosa ni la otra</strong>. Cada edad tiene su puerta de entrada a la danza — solo hay que saber cuál es.</p>

<h2>a los 3-4 años: la danza es un juego</h2>
<p>A esta edad no hablamos de técnica, hablamos de <strong>psicomotricidad, música e imaginación</strong>. En las clases de iniciación a la danza, los más pequeños aprenden a escuchar el ritmo, a controlar el cuerpo, a esperar su turno y a compartir espacio con otros niños. Todo se hace jugando: somos mariposas, somos gigantes, somos gotas de lluvia. Sin darse cuenta, están construyendo la base de todo lo que vendrá: equilibrio, coordinación, lateralidad y — quizá lo más importante — <strong>la asociación de bailar con pasarlo bien</strong>.</p>

<h2>de los 5 a los 7: la primera técnica (sin prisas)</h2>
<p>Aquí el juego empieza a tener estructura. Aparecen las primeras posiciones, las primeras coreografías cortas, la memoria del movimiento. Es una edad fantástica para empezar <a href="/es/ballet-clasico/">ballet clásico</a>, porque el cuerpo es flexible, la cabeza es una esponja y todavía no hay vergüenza. Pero cuidado: la clave en esta franja es que la técnica llegue <strong>sin quitar la ilusión</strong>. Un niño de 6 años que sale de clase contento volverá toda la vida; uno que se aburre con ejercicios demasiado rígidos, no.</p>

<h2>de los 8 a los 12: la edad de oro para elegir estilo</h2>
<p>Entre los 8 y los 12 años los niños ya tienen suficiente control corporal para aprender de verdad, y suficiente personalidad para saber qué les gusta. Es el momento de <strong>probar estilos</strong>: hay quien se enamora de la disciplina del clásico, quien vibra con la energía del <a href="/es/hip-hop/">hip-hop</a> o del jazz, y quien descubre que lo que le gusta es actuar, cantar y bailar a la vez. Si empieza de cero a esta edad, ningún problema: los grupos están pensados por edad <strong>y</strong> por nivel, así que nunca se sentirá fuera de lugar.</p>

<h2>adolescentes: no, no llegan tarde</h2>
<p>Lo decimos bien claro porque es la duda que más frena: <strong>un adolescente que empieza de cero no llega tarde</strong>. Llega tarde quien quiere ser primera bailarina de una compañía profesional — y ese no es el caso del 99% de las familias que nos lo preguntan. Para todo lo demás (bailar bien, hacer ejercicio, ganar confianza, tener un grupo, subir a un escenario), los 13, 14 o 15 años son una edad magnífica. De hecho, los adolescentes aprenden rapidísimo: en un curso hacen el camino que un niño pequeño hace en tres.</p>

<h2>las señales de que está a punto</h2>
<p>Más que la edad, fíjate en esto:</p>
<ul>
<li><strong>Baila en casa.</strong> Cuando suena música y el cuerpo se va solo, el mensaje es claro.</li>
<li><strong>Aguanta una actividad dirigida.</strong> Si ya sigue una clase (o el ritmo de la guardería) sin frustrarse, puede seguir una clase de danza.</li>
<li><strong>Tiene ganas.</strong> El mejor predictor de todos. La danza propuesta funciona; la danza impuesta, no.</li>
</ul>

<h2>cómo lo hacemos en la escuela</h2>
<p>En la escuela tenemos grupos desde los 3 años hasta la adolescencia, organizados por edad y nivel, con un recorrido que va de la <a href="/es/danza-infantil/">iniciación a la danza</a> hasta las puntas y los exámenes oficiales. Y la manera de saber si tu hijo o hija está a punto no es ningún test: es <strong>venir a probar una clase</strong>. La primera es gratuita, precisamente por eso — porque la respuesta a «¿cuál es la buena edad?» la da el niño cuando sale de la sala con una sonrisa. Mira la <a href="/es/horarios/">parrilla de horarios</a> y busca su grupo: seguro que hay uno que le va como anillo al dedo.</p>
""",
        "faqs_es": [
            ("¿cuál es la mejor edad para empezar danza?",
             "No hay una sola: a los 3-4 años se empieza jugando con la iniciación a la danza, de los 5 a los 7 llega la primera técnica, de los 8 a los 12 es la edad ideal para elegir estilo, y los adolescentes que empiezan de cero aprenden rapidísimo. La mejor edad es cuando el niño tiene ganas."),
            ("mi hijo es muy movido (o muy tímido): ¿le irá bien la danza?",
             "En ambos casos, sí. A los niños movidos la danza les da una estructura donde canalizar la energía; a los tímidos, un lenguaje para expresarse sin palabras y un grupo estable donde ganar confianza. Lo vemos cada curso."),
            ("¿qué necesita para la primera clase de prueba?",
             "Ropa cómoda que le permita moverse y calcetines o zapatillas. Nada más: la primera clase es gratuita y sin compromiso, y si después se apunta ya os orientamos sobre el vestuario de cada disciplina."),
        ],
    },
    {
        "slug": "comencar-dansa-adults",
        "slug_es": "empezar-danza-adultos",
        "categoria": "adults",
        "categoria_es": "adultos",
        "data": "2026-09-01",
        "data_ca": "1 de setembre de 2026",
        "data_es": "1 de septiembre de 2026",
        "minuts": 5,
        "nom_wa": "dansa per a adults",
        "nom_wa_es": "danza para adultos",
        "og": "blog-dansa-adults.jpg",
        "img": "blog-dansa-adults.jpg",
        "img_alt": "Mans d'adults sobre la barra de fusta d'una sala de dansa amb llum càlida de tarda",
        "img_alt_es": "Manos de adultos sobre la barra de madera de una sala de danza con luz cálida de tarde",
        "related_pagines": ["dansa-adults", "cos-benestar", "dansa-oriental", "preus"],
        "related_posts": ["a-quina-edat-comencar-dansa"],

        "title": "mai no és tard: començar a ballar d'adult (de zero) · escola de dansa cristina colomé",
        "desc": "Vols ballar però creus que ja no tens edat? Mentida. Guia per començar dansa d'adult i de zero: què frena de veritat, què hi guanyaràs, quins estils són ideals per començar i com és la primera classe.",
        "h1": "mai no és tard: començar a ballar d'adult",
        "intro": "«M'encantaria, però a la meva edat...» — la frase que més sentim, i la més equivocada. Si tens ganes de ballar, això és tot el que necessites. La resta t'ho expliquem aquí.",
        "excerpt": "«M'encantaria, però a la meva edat...» és la frase més equivocada que sentim. Què frena de veritat, què hi guanyaràs i per quin estil començar de zero.",
        "cos": """
<p>Hi ha una cosa que passa cada any a les classes d'adults de l'escola, sense excepció: algú que «sempre havia volgut ballar» finalment s'hi atreveix, i al cap de tres setmanes ens diu la mateixa frase — <strong>«per què no ho he fet abans?»</strong>. Tenim alumnes que han començat de zero als 30, als 45 i més enllà dels 60. Cap ni un no se n'ha penedit. Aquest article és per a tu, que fa anys que ho rumies.</p>

<h2>la vergonya: l'únic mur de veritat</h2>
<p>No és el cos, no és l'edat, no és la flexibilitat: el que frena els adults és <strong>la por de fer el ridícul</strong>. I aquí va el secret que descobreix tothom el primer dia: a la classe d'adults iniciació ningú no en sap. Aquesta és exactament la gràcia. Tots els companys de sala han passat pel mateix moment de «no sé on posar els peus», i per això l'ambient és el contrari d'un tribunal: és un grup de gent gran que ha decidit passar-s'ho bé. Els primers deu minuts fan una mica de vertigen; a partir del minut onze, només queda la música.</p>

<h2>què hi guanyaràs (i no és només exercici)</h2>
<ul>
<li><strong>Un cos més fort i més àgil.</strong> La dansa treballa força, equilibri, mobilitat i postura alhora — poques activitats són tan completes.</li>
<li><strong>Un cap més lliure.</strong> Una hora de coreografia és una hora sense mòbil, sense feina i sense llista de pendents: la concentració que demana ballar no deixa lloc a res més.</li>
<li><strong>Memòria i coordinació.</strong> Aprendre seqüències de moviment és gimnàstica pura per al cervell, a qualsevol edat.</li>
<li><strong>Un grup.</strong> Els grups d'adults de l'escola fan pinya: gent que es troba cada setmana, any rere any, per una estona que és seva.</li>
</ul>

<h2>per on començar si parteixes de zero</h2>
<p>No hi ha un únic camí bo — hi ha el que et faci més ganes:</p>
<ul>
<li><strong>Ballet clàssic iniciació</strong>: si busques tècnica, elegància i postura. Tenim grups d'adults pensats per començar de zero, sense haver trepitjat mai una barra.</li>
<li><strong>Contemporani</strong>: si el que vols és moure't lliure i expressar-te, amb un treball físic complet.</li>
<li><strong><a href="/dansa-oriental/">Dansa oriental</a></strong>: suau amb les articulacions, potent amb el centre del cos, i molt agraïda des del primer dia.</li>
<li><strong>Fit dance, ioga i barre</strong>: si prefereixes entrar per la porta del <a href="/cos-benestar/">benestar i l'exercici</a> i que el ball vingui sol. Els matins de barre (dilluns i dimecres a les 11 h) són perfectes si tens els vespres ocupats.</li>
</ul>
<p>Tots els grups d'adults, amb nivells i horaris, són a la pàgina de <a href="/dansa-adults/">dansa per a adults</a>.</p>

<h2>com és la primera classe</h2>
<p>Arribes, et presentem el grup, i fas la classe sencera al teu ritme — la professora t'anirà donant alternatives més senzilles de cada exercici. Ningú no espera que segueixis tot: espera que t'ho passis bé. Necessites roba còmoda i prou. I el més important: <strong>la primera classe és gratuïta</strong>, precisament perquè la decisió la prenguis havent-ho provat, no imaginant-t'ho des del sofà.</p>

<h2>el truc final</h2>
<p>Vine acompanyat si et fa mandra venir sol — mitja escola d'adults va començar «perquè una amiga m'hi va arrossegar». Però si no tens qui t'acompanyi, vine igualment: l'acompanyament el trobaràs dins la sala. Les <a href="/preus/">quotes d'adults comencen als 60 €/mes</a>, i el primer pas no costa res. Literalment.</p>
""",
        "faqs": [
            ("necessito flexibilitat o forma física per començar?",
             "No. La flexibilitat i la forma física són el resultat de ballar, no el requisit. Les classes d'iniciació parteixen de zero i cada exercici té versions per a tots els nivells."),
            ("tinc més de 40/50/60 anys: puc començar igualment?",
             "Sí, i no seràs l'excepció: els grups d'adults de l'escola tenen alumnes de totes les dècades, molts dels quals van començar de zero. L'única condició real són les ganes."),
            ("he de comprar roba o sabatilles especials?",
             "Per a la classe de prova, roba còmoda i prou. Si després t'hi apuntes, t'orientem sobre què cal per a cada disciplina — i en la majoria d'estils és mínim."),
        ],

        "title_es": "nunca es tarde: empezar a bailar de adulto (desde cero) · escola de dansa cristina colomé",
        "desc_es": "¿Quieres bailar pero crees que ya no tienes edad? Mentira. Guía para empezar danza de adulto y desde cero: qué frena de verdad, qué ganarás, qué estilos son ideales para empezar y cómo es la primera clase.",
        "h1_es": "nunca es tarde: empezar a bailar de adulto",
        "intro_es": "«Me encantaría, pero a mi edad...» — la frase que más oímos, y la más equivocada. Si tienes ganas de bailar, eso es todo lo que necesitas. El resto te lo contamos aquí.",
        "excerpt_es": "«Me encantaría, pero a mi edad...» es la frase más equivocada que oímos. Qué frena de verdad, qué ganarás y por qué estilo empezar desde cero.",
        "cos_es": """
<p>Hay algo que pasa cada año en las clases de adultos de la escuela, sin excepción: alguien que «siempre había querido bailar» por fin se atreve, y a las tres semanas nos dice la misma frase — <strong>«¿por qué no lo he hecho antes?»</strong>. Tenemos alumnos que han empezado de cero a los 30, a los 45 y más allá de los 60. Ni uno solo se ha arrepentido. Este artículo es para ti, que llevas años dándole vueltas.</p>

<h2>la vergüenza: el único muro de verdad</h2>
<p>No es el cuerpo, no es la edad, no es la flexibilidad: lo que frena a los adultos es <strong>el miedo a hacer el ridículo</strong>. Y aquí va el secreto que descubre todo el mundo el primer día: en la clase de adultos iniciación nadie sabe. Esa es exactamente la gracia. Todos los compañeros de sala han pasado por el mismo momento de «no sé dónde poner los pies», y por eso el ambiente es lo contrario de un tribunal: es un grupo de gente adulta que ha decidido pasarlo bien. Los primeros diez minutos dan algo de vértigo; a partir del minuto once, solo queda la música.</p>

<h2>qué ganarás (y no es solo ejercicio)</h2>
<ul>
<li><strong>Un cuerpo más fuerte y más ágil.</strong> La danza trabaja fuerza, equilibrio, movilidad y postura a la vez — pocas actividades son tan completas.</li>
<li><strong>Una cabeza más libre.</strong> Una hora de coreografía es una hora sin móvil, sin trabajo y sin lista de pendientes: la concentración que pide bailar no deja sitio a nada más.</li>
<li><strong>Memoria y coordinación.</strong> Aprender secuencias de movimiento es gimnasia pura para el cerebro, a cualquier edad.</li>
<li><strong>Un grupo.</strong> Los grupos de adultos de la escuela hacen piña: gente que se encuentra cada semana, año tras año, para un rato que es suyo.</li>
</ul>

<h2>por dónde empezar si partes de cero</h2>
<p>No hay un único camino bueno — está el que te apetezca más:</p>
<ul>
<li><strong>Ballet clásico iniciación</strong>: si buscas técnica, elegancia y postura. Tenemos grupos de adultos pensados para empezar de cero, sin haber pisado nunca una barra.</li>
<li><strong>Contemporáneo</strong>: si lo que quieres es moverte libre y expresarte, con un trabajo físico completo.</li>
<li><strong><a href="/es/danza-oriental/">Danza oriental</a></strong>: suave con las articulaciones, potente con el centro del cuerpo, y muy agradecida desde el primer día.</li>
<li><strong>Fit dance, yoga y barre</strong>: si prefieres entrar por la puerta del <a href="/es/cuerpo-bienestar/">bienestar y el ejercicio</a> y que el baile venga solo. Las mañanas de barre (lunes y miércoles a las 11 h) son perfectas si tienes las tardes ocupadas.</li>
</ul>
<p>Todos los grupos de adultos, con niveles y horarios, están en la página de <a href="/es/danza-adultos/">danza para adultos</a>.</p>

<h2>cómo es la primera clase</h2>
<p>Llegas, te presentamos el grupo, y haces la clase entera a tu ritmo — la profesora te irá dando alternativas más sencillas de cada ejercicio. Nadie espera que sigas todo: espera que lo pases bien. Necesitas ropa cómoda y ya está. Y lo más importante: <strong>la primera clase es gratuita</strong>, precisamente para que la decisión la tomes habiéndolo probado, no imaginándolo desde el sofá.</p>

<h2>el truco final</h2>
<p>Ven acompañado si te da pereza venir solo — media escuela de adultos empezó «porque una amiga me arrastró». Pero si no tienes quien te acompañe, ven igualmente: la compañía la encontrarás dentro de la sala. Las <a href="/es/precios/">cuotas de adultos empiezan en 60 €/mes</a>, y el primer paso no cuesta nada. Literalmente.</p>
""",
        "faqs_es": [
            ("¿necesito flexibilidad o forma física para empezar?",
             "No. La flexibilidad y la forma física son el resultado de bailar, no el requisito. Las clases de iniciación parten de cero y cada ejercicio tiene versiones para todos los niveles."),
            ("tengo más de 40/50/60 años: ¿puedo empezar igualmente?",
             "Sí, y no serás la excepción: los grupos de adultos de la escuela tienen alumnos de todas las décadas, muchos de los cuales empezaron de cero. La única condición real son las ganas."),
            ("¿tengo que comprar ropa o zapatillas especiales?",
             "Para la clase de prueba, ropa cómoda y ya está. Si después te apuntas, te orientamos sobre qué hace falta para cada disciplina — y en la mayoría de estilos es mínimo."),
        ],
    },
]
