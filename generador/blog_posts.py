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
        "data": "2026-07-01",
        "data_ca": "1 de juliol de 2026",
        "data_es": "1 de julio de 2026",
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
        "data": "2026-07-08",
        "data_ca": "8 de juliol de 2026",
        "data_es": "8 de julio de 2026",
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
    {
        "slug": "triar-estil-dansa-fill",
        "slug_es": "elegir-estilo-danza-hijo",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-07-15",
        "data_ca": "15 de juliol de 2026",
        "data_es": "15 de julio de 2026",
        "minuts": 5,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-triar-estil.jpg",
        "img": "blog-triar-estil.jpg",
        "img_alt": "Tres parells de sabatilles de dansa en fila a terra d'una sala: ballet, jazz i vambes urbanes",
        "img_alt_es": "Tres pares de zapatillas de danza en fila en el suelo de una sala: ballet, jazz y deportivas urbanas",
        "related_pagines": ["ballet-classic", "jazz", "hip-hop", "musical-interpretacio"],
        "related_posts": ["a-quina-edat-comencar-dansa", "primer-dia-classe-dansa"],

        "title": "ballet, jazz o hip-hop? com triar l'estil de dansa del teu fill · escola de dansa cristina colomé",
        "desc": "Guia pràctica per triar l'estil de dansa d'un nen o nena segons el seu caràcter: ballet clàssic, jazz, hip-hop, contemporani o musical. I el mètode que mai falla: la classe de prova.",
        "h1": "ballet, jazz o hip-hop? com triar l'estil del teu fill",
        "intro": "No hi ha estils bons i dolents: hi ha estils que encaixen amb cada criatura. Una guia ràpida pel caràcter del teu fill — i el mètode infal·lible per encertar-la.",
        "excerpt": "No hi ha estils bons i dolents: hi ha estils que encaixen amb cada criatura. Guia ràpida pel caràcter del teu fill i el mètode infal·lible per encertar-la.",
        "cos": """
<p>«I quin li anirà millor?» és la segona pregunta que més sentim, just després de la de l'edat. La resposta honesta: depèn menys de l'estil i més del nen. A l'escola fem una dotzena de disciplines i n'hem vist de tots colors: la tímida que va florir amb el hip-hop, el mogut que va trobar la calma al clàssic. Però sí que hi ha pistes que ajuden a encertar el primer tret.</p>

<h2>si li agrada l'ordre, la precisió i els reptes: clàssic</h2>
<p>El <a href="/ballet-classic/">ballet clàssic</a> és l'estil de la tècnica i el detall: cada posició té nom, cada exercici té una manera correcta de fer-se. Als nens que gaudeixen fent les coses ben fetes — els que acaben el puzle, els que repeteixen fins que surt — el clàssic els dona una escala per pujar tota la vida: de la iniciació fins a les puntes i els exàmens oficials.</p>

<h2>si vessa energia i li agrada la música que sona a la ràdio: jazz o hip-hop</h2>
<p>El <a href="/jazz/">jazz</a> és energia coreografiada: ritme, salts i cançons que reconeixen. El <a href="/hip-hop/">hip-hop</a> hi afegeix l'actitud del carrer i una cultura que els encanta a partir dels 8-10 anys. Tots dos són la porta d'entrada perfecta per a nens que «no pararien mai de moure's» — aquí aquesta energia no és un problema: és la matèria primera.</p>

<h2>si és expressiu, sensible o teatral: contemporani o musical</h2>
<p>Hi ha nens que quan ballen expliquen coses. Per a ells, el contemporani (moviment lliure, emocions, creació) o el <a href="/musical-interpretacio/">musical i interpretació</a> — on es balla, es canta i s'actua — són un regal: no només aprenen passos, aprenen a dir coses amb el cos.</p>

<h2>si no es decideix: formació escènica, el menú degustació</h2>
<p>Els divendres tenim un pack que és exactament això: jazz, hip-hop, claqué, cant i interpretació en una mateixa tarda. Per als indecisos (o els que ho volen tot), és la manera de tastar-ho abans de triar.</p>

<h2>el mètode que no falla mai</h2>
<p>Tot l'anterior són orientacions; la decisió de veritat es pren a la sala. El nostre consell de sempre: <strong>tria dues opcions i prova-les</strong>. La primera classe de cada estil és gratuïta, així que el «test» no costa res. I una última cosa, potser la més important: <strong>que triï ell o ella</strong>. L'estil que un nen tria és l'estil al qual torna cada setmana amb ganes — i les ganes són el 90% de tot.</p>
""",
        "faqs": [
            ("pot fer més d'un estil alhora?",
             "Sí, i és molt habitual: moltes alumnes combinen clàssic amb jazz o contemporani, i les quotes per 2, 3 o 4 dies per setmana estan pensades exactament per a això."),
            ("i si comença un estil i després vol canviar?",
             "Cap problema — passa sovint i és sa. La base que s'emporta d'un estil serveix per al següent, i canviar de grup és tan fàcil com dir-nos-ho."),
            ("el ballet és només per a nenes? i el hip-hop per a nens?",
             "No i no. Tenim nens a clàssic i nenes a hip-hop, i tant de bo cada cop més: els estils no tenen gènere, tenen música."),
        ],

        "title_es": "¿ballet, jazz o hip-hop? cómo elegir el estilo de danza de tu hijo · escola de dansa cristina colomé",
        "desc_es": "Guía práctica para elegir el estilo de danza de un niño o niña según su carácter: ballet clásico, jazz, hip-hop, contemporáneo o musical. Y el método que nunca falla: la clase de prueba.",
        "h1_es": "¿ballet, jazz o hip-hop? cómo elegir el estilo de tu hijo",
        "intro_es": "No hay estilos buenos y malos: hay estilos que encajan con cada criatura. Una guía rápida según el carácter de tu hijo — y el método infalible para acertar.",
        "excerpt_es": "No hay estilos buenos y malos: hay estilos que encajan con cada criatura. Guía rápida según el carácter de tu hijo y el método infalible para acertar.",
        "cos_es": """
<p>«¿Y cuál le irá mejor?» es la segunda pregunta que más oímos, justo después de la de la edad. La respuesta honesta: depende menos del estilo y más del niño. En la escuela hacemos una docena de disciplinas y hemos visto de todo: la tímida que floreció con el hip-hop, el movido que encontró la calma en el clásico. Pero sí hay pistas que ayudan a acertar el primer tiro.</p>

<h2>si le gusta el orden, la precisión y los retos: clásico</h2>
<p>El <a href="/es/ballet-clasico/">ballet clásico</a> es el estilo de la técnica y el detalle: cada posición tiene nombre, cada ejercicio tiene una manera correcta de hacerse. A los niños que disfrutan haciendo las cosas bien hechas — los que terminan el puzle, los que repiten hasta que sale — el clásico les da una escalera para subir toda la vida: de la iniciación hasta las puntas y los exámenes oficiales.</p>

<h2>si desborda energía y le gusta la música de la radio: jazz o hip-hop</h2>
<p>El <a href="/es/jazz/">jazz</a> es energía coreografiada: ritmo, saltos y canciones que reconocen. El <a href="/es/hip-hop/">hip-hop</a> añade la actitud de la calle y una cultura que les encanta a partir de los 8-10 años. Ambos son la puerta de entrada perfecta para niños que «no pararían nunca de moverse» — aquí esa energía no es un problema: es la materia prima.</p>

<h2>si es expresivo, sensible o teatral: contemporáneo o musical</h2>
<p>Hay niños que cuando bailan cuentan cosas. Para ellos, el contemporáneo (movimiento libre, emociones, creación) o el <a href="/es/musical-interpretacion/">musical e interpretación</a> — donde se baila, se canta y se actúa — son un regalo: no solo aprenden pasos, aprenden a decir cosas con el cuerpo.</p>

<h2>si no se decide: formación escénica, el menú degustación</h2>
<p>Los viernes tenemos un pack que es exactamente eso: jazz, hip-hop, claqué, canto e interpretación en una misma tarde. Para los indecisos (o los que lo quieren todo), es la manera de probarlo antes de elegir.</p>

<h2>el método que no falla nunca</h2>
<p>Todo lo anterior son orientaciones; la decisión de verdad se toma en la sala. Nuestro consejo de siempre: <strong>elige dos opciones y pruébalas</strong>. La primera clase de cada estilo es gratuita, así que el «test» no cuesta nada. Y una última cosa, quizá la más importante: <strong>que elija él o ella</strong>. El estilo que un niño elige es el estilo al que vuelve cada semana con ganas — y las ganas son el 90% de todo.</p>
""",
        "faqs_es": [
            ("¿puede hacer más de un estilo a la vez?",
             "Sí, y es muy habitual: muchas alumnas combinan clásico con jazz o contemporáneo, y las cuotas por 2, 3 o 4 días por semana están pensadas exactamente para eso."),
            ("¿y si empieza un estilo y luego quiere cambiar?",
             "Ningún problema — pasa a menudo y es sano. La base que se lleva de un estilo sirve para el siguiente, y cambiar de grupo es tan fácil como decírnoslo."),
            ("¿el ballet es solo para niñas? ¿y el hip-hop para niños?",
             "No y no. Tenemos niños en clásico y niñas en hip-hop, y ojalá cada vez más: los estilos no tienen género, tienen música."),
        ],
    },
    {
        "slug": "primer-dia-classe-dansa",
        "slug_es": "primer-dia-clase-danza",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-07-22",
        "data_ca": "22 de juliol de 2026",
        "data_es": "22 de julio de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-primer-dia.jpg",
        "img": "blog-primer-dia.jpg",
        "img_alt": "Una bossa de dansa oberta sobre un banc de fusta amb sabatilles, roba i una ampolla d'aigua",
        "img_alt_es": "Una bolsa de danza abierta sobre un banco de madera con zapatillas, ropa y una botella de agua",
        "related_pagines": ["dansa-infantil", "horaris", "preus"],
        "related_posts": ["a-quina-edat-comencar-dansa", "classe-de-prova-gratuita"],

        "title": "què cal portar el primer dia de classe de dansa · escola de dansa cristina colomé",
        "desc": "La llista del primer dia de classe de dansa: què posar a la bossa, què no cal comprar encara, com anar pentinades i els consells que donem a totes les famílies noves de l'escola.",
        "h1": "què cal portar el primer dia de classe de dansa",
        "intro": "La bona notícia: molt menys del que et penses. La llista completa de la bossa del primer dia — i, sobretot, el que NO has de comprar encara.",
        "excerpt": "Molt menys del que et penses: la llista completa de la bossa del primer dia — i, sobretot, el que NO has de comprar encara.",
        "cos": """
<p>Cada setembre veiem arribar famílies amb la bossa a vessar: maillot nou, mitges noves, sabatilles de mitja punta, faldilleta, malla d'hivern per si de cas... i la meitat, sense estrenar, acaba al fons de l'armari. Aquest article és per estalviar-te aquest viatge. La regla d'or del primer dia és senzilla: <strong>primer prova, després compra</strong>.</p>

<h2>la llista del primer dia (de veritat)</h2>
<ul>
<li><strong>Roba còmoda i ajustadeta.</strong> Uns leggings o malles i una samarreta que no balli gaire: la professora ha de poder veure com es col·loca el cos. No cal que sigui «roba de dansa».</li>
<li><strong>Mitjons o sabatilles que ja tingui.</strong> Per a la primera classe, amb mitjons antilliscants o unes vambes netes n'hi ha prou, segons l'estil.</li>
<li><strong>Una ampolla d'aigua petita.</strong> Ballar dona set, i les pauses per beure formen part de la classe.</li>
<li><strong>Cabells recollits</strong> si els porta llargs: una cua o trena ben feta. El monyo de ballarina ja arribarà — el primer dia, que no li estiri!</li>
</ul>

<h2>el que no has de comprar (encara)</h2>
<p>Ni maillot, ni mitges de ballet, ni sabatilles de disciplina, ni faldilles. Per dos motius: primer, perquè fins que no sapiguem l'estil i el grup definitius no sabreu què cal exactament; i segon, perquè cada disciplina té el seu material i és una pena duplicar. Quan l'alumna es quedi, <strong>us donarem la llista exacta del seu grup</strong> — i us direm on comprar-ho sense pagar de més.</p>

<h2>els nervis també venen a la primera classe</h2>
<p>És normal que el primer dia hi hagi una mica de vertigen — seu, i potser teu i tot. Us ho posem fàcil: arribeu 10 minuts abans, la professora els rep pel seu nom, i tu pots esperar a fora tranquil·lament. La immensa majoria de «no vull entrar-hi» es converteixen en «quan hi tornem?» abans que s'acabi la música. I si un dia no surt bé, no passa res: es torna a provar un altre dia, sense pressió.</p>

<h2>on i quan</h2>
<p>Som al carrer Craywinckel, 25 (Sant Gervasi, a dos minuts de l'FGC Av. Tibidabo). Mira la <a href="/horaris/">graella d'horaris</a> per trobar el grup que toca per edat, i recorda que la <a href="/preus/">primera classe és gratuïta</a>: el primer dia, l'única cosa imprescindible a la bossa són les ganes.</p>
""",
        "faqs": [
            ("cal comprar roba de dansa per a la classe de prova?",
             "No: roba còmoda i ajustada, mitjons o vambes netes i una ampolla d'aigua. La llista de material de veritat us la donem quan l'alumna ja té grup definitiu."),
            ("els pares podem quedar-nos a mirar la classe?",
             "Els primers minuts del primer dia, si el nen ho necessita, sí. Després els alumnes treballen millor sols — i us ho expliquen tot sortint, que és encara més bonic."),
            ("què passa si arriba tard o es perd un dia?",
             "No passa res: ens avises i llestos. I si un dia no pot venir al seu horari, mirem si pot recuperar la classe amb un altre grup del seu nivell."),
        ],

        "title_es": "qué llevar el primer día de clase de danza · escola de dansa cristina colomé",
        "desc_es": "La lista del primer día de clase de danza: qué poner en la bolsa, qué no hace falta comprar todavía, cómo ir peinadas y los consejos que damos a todas las familias nuevas de la escuela.",
        "h1_es": "qué llevar el primer día de clase de danza",
        "intro_es": "La buena noticia: mucho menos de lo que crees. La lista completa de la bolsa del primer día — y, sobre todo, lo que NO tienes que comprar todavía.",
        "excerpt_es": "Mucho menos de lo que crees: la lista completa de la bolsa del primer día — y, sobre todo, lo que NO tienes que comprar todavía.",
        "cos_es": """
<p>Cada septiembre vemos llegar familias con la bolsa a rebosar: maillot nuevo, medias nuevas, zapatillas de media punta, faldita, malla de invierno por si acaso... y la mitad, sin estrenar, acaba en el fondo del armario. Este artículo es para ahorrarte ese viaje. La regla de oro del primer día es sencilla: <strong>primero prueba, después compra</strong>.</p>

<h2>la lista del primer día (de verdad)</h2>
<ul>
<li><strong>Ropa cómoda y ajustadita.</strong> Unos leggings o mallas y una camiseta que no baile mucho: la profesora tiene que poder ver cómo se coloca el cuerpo. No hace falta que sea «ropa de danza».</li>
<li><strong>Calcetines o zapatillas que ya tenga.</strong> Para la primera clase, con calcetines antideslizantes o unas deportivas limpias es suficiente, según el estilo.</li>
<li><strong>Una botella de agua pequeña.</strong> Bailar da sed, y las pausas para beber forman parte de la clase.</li>
<li><strong>Pelo recogido</strong> si lo lleva largo: una coleta o trenza bien hecha. El moño de bailarina ya llegará — ¡el primer día, que no le tire!</li>
</ul>

<h2>lo que no tienes que comprar (todavía)</h2>
<p>Ni maillot, ni medias de ballet, ni zapatillas de disciplina, ni faldas. Por dos motivos: primero, porque hasta que no sepamos el estilo y el grupo definitivos no sabréis qué hace falta exactamente; y segundo, porque cada disciplina tiene su material y es una pena duplicar. Cuando la alumna se quede, <strong>os daremos la lista exacta de su grupo</strong> — y os diremos dónde comprarlo sin pagar de más.</p>

<h2>los nervios también vienen a la primera clase</h2>
<p>Es normal que el primer día haya algo de vértigo — suyo, y puede que tuyo también. Os lo ponemos fácil: llegad 10 minutos antes, la profesora los recibe por su nombre, y tú puedes esperar fuera tranquilamente. La inmensa mayoría de «no quiero entrar» se convierten en «¿cuándo volvemos?» antes de que termine la música. Y si un día no sale bien, no pasa nada: se vuelve a probar otro día, sin presión.</p>

<h2>dónde y cuándo</h2>
<p>Estamos en la calle Craywinckel, 25 (Sant Gervasi, a dos minutos del FGC Av. Tibidabo). Mira la <a href="/es/horarios/">parrilla de horarios</a> para encontrar el grupo que toca por edad, y recuerda que la <a href="/es/precios/">primera clase es gratuita</a>: el primer día, lo único imprescindible en la bolsa son las ganas.</p>
""",
        "faqs_es": [
            ("¿hay que comprar ropa de danza para la clase de prueba?",
             "No: ropa cómoda y ajustada, calcetines o deportivas limpias y una botella de agua. La lista de material de verdad os la damos cuando la alumna ya tiene grupo definitivo."),
            ("¿los padres podemos quedarnos a mirar la clase?",
             "Los primeros minutos del primer día, si el niño lo necesita, sí. Después los alumnos trabajan mejor solos — y os lo cuentan todo al salir, que es aún más bonito."),
            ("¿qué pasa si llega tarde o se pierde un día?",
             "No pasa nada: nos avisas y listo. Y si un día no puede venir en su horario, miramos si puede recuperar la clase con otro grupo de su nivel."),
        ],
    },
    {
        "slug": "beneficis-dansa-nens",
        "slug_es": "beneficios-danza-ninos",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-07-29",
        "data_ca": "29 de juliol de 2026",
        "data_es": "29 de julio de 2026",
        "minuts": 5,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-beneficis-nens.jpg",
        "img": "blog-beneficis-nens.jpg",
        "img_alt": "Cames d'una nena amb mitges i sabatilles de ballet posant-se de puntetes a terra d'una sala de dansa",
        "img_alt_es": "Piernas de una niña con medias y zapatillas de ballet poniéndose de puntillas en el suelo de una sala de danza",
        "related_pagines": ["dansa-infantil", "ballet-classic", "musical-interpretacio"],
        "related_posts": ["a-quina-edat-comencar-dansa", "dansa-i-timidesa"],

        "title": "els beneficis de la dansa per a nens i nenes, segons la ciència · escola de dansa cristina colomé",
        "desc": "Què diu la recerca sobre la dansa en la infància: desenvolupament motor, memòria i funcions executives, gestió emocional, confiança i vincle social. I com ho veiem cada dia a la sala.",
        "h1": "els beneficis de la dansa per a nens, segons la ciència",
        "intro": "Fa més de 25 anys que veiem què fa la dansa a les criatures. Ara la recerca hi posa noms: motricitat, memòria, emocions, confiança. T'ho expliquem sense bata blanca.",
        "excerpt": "Motricitat, memòria, gestió emocional, confiança: el que la recerca diu de la dansa en la infància — i com ho veiem cada dia a la sala.",
        "cos": """
<p>A l'escola no ens calen estudis per saber que la dansa transforma els nens: ho veiem cada tarda. Però és bonic comprovar que, quan els investigadors s'hi posen, troben exactament el que nosaltres observem des de fa dècades. Aquí va el resum — la ciència en cursiva, la sala de dansa en negreta.</p>

<h2>un cos que aprèn a fer-se seu</h2>
<p>La dansa és de les activitats més completes que existeixen per al desenvolupament motor: treballa equilibri, coordinació, lateralitat, postura i consciència corporal alhora — i ho fa amb música, que ho fa tot més fàcil. En una època de pantalles i estones assegudes, una hora de dansa és una hora de moviment de qualitat, variat i progressiu. <strong>A la sala es veu així:</strong> la nena que al setembre ensopegava amb els seus propis peus, al festival de final de curs gira, salta i aterra on toca.</p>

<h2>un cervell que balla</h2>
<p>Aprendre coreografies és un exercici cognitiu de primera: memòria de seqüències, atenció sostinguda, anticipació, adaptació als errors en temps real. Els estudis sobre dansa i desenvolupament infantil apunten a millores en la memòria de treball i les funcions executives — les mateixes que després fan servir per estudiar. <strong>A la sala es veu així:</strong> «t'has après la coreo sencera?» és, sense que ho sembli, un entrenament de concentració de vuit minuts seguits.</p>

<h2>emocions amb sortida</h2>
<p>Ballar és un llenguatge: permet expressar alegria, ràbia, por o tendresa sense necessitat de paraules. Per als nens — que sovint senten més del que saben explicar — això és una vàlvula i una eina. La dansa s'associa a menys estrès i més benestar emocional a totes les edats. <strong>A la sala es veu així:</strong> hi ha nens que entren carregats del dia d'escola i surten lleugers. Les famílies ho descriuen igual: «surt diferent».</p>

<h2>confiança que es construeix pas a pas</h2>
<p>Cada setmana hi ha un petit repte assolible: un pas nou, un gir que ahir no sortia. Aquesta acumulació de «me n'he sortit» és la matèria de què està feta l'autoestima. I un cop l'any, l'escenari: assajar, posar-se el vestuari i ballar davant del públic és una lliçó de valentia que es queda per sempre. <strong>A la sala es veu així:</strong> les cares en acabar el festival ho diuen tot.</p>

<h2>un grup on pertànyer</h2>
<p>La dansa d'escola és una activitat d'equip encoberta: es balla junts, es compta amb l'altra, es celebra en grup. Els companys de dansa sovint es converteixen en la colla de tota la infància — a l'escola tenim amistats que han crescut de la <a href="/dansa-infantil/">iniciació</a> fins als grups juvenils. I això, que no surt a cap estudi, potser és el benefici més gran de tots.</p>
""",
        "faqs": [
            ("la dansa és prou exercici físic per a un nen?",
             "Sí: una classe de dansa treballa resistència, força, flexibilitat i coordinació — i compta com l'activitat física regular que recomanen els pediatres, amb l'avantatge que als nens no els sembla «fer exercici», els sembla jugar amb música."),
            ("la dansa pot ajudar un nen amb poca confiança?",
             "És un dels casos on més es nota: els reptes petits i assolibles de cada setmana, el grup estable i l'experiència de l'escenari construeixen seguretat de manera natural. En parlem més a fons a l'article sobre dansa i timidesa."),
            ("i si només ve a passar-s'ho bé, sense cap objectiu?",
             "Perfecte — aquest és exactament el pla. Tots els beneficis d'aquest article arriben sols, de propina, mentre es diverteixen. La dansa no cal que porti enlloc: ja és el lloc."),
        ],

        "title_es": "los beneficios de la danza para niños y niñas, según la ciencia · escola de dansa cristina colomé",
        "desc_es": "Qué dice la investigación sobre la danza en la infancia: desarrollo motor, memoria y funciones ejecutivas, gestión emocional, confianza y vínculo social. Y cómo lo vemos cada día en la sala.",
        "h1_es": "los beneficios de la danza para niños, según la ciencia",
        "intro_es": "Llevamos más de 25 años viendo qué hace la danza en las criaturas. Ahora la investigación le pone nombres: motricidad, memoria, emociones, confianza. Te lo contamos sin bata blanca.",
        "excerpt_es": "Motricidad, memoria, gestión emocional, confianza: lo que la investigación dice de la danza en la infancia — y cómo lo vemos cada día en la sala.",
        "cos_es": """
<p>En la escuela no necesitamos estudios para saber que la danza transforma a los niños: lo vemos cada tarde. Pero es bonito comprobar que, cuando los investigadores se ponen, encuentran exactamente lo que nosotros observamos desde hace décadas. Aquí va el resumen — la ciencia en cursiva, la sala de danza en negrita.</p>

<h2>un cuerpo que aprende a hacerse suyo</h2>
<p>La danza es de las actividades más completas que existen para el desarrollo motor: trabaja equilibrio, coordinación, lateralidad, postura y conciencia corporal a la vez — y lo hace con música, que lo hace todo más fácil. En una época de pantallas y ratos sentados, una hora de danza es una hora de movimiento de calidad, variado y progresivo. <strong>En la sala se ve así:</strong> la niña que en septiembre tropezaba con sus propios pies, en el festival de final de curso gira, salta y aterriza donde toca.</p>

<h2>un cerebro que baila</h2>
<p>Aprender coreografías es un ejercicio cognitivo de primera: memoria de secuencias, atención sostenida, anticipación, adaptación a los errores en tiempo real. Los estudios sobre danza y desarrollo infantil apuntan a mejoras en la memoria de trabajo y las funciones ejecutivas — las mismas que luego usan para estudiar. <strong>En la sala se ve así:</strong> «¿te has aprendido la coreo entera?» es, sin que lo parezca, un entrenamiento de concentración de ocho minutos seguidos.</p>

<h2>emociones con salida</h2>
<p>Bailar es un lenguaje: permite expresar alegría, rabia, miedo o ternura sin necesidad de palabras. Para los niños — que a menudo sienten más de lo que saben explicar — eso es una válvula y una herramienta. La danza se asocia a menos estrés y más bienestar emocional a todas las edades. <strong>En la sala se ve así:</strong> hay niños que entran cargados del día de colegio y salen ligeros. Las familias lo describen igual: «sale diferente».</p>

<h2>confianza que se construye paso a paso</h2>
<p>Cada semana hay un pequeño reto alcanzable: un paso nuevo, un giro que ayer no salía. Esa acumulación de «lo he conseguido» es la materia de la que está hecha la autoestima. Y una vez al año, el escenario: ensayar, ponerse el vestuario y bailar ante el público es una lección de valentía que se queda para siempre. <strong>En la sala se ve así:</strong> las caras al terminar el festival lo dicen todo.</p>

<h2>un grupo al que pertenecer</h2>
<p>La danza de escuela es una actividad de equipo encubierta: se baila juntos, se cuenta con la otra, se celebra en grupo. Las compañeras de danza a menudo se convierten en la pandilla de toda la infancia — en la escuela tenemos amistades que han crecido de la <a href="/es/danza-infantil/">iniciación</a> hasta los grupos juveniles. Y eso, que no sale en ningún estudio, quizá es el beneficio más grande de todos.</p>
""",
        "faqs_es": [
            ("¿la danza es suficiente ejercicio físico para un niño?",
             "Sí: una clase de danza trabaja resistencia, fuerza, flexibilidad y coordinación — y cuenta como la actividad física regular que recomiendan los pediatras, con la ventaja de que a los niños no les parece «hacer ejercicio», les parece jugar con música."),
            ("¿la danza puede ayudar a un niño con poca confianza?",
             "Es uno de los casos donde más se nota: los retos pequeños y alcanzables de cada semana, el grupo estable y la experiencia del escenario construyen seguridad de manera natural. Hablamos de ello a fondo en el artículo sobre danza y timidez."),
            ("¿y si solo viene a pasarlo bien, sin ningún objetivo?",
             "Perfecto — ese es exactamente el plan. Todos los beneficios de este artículo llegan solos, de propina, mientras se divierten. La danza no hace falta que lleve a ningún sitio: ya es el sitio."),
        ],
    },
    {
        "slug": "examens-rad-ballet",
        "slug_es": "examenes-rad-ballet",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-08-05",
        "data_ca": "5 d'agost de 2026",
        "data_es": "5 de agosto de 2026",
        "minuts": 5,
        "nom_wa": "ballet clàssic",
        "nom_wa_es": "ballet clásico",
        "og": "blog-examens-rad.jpg",
        "img": "blog-examens-rad.jpg",
        "img_alt": "Puntes de ballet de setí rosa al costat d'un certificat amb llaç granat a terra d'una sala de dansa",
        "img_alt_es": "Puntas de ballet de satén rosa junto a un certificado con lazo granate en el suelo de una sala de danza",
        "related_pagines": ["ballet-classic", "dansa-infantil", "horaris"],
        "related_posts": ["triar-estil-dansa-fill", "a-quina-edat-comencar-dansa"],

        "title": "què són els exàmens RAD de ballet i com els preparem · escola de dansa cristina colomé",
        "desc": "Els exàmens de la Royal Academy of Dance (RAD) explicats per a famílies: què són, què aporten a l'alumna, com és el dia de l'examen i com preparem els grups a l'escola. Sense mites.",
        "h1": "què són els exàmens RAD i com els preparem",
        "intro": "Un títol de ballet reconegut a tot el món, explicat sense solemnitat: què són els exàmens de la Royal Academy of Dance, què hi guanya l'alumna i com ho vivim a l'escola.",
        "excerpt": "Els exàmens de la Royal Academy of Dance explicats per a famílies: què aporten, com és el gran dia i com els preparem — sense mites ni solemnitat.",
        "cos": """
<p>Quan diem a una família que la seva filla pot preparar «els RAD», la primera reacció sol ser una barreja d'orgull i pànic. Tranquils: no és una oposició, és una de les experiències més formatives que pot viure una alumna de clàssic. Us ho expliquem com ho expliquem a les mares i pares a recepció.</p>

<h2>què és la RAD</h2>
<p>La <strong>Royal Academy of Dance</strong> és una de les institucions de dansa més prestigioses del món, fundada a Londres el 1920, amb presència a desenes de països. El seu programa d'exàmens estableix nivells progressius amb un temari precís, i els avaluen <strong>examinadores oficials de la RAD</strong>. El certificat que se n'obté és el mateix a Barcelona que a Londres o a Sydney: un estàndard internacional.</p>

<h2>què hi guanya l'alumna (a banda del títol)</h2>
<ul>
<li><strong>Un objectiu amb data.</strong> Preparar un examen dona sentit al curs: cada exercici té un perquè, i l'esforç té una meta visible.</li>
<li><strong>Tècnica polida de veritat.</strong> El temari obliga a treballar cada detall fins que està madur — el salt de qualitat d'un curs d'examen es nota anys després.</li>
<li><strong>Serenitat sota pressió.</strong> Presentar-se davant d'una examinadora, sola o en grup petit, és un entrenament d'aplom que serveix per a la dansa i per a la vida.</li>
<li><strong>Un reconeixement objectiu.</strong> La nota no la posa la seva professora que se l'estima: la posa una experta externa. Aprovar té un gust especial.</li>
</ul>

<h2>com ho preparem a l'escola</h2>
<p>La preparació s'integra al curs de <a href="/ballet-classic/">ballet clàssic</a>: les alumnes dels grups d'examen treballen el temari del seu nivell dins les classes habituals, amb intensificació els mesos previs. La decisió de presentar-se es pren conjuntament — professora, alumna i família — i mai per pressió: <strong>l'examen és una oportunitat, no una obligació</strong>. Qui no s'examina segueix el curs amb tota normalitat.</p>

<h2>com és el gran dia</h2>
<p>L'examen dura uns 20-40 minuts segons el nivell: les alumnes entren en grups petits, amb l'uniforme del seu nivell i el número prendat, i executen el programa treballat. Setmanes després arriba el resultat amb el certificat i el desglossament de l'avaluació. I sí: els nervis del dia abans i l'abraçada de després formen part del ritual — com a totes les coses que valen la pena.</p>
""",
        "faqs": [
            ("l'examen RAD és obligatori per fer ballet a l'escola?",
             "No, en absolut: és una oportunitat per a qui la vol. Les alumnes que no s'examinen segueixen les classes amb tota normalitat, i la decisió es pren sempre entre professora, alumna i família."),
            ("a partir de quina edat o nivell es pot examinar?",
             "La RAD té nivells des d'infantil fins a graus avançats: la professora proposa el moment en què cada alumna té el nivell madur. No hi ha pressa — l'examen es fa quan pot ser una bona experiència."),
            ("serveix d'alguna cosa el certificat RAD?",
             "És un estàndard internacional: acredita el nivell de ballet en qualsevol país i és la base per a qui més endavant vulgui fer el camí de la dansa amb més serietat. I encara que no es vagi per aquest camí, el que queda — tècnica, disciplina, aplom — ja ha valgut la pena."),
        ],

        "title_es": "qué son los exámenes RAD de ballet y cómo los preparamos · escola de dansa cristina colomé",
        "desc_es": "Los exámenes de la Royal Academy of Dance (RAD) explicados para familias: qué son, qué aportan a la alumna, cómo es el día del examen y cómo preparamos los grupos en la escuela. Sin mitos.",
        "h1_es": "qué son los exámenes RAD y cómo los preparamos",
        "intro_es": "Un título de ballet reconocido en todo el mundo, explicado sin solemnidad: qué son los exámenes de la Royal Academy of Dance, qué gana la alumna y cómo lo vivimos en la escuela.",
        "excerpt_es": "Los exámenes de la Royal Academy of Dance explicados para familias: qué aportan, cómo es el gran día y cómo los preparamos — sin mitos ni solemnidad.",
        "cos_es": """
<p>Cuando le decimos a una familia que su hija puede preparar «los RAD», la primera reacción suele ser una mezcla de orgullo y pánico. Tranquilos: no es una oposición, es una de las experiencias más formativas que puede vivir una alumna de clásico. Os lo contamos como se lo contamos a las madres y padres en recepción.</p>

<h2>qué es la RAD</h2>
<p>La <strong>Royal Academy of Dance</strong> es una de las instituciones de danza más prestigiosas del mundo, fundada en Londres en 1920, con presencia en decenas de países. Su programa de exámenes establece niveles progresivos con un temario preciso, y los evalúan <strong>examinadoras oficiales de la RAD</strong>. El certificado que se obtiene es el mismo en Barcelona que en Londres o en Sídney: un estándar internacional.</p>

<h2>qué gana la alumna (además del título)</h2>
<ul>
<li><strong>Un objetivo con fecha.</strong> Preparar un examen da sentido al curso: cada ejercicio tiene un porqué, y el esfuerzo tiene una meta visible.</li>
<li><strong>Técnica pulida de verdad.</strong> El temario obliga a trabajar cada detalle hasta que está maduro — el salto de calidad de un curso de examen se nota años después.</li>
<li><strong>Serenidad bajo presión.</strong> Presentarse ante una examinadora, sola o en grupo pequeño, es un entrenamiento de aplomo que sirve para la danza y para la vida.</li>
<li><strong>Un reconocimiento objetivo.</strong> La nota no la pone su profesora que la quiere: la pone una experta externa. Aprobar tiene un sabor especial.</li>
</ul>

<h2>cómo lo preparamos en la escuela</h2>
<p>La preparación se integra en el curso de <a href="/es/ballet-clasico/">ballet clásico</a>: las alumnas de los grupos de examen trabajan el temario de su nivel dentro de las clases habituales, con intensificación los meses previos. La decisión de presentarse se toma conjuntamente — profesora, alumna y familia — y nunca por presión: <strong>el examen es una oportunidad, no una obligación</strong>. Quien no se examina sigue el curso con total normalidad.</p>

<h2>cómo es el gran día</h2>
<p>El examen dura unos 20-40 minutos según el nivel: las alumnas entran en grupos pequeños, con el uniforme de su nivel y el número prendido, y ejecutan el programa trabajado. Semanas después llega el resultado con el certificado y el desglose de la evaluación. Y sí: los nervios del día antes y el abrazo de después forman parte del ritual — como en todas las cosas que valen la pena.</p>
""",
        "faqs_es": [
            ("¿el examen RAD es obligatorio para hacer ballet en la escuela?",
             "No, en absoluto: es una oportunidad para quien la quiere. Las alumnas que no se examinan siguen las clases con total normalidad, y la decisión se toma siempre entre profesora, alumna y familia."),
            ("¿a partir de qué edad o nivel se puede examinar?",
             "La RAD tiene niveles desde infantil hasta grados avanzados: la profesora propone el momento en que cada alumna tiene el nivel maduro. No hay prisa — el examen se hace cuando puede ser una buena experiencia."),
            ("¿sirve de algo el certificado RAD?",
             "Es un estándar internacional: acredita el nivel de ballet en cualquier país y es la base para quien más adelante quiera tomarse el camino de la danza más en serio. Y aunque no se vaya por ese camino, lo que queda — técnica, disciplina, aplomo — ya ha valido la pena."),
        ],
    },
    {
        "slug": "dansa-i-timidesa",
        "slug_es": "danza-y-timidez",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-08-12",
        "data_ca": "12 d'agost de 2026",
        "data_es": "12 de agosto de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-timidesa-escenari.jpg",
        "img": "blog-timidesa-escenari.jpg",
        "img_alt": "Un teló de vellut granat entreobert amb un feix de llum càlida que il·lumina l'escenari de fusta",
        "img_alt_es": "Un telón de terciopelo granate entreabierto con un haz de luz cálida que ilumina el escenario de madera",
        "related_pagines": ["dansa-infantil", "musical-interpretacio", "formacio-escenica"],
        "related_posts": ["beneficis-dansa-nens", "a-quina-edat-comencar-dansa"],

        "title": "dansa i timidesa: què passa quan un nen vergonyós puja a l'escenari · escola de dansa cristina colomé",
        "desc": "Per què la dansa és una de les millors eines per a nens tímids: grup estable, llenguatge sense paraules, reptes petits i l'experiència transformadora de l'escenari. Explicat des de la sala.",
        "h1": "dansa i timidesa: quan un nen vergonyós puja a l'escenari",
        "intro": "«És que la meva filla és molt tímida...» — ens ho diuen com un dubte, i és el millor motiu per venir. El que hem après en 25 anys de veure nens vergonyosos trobar el seu lloc.",
        "excerpt": "«És que és molt tímida...» — ens ho diuen com un dubte i és el millor motiu per venir. El que passa quan un nen vergonyós troba el seu lloc a la sala.",
        "cos": """
<p>Hi ha una escena que es repeteix cada curs: una família a recepció, un nen mig amagat darrere la cama del pare, i la frase — «és que és molt tímid, no sé si això és per a ell». La nostra resposta, després de dècades veient-ho, és sempre la mateixa: la dansa no és <em>malgrat</em> la timidesa; sovint és <em>la millor resposta</em> a la timidesa. I no perquè la «curi» — la timidesa no és cap malaltia — sinó perquè li dona al nen exactament el que necessita per estar bé sent com és.</p>

<h2>un lloc on no cal parlar</h2>
<p>La majoria d'activitats socials demanen paraules, i és just on el nen tímid pateix. A la sala de dansa la conversa és una altra: la música mana, el cos respon, i ningú no espera que diguis res enginyós. Molts nens vergonyosos descobreixen ballant que <strong>tenen moltes coses a dir — només que no eren amb paraules</strong>.</p>

<h2>un grup petit, estable i previsible</h2>
<p>El que espanta la timidesa és la incertesa social: gent nova, situacions obertes. Una classe de dansa és el contrari — les mateixes companyes cada setmana, la mateixa professora, una estructura que es repeteix i es domina. Aquesta previsibilitat és un matalàs: quan l'entorn és segur, el nen tímid es desplega. A vegades triga tres setmanes; a vegades, tres mesos. Sempre arriba.</p>

<h2>la confiança no es predica: s'acumula</h2>
<p>A un nen insegur no li serveix que li diguin «tu pots!». Li serveix comprovar-ho. La dansa és una màquina de petites comprovacions: aquesta setmana el gir, l'altra el pas nou, després la coreografia sencera. Cada «m'ha sortit» és un maó. No es nota de un dia per l'altre — es nota al cap d'un curs, quan la mateixa criatura que no aixecava la mirada demana posar-se a primera fila.</p>

<h2>i llavors arriba l'escenari</h2>
<p>El festival de final de curs és el capítol que cap família tímida no es creu per endavant. Setmanes d'assaig, un vestuari, el teló, els llums — i el nen que «no parlava amb ningú» ballant davant de centenars de persones. No perquè hagi deixat de ser tímid: <strong>perquè dalt de l'escenari no hi puja sol — hi puja amb el seu grup, fent una cosa que domina</strong>. I l'ovació que ve després val per mil xerrades motivacionals. Les mares ens ho diuen amb llàgrimes als ulls cada juny, i cada juny els responem el mateix: nosaltres només hem posat la música; això ho ha fet ell.</p>

<h2>per on començar</h2>
<p>Si el teu fill o filla és dels de darrere la cama, comença suau: una <a href="/dansa-infantil/">classe del seu grup d'edat</a>, sense pressa i sense públic. La primera classe és gratuïta, i si el primer dia només mira, també val: mirar és la primera manera de participar dels tímids. La resta arriba sola — nosaltres ho hem vist centenars de vegades.</p>
""",
        "faqs": [
            ("i si arriba el dia del festival i no vol sortir a l'escenari?",
             "No passa gairebé mai — el grup i la coreografia dominada fan de xarxa — però si passa, no es força: pot mirar des de dins amb les companyes. Sovint qui no volia sortir al desembre és qui més gaudeix al juny."),
            ("millor una activitat individual o de grup per a un nen tímid?",
             "El grup petit i estable de la dansa dona el millor dels dos mons: treball personal dins d'un col·lectiu segur, sense l'exposició d'un esport de competició ni la solitud d'una activitat individual."),
            ("quant triga a «obrir-se» un nen tímid a dansa?",
             "Cada nen té el seu ritme: n'hi ha que a la tercera classe ja canten, d'altres que necessiten un trimestre. La clau és no tenir pressa — la constància setmanal fa la feina sola."),
        ],

        "title_es": "danza y timidez: qué pasa cuando un niño vergonzoso sube al escenario · escola de dansa cristina colomé",
        "desc_es": "Por qué la danza es una de las mejores herramientas para niños tímidos: grupo estable, lenguaje sin palabras, retos pequeños y la experiencia transformadora del escenario. Contado desde la sala.",
        "h1_es": "danza y timidez: cuando un niño vergonzoso sube al escenario",
        "intro_es": "«Es que mi hija es muy tímida...» — nos lo dicen como una duda, y es el mejor motivo para venir. Lo que hemos aprendido en 25 años viendo a niños vergonzosos encontrar su lugar.",
        "excerpt_es": "«Es que es muy tímida...» — nos lo dicen como una duda y es el mejor motivo para venir. Lo que pasa cuando un niño vergonzoso encuentra su lugar en la sala.",
        "cos_es": """
<p>Hay una escena que se repite cada curso: una familia en recepción, un niño medio escondido detrás de la pierna del padre, y la frase — «es que es muy tímido, no sé si esto es para él». Nuestra respuesta, después de décadas viéndolo, es siempre la misma: la danza no es <em>a pesar de</em> la timidez; a menudo es <em>la mejor respuesta</em> a la timidez. Y no porque la «cure» — la timidez no es ninguna enfermedad — sino porque le da al niño exactamente lo que necesita para estar bien siendo como es.</p>

<h2>un lugar donde no hace falta hablar</h2>
<p>La mayoría de actividades sociales piden palabras, y es justo donde el niño tímido sufre. En la sala de danza la conversación es otra: la música manda, el cuerpo responde, y nadie espera que digas nada ingenioso. Muchos niños vergonzosos descubren bailando que <strong>tienen muchas cosas que decir — solo que no eran con palabras</strong>.</p>

<h2>un grupo pequeño, estable y previsible</h2>
<p>Lo que asusta a la timidez es la incertidumbre social: gente nueva, situaciones abiertas. Una clase de danza es lo contrario — las mismas compañeras cada semana, la misma profesora, una estructura que se repite y se domina. Esa previsibilidad es un colchón: cuando el entorno es seguro, el niño tímido se despliega. A veces tarda tres semanas; a veces, tres meses. Siempre llega.</p>

<h2>la confianza no se predica: se acumula</h2>
<p>A un niño inseguro no le sirve que le digan «¡tú puedes!». Le sirve comprobarlo. La danza es una máquina de pequeñas comprobaciones: esta semana el giro, la otra el paso nuevo, después la coreografía entera. Cada «me ha salido» es un ladrillo. No se nota de un día para otro — se nota al cabo de un curso, cuando la misma criatura que no levantaba la mirada pide ponerse en primera fila.</p>

<h2>y entonces llega el escenario</h2>
<p>El festival de final de curso es el capítulo que ninguna familia tímida se cree de antemano. Semanas de ensayo, un vestuario, el telón, las luces — y el niño que «no hablaba con nadie» bailando delante de cientos de personas. No porque haya dejado de ser tímido: <strong>porque al escenario no sube solo — sube con su grupo, haciendo algo que domina</strong>. Y la ovación que viene después vale por mil charlas motivacionales. Las madres nos lo dicen con lágrimas en los ojos cada junio, y cada junio les respondemos lo mismo: nosotros solo hemos puesto la música; esto lo ha hecho él.</p>

<h2>por dónde empezar</h2>
<p>Si tu hijo o hija es de los de detrás de la pierna, empieza suave: una <a href="/es/danza-infantil/">clase de su grupo de edad</a>, sin prisa y sin público. La primera clase es gratuita, y si el primer día solo mira, también vale: mirar es la primera manera de participar de los tímidos. El resto llega solo — nosotros lo hemos visto cientos de veces.</p>
""",
        "faqs_es": [
            ("¿y si llega el día del festival y no quiere salir al escenario?",
             "No pasa casi nunca — el grupo y la coreografía dominada hacen de red — pero si pasa, no se fuerza: puede mirar desde dentro con las compañeras. A menudo quien no quería salir en diciembre es quien más disfruta en junio."),
            ("¿mejor una actividad individual o de grupo para un niño tímido?",
             "El grupo pequeño y estable de la danza da lo mejor de los dos mundos: trabajo personal dentro de un colectivo seguro, sin la exposición de un deporte de competición ni la soledad de una actividad individual."),
            ("¿cuánto tarda en «abrirse» un niño tímido en danza?",
             "Cada niño tiene su ritmo: hay quien a la tercera clase ya canta, y quien necesita un trimestre. La clave es no tener prisa — la constancia semanal hace el trabajo sola."),
        ],
    },
    {
        "slug": "barre-entrenament-ballet",
        "slug_es": "barre-entrenamiento-ballet",
        "categoria": "adults",
        "categoria_es": "adultos",
        "data": "2026-08-19",
        "data_ca": "19 d'agost de 2026",
        "data_es": "19 de agosto de 2026",
        "minuts": 4,
        "nom_wa": "barre",
        "nom_wa_es": "barre",
        "og": "blog-barre.jpg",
        "img": "blog-barre.jpg",
        "img_alt": "Peus d'una adulta amb mitjons antilliscants posant-se de puntetes al costat d'una barra de ballet amb llum de matí",
        "img_alt_es": "Pies de una adulta con calcetines antideslizantes poniéndose de puntillas junto a una barra de ballet con luz de mañana",
        "related_pagines": ["cos-benestar", "dansa-adults", "horaris"],
        "related_posts": ["comencar-dansa-adults"],

        "title": "barre: l'entrenament que ve del ballet (i per què enganxa) · escola de dansa cristina colomé",
        "desc": "Què és el barre, l'entrenament inspirat en el ballet que tonifica, allarga i millora la postura sense impacte. Com és una classe, per a qui és i els horaris de matí a la nostra escola de Barcelona.",
        "h1": "barre: l'entrenament que ve del ballet (i per què enganxa)",
        "intro": "Tonifica com el gimnàs, allarga com el ioga i s'entrena amb música vora una barra de ballet. El barre és l'entrenament de moda a mig món — i tenim els matins reservats per a ell.",
        "excerpt": "Tonifica com el gimnàs, allarga com el ioga i s'entrena vora una barra de ballet. Què és el barre, com és una classe i per què enganxa tant.",
        "cos": """
<p>Si has sentit a parlar del barre i t'imagines una classe de ballet per a experts, esborra la imatge: el barre és un <strong>entrenament físic</strong> que agafa del ballet la barra, la música i l'elegància — i deixa fora les coreografies i la pressió. No cal haver ballat mai. Cal tenir ganes de sortir de la classe més llarg, més fort i més recte del que has entrat.</p>

<h2>què és exactament</h2>
<p>El barre combina exercicis de força inspirats en la tècnica del ballet (pliés, relevés, treball de cames i glutis a la barra) amb pilates, estiraments i treball de centre. La fórmula és característica: <strong>moviments petits, moltes repeticions, zero impacte</strong>. Aquella tremolor de cames del minut quinze és la firma de la casa — i el motiu que funcioni.</p>

<h2>què hi guanyaràs</h2>
<ul>
<li><strong>To muscular sense volum:</strong> cames, glutis, abdomen i braços treballats amb el pes del cos, a l'estil allargat de les ballarines.</li>
<li><strong>Postura:</strong> el treball a la barra recol·loca esquena i espatlles — ho notaràs assegut a la feina.</li>
<li><strong>Flexibilitat i equilibri:</strong> cada sessió acaba estirant el que has enfortit; el cos ho agraeix amb anys de propina.</li>
<li><strong>Articulacions contentes:</strong> en ser de baix impacte, és ideal si véns de lesions, del sedentarisme o simplement no vols castigar genolls.</li>
</ul>

<h2>per a qui és</h2>
<p>Per a tothom, i ho diem literalment: dels 20 als 70 i escaig, gent que no ha fet mai exercici i esportistes que busquen complement. Cada exercici té versions per a cada nivell, així que la classe s'adapta a tu i no al revés. I si t'agrada la música i l'estètica de la dansa però «ballar» et fa mandra o vergonya, el barre és la teva porta: <strong>tot el bo del ballet, sense haver de ballar</strong>.</p>

<h2>quan i on</h2>
<p>A l'escola el barre viu als <strong>matins: dilluns i dimecres a les 11 h</strong> — l'hora perfecta si tens els vespres ocupats o vols començar el dia amb el cos posat a lloc. Forma part de la família de <a href="/cos-benestar/">cos i benestar</a>, juntament amb el ioga i la zumba, i com tot a l'escola, <strong>la primera classe és gratuïta</strong>. Vine amb roba còmoda i mitjons: la barra t'espera.</p>
""",
        "faqs": [
            ("cal haver fet ballet per fer barre?",
             "No, gens: el barre agafa la barra i l'estil del ballet, però és un entrenament físic sense coreografies. La majoria d'alumnes no han ballat mai."),
            ("el barre és un exercici complet o cal combinar-lo amb res més?",
             "És molt complet: força, flexibilitat, equilibri i postura en una mateixa sessió. Dues classes per setmana (dilluns i dimecres) són una rutina rodona per si sola."),
            ("estic embarassada o em recupero d'una lesió: puc fer barre?",
             "En ser de baix impacte, el barre sol ser una gran opció en aquestes situacions — sempre amb el vistiplau del teu metge i avisant la professora, que t'adaptarà els exercicis."),
        ],

        "title_es": "barre: el entrenamiento que viene del ballet (y por qué engancha) · escola de dansa cristina colomé",
        "desc_es": "Qué es el barre, el entrenamiento inspirado en el ballet que tonifica, alarga y mejora la postura sin impacto. Cómo es una clase, para quién es y los horarios de mañana en nuestra escuela de Barcelona.",
        "h1_es": "barre: el entrenamiento que viene del ballet (y por qué engancha)",
        "intro_es": "Tonifica como el gimnasio, alarga como el yoga y se entrena con música junto a una barra de ballet. El barre es el entrenamiento de moda en medio mundo — y tenemos las mañanas reservadas para él.",
        "excerpt_es": "Tonifica como el gimnasio, alarga como el yoga y se entrena junto a una barra de ballet. Qué es el barre, cómo es una clase y por qué engancha tanto.",
        "cos_es": """
<p>Si has oído hablar del barre y te imaginas una clase de ballet para expertos, borra la imagen: el barre es un <strong>entrenamiento físico</strong> que toma del ballet la barra, la música y la elegancia — y deja fuera las coreografías y la presión. No hace falta haber bailado nunca. Hace falta tener ganas de salir de la clase más largo, más fuerte y más recto de lo que has entrado.</p>

<h2>qué es exactamente</h2>
<p>El barre combina ejercicios de fuerza inspirados en la técnica del ballet (pliés, relevés, trabajo de piernas y glúteos en la barra) con pilates, estiramientos y trabajo de centro. La fórmula es característica: <strong>movimientos pequeños, muchas repeticiones, cero impacto</strong>. Ese temblor de piernas del minuto quince es la firma de la casa — y el motivo de que funcione.</p>

<h2>qué ganarás</h2>
<ul>
<li><strong>Tono muscular sin volumen:</strong> piernas, glúteos, abdomen y brazos trabajados con el peso del cuerpo, al estilo alargado de las bailarinas.</li>
<li><strong>Postura:</strong> el trabajo en la barra recoloca espalda y hombros — lo notarás sentado en el trabajo.</li>
<li><strong>Flexibilidad y equilibrio:</strong> cada sesión termina estirando lo que has fortalecido; el cuerpo lo agradece con años de propina.</li>
<li><strong>Articulaciones contentas:</strong> al ser de bajo impacto, es ideal si vienes de lesiones, del sedentarismo o simplemente no quieres castigar rodillas.</li>
</ul>

<h2>para quién es</h2>
<p>Para todo el mundo, y lo decimos literalmente: de los 20 a los 70 y pico, gente que no ha hecho nunca ejercicio y deportistas que buscan complemento. Cada ejercicio tiene versiones para cada nivel, así que la clase se adapta a ti y no al revés. Y si te gusta la música y la estética de la danza pero «bailar» te da pereza o vergüenza, el barre es tu puerta: <strong>todo lo bueno del ballet, sin tener que bailar</strong>.</p>

<h2>cuándo y dónde</h2>
<p>En la escuela el barre vive en las <strong>mañanas: lunes y miércoles a las 11 h</strong> — la hora perfecta si tienes las tardes ocupadas o quieres empezar el día con el cuerpo puesto en su sitio. Forma parte de la familia de <a href="/es/cuerpo-bienestar/">cuerpo y bienestar</a>, junto con el yoga y la zumba, y como todo en la escuela, <strong>la primera clase es gratuita</strong>. Ven con ropa cómoda y calcetines: la barra te espera.</p>
""",
        "faqs_es": [
            ("¿hay que haber hecho ballet para hacer barre?",
             "No, para nada: el barre toma la barra y el estilo del ballet, pero es un entrenamiento físico sin coreografías. La mayoría de alumnas no han bailado nunca."),
            ("¿el barre es un ejercicio completo o hay que combinarlo con algo más?",
             "Es muy completo: fuerza, flexibilidad, equilibrio y postura en una misma sesión. Dos clases por semana (lunes y miércoles) son una rutina redonda por sí sola."),
            ("estoy embarazada o me recupero de una lesión: ¿puedo hacer barre?",
             "Al ser de bajo impacto, el barre suele ser una gran opción en estas situaciones — siempre con el visto bueno de tu médico y avisando a la profesora, que te adaptará los ejercicios."),
        ],
    },
    {
        "slug": "classe-de-prova-gratuita",
        "slug_es": "clase-de-prueba-gratuita",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-08-26",
        "data_ca": "26 d'agost de 2026",
        "data_es": "26 de agosto de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-classe-prova.jpg",
        "img": "blog-classe-prova.jpg",
        "img_alt": "Una jaqueta de punt granat penjada a la barra de ballet de fusta, amb llum càlida de finestra",
        "img_alt_es": "Una chaqueta de punto granate colgada en la barra de ballet de madera, con luz cálida de ventana",
        "related_pagines": ["horaris", "dansa-infantil", "dansa-adults"],
        "related_posts": ["primer-dia-classe-dansa", "comencar-dansa-adults"],

        "title": "com és la classe de prova gratuïta (i per què la fem) · escola de dansa cristina colomé",
        "desc": "La primera classe a la nostra escola de dansa de Barcelona és gratuïta i sense compromís: com reservar-la, què passa quan arribes, què valorar en sortir i per què fa 25 anys que la regalem.",
        "h1": "com és la classe de prova (i per què és gratuïta)",
        "intro": "Cap decisió a cegues: a l'escola, la primera classe de qualsevol disciplina és gratis. T'expliquem com va, què mirar-hi — i el motiu de fons pel qual fa dècades que la regalem.",
        "excerpt": "Cap decisió a cegues: la primera classe de qualsevol disciplina és gratis. Com va, què mirar-hi i el motiu de fons pel qual fa dècades que la regalem.",
        "cos": """
<p>Hi ha coses que no es poden triar per catàleg, i una escola de dansa n'és una. Pots llegir-te tota la web (gràcies!), mirar els horaris i comparar preus — però la decisió de veritat es pren en un sol lloc: <strong>dins de la sala</strong>. Per això la primera classe a l'escola és gratuïta des de sempre. No és una promoció: és la nostra manera d'entendre com s'ha de començar.</p>

<h2>com es reserva</h2>
<p>Fàcil: truca'ns, escriu-nos per WhatsApp o pel formulari, digue'ns l'edat i què us ve de gust provar, i et proposem el grup i l'horari que toca. Si no ho teniu clar, us orientem — «té 7 anys i no para quieta» és tota la informació que necessitem per proposar-vos bé. Mira la <a href="/horaris/">graella d'horaris</a> per fer-te una idea, però no cal que vinguis amb els deures fets.</p>

<h2>què passa quan arribes</h2>
<p>Vine 10 minuts abans amb roba còmoda. Et rebem, et presentem la professora i el grup, i fas <strong>la classe sencera, de dins</strong> — no una exhibició ni una versió descafeïnada: la classe real, amb el grup real que seria el teu. Els nens s'incorporen al joc de seguida; els adults tenen permís explícit per equivocar-se tot el que calgui. En acabar, la professora us comenta com ho ha vist: nivell, grup recomanat, i qualsevol dubte.</p>

<h2>què val la pena observar</h2>
<ul>
<li><strong>La cara en sortir.</strong> El termòmetre infal·lible. Si surt il·luminat, ja tens la resposta.</li>
<li><strong>El grup.</strong> T'hi has sentit còmode? Els companys tenen una edat i nivell semblants?</li>
<li><strong>La professora.</strong> Com tracta els alumnes, com corregeix, com anima. És amb qui passaràs una hora cada setmana.</li>
<li><strong>La logística.</strong> L'horari encaixa amb la vida real? (Som a dos minuts de l'FGC Av. Tibidabo — això ajuda.)</li>
</ul>

<h2>i si no t'agrada?</h2>
<p>Doncs no passa absolutament res: ens ho dius (o no ens dius res) i aquí s'acaba, sense compromís ni trucades insistents. De vegades la resposta és «un altre estil» — i llavors proves aquell, també gratis. La classe de prova funciona en les dues direccions: tu ens proves a nosaltres, i nosaltres ens assegurem que quedis al grup on estaràs bé. <strong>Per això la regalem: perquè quan algú es queda, es queda de veritat.</strong> I fa més de 25 anys que ens funciona.</p>
""",
        "faqs": [
            ("la classe de prova és gratuïta per a totes les disciplines?",
             "Sí: qualsevol estil, qualsevol edat, qualsevol grup. I si després vols provar una segona disciplina diferent, aquella primera classe també és gratuïta."),
            ("he de portar alguna cosa o pagar alguna cosa per la prova?",
             "Res de res: roba còmoda, aigua i ganes. Sense matrícula, sense compromís i sense lletra petita — si no et quedes, no has gastat ni un euro."),
            ("puc fer la classe de prova a mig curs?",
             "Sí — s'hi pot entrar tot l'any, sempre que quedin places al grup. Al setembre hi ha més tria d'horaris, però els grups acullen alumnes nous a qualsevol mes."),
        ],

        "title_es": "cómo es la clase de prueba gratuita (y por qué la hacemos) · escola de dansa cristina colomé",
        "desc_es": "La primera clase en nuestra escuela de danza de Barcelona es gratuita y sin compromiso: cómo reservarla, qué pasa cuando llegas, qué valorar al salir y por qué llevamos 25 años regalándola.",
        "h1_es": "cómo es la clase de prueba (y por qué es gratuita)",
        "intro_es": "Ninguna decisión a ciegas: en la escuela, la primera clase de cualquier disciplina es gratis. Te contamos cómo va, qué mirar — y el motivo de fondo por el que llevamos décadas regalándola.",
        "excerpt_es": "Ninguna decisión a ciegas: la primera clase de cualquier disciplina es gratis. Cómo va, qué mirar y el motivo de fondo por el que llevamos décadas regalándola.",
        "cos_es": """
<p>Hay cosas que no se pueden elegir por catálogo, y una escuela de danza es una de ellas. Puedes leerte toda la web (¡gracias!), mirar los horarios y comparar precios — pero la decisión de verdad se toma en un solo sitio: <strong>dentro de la sala</strong>. Por eso la primera clase en la escuela es gratuita desde siempre. No es una promoción: es nuestra manera de entender cómo se debe empezar.</p>

<h2>cómo se reserva</h2>
<p>Fácil: llámanos, escríbenos por WhatsApp o por el formulario, dinos la edad y qué os apetece probar, y te proponemos el grupo y el horario que toca. Si no lo tenéis claro, os orientamos — «tiene 7 años y no para quieta» es toda la información que necesitamos para proponeros bien. Mira la <a href="/es/horarios/">parrilla de horarios</a> para hacerte una idea, pero no hace falta que vengas con los deberes hechos.</p>

<h2>qué pasa cuando llegas</h2>
<p>Ven 10 minutos antes con ropa cómoda. Te recibimos, te presentamos a la profesora y al grupo, y haces <strong>la clase entera, desde dentro</strong> — no una exhibición ni una versión descafeinada: la clase real, con el grupo real que sería el tuyo. Los niños se incorporan al juego enseguida; los adultos tienen permiso explícito para equivocarse todo lo que haga falta. Al terminar, la profesora os comenta cómo lo ha visto: nivel, grupo recomendado, y cualquier duda.</p>

<h2>qué vale la pena observar</h2>
<ul>
<li><strong>La cara al salir.</strong> El termómetro infalible. Si sale iluminado, ya tienes la respuesta.</li>
<li><strong>El grupo.</strong> ¿Te has sentido cómodo? ¿Los compañeros tienen una edad y nivel parecidos?</li>
<li><strong>La profesora.</strong> Cómo trata a los alumnos, cómo corrige, cómo anima. Es con quien pasarás una hora cada semana.</li>
<li><strong>La logística.</strong> ¿El horario encaja con la vida real? (Estamos a dos minutos del FGC Av. Tibidabo — eso ayuda.)</li>
</ul>

<h2>¿y si no te gusta?</h2>
<p>Pues no pasa absolutamente nada: nos lo dices (o no nos dices nada) y aquí se acaba, sin compromiso ni llamadas insistentes. A veces la respuesta es «otro estilo» — y entonces pruebas aquel, también gratis. La clase de prueba funciona en las dos direcciones: tú nos pruebas a nosotros, y nosotros nos aseguramos de que te quedes en el grupo donde estarás bien. <strong>Por eso la regalamos: porque cuando alguien se queda, se queda de verdad.</strong> Y llevamos más de 25 años comprobando que funciona.</p>
""",
        "faqs_es": [
            ("¿la clase de prueba es gratuita para todas las disciplinas?",
             "Sí: cualquier estilo, cualquier edad, cualquier grupo. Y si después quieres probar una segunda disciplina diferente, esa primera clase también es gratuita."),
            ("¿tengo que llevar algo o pagar algo por la prueba?",
             "Nada de nada: ropa cómoda, agua y ganas. Sin matrícula, sin compromiso y sin letra pequeña — si no te quedas, no has gastado ni un euro."),
            ("¿puedo hacer la clase de prueba a mitad de curso?",
             "Sí — se puede entrar todo el año, siempre que queden plazas en el grupo. En septiembre hay más donde elegir, pero los grupos acogen alumnos nuevos en cualquier mes."),
        ],
    },
    {
        "slug": "historia-escola-25-anys",
        "slug_es": "historia-escuela-25-anos",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-09-02",
        "data_ca": "2 de setembre de 2026",
        "data_es": "2 de septiembre de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-historia-escola.jpg",
        "img": "blog-historia-escola.jpg",
        "img_alt": "Unes sabatilles de ballet velles i gastades al costat d'unes de noves, a terra d'una sala de dansa",
        "img_alt_es": "Unas zapatillas de ballet viejas y gastadas junto a unas nuevas, en el suelo de una sala de danza",
        "related_pagines": ["dansa-infantil", "dansa-adults", "horaris"],
        "related_posts": ["classe-de-prova-gratuita", "a-quina-edat-comencar-dansa"],

        "title": "més de 25 anys movent Sant Gervasi: la història de l'escola · escola de dansa cristina colomé",
        "desc": "La història de l'Escola de Dansa Cristina Colomé, al carrer Craywinckel de Sant Gervasi (Barcelona): més de 25 anys, generacions d'alumnes, 3 sales i una manera pròpia d'ensenyar a ballar.",
        "h1": "més de 25 anys movent Sant Gervasi",
        "intro": "Hi ha alumnes que van venir de petites i ara hi porten les seves filles. Aquesta és la història — i la manera de fer — d'una escola de barri que fa més d'un quart de segle que balla.",
        "excerpt": "Hi ha alumnes que van venir de petites i ara hi porten les seves filles. La història i la manera de fer d'una escola de barri que fa més d'un quart de segle que balla.",
        "cos": """
<p>Al món de les extraescolars, on tot canvia cada setembre, durar més de 25 anys no és un detall: és una declaració. L'Escola de Dansa Cristina Colomé fa més d'un quart de segle que obre cada tarda al <strong>carrer Craywinckel, 25</strong>, a Sant Gervasi — a dos minuts de l'FGC Av. Tibidabo — i si haguéssim de resumir per què seguim aquí, ho faríem amb una escena: una antiga alumna entrant per la porta amb la seva filla de la mà, dient «jo venia aquí de petita».</p>

<h2>una escola amb nom i cognoms</h2>
<p>L'escola porta el nom de la seva fundadora i ànima, la <strong>Cristina Colomé</strong>, i això ho explica gairebé tot: no som una franquícia ni un gimnàs amb classes de ball — som una escola de barri en el millor sentit de la paraula. Aquí les professores saben com et dius, com et va l'escola i quin pas se't resisteix. Aquesta escala humana no és una estratègia: és l'única manera que coneixem de fer-ho.</p>

<h2>el que ha canviat (i el que no)</h2>
<p>En 25 anys la dansa ha viscut revolucions: el hip-hop va entrar a les escoles, els musicals van tornar a omplir teatres, el K-pop va arribar de Corea i el barre va posar les barres de ballet de moda als gimnasos de mig món. L'escola ho ha anat abraçant tot — avui tenim <strong>una dotzena de disciplines, dels 3 als 99 anys, en 3 sales condicionades i insonoritzades</strong> — però el nucli no s'ha mogut mai: tècnica ben ensenyada, grups per edat i nivell, i la convicció que ballar ha de fer feliç. Primer la persona, després el pas.</p>

<h2>generacions dalt del mateix escenari</h2>
<p>Si una cosa mesura la vida d'una escola, són els seus festivals: dècades de coreografies, vestuaris, nervis entre bastidors i ovacions de famílies. Pel nostre escenari hi han passat milers d'alumnes — nenes que van fer aquí les primeres puntes, adolescents que van descobrir el claqué, adults que van perdre la vergonya passats els quaranta. Alguns han acabat dedicant-se a la dansa; la immensa majoria se n'han endut una cosa igual de valuosa: <strong>un lloc on el cos i la música van ser seus una estona cada setmana</strong>.</p>

<h2>el capítol que ve</h2>
<p>La història continua escrivint-se cada tarda: la graella del curs <a href="/horaris/">2026–27</a> és plena de vida, dels grups d'<a href="/dansa-infantil/">iniciació</a> als vespres d'<a href="/dansa-adults/">adults</a>. I la porta segueix fent el que ha fet sempre: obrir-se. Si mai has pensat que t'agradaria ballar — o que li agradaria a algú de casa — ja saps com comença tot aquí: amb una primera classe gratuïta. Fa més de 25 anys que la regalem, i pensem seguir fent-ho.</p>
""",
        "faqs": [
            ("qui és la Cristina Colomé?",
             "La fundadora i directora de l'escola: la persona que fa més de 25 anys la va posar en marxa a Sant Gervasi i que n'ha marcat la manera de fer — tècnica seriosa, tracte proper i la convicció que ballar ha de fer feliç."),
            ("què vol dir que sou una «escola de barri»?",
             "Que les professores coneixen cada alumne pel nom, que les famílies es coneixen entre elles, i que moltes alumnes d'avui són filles d'alumnes d'ahir. La dansa s'ensenya millor a escala humana."),
            ("les sales també es lloguen?",
             "Sí: les 3 sales, condicionades i insonoritzades, es lloguen per a assajos i activitats — i també fem celebracions especials, dels aniversaris als balls de núvis."),
        ],

        "title_es": "más de 25 años moviendo Sant Gervasi: la historia de la escuela · escola de dansa cristina colomé",
        "desc_es": "La historia de la Escola de Dansa Cristina Colomé, en la calle Craywinckel de Sant Gervasi (Barcelona): más de 25 años, generaciones de alumnos, 3 salas y una manera propia de enseñar a bailar.",
        "h1_es": "más de 25 años moviendo Sant Gervasi",
        "intro_es": "Hay alumnas que vinieron de pequeñas y ahora traen a sus hijas. Esta es la historia — y la manera de hacer — de una escuela de barrio que lleva más de un cuarto de siglo bailando.",
        "excerpt_es": "Hay alumnas que vinieron de pequeñas y ahora traen a sus hijas. La historia y la manera de hacer de una escuela de barrio que lleva más de un cuarto de siglo bailando.",
        "cos_es": """
<p>En el mundo de las extraescolares, donde todo cambia cada septiembre, durar más de 25 años no es un detalle: es una declaración. La Escola de Dansa Cristina Colomé lleva más de un cuarto de siglo abriendo cada tarde en la <strong>calle Craywinckel, 25</strong>, en Sant Gervasi — a dos minutos del FGC Av. Tibidabo — y si tuviéramos que resumir por qué seguimos aquí, lo haríamos con una escena: una antigua alumna entrando por la puerta con su hija de la mano, diciendo «yo venía aquí de pequeña».</p>

<h2>una escuela con nombre y apellidos</h2>
<p>La escuela lleva el nombre de su fundadora y alma, <strong>Cristina Colomé</strong>, y eso lo explica casi todo: no somos una franquicia ni un gimnasio con clases de baile — somos una escuela de barrio en el mejor sentido de la palabra. Aquí las profesoras saben cómo te llamas, cómo te va el colegio y qué paso se te resiste. Esa escala humana no es una estrategia: es la única manera que conocemos de hacerlo.</p>

<h2>lo que ha cambiado (y lo que no)</h2>
<p>En 25 años la danza ha vivido revoluciones: el hip-hop entró en las escuelas, los musicales volvieron a llenar teatros, el K-pop llegó de Corea y el barre puso las barras de ballet de moda en los gimnasios de medio mundo. La escuela lo ha ido abrazando todo — hoy tenemos <strong>una docena de disciplinas, de los 3 a los 99 años, en 3 salas acondicionadas e insonorizadas</strong> — pero el núcleo no se ha movido nunca: técnica bien enseñada, grupos por edad y nivel, y la convicción de que bailar debe hacer feliz. Primero la persona, después el paso.</p>

<h2>generaciones sobre el mismo escenario</h2>
<p>Si algo mide la vida de una escuela, son sus festivales: décadas de coreografías, vestuarios, nervios entre bastidores y ovaciones de familias. Por nuestro escenario han pasado miles de alumnos — niñas que hicieron aquí sus primeras puntas, adolescentes que descubrieron el claqué, adultos que perdieron la vergüenza pasados los cuarenta. Algunos han acabado dedicándose a la danza; la inmensa mayoría se han llevado algo igual de valioso: <strong>un lugar donde el cuerpo y la música fueron suyos un rato cada semana</strong>.</p>

<h2>el capítulo que viene</h2>
<p>La historia sigue escribiéndose cada tarde: la parrilla del curso <a href="/es/horarios/">2026–27</a> está llena de vida, de los grupos de <a href="/es/danza-infantil/">iniciación</a> a las noches de <a href="/es/danza-adultos/">adultos</a>. Y la puerta sigue haciendo lo que ha hecho siempre: abrirse. Si alguna vez has pensado que te gustaría bailar — o que le gustaría a alguien de casa — ya sabes cómo empieza todo aquí: con una primera clase gratuita. Llevamos más de 25 años regalándola, y pensamos seguir haciéndolo.</p>
""",
        "faqs_es": [
            ("¿quién es Cristina Colomé?",
             "La fundadora y directora de la escuela: la persona que hace más de 25 años la puso en marcha en Sant Gervasi y que ha marcado su manera de hacer — técnica seria, trato cercano y la convicción de que bailar debe hacer feliz."),
            ("¿qué significa que sois una «escuela de barrio»?",
             "Que las profesoras conocen a cada alumno por su nombre, que las familias se conocen entre ellas, y que muchas alumnas de hoy son hijas de alumnas de ayer. La danza se enseña mejor a escala humana."),
            ("¿las salas también se alquilan?",
             "Sí: las 3 salas, acondicionadas e insonorizadas, se alquilan para ensayos y actividades — y también hacemos celebraciones especiales, de los cumpleaños a los bailes de novios."),
        ],
    },

    {
        "slug": "roba-dansa-que-portar",
        "slug_es": "ropa-danza-que-llevar",
        "categoria": "famílies",
        "categoria_es": "familias",
        "data": "2026-06-24",
        "data_ca": "24 de juny de 2026",
        "data_es": "24 de junio de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-roba-dansa.jpg",
        "img": "blog-roba-dansa.jpg",
        "img_alt": "Una bossa de dansa oberta sobre el parquet amb sabatilles, mitges i una gometa de cabell",
        "img_alt_es": "Una bolsa de danza abierta sobre el parquet con zapatillas, medias y una goma de pelo",
        "related_pagines": ["dansa-infantil", "ballet-classic", "hip-hop", "preus"],
        "related_posts": ["primer-dia-classe-dansa"],

        "title": "què ha de portar a la bossa de dansa? la guia per disciplines · escola de dansa cristina colomé",
        "desc": "Sabatilles, mitges, roba còmoda... què cal per a cada disciplina de dansa i què no cal comprar el primer dia. La guia pràctica que donem a totes les famílies noves de l'escola.",
        "h1": "què ha de portar a la bossa de dansa? la guia per disciplines",
        "intro": "El primer dubte pràctic de tota família nova: què comprem? La resposta que donem sempre: de moment, gairebé res. Aquí tens la guia sencera, disciplina per disciplina.",
        "excerpt": "Sabatilles, mitges, roba còmoda... què cal per a cada disciplina i què no cal comprar el primer dia. La guia pràctica per no gastar de més.",
        "cos": """
<p>Cada setembre veiem famílies que arriben el primer dia amb l'equip complet: maillot nou, mitges noves, sabatilles de mitja punta acabades d'estrenar. I ens sap greu dir-los que potser han corregut massa. El nostre consell de sempre és el contrari: <strong>vine amb roba còmoda, prova, i compra després</strong>. Aquí tens què cal de debò per a cada disciplina.</p>

<h2>el primer dia: roba còmoda i prou</h2>
<p>Per a la <a href="/classe-de-prova-gratuita/">classe de prova</a> i les primeres setmanes, amb uns leggings o pantalons elàstics, una samarreta que no balli massa i mitjons n'hi ha prou. Volem que el nen o la nena decideixi si li agrada la dansa, no que estreni vestuari. Quan la plaça ja és seva, la professora us dirà exactament què necessita el seu grup — i us estalviareu compres equivocades.</p>

<h2>clàssic: el ritual més bonic</h2>
<p>Al <a href="/ballet-classic/">ballet clàssic</a> el vestuari és part de l'aprenentatge: maillot, mitges i sabatilles de mitja punta (les puntes arriben molt més endavant, quan el peu i la tècnica estan a punt — mai abans). El cabell recollit en un monyo no és mania: és seguretat i és tradició. Tot plegat costa menys del que sembla i dura cursos sencers.</p>

<h2>urbanes i modernes: llibertat amb criteri</h2>
<p>Per a <a href="/hip-hop/">hip-hop</a>, jazz o k-pop, roba amb què es puguin moure de gust i <strong>sabatilles esportives netes d'ús exclusiu per a la sala</strong> — aquest detall importa: el parquet ho agraeix i els turmells també. Per al contemporani es balla descalç o amb mitjons: el més barat de tots els equips!</p>

<h2>el que no cal comprar mai (d'entrada)</h2>
<ul>
<li><strong>Puntes.</strong> Les decideix la professora quan toca, ni un dia abans.</li>
<li><strong>Roba de marca de dansa.</strong> Als 6 anys, el maillot bàsic fa exactament el mateix servei.</li>
<li><strong>Dues talles de tot «perquè creixerà».</strong> La roba de dansa és elàstica: compra la seva talla.</li>
</ul>

<h2>el truc de la bossa</h2>
<p>Una bossa petita que sigui només de dansa, preparada sempre amb el mateix: sabatilles, ampolla d'aigua, gometa de recanvi. Els nens que porten la seva bossa «de ballarina» des del primer dia se senten part de l'escola abans i que no falti mai res a dins es converteix en responsabilitat seva. Petita, però seva. Si teniu dubtes amb el vestuari del vostre grup, pregunteu-nos al taulell — us ho resolem en un minut.</p>
""",
        "faqs": [
            ("cal comprar l'equip abans de la primera classe?",
             "No. Per a la classe de prova i les primeres setmanes n'hi ha prou amb roba còmoda i mitjons. Quan la plaça sigui seva, la professora us dirà exactament què necessita el grup."),
            ("quan es comencen a portar puntes al ballet?",
             "Quan la professora ho indica, mai abans: cal que el peu, el turmell i la tècnica estiguin preparats. Avançar les puntes per il·lusió és la manera més ràpida de fer-se mal."),
            ("les sabatilles esportives del carrer valen per al hip-hop?",
             "Millor que no: demanem esportives netes d'ús exclusiu per a la sala. El parquet es conserva millor i l'adherència és la correcta per ballar."),
        ],

        "title_es": "¿qué tiene que llevar en la bolsa de danza? la guía por disciplinas · escola de dansa cristina colomé",
        "desc_es": "Zapatillas, medias, ropa cómoda... qué hace falta para cada disciplina de danza y qué no hay que comprar el primer día. La guía práctica que damos a todas las familias nuevas de la escuela.",
        "h1_es": "¿qué tiene que llevar en la bolsa de danza? la guía por disciplinas",
        "intro_es": "La primera duda práctica de toda familia nueva: ¿qué compramos? La respuesta que damos siempre: de momento, casi nada. Aquí tienes la guía entera, disciplina por disciplina.",
        "excerpt_es": "Zapatillas, medias, ropa cómoda... qué hace falta para cada disciplina y qué no hay que comprar el primer día. La guía práctica para no gastar de más.",
        "cos_es": """
<p>Cada septiembre vemos familias que llegan el primer día con el equipo completo: maillot nuevo, medias nuevas, zapatillas de media punta recién estrenadas. Y nos sabe mal decirles que quizá han corrido demasiado. Nuestro consejo de siempre es el contrario: <strong>ven con ropa cómoda, prueba, y compra después</strong>. Aquí tienes qué hace falta de verdad para cada disciplina.</p>

<h2>el primer día: ropa cómoda y punto</h2>
<p>Para la <a href="/es/blog/clase-de-prueba-gratuita/">clase de prueba</a> y las primeras semanas, con unos leggings o pantalones elásticos, una camiseta que no baile demasiado y calcetines es suficiente. Queremos que el niño o la niña decida si le gusta la danza, no que estrene vestuario. Cuando la plaza ya sea suya, la profesora os dirá exactamente qué necesita su grupo — y os ahorraréis compras equivocadas.</p>

<h2>clásico: el ritual más bonito</h2>
<p>En el <a href="/es/ballet-clasico/">ballet clásico</a> el vestuario es parte del aprendizaje: maillot, medias y zapatillas de media punta (las puntas llegan mucho más adelante, cuando el pie y la técnica están a punto — nunca antes). El pelo recogido en un moño no es manía: es seguridad y es tradición. Todo junto cuesta menos de lo que parece y dura cursos enteros.</p>

<h2>urbanas y modernas: libertad con criterio</h2>
<p>Para <a href="/es/hip-hop/">hip-hop</a>, jazz o k-pop, ropa con la que se puedan mover a gusto y <strong>zapatillas deportivas limpias de uso exclusivo para la sala</strong> — este detalle importa: el parquet lo agradece y los tobillos también. Para el contemporáneo se baila descalzo o con calcetines: ¡el más barato de todos los equipos!</p>

<h2>lo que no hay que comprar nunca (de entrada)</h2>
<ul>
<li><strong>Puntas.</strong> Las decide la profesora cuando toca, ni un día antes.</li>
<li><strong>Ropa de marca de danza.</strong> A los 6 años, el maillot básico hace exactamente el mismo servicio.</li>
<li><strong>Dos tallas de todo «porque crecerá».</strong> La ropa de danza es elástica: compra su talla.</li>
</ul>

<h2>el truco de la bolsa</h2>
<p>Una bolsa pequeña que sea solo de danza, preparada siempre con lo mismo: zapatillas, botella de agua, goma de recambio. Los niños que llevan su bolsa «de bailarina» desde el primer día se sienten parte de la escuela antes, y que no falte nunca nada dentro se convierte en responsabilidad suya. Pequeña, pero suya. Si tenéis dudas con el vestuario de vuestro grupo, preguntadnos en recepción — os lo resolvemos en un minuto.</p>
""",
        "faqs_es": [
            ("¿hay que comprar el equipo antes de la primera clase?",
             "No. Para la clase de prueba y las primeras semanas basta con ropa cómoda y calcetines. Cuando la plaza sea suya, la profesora os dirá exactamente qué necesita el grupo."),
            ("¿cuándo se empiezan a llevar puntas en ballet?",
             "Cuando la profesora lo indica, nunca antes: el pie, el tobillo y la técnica deben estar preparados. Adelantar las puntas por ilusión es la manera más rápida de hacerse daño."),
            ("¿las deportivas de calle valen para el hip-hop?",
             "Mejor que no: pedimos deportivas limpias de uso exclusivo para la sala. El parquet se conserva mejor y la adherencia es la correcta para bailar."),
        ],
    },
    {
        "slug": "hip-hop-nens-adolescents",
        "slug_es": "hip-hop-ninos-adolescentes",
        "categoria": "estils",
        "categoria_es": "estilos",
        "data": "2026-06-17",
        "data_ca": "17 de juny de 2026",
        "data_es": "17 de junio de 2026",
        "minuts": 4,
        "nom_wa": "hip-hop",
        "nom_wa_es": "hip-hop",
        "og": "blog-hiphop-joves.jpg",
        "img": "blog-hiphop-joves.jpg",
        "img_alt": "Unes sabatilles esportives blanques i una gorra sobre el parquet d'una sala de dansa amb llum càlida",
        "img_alt_es": "Unas zapatillas deportivas blancas y una gorra sobre el parquet de una sala de danza con luz cálida",
        "related_pagines": ["hip-hop", "dansa-infantil", "k-pop-heels", "horaris"],
        "related_posts": ["triar-estil-dansa-fill"],

        "title": "hip-hop per a nens i adolescents: molt més que passos · escola de dansa cristina colomé",
        "desc": "Per què el hip-hop enganxa tant els nens i adolescents: energia, identitat, grup i una tècnica més seriosa del que sembla. Com són les classes de hip-hop per edats a l'escola.",
        "h1": "hip-hop per a nens i adolescents: molt més que passos",
        "intro": "És l'estil que més creix a l'escola des de fa anys. I no és casualitat: pocs llocs donen a un nen o a un adolescent tanta energia, tanta identitat i tant grup alhora.",
        "excerpt": "Per què el hip-hop enganxa tant: energia, identitat, grup i una tècnica més seriosa del que sembla. Com són les classes per edats.",
        "cos": """
<p>Quan una família ve a informar-se i el nen diu «jo vull fer hip-hop», sovint la mare o el pare ens mira com demanant disculpes. No cal: <strong>el hip-hop és una gran porta d'entrada a la dansa</strong>, amb tècnica seriosa, disciplina real i una cultura riquíssima al darrere. I sí: enganxa moltíssim.</p>

<h2>per què els enganxa tant</h2>
<p>Perquè és la seva música. La que sona als seus mòbils, als seus videojocs, a les seves xarxes. Quan la classe balla amb la banda sonora de la seva vida, la motivació ve de sèrie. I perquè el hip-hop premia allò que l'adolescència demana a crits: <strong>tenir un estil propi</strong>. Dins d'una mateixa coreografia, cadascú hi posa el seu accent.</p>

<h2>la tècnica que no es veu</h2>
<p>Des de fora sembla espontani; des de dins és feina fina: aïllaments, musicalitat, control del pes, memòria coreogràfica i una condició física que ja voldrien molts esports. Els nostres grups de <a href="/hip-hop/">hip-hop</a> van per edats i nivells — dels infantils que hi aprenen coordinació jugant fins als juvenils que preparen coreografies de festival que posen la pell de gallina.</p>

<h2>l'efecte grup</h2>
<p>Si hi ha una cosa que veiem curs rere curs és la colla que es forma a les classes de hip-hop. Ballar en grup, suar en grup, equivocar-se en grup i clavar-la en grup crea un vincle que va molt més enllà de la sala. Per a molts adolescents, la classe de la setmana és <strong>el seu lloc</strong> — i això, a segons quines edats, val or.</p>

<h2>com començar</h2>
<p>Com sempre a l'escola: <a href="/classe-de-prova-gratuita/">amb una classe de prova gratuïta</a>. Roba còmoda, esportives netes i ganes de moure's. Mira els grups de hip-hop a la <a href="/horaris/">graella d'horaris</a> — n'hi ha des d'infantil fins a adults — i si el que t'estira és el k-pop o les heels, també <a href="/k-pop-heels/">tenim classe per a tu</a>.</p>
""",
        "faqs": [
            ("a partir de quina edat es pot fer hip-hop?",
             "A l'escola tenim grups de hip-hop des d'infantil: els més petits hi treballen coordinació i ritme jugant, i a mesura que creixen la tècnica i les coreografies pugen de nivell."),
            ("el hip-hop té tècnica o és ballar lliure?",
             "Té molta tècnica: aïllaments, musicalitat, control del pes i memòria coreogràfica. La sensació de llibertat és precisament el resultat de dominar aquesta base."),
            ("què cal portar a una classe de hip-hop?",
             "Roba còmoda i esportives netes d'ús exclusiu per a la sala. Per a la primera classe de prova, amb això n'hi ha prou."),
        ],

        "title_es": "hip-hop para niños y adolescentes: mucho más que pasos · escola de dansa cristina colomé",
        "desc_es": "Por qué el hip-hop engancha tanto a niños y adolescentes: energía, identidad, grupo y una técnica más seria de lo que parece. Cómo son las clases de hip-hop por edades en la escuela.",
        "h1_es": "hip-hop para niños y adolescentes: mucho más que pasos",
        "intro_es": "Es el estilo que más crece en la escuela desde hace años. Y no es casualidad: pocos lugares dan a un niño o a un adolescente tanta energía, tanta identidad y tanto grupo a la vez.",
        "excerpt_es": "Por qué el hip-hop engancha tanto: energía, identidad, grupo y una técnica más seria de lo que parece. Cómo son las clases por edades.",
        "cos_es": """
<p>Cuando una familia viene a informarse y el niño dice «yo quiero hacer hip-hop», a menudo la madre o el padre nos mira como pidiendo disculpas. No hace falta: <strong>el hip-hop es una gran puerta de entrada a la danza</strong>, con técnica seria, disciplina real y una cultura riquísima detrás. Y sí: engancha muchísimo.</p>

<h2>por qué les engancha tanto</h2>
<p>Porque es su música. La que suena en sus móviles, en sus videojuegos, en sus redes. Cuando la clase baila con la banda sonora de su vida, la motivación viene de serie. Y porque el hip-hop premia lo que la adolescencia pide a gritos: <strong>tener un estilo propio</strong>. Dentro de una misma coreografía, cada uno pone su acento.</p>

<h2>la técnica que no se ve</h2>
<p>Desde fuera parece espontáneo; desde dentro es trabajo fino: aislamientos, musicalidad, control del peso, memoria coreográfica y una condición física que ya quisieran muchos deportes. Nuestros grupos de <a href="/es/hip-hop/">hip-hop</a> van por edades y niveles — desde los infantiles que aprenden coordinación jugando hasta los juveniles que preparan coreografías de festival que ponen la piel de gallina.</p>

<h2>el efecto grupo</h2>
<p>Si hay algo que vemos curso tras curso es la pandilla que se forma en las clases de hip-hop. Bailar en grupo, sudar en grupo, equivocarse en grupo y clavarla en grupo crea un vínculo que va mucho más allá de la sala. Para muchos adolescentes, la clase de la semana es <strong>su lugar</strong> — y eso, a según qué edades, vale oro.</p>

<h2>cómo empezar</h2>
<p>Como siempre en la escuela: <a href="/es/blog/clase-de-prueba-gratuita/">con una clase de prueba gratuita</a>. Ropa cómoda, deportivas limpias y ganas de moverse. Mira los grupos de hip-hop en la <a href="/es/horarios/">parrilla de horarios</a> — los hay desde infantil hasta adultos — y si lo que te tira es el k-pop o las heels, también <a href="/es/k-pop-heels/">tenemos clase para ti</a>.</p>
""",
        "faqs_es": [
            ("¿a partir de qué edad se puede hacer hip-hop?",
             "En la escuela tenemos grupos de hip-hop desde infantil: los más pequeños trabajan coordinación y ritmo jugando, y a medida que crecen la técnica y las coreografías suben de nivel."),
            ("¿el hip-hop tiene técnica o es bailar libre?",
             "Tiene mucha técnica: aislamientos, musicalidad, control del peso y memoria coreográfica. La sensación de libertad es precisamente el resultado de dominar esa base."),
            ("¿qué hay que llevar a una clase de hip-hop?",
             "Ropa cómoda y deportivas limpias de uso exclusivo para la sala. Para la primera clase de prueba, con eso es suficiente."),
        ],
    },
    {
        "slug": "claque-el-ball-que-sona",
        "slug_es": "claque-el-baile-que-suena",
        "categoria": "estils",
        "categoria_es": "estilos",
        "data": "2026-06-10",
        "data_ca": "10 de juny de 2026",
        "data_es": "10 de junio de 2026",
        "minuts": 4,
        "nom_wa": "claqué",
        "nom_wa_es": "claqué",
        "og": "blog-claque.jpg",
        "img": "blog-claque.jpg",
        "img_alt": "Un parell de sabates de claqué negres amb les plaques metàl·liques brillants sobre el parquet",
        "img_alt_es": "Un par de zapatos de claqué negros con las placas metálicas brillantes sobre el parquet",
        "related_pagines": ["claque", "jazz", "musical-interpretacio", "horaris"],
        "related_posts": ["triar-estil-dansa-fill"],

        "title": "el claqué: el ball que també és música · escola de dansa cristina colomé",
        "desc": "Al claqué els peus són l'instrument: cada pas és un so i cada coreografia, una partitura. Què fa tan especial el claqué, per què va bé a totes les edats i com són les classes.",
        "h1": "el claqué: el ball que també és música",
        "intro": "Hi ha una disciplina a l'escola on no només balles la música: la fas. Benvinguts al claqué, l'art de convertir els peus en un instrument de percussió.",
        "excerpt": "Al claqué els peus són l'instrument: cada pas és un so i cada coreografia, una partitura. Per què va bé a totes les edats.",
        "cos": """
<p>El primer dia de claqué passa sempre el mateix: algú fa el primer «tap» amb la placa metàl·lica i se li escapa el somriure. És un so que engancha. Perquè el <a href="/claque/">claqué</a> té una cosa que cap altra disciplina de l'escola té: <strong>quan balles, sones</strong>.</p>

<h2>ballarins que són músics</h2>
<p>Al claqué cada pas és una nota: el taló i la punta fan sons diferents, els silencis compten tant com els cops i una coreografia és, literalment, una partitura. Per això treballa una musicalitat finíssima: qui fa claqué aprèn a escoltar el ritme per dins, i això després es nota en qualsevol altre ball — i en qualsevol instrument.</p>

<h2>d'on ve aquest art</h2>
<p>El claqué va néixer als Estats Units de la trobada entre les danses percudides irlandeses i els ritmes africans, i va viure la seva edat daurada amb el swing i els grans musicals de Hollywood. Fred Astaire, Ginger Rogers, Gene Kelly... Quan en fas, entres en una tradició de gairebé dos segles — i t'adones que aquella elegància de les pel·lícules en blanc i negre s'aprèn pas a pas.</p>

<h2>per a qui és?</h2>
<p>Aquesta és la millor part: <strong>per a gairebé tothom</strong>. Els nens hi aprenen ritme i coordinació d'una manera que sembla màgia; els adolescents hi troben una habilitat que ningú més té; i els adults el descobreixen com una gimnàstica mental i física fantàstica — memòria, ritme, cames i riures, tot alhora. A l'escola tenim grups juvenils i d'adults, i el nivell es construeix des de zero.</p>

<h2>prova-ho: el so et convencerà</h2>
<p>El claqué s'ha de sentir als peus. Vine a fer una <a href="/classe-de-prova-gratuita/">classe de prova gratuïta</a> — les primeres classes es poden fer amb sabata de sola dura mentre decideixes — i mira els horaris dels grups a la <a href="/horaris/">graella</a>. T'avisem d'una cosa: el «tap-tap» és addictiu.</p>
""",
        "faqs": [
            ("cal haver fet dansa abans per començar claqué?",
             "No. El claqué es construeix des de zero: primer els sons bàsics de taló i punta, després les combinacions. La musicalitat s'entrena a cada classe."),
            ("necessito sabates de claqué per provar?",
             "Per a la classe de prova no: unes sabates de sola dura serveixen per començar. Si t'hi quedes, t'orientem sobre quines comprar."),
            ("el claqué és per a nens o per a adults?",
             "Per a tots dos: tenim grups juvenils i d'adults. És de les disciplines que millor envelleixen — es pot començar i gaudir a qualsevol edat."),
        ],

        "title_es": "el claqué: el baile que también es música · escola de dansa cristina colomé",
        "desc_es": "En el claqué los pies son el instrumento: cada paso es un sonido y cada coreografía, una partitura. Qué hace tan especial el claqué, por qué va bien a todas las edades y cómo son las clases.",
        "h1_es": "el claqué: el baile que también es música",
        "intro_es": "Hay una disciplina en la escuela donde no solo bailas la música: la haces. Bienvenidos al claqué, el arte de convertir los pies en un instrumento de percusión.",
        "excerpt_es": "En el claqué los pies son el instrumento: cada paso es un sonido y cada coreografía, una partitura. Por qué va bien a todas las edades.",
        "cos_es": """
<p>El primer día de claqué pasa siempre lo mismo: alguien hace el primer «tap» con la placa metálica y se le escapa la sonrisa. Es un sonido que engancha. Porque el <a href="/es/claque/">claqué</a> tiene algo que ninguna otra disciplina de la escuela tiene: <strong>cuando bailas, suenas</strong>.</p>

<h2>bailarines que son músicos</h2>
<p>En el claqué cada paso es una nota: el tacón y la punta hacen sonidos distintos, los silencios cuentan tanto como los golpes y una coreografía es, literalmente, una partitura. Por eso trabaja una musicalidad finísima: quien hace claqué aprende a escuchar el ritmo por dentro, y eso luego se nota en cualquier otro baile — y en cualquier instrumento.</p>

<h2>de dónde viene este arte</h2>
<p>El claqué nació en Estados Unidos del encuentro entre las danzas percutidas irlandesas y los ritmos africanos, y vivió su edad dorada con el swing y los grandes musicales de Hollywood. Fred Astaire, Ginger Rogers, Gene Kelly... Cuando lo practicas, entras en una tradición de casi dos siglos — y descubres que aquella elegancia de las películas en blanco y negro se aprende paso a paso.</p>

<h2>¿para quién es?</h2>
<p>Esta es la mejor parte: <strong>para casi todo el mundo</strong>. Los niños aprenden ritmo y coordinación de una manera que parece magia; los adolescentes encuentran una habilidad que nadie más tiene; y los adultos lo descubren como una gimnasia mental y física fantástica — memoria, ritmo, piernas y risas, todo a la vez. En la escuela tenemos grupos juveniles y de adultos, y el nivel se construye desde cero.</p>

<h2>pruébalo: el sonido te convencerá</h2>
<p>El claqué hay que sentirlo en los pies. Ven a hacer una <a href="/es/blog/clase-de-prueba-gratuita/">clase de prueba gratuita</a> — las primeras clases se pueden hacer con zapato de suela dura mientras decides — y mira los horarios de los grupos en la <a href="/es/horarios/">parrilla</a>. Te avisamos de una cosa: el «tap-tap» es adictivo.</p>
""",
        "faqs_es": [
            ("¿hay que haber hecho danza antes de empezar claqué?",
             "No. El claqué se construye desde cero: primero los sonidos básicos de tacón y punta, después las combinaciones. La musicalidad se entrena en cada clase."),
            ("¿necesito zapatos de claqué para probar?",
             "Para la clase de prueba no: unos zapatos de suela dura sirven para empezar. Si te quedas, te orientamos sobre cuáles comprar."),
            ("¿el claqué es para niños o para adultos?",
             "Para ambos: tenemos grupos juveniles y de adultos. Es de las disciplinas que mejor envejecen — se puede empezar y disfrutar a cualquier edad."),
        ],
    },

    {
        "slug": "classic-o-contemporani",
        "slug_es": "clasico-o-contemporaneo",
        "categoria": "estils",
        "categoria_es": "estilos",
        "data": "2026-06-03",
        "data_ca": "3 de juny de 2026",
        "data_es": "3 de junio de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-classic-contemporani.jpg",
        "img": "blog-classic-contemporani.jpg",
        "img_alt": "Unes sabatilles de mitja punta rosades al costat d'uns mitjons de dansa, sobre el parquet amb llum de tarda",
        "img_alt_es": "Unas zapatillas de media punta rosadas junto a unos calcetines de danza, sobre el parquet con luz de tarde",
        "related_pagines": ["ballet-classic", "dansa-contemporania", "dansa-adults", "horaris"],
        "related_posts": ["triar-estil-dansa-fill"],

        "title": "clàssic o contemporani? les diferències explicades fàcil · escola de dansa cristina colomé",
        "desc": "El ballet clàssic i la dansa contemporània comparteixen base però parlen llengües diferents: forma i codi contra pes i llibertat. Les diferències explicades fàcil per ajudar-te a triar — o a fer tots dos.",
        "h1": "clàssic o contemporani? les diferències explicades fàcil",
        "intro": "És una de les preguntes que més sentim quan algú vol començar: «i quina diferència hi ha?». Aquí la tens sense tecnicismes — i amb un secret final: no cal triar.",
        "excerpt": "Ballet clàssic i dansa contemporània comparteixen base però parlen llengües diferents: forma i codi contra pes i llibertat. Explicat fàcil.",
        "cos": """
<p>Imagina dues maneres de dir la mateixa frase: una recitada amb una dicció perfecta, cada síl·laba al seu lloc; l'altra dita a cau d'orella, amb pauses i respiracions pròpies. Doncs això són, si fa no fa, el <a href="/ballet-classic/">clàssic</a> i el <a href="/dansa-contemporania/">contemporani</a>: la mateixa llengua — el cos — parlada amb dos accents molt diferents.</p>

<h2>el clàssic: la bellesa del codi</h2>
<p>El ballet clàssic és un llenguatge codificat des de fa més de tres segles: les cinc posicions, el vocabulari en francès, la verticalitat, la lleugeresa. La seva gràcia és precisament aquesta: <strong>tothom al món balla el mateix plié</strong>, i la bellesa surt de polir-lo tota la vida. Dona una base tècnica que serveix per a qualsevol altre estil, postura per al dia a dia i una disciplina que ordena el cap.</p>

<h2>el contemporani: el pes i la veritat</h2>
<p>El contemporani va néixer precisament per trencar el codi: ballar descalç, treballar amb el pes del cos en lloc de contra ell, baixar a terra i tornar-se a aixecar, respirar el moviment. Aquí no es busca la forma perfecta sinó <strong>el moviment veritat</strong>: què vol dir aquest gest, d'on surt, cap on va. És físic, és emocional i és profundament creatiu.</p>

<h2>quin em convé?</h2>
<p>Depèn més del caràcter que del cos. Si t'ordena la vida tenir un marc clar i gaudir del detall, el clàssic t'enamorarà. Si el que et crida és expressar, explorar i que cada classe sigui un viatge diferent, el contemporani és casa teva. Els nens solen començar pel clàssic (la base ho agraeix); els adolescents i adults sovint es reparteixen per pura afinitat de pell.</p>

<h2>el secret: es multipliquen</h2>
<p>La resposta que donem més sovint és «per què no tots dos?». El clàssic dona al contemporani la tècnica; el contemporani dona al clàssic la llibertat. Les nostres alumnes que en fan tots dos ho noten en setmanes. Mira els grups de cada disciplina a la <a href="/horaris/">graella d'horaris</a> i, si dubtes, comença amb una <a href="/classe-de-prova-gratuita/">classe de prova gratuïta</a> de cadascun: el cos et dirà quin li toca — o si li toquen tots dos.</p>
""",
        "faqs": [
            ("puc fer contemporani sense haver fet mai clàssic?",
             "Sí. La base clàssica ajuda, però els grups de contemporani treballen la seva pròpia tècnica des de zero: pes, terra, respiració i qualitat de moviment."),
            ("quin és millor per a un nen que comença?",
             "Per als més petits solem recomanar començar pel clàssic o la iniciació a la dansa, perquè construeixen una base que després serveix per a tot. A partir dels 8-10 anys, l'afinitat personal mana."),
            ("es poden combinar les dues disciplines?",
             "És la combinació estrella: el clàssic aporta tècnica i el contemporani, llibertat. Moltes alumnes de l'escola fan totes dues i el progrés es multiplica."),
        ],

        "title_es": "¿clásico o contemporáneo? las diferencias explicadas fácil · escola de dansa cristina colomé",
        "desc_es": "El ballet clásico y la danza contemporánea comparten base pero hablan lenguas distintas: forma y código contra peso y libertad. Las diferencias explicadas fácil para ayudarte a elegir — o a hacer ambos.",
        "h1_es": "¿clásico o contemporáneo? las diferencias explicadas fácil",
        "intro_es": "Es una de las preguntas que más oímos cuando alguien quiere empezar: «¿y qué diferencia hay?». Aquí la tienes sin tecnicismos — y con un secreto final: no hace falta elegir.",
        "excerpt_es": "Ballet clásico y danza contemporánea comparten base pero hablan lenguas distintas: forma y código contra peso y libertad. Explicado fácil.",
        "cos_es": """
<p>Imagina dos maneras de decir la misma frase: una recitada con una dicción perfecta, cada sílaba en su sitio; la otra dicha al oído, con pausas y respiraciones propias. Pues eso son, más o menos, el <a href="/es/ballet-clasico/">clásico</a> y el <a href="/es/danza-contemporanea/">contemporáneo</a>: la misma lengua — el cuerpo — hablada con dos acentos muy distintos.</p>

<h2>el clásico: la belleza del código</h2>
<p>El ballet clásico es un lenguaje codificado desde hace más de tres siglos: las cinco posiciones, el vocabulario en francés, la verticalidad, la ligereza. Su gracia es precisamente esa: <strong>todo el mundo baila el mismo plié</strong>, y la belleza sale de pulirlo toda la vida. Da una base técnica que sirve para cualquier otro estilo, postura para el día a día y una disciplina que ordena la cabeza.</p>

<h2>el contemporáneo: el peso y la verdad</h2>
<p>El contemporáneo nació precisamente para romper el código: bailar descalzo, trabajar con el peso del cuerpo en lugar de contra él, bajar al suelo y volver a levantarse, respirar el movimiento. Aquí no se busca la forma perfecta sino <strong>el movimiento verdad</strong>: qué significa este gesto, de dónde sale, hacia dónde va. Es físico, es emocional y es profundamente creativo.</p>

<h2>¿cuál me conviene?</h2>
<p>Depende más del carácter que del cuerpo. Si te ordena la vida tener un marco claro y disfrutar del detalle, el clásico te enamorará. Si lo que te llama es expresar, explorar y que cada clase sea un viaje distinto, el contemporáneo es tu casa. Los niños suelen empezar por el clásico (la base lo agradece); los adolescentes y adultos a menudo se reparten por pura afinidad de piel.</p>

<h2>el secreto: se multiplican</h2>
<p>La respuesta que damos más a menudo es «¿por qué no ambos?». El clásico da al contemporáneo la técnica; el contemporáneo da al clásico la libertad. Nuestras alumnas que hacen los dos lo notan en semanas. Mira los grupos de cada disciplina en la <a href="/es/horarios/">parrilla de horarios</a> y, si dudas, empieza con una <a href="/es/blog/clase-de-prueba-gratuita/">clase de prueba gratuita</a> de cada uno: el cuerpo te dirá cuál le toca — o si le tocan los dos.</p>
""",
        "faqs_es": [
            ("¿puedo hacer contemporáneo sin haber hecho nunca clásico?",
             "Sí. La base clásica ayuda, pero los grupos de contemporáneo trabajan su propia técnica desde cero: peso, suelo, respiración y calidad de movimiento."),
            ("¿cuál es mejor para un niño que empieza?",
             "Para los más pequeños solemos recomendar empezar por el clásico o la iniciación a la danza, porque construyen una base que luego sirve para todo. A partir de los 8-10 años, manda la afinidad personal."),
            ("¿se pueden combinar las dos disciplinas?",
             "Es la combinación estrella: el clásico aporta técnica y el contemporáneo, libertad. Muchas alumnas de la escuela hacen ambas y el progreso se multiplica."),
        ],
    },
    {
        "slug": "ballar-en-familia",
        "slug_es": "bailar-en-familia",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-05-27",
        "data_ca": "27 de maig de 2026",
        "data_es": "27 de mayo de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-familia.jpg",
        "img": "blog-familia.jpg",
        "img_alt": "Dues bosses de dansa penjades una al costat de l'altra, una de petita i una de gran, amb llum càlida",
        "img_alt_es": "Dos bolsas de danza colgadas una junto a la otra, una pequeña y una grande, con luz cálida",
        "related_pagines": ["dansa-adults", "dansa-infantil", "cos-benestar", "horaris"],
        "related_posts": ["comencar-dansa-adults"],

        "title": "ballar en família: quan mares i filles comparteixen escola · escola de dansa cristina colomé",
        "desc": "A l'escola és cada cop més habitual: la filla fa clàssic a una sala i la mare fa barre o ioga a l'altra. Per què compartir escola (que no classe) enforteix el vincle i simplifica la logística familiar.",
        "h1": "ballar en família: quan mares i filles comparteixen escola",
        "intro": "Una de les escenes que més ens agraden: la nena entra a la seva classe, i la mare — en lloc de fer temps en un banc — entra a la seva. Mateixa hora, mateixa escola, cadascuna al seu món.",
        "excerpt": "La filla fa clàssic a una sala i la mare fa barre o ioga a l'altra. Compartir escola (que no classe) enforteix el vincle i arregla la logística.",
        "cos": """
<p>Fa anys, la imatge típica de la porta de l'escola era una filera de mares i pares esperant amb el mòbil a la mà. Cada cop més, aquella espera s'ha convertit en una altra cosa: <strong>la seva pròpia classe</strong>. Mentre la petita fa clàssic infantil, la mare fa <a href="/cos-benestar/">barre o ioga</a>; mentre l'adolescent sua al hip-hop, el pare descobreix que el claqué era el seu ball secret.</p>

<h2>la logística que es resol sola</h2>
<p>El primer avantatge és pràctic i és enorme: <strong>un sol viatge, dues activitats</strong>. La conciliació és el gran enemic de l'exercici dels adults — «no tinc temps» quasi sempre vol dir «no tinc una hora que quadri». Si la teva hora quadra exactament amb la de la teva filla, l'excusa s'evapora. Mireu junts la <a href="/horaris/">graella</a>: hi ha més coincidències de les que us penseu.</p>

<h2>el vincle que es crea</h2>
<p>Hi ha alguna cosa especial a compartir el camí de l'escola: sortir de casa amb les bosses de dansa, comentar la classe de tornada, entendre de què parla l'altra quan diu que avui «li ha sortit el gir». No cal ballar juntes ni fer el mateix estil — de fet, gairebé millor que no: <strong>cadascuna té el seu espai</strong>, i el que es comparteix és la passió, no la sala.</p>

<h2>l'exemple silenciós</h2>
<p>I hi ha un efecte més profund que veiem sovint: quan una nena veu que la seva mare també va a classe, també s'equivoca, també repeteix i també progressa, el missatge que rep no és cap sermó — és un exemple. L'esforç, la constància i el gust per aprendre <strong>es transmeten millor ballant que dient-los</strong>.</p>

<h2>com quadrar-ho</h2>
<p>Digueu-nos els horaris de la criatura i us busquem les classes d'adults que hi encaixen — o al revés. I si fa temps que no us moveu, cap por: els grups d'<a href="/dansa-adults/">adults</a> tenen nivells d'iniciació de veritat, i la primera classe, com sempre, <a href="/classe-de-prova-gratuita/">és gratuïta</a>. Potser d'aquí a uns mesos, la conversa del sopar serà quina de les dues té el festival més a punt.</p>
""",
        "faqs": [
            ("hi ha classes d'adults a la mateixa hora que les infantils?",
             "Moltes: la graella està pensada perquè les franges de tarda tinguin alhora grups infantils i d'adults (barre, ioga, clàssic, contemporani...). Digueu-nos l'horari del vostre fill i us busquem la coincidència."),
            ("mare i filla poden anar a la mateixa classe?",
             "Els grups van per edats, així que normalment cadascuna té el seu. És part de la gràcia: compartir escola i passió, cadascuna al seu espai."),
            ("fa anys que no faig exercici: puc començar igualment?",
             "I tant. Els grups d'adults d'iniciació comencen de zero de debò, i disciplines com el barre o el ioga són una porta d'entrada amable per a qualsevol condició física."),
        ],

        "title_es": "bailar en familia: cuando madres e hijas comparten escuela · escola de dansa cristina colomé",
        "desc_es": "En la escuela es cada vez más habitual: la hija hace clásico en una sala y la madre hace barre o yoga en la otra. Por qué compartir escuela (que no clase) refuerza el vínculo y simplifica la logística familiar.",
        "h1_es": "bailar en familia: cuando madres e hijas comparten escuela",
        "intro_es": "Una de las escenas que más nos gustan: la niña entra a su clase, y la madre — en lugar de hacer tiempo en un banco — entra a la suya. Misma hora, misma escuela, cada una en su mundo.",
        "excerpt_es": "La hija hace clásico en una sala y la madre hace barre o yoga en la otra. Compartir escuela (que no clase) refuerza el vínculo y arregla la logística.",
        "cos_es": """
<p>Hace años, la imagen típica de la puerta de la escuela era una fila de madres y padres esperando con el móvil en la mano. Cada vez más, esa espera se ha convertido en otra cosa: <strong>su propia clase</strong>. Mientras la pequeña hace clásico infantil, la madre hace <a href="/es/cuerpo-bienestar/">barre o yoga</a>; mientras el adolescente suda en el hip-hop, el padre descubre que el claqué era su baile secreto.</p>

<h2>la logística que se resuelve sola</h2>
<p>La primera ventaja es práctica y es enorme: <strong>un solo viaje, dos actividades</strong>. La conciliación es el gran enemigo del ejercicio de los adultos — «no tengo tiempo» casi siempre significa «no tengo una hora que cuadre». Si tu hora cuadra exactamente con la de tu hija, la excusa se evapora. Mirad juntos la <a href="/es/horarios/">parrilla</a>: hay más coincidencias de las que pensáis.</p>

<h2>el vínculo que se crea</h2>
<p>Hay algo especial en compartir el camino de la escuela: salir de casa con las bolsas de danza, comentar la clase a la vuelta, entender de qué habla la otra cuando dice que hoy «le ha salido el giro». No hace falta bailar juntas ni hacer el mismo estilo — de hecho, casi mejor que no: <strong>cada una tiene su espacio</strong>, y lo que se comparte es la pasión, no la sala.</p>

<h2>el ejemplo silencioso</h2>
<p>Y hay un efecto más profundo que vemos a menudo: cuando una niña ve que su madre también va a clase, también se equivoca, también repite y también progresa, el mensaje que recibe no es ningún sermón — es un ejemplo. El esfuerzo, la constancia y el gusto por aprender <strong>se transmiten mejor bailando que diciéndolos</strong>.</p>

<h2>cómo cuadrarlo</h2>
<p>Decidnos los horarios de la criatura y os buscamos las clases de adultos que encajan — o al revés. Y si hace tiempo que no os movéis, sin miedo: los grupos de <a href="/es/danza-adultos/">adultos</a> tienen niveles de iniciación de verdad, y la primera clase, como siempre, <a href="/es/blog/clase-de-prueba-gratuita/">es gratuita</a>. Quizá dentro de unos meses, la conversación de la cena sea cuál de las dos tiene el festival más a punto.</p>
""",
        "faqs_es": [
            ("¿hay clases de adultos a la misma hora que las infantiles?",
             "Muchas: la parrilla está pensada para que las franjas de tarde tengan a la vez grupos infantiles y de adultos (barre, yoga, clásico, contemporáneo...). Decidnos el horario de vuestro hijo y os buscamos la coincidencia."),
            ("¿madre e hija pueden ir a la misma clase?",
             "Los grupos van por edades, así que normalmente cada una tiene el suyo. Es parte de la gracia: compartir escuela y pasión, cada una en su espacio."),
            ("hace años que no hago ejercicio: ¿puedo empezar igualmente?",
             "Por supuesto. Los grupos de adultos de iniciación empiezan de cero de verdad, y disciplinas como el barre o el yoga son una puerta de entrada amable para cualquier condición física."),
        ],
    },
    {
        "slug": "musica-a-les-classes",
        "slug_es": "musica-en-las-clases",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-05-20",
        "data_ca": "20 de maig de 2026",
        "data_es": "20 de mayo de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-musica.jpg",
        "img": "blog-musica.jpg",
        "img_alt": "Un altaveu antic i una llibreta de notes sobre una tauleta de fusta en una sala de dansa",
        "img_alt_es": "Un altavoz antiguo y una libreta de notas sobre una mesita de madera en una sala de danza",
        "related_pagines": ["ballet-classic", "hip-hop", "dansa-contemporania", "horaris"],
        "related_posts": ["dansa-i-timidesa"],

        "title": "la música de les classes: com la triem i per què importa tant · escola de dansa cristina colomé",
        "desc": "Del piano del clàssic a les llistes que demanen els adolescents de hip-hop: com es tria la música de cada classe de dansa, i per què és la meitat invisible de l'aprenentatge.",
        "h1": "la música de les classes: com la triem i per què importa tant",
        "intro": "Si preguntes a una alumna què recorda de fa tres cursos, potser no recordarà la coreografia — però taral·lejarà la cançó. La música és la meitat invisible de cada classe, i triar-la és un ofici.",
        "excerpt": "Del piano del clàssic a les llistes que demanen els adolescents: com es tria la música de cada classe i per què és la meitat de l'aprenentatge.",
        "cos": """
<p>Hi ha una feina que les professores fan cada setmana i que gairebé ningú veu: <strong>triar la música</strong>. Sembla un detall, però qui es dedica a ensenyar dansa sap que una classe amb la música ben triada funciona sola — i una amb la música equivocada costa el doble.</p>

<h2>al clàssic, la música és estructura</h2>
<p>Una classe de <a href="/ballet-classic/">ballet clàssic</a> té una arquitectura musical mil·limetrada: cada exercici demana el seu tempo, el seu compàs i el seu caràcter — un plié no respira igual que un gran allegro. Per això el repertori de piano per a classe és tot un gènere en ell mateix, i per això les alumnes de clàssic acaben tenint, sense adonar-se'n, una cultura musical clàssica que ja voldrien molts adults.</p>

<h2>al contemporani, la música és paisatge</h2>
<p>Al <a href="/dansa-contemporania/">contemporani</a> la música fa una altra feina: crea l'atmosfera on el moviment pren sentit. Un dia és un piano minimalista, l'altre una electrònica ambient, l'altre el silenci i la pròpia respiració. Aprendre a ballar «dins» de músiques tan diferents és part de la formació: el cos aprèn a escoltar.</p>

<h2>a les urbanes, la música és el pacte</h2>
<p>I al <a href="/hip-hop/">hip-hop</a> i al k-pop passa una cosa preciosa: la música és el pacte entre professora i alumnes. Les professores escolten què porta el grup — la cançó del moment, l'artista que els té el cap girat — i ho converteixen en coreografia. Quan un adolescent balla la seva música, la classe deixa de ser una activitat i passa a ser <strong>el seu moment de la setmana</strong>.</p>

<h2>un consell per a casa</h2>
<p>Si el teu fill o filla surt de classe cantussejant, aprofita-ho: pregunta-li quina cançó és, poseu-la a casa, deixa que t'ensenyi els passos. Aquell moment de cuina i sofà és or: consolida el que ha après i us regala una estona junts. I si la cançó se t'enganxa a tu també... ja saps <a href="/horaris/">on som</a>.</p>
""",
        "faqs": [
            ("les classes de clàssic es fan amb música en directe?",
             "Treballem amb el gran repertori de piano per a classe de ballet, triat exercici a exercici. L'estructura musical del clàssic és part fonamental del que s'aprèn."),
            ("els alumnes poden demanar cançons?",
             "A les disciplines urbanes, i tant: les professores escolten què porta el grup i ho incorporen a les coreografies. És part del que fa que les classes enganxin."),
            ("la dansa ajuda a l'educació musical?",
             "Moltíssim: ritme, compàs, fraseig, estils... Ballar és escoltar amb tot el cos, i aquesta escolta es queda per sempre."),
        ],

        "title_es": "la música de las clases: cómo la elegimos y por qué importa tanto · escola de dansa cristina colomé",
        "desc_es": "Del piano del clásico a las listas que piden los adolescentes de hip-hop: cómo se elige la música de cada clase de danza, y por qué es la mitad invisible del aprendizaje.",
        "h1_es": "la música de las clases: cómo la elegimos y por qué importa tanto",
        "intro_es": "Si preguntas a una alumna qué recuerda de hace tres cursos, quizá no recuerde la coreografía — pero tarareará la canción. La música es la mitad invisible de cada clase, y elegirla es un oficio.",
        "excerpt_es": "Del piano del clásico a las listas que piden los adolescentes: cómo se elige la música de cada clase y por qué es la mitad del aprendizaje.",
        "cos_es": """
<p>Hay un trabajo que las profesoras hacen cada semana y que casi nadie ve: <strong>elegir la música</strong>. Parece un detalle, pero quien se dedica a enseñar danza sabe que una clase con la música bien elegida funciona sola — y una con la música equivocada cuesta el doble.</p>

<h2>en el clásico, la música es estructura</h2>
<p>Una clase de <a href="/es/ballet-clasico/">ballet clásico</a> tiene una arquitectura musical milimetrada: cada ejercicio pide su tempo, su compás y su carácter — un plié no respira igual que un gran allegro. Por eso el repertorio de piano para clase es todo un género en sí mismo, y por eso las alumnas de clásico acaban teniendo, sin darse cuenta, una cultura musical clásica que ya quisieran muchos adultos.</p>

<h2>en el contemporáneo, la música es paisaje</h2>
<p>En el <a href="/es/danza-contemporanea/">contemporáneo</a> la música hace otro trabajo: crea la atmósfera donde el movimiento cobra sentido. Un día es un piano minimalista, otro una electrónica ambient, otro el silencio y la propia respiración. Aprender a bailar «dentro» de músicas tan distintas es parte de la formación: el cuerpo aprende a escuchar.</p>

<h2>en las urbanas, la música es el pacto</h2>
<p>Y en el <a href="/es/hip-hop/">hip-hop</a> y el k-pop pasa algo precioso: la música es el pacto entre profesora y alumnos. Las profesoras escuchan qué trae el grupo — la canción del momento, el artista que les tiene la cabeza girada — y lo convierten en coreografía. Cuando un adolescente baila su música, la clase deja de ser una actividad y pasa a ser <strong>su momento de la semana</strong>.</p>

<h2>un consejo para casa</h2>
<p>Si tu hijo o hija sale de clase canturreando, aprovéchalo: pregúntale qué canción es, ponedla en casa, deja que te enseñe los pasos. Ese momento de cocina y sofá es oro: consolida lo aprendido y os regala un rato juntos. Y si la canción se te pega a ti también... ya sabes <a href="/es/horarios/">dónde estamos</a>.</p>
""",
        "faqs_es": [
            ("¿las clases de clásico se hacen con música en directo?",
             "Trabajamos con el gran repertorio de piano para clase de ballet, elegido ejercicio a ejercicio. La estructura musical del clásico es parte fundamental de lo que se aprende."),
            ("¿los alumnos pueden pedir canciones?",
             "En las disciplinas urbanas, por supuesto: las profesoras escuchan qué trae el grupo y lo incorporan a las coreografías. Es parte de lo que hace que las clases enganchen."),
            ("¿la danza ayuda a la educación musical?",
             "Muchísimo: ritmo, compás, fraseo, estilos... Bailar es escuchar con todo el cuerpo, y esa escucha se queda para siempre."),
        ],
    },

    {
        "slug": "dansa-oriental-forca-elegancia",
        "slug_es": "danza-oriental-fuerza-elegancia",
        "categoria": "estils",
        "categoria_es": "estilos",
        "data": "2026-05-13",
        "data_ca": "13 de maig de 2026",
        "data_es": "13 de mayo de 2026",
        "minuts": 4,
        "nom_wa": "dansa del ventre",
        "nom_wa_es": "danza del vientre",
        "og": "blog-oriental.jpg",
        "img": "blog-oriental.jpg",
        "img_alt": "Un mocador de dansa oriental amb monedes daurades sobre el parquet, amb llum càlida de tarda",
        "img_alt_es": "Un pañuelo de danza oriental con monedas doradas sobre el parquet, con luz cálida de tarde",
        "related_pagines": ["dansa-oriental", "dansa-adults", "cos-benestar", "horaris"],
        "related_posts": ["comencar-dansa-adults"],

        "title": "dansa oriental: la força que s'amaga darrere l'elegància · escola de dansa cristina colomé",
        "desc": "La dansa oriental (dansa del ventre) és una de les disciplines més completes per a adults: tècnica mil·lenària, treball profund del centre del cos i una relació amb el propi cos que canvia la mirada.",
        "h1": "dansa oriental: la força que s'amaga darrere l'elegància",
        "intro": "De fora es veu elegància: braços que onegen, malucs que dibuixen cercles, el dring de les monedes. De dins, és una de les disciplines més exigents i alliberadores que tenim a l'escola.",
        "excerpt": "La dansa oriental és de les disciplines més completes per a adults: tècnica mil·lenària, treball profund del centre i una nova relació amb el cos.",
        "cos": """
<p>Poques disciplines arrosseguen tants malentesos com la <a href="/dansa-oriental/">dansa oriental</a>. I poques sorprenen tant quan es prova: darrere de l'estètica hi ha una tècnica mil·lenària, un treball físic profund i — potser el més valuós — una manera nova de mirar-se el propi cos.</p>

<h2>una tècnica de precisió</h2>
<p>La dansa oriental es construeix sobre els <strong>aïllaments</strong>: moure el maluc sense moure les espatlles, dibuixar un vuit amb la cintura mentre els braços fan una altra frase. És feina de precisió quirúrgica que demana anys — i que engancha precisament per això: sempre hi ha una capa més per polir. Els shimmies, els cercles, les ondulacions... cada element té la seva escola i la seva història.</p>

<h2>el centre del cos, despert</h2>
<p>Físicament és un entrenament esplèndid del <strong>core</strong>: tota la musculatura profunda de l'abdomen, l'esquena i el sòl pelvià treballa sense parar, però sense impacte. Per això és una disciplina tan agraïda a totes les edats adultes: enforteix allà on més ho necessitem, millora la postura i desperta zones del cos que la vida de cadira adorm.</p>

<h2>ballar per a una mateixa</h2>
<p>I hi ha l'efecte que les alumnes veteranes citen sempre: la dansa oriental <strong>reconcilia amb el propi cos</strong>. No hi ha un cos ideal per ballar-la — hi ha el teu, i la dansa el celebra tal com és. En un grup de dones de totes les edats i totes les formes, ballant una tradició que fa segles que celebra el moviment femení, passa una cosa difícil d'explicar i fàcil de sentir: una es fa amiga del mirall.</p>

<h2>vine a provar-ho</h2>
<p>Els grups d'oriental de l'escola van per nivells, del zero absolut a l'avançat, i el mocador de monedes — que fa tanta patxoca — te'l deixem el primer dia. <a href="/classe-de-prova-gratuita/">La primera classe és gratuïta</a>: vine amb roba còmoda i deixa que els malucs facin la resta. Els horaris, com sempre, <a href="/horaris/">a la graella</a>.</p>
""",
        "faqs": [
            ("cal tenir bona forma física per començar dansa oriental?",
             "No: és una disciplina sense impacte que s'adapta a qualsevol punt de partida. La força del centre del cos es construeix a poc a poc, classe a classe."),
            ("la dansa oriental és només per a dones?",
             "Històricament la ballen persones de tots els gèneres i els nostres grups estan oberts a tothom. La majoria d'alumnes són dones, però la porta és oberta."),
            ("què em cal per a la primera classe?",
             "Roba còmoda que et deixi veure la cintura (o no, com et sentis bé) i peus descalços o mitjons. El mocador de monedes te'l deixem nosaltres."),
        ],

        "title_es": "danza oriental: la fuerza que se esconde tras la elegancia · escola de dansa cristina colomé",
        "desc_es": "La danza oriental (danza del vientre) es una de las disciplinas más completas para adultos: técnica milenaria, trabajo profundo del centro del cuerpo y una relación con el propio cuerpo que cambia la mirada.",
        "h1_es": "danza oriental: la fuerza que se esconde tras la elegancia",
        "intro_es": "Desde fuera se ve elegancia: brazos que ondean, caderas que dibujan círculos, el tintineo de las monedas. Desde dentro, es una de las disciplinas más exigentes y liberadoras que tenemos en la escuela.",
        "excerpt_es": "La danza oriental es de las disciplinas más completas para adultos: técnica milenaria, trabajo profundo del centro y una nueva relación con el cuerpo.",
        "cos_es": """
<p>Pocas disciplinas arrastran tantos malentendidos como la <a href="/es/danza-oriental/">danza oriental</a>. Y pocas sorprenden tanto cuando se prueba: detrás de la estética hay una técnica milenaria, un trabajo físico profundo y — quizá lo más valioso — una manera nueva de mirarse el propio cuerpo.</p>

<h2>una técnica de precisión</h2>
<p>La danza oriental se construye sobre los <strong>aislamientos</strong>: mover la cadera sin mover los hombros, dibujar un ocho con la cintura mientras los brazos hacen otra frase. Es trabajo de precisión quirúrgica que pide años — y que engancha precisamente por eso: siempre hay una capa más que pulir. Los shimmies, los círculos, las ondulaciones... cada elemento tiene su escuela y su historia.</p>

<h2>el centro del cuerpo, despierto</h2>
<p>Físicamente es un entrenamiento espléndido del <strong>core</strong>: toda la musculatura profunda del abdomen, la espalda y el suelo pélvico trabaja sin parar, pero sin impacto. Por eso es una disciplina tan agradecida a todas las edades adultas: fortalece donde más lo necesitamos, mejora la postura y despierta zonas del cuerpo que la vida de silla adormece.</p>

<h2>bailar para una misma</h2>
<p>Y está el efecto que las alumnas veteranas citan siempre: la danza oriental <strong>reconcilia con el propio cuerpo</strong>. No hay un cuerpo ideal para bailarla — está el tuyo, y la danza lo celebra tal como es. En un grupo de mujeres de todas las edades y todas las formas, bailando una tradición que lleva siglos celebrando el movimiento femenino, pasa algo difícil de explicar y fácil de sentir: una se hace amiga del espejo.</p>

<h2>ven a probarlo</h2>
<p>Los grupos de oriental de la escuela van por niveles, del cero absoluto al avanzado, y el pañuelo de monedas — que luce tanto — te lo dejamos el primer día. <a href="/es/blog/clase-de-prueba-gratuita/">La primera clase es gratuita</a>: ven con ropa cómoda y deja que las caderas hagan el resto. Los horarios, como siempre, <a href="/es/horarios/">en la parrilla</a>.</p>
""",
        "faqs_es": [
            ("¿hace falta buena forma física para empezar danza oriental?",
             "No: es una disciplina sin impacto que se adapta a cualquier punto de partida. La fuerza del centro del cuerpo se construye poco a poco, clase a clase."),
            ("¿la danza oriental es solo para mujeres?",
             "Históricamente la bailan personas de todos los géneros y nuestros grupos están abiertos a todo el mundo. La mayoría de alumnas son mujeres, pero la puerta está abierta."),
            ("¿qué necesito para la primera clase?",
             "Ropa cómoda que te deje ver la cintura (o no, como te sientas bien) y pies descalzos o calcetines. El pañuelo de monedas te lo dejamos nosotras."),
        ],
    },
    {
        "slug": "festival-fi-de-curs",
        "slug_es": "festival-fin-de-curso",
        "categoria": "l'escola",
        "categoria_es": "la escuela",
        "data": "2026-05-06",
        "data_ca": "6 de maig de 2026",
        "data_es": "6 de mayo de 2026",
        "minuts": 4,
        "nom_wa": "dansa",
        "nom_wa_es": "danza",
        "og": "blog-festival.jpg",
        "img": "blog-festival.jpg",
        "img_alt": "Un feix de llum d'escenari il·luminant el terra de fusta d'un teatre buit abans de la funció",
        "img_alt_es": "Un haz de luz de escenario iluminando el suelo de madera de un teatro vacío antes de la función",
        "related_pagines": ["formacio-escenica", "dansa-infantil", "musical-interpretacio", "horaris"],
        "related_posts": ["dansa-i-timidesa", "historia-escola-25-anys"],

        "title": "per què el festival de fi de curs és el cor de l'escola · escola de dansa cristina colomé",
        "desc": "El festival de fi de curs no és una exhibició: és el moment on tot l'aprenentatge de l'any pren sentit. Nervis, teló, famílies i el creixement que només dona un escenari de veritat.",
        "h1": "per què el festival de fi de curs és el cor de l'escola",
        "intro": "Cada juny, quan s'apaguen els llums del teatre i s'obre el teló, passa la cosa més important del curs. I no és la coreografia: és el que el escenari fa amb cada alumna.",
        "excerpt": "El festival no és una exhibició: és el moment on l'aprenentatge de l'any pren sentit. Nervis, teló i el creixement que només dona un escenari.",
        "cos": """
<p>Si ens preguntes quin dia de l'any resumeix millor què és l'escola, no et direm cap dimarts de classe: et direm <strong>el dia del festival</strong>. El teatre ple, les bambolines nervioses, les professores repassant entrades i sortides, i tres-centes famílies esperant que s'obri el teló.</p>

<h2>l'escenari ho canvia tot</h2>
<p>Es pot assajar una coreografia cent vegades a la sala, però l'escenari és una altra dimensió: els llums que t'encenen la pell, el públic que respira a les fosques, aquell silenci d'un segon abans que comenci la música. <strong>Cap classe pot ensenyar el que ensenya aquest moment</strong>: sortir, fer-ho, i descobrir que en eres capaç.</p>

<h2>els nervis són part del regal</h2>
<p>Sempre hi ha famílies que pateixen pels nervis de les criatures. El nostre missatge: els nervis són exactament el que hem vingut a treballar. Aprendre que la por escènica es transforma en energia, que l'equip et sosté i que després del teló hi ha l'aplaudiment — això és una lliçó de vida disfressada de ballet. Les alumnes de <a href="/formacio-escenica/">formació escènica</a> ho saben bé: l'escenari s'entrena, com tot.</p>

<h2>la feina invisible</h2>
<p>Un festival són mesos de feina que no es veu: triar músiques, cosir vestuaris, quadrar entrades de dues-centes criatures perquè tot flueixi, assajos generals on tot surt malament perquè el dia bo surti tot bé. És l'obra col·lectiva de tota l'escola — professores, famílies i alumnes — i per això el vincle que crea dura anys.</p>

<h2>un motiu per començar al setembre</h2>
<p>Si esteu dubtant si apuntar el vostre fill o filla, penseu-ho així: <strong>el curs és un viatge que acaba en un escenari</strong>. Començar al setembre vol dir tenir tot l'any per preparar aquell moment. I creieu-nos: la cara d'una nena saludant al públic amb el seu grup és de les coses que una família no oblida. <a href="/horaris/">Els horaris són aquí</a> — el teló del juny vinent, també.</p>
""",
        "faqs": [
            ("tots els alumnes participen al festival?",
             "Tots els grups hi tenen el seu número, dels més petits als adults. Participar és molt recomanable — és el gran moment del curs — però sempre es parla amb cada família."),
            ("i si al meu fill li fa por l'escenari?",
             "És normal i és part del procés: els nervis es treballen durant el curs i el grup sosté molt. La immensa majoria de pors escèniques es fonen quan s'obre el teló — i la sensació d'haver-ho fet val un tresor."),
            ("les famílies poden veure el festival?",
             "És clar: el festival es fa en un teatre amb entrades per a les famílies. És el dia que l'escola surt de Craywinckel i es planta davant del seu públic."),
        ],

        "title_es": "por qué el festival de fin de curso es el corazón de la escuela · escola de dansa cristina colomé",
        "desc_es": "El festival de fin de curso no es una exhibición: es el momento donde todo el aprendizaje del año cobra sentido. Nervios, telón, familias y el crecimiento que solo da un escenario de verdad.",
        "h1_es": "por qué el festival de fin de curso es el corazón de la escuela",
        "intro_es": "Cada junio, cuando se apagan las luces del teatro y se abre el telón, pasa lo más importante del curso. Y no es la coreografía: es lo que el escenario hace con cada alumna.",
        "excerpt_es": "El festival no es una exhibición: es el momento donde el aprendizaje del año cobra sentido. Nervios, telón y el crecimiento que solo da un escenario.",
        "cos_es": """
<p>Si nos preguntas qué día del año resume mejor qué es la escuela, no te diremos ningún martes de clase: te diremos <strong>el día del festival</strong>. El teatro lleno, los bastidores nerviosos, las profesoras repasando entradas y salidas, y trescientas familias esperando que se abra el telón.</p>

<h2>el escenario lo cambia todo</h2>
<p>Se puede ensayar una coreografía cien veces en la sala, pero el escenario es otra dimensión: las luces que te encienden la piel, el público que respira en la oscuridad, ese silencio de un segundo antes de que empiece la música. <strong>Ninguna clase puede enseñar lo que enseña ese momento</strong>: salir, hacerlo, y descubrir que eras capaz.</p>

<h2>los nervios son parte del regalo</h2>
<p>Siempre hay familias que sufren por los nervios de las criaturas. Nuestro mensaje: los nervios son exactamente lo que hemos venido a trabajar. Aprender que el miedo escénico se transforma en energía, que el equipo te sostiene y que después del telón está el aplauso — eso es una lección de vida disfrazada de ballet. Las alumnas de <a href="/es/formacion-escenica/">formación escénica</a> lo saben bien: el escenario se entrena, como todo.</p>

<h2>el trabajo invisible</h2>
<p>Un festival son meses de trabajo que no se ve: elegir músicas, coser vestuarios, cuadrar entradas de doscientas criaturas para que todo fluya, ensayos generales donde todo sale mal para que el día bueno salga todo bien. Es la obra colectiva de toda la escuela — profesoras, familias y alumnas — y por eso el vínculo que crea dura años.</p>

<h2>un motivo para empezar en septiembre</h2>
<p>Si estáis dudando si apuntar a vuestro hijo o hija, pensadlo así: <strong>el curso es un viaje que termina en un escenario</strong>. Empezar en septiembre significa tener todo el año para preparar ese momento. Y creednos: la cara de una niña saludando al público con su grupo es de las cosas que una familia no olvida. <a href="/es/horarios/">Los horarios están aquí</a> — el telón del próximo junio, también.</p>
""",
        "faqs_es": [
            ("¿todos los alumnos participan en el festival?",
             "Todos los grupos tienen su número, de los más pequeños a los adultos. Participar es muy recomendable — es el gran momento del curso — pero siempre se habla con cada familia."),
            ("¿y si a mi hijo le da miedo el escenario?",
             "Es normal y es parte del proceso: los nervios se trabajan durante el curso y el grupo sostiene mucho. La inmensa mayoría de miedos escénicos se funden cuando se abre el telón — y la sensación de haberlo hecho vale un tesoro."),
            ("¿las familias pueden ver el festival?",
             "Claro: el festival se hace en un teatro con entradas para las familias. Es el día que la escuela sale de Craywinckel y se planta ante su público."),
        ],
    },

    {
        "slug": "ballar-als-50-i-mes",
        "slug_es": "bailar-a-los-50-y-mas",
        "categoria": "adults",
        "categoria_es": "adultos",
        "data": "2026-04-29",
        "data_ca": "29 d'abril de 2026",
        "data_es": "29 de abril de 2026",
        "minuts": 4,
        "nom_wa": "dansa per a adults",
        "nom_wa_es": "danza para adultos",
        "og": "blog-adults-grans.jpg",
        "img": "blog-adults-grans.jpg",
        "img_alt": "Unes sabatilles de dansa clares amb una tovallola i una ampolla d'aigua sobre un banc de fusta",
        "img_alt_es": "Unas zapatillas de danza claras con una toalla y una botella de agua sobre un banco de madera",
        "related_pagines": ["dansa-adults", "cos-benestar", "ball-espanyol", "horaris"],
        "related_posts": ["comencar-dansa-adults", "barre-entrenament-ballet"],

        "title": "ballar als 50, als 60 i més enllà: el cos ho agraeix · escola de dansa cristina colomé",
        "desc": "La dansa és de les millors activitats físiques a partir dels 50: memòria, equilibri, força i vida social en una sola hora. Per què mai no és tard i quines disciplines van millor per començar.",
        "h1": "ballar als 50, als 60 i més enllà: el cos ho agraeix",
        "intro": "Hi ha una idea que voldríem esborrar per sempre: que la dansa és cosa de joves. A les nostres sales hi ha alumnes que van començar amb els cabells ja blancs — i són de les més constants de l'escola.",
        "excerpt": "La dansa és de les millors activitats a partir dels 50: memòria, equilibri, força i vida social en una sola hora. Mai no és tard.",
        "cos": """
<p>«Jo ja no tinc edat.» Si ens donessin un euro per cada cop que ho hem sentit a recepció — i un altre per cada cop que la mateixa persona, tres mesos després, surt de classe radiant — tindríem el parquet fet d'or. La veritat, avalada per l'experiència i per la ciència: <strong>a partir dels 50, ballar és de les millors coses que pots fer pel teu cos i pel teu cap</strong>.</p>

<h2>el que diu la ciència</h2>
<p>Ballar és de les poques activitats que entrena el cos i el cervell alhora: memòria (les coreografies), coordinació, equilibri, ritme i decisió en temps real. Els estudis que comparen activitats en persones grans donen a la dansa un lloc d'honor precisament per aquesta combinació — i els metges la recomanen cada cop més per mantenir l'agilitat física i mental.</p>

<h2>el que diu l'experiència</h2>
<p>El que veiem nosaltres cada setmana: millora la postura en poques setmanes, els equilibris guanyen seguretat, l'esquena es queixa menys i — potser el més important — <strong>la setmana té una cita fixa amb una mateixa</strong>. La classe és una hora on el cap només pot ser allà: comptant, escoltant, ballant. La millor desconnexió que existeix.</p>

<h2>per on començar</h2>
<p>Depèn del que et demani el cos. El <a href="/cos-benestar/">barre i el ioga</a> són portes d'entrada suaus i molt completes; el <a href="/ball-espanyol/">ball espanyol</a> i la dansa oriental tenen una riquesa i una alegria que enganxen; i el clàssic per a adults — sí, es pot començar clàssic de gran — és elegància pura a foc lent. Tots els grups d'<a href="/dansa-adults/">adults</a> tenen nivells d'iniciació on ningú no espera que sàpigues res.</p>

<h2>l'única condició</h2>
<p>Venir. La resta — el nivell, la forma, la vergonya dels primers dies — es resol sol amb les setmanes. La primera classe <a href="/classe-de-prova-gratuita/">és gratuïta</a> i sense compromís, i els horaris de matí i vespre són a la <a href="/horaris/">graella</a>. El cos que tens és el cos perfecte per començar: és l'únic que necessites portar.</p>
""",
        "faqs": [
            ("puc començar a ballar dels 50 en amunt sense haver ballat mai?",
             "I tant: tenim alumnes que van començar de zero passats els 50 i els 60. Els grups d'iniciació per a adults comencen des del principi de debò, i el progrés arriba abans del que et penses."),
            ("quina disciplina va millor per començar de gran?",
             "El barre i el ioga són les portes més suaus; el ball espanyol, l'oriental i el clàssic per a adults, les més riques en tècnica i tradició. La millor és la que et faci venir de gust tornar."),
            ("i si tinc alguna limitació física?",
             "Explica-nos-la i adaptem: les professores ajusten exercicis contínuament. La dansa ben ensenyada suma salut, mai en resta."),
        ],

        "title_es": "bailar a los 50, a los 60 y más allá: el cuerpo lo agradece · escola de dansa cristina colomé",
        "desc_es": "La danza es de las mejores actividades físicas a partir de los 50: memoria, equilibrio, fuerza y vida social en una sola hora. Por qué nunca es tarde y qué disciplinas van mejor para empezar.",
        "h1_es": "bailar a los 50, a los 60 y más allá: el cuerpo lo agradece",
        "intro_es": "Hay una idea que querríamos borrar para siempre: que la danza es cosa de jóvenes. En nuestras salas hay alumnas que empezaron con el pelo ya blanco — y son de las más constantes de la escuela.",
        "excerpt_es": "La danza es de las mejores actividades a partir de los 50: memoria, equilibrio, fuerza y vida social en una sola hora. Nunca es tarde.",
        "cos_es": """
<p>«Yo ya no tengo edad.» Si nos dieran un euro por cada vez que lo hemos oído en recepción — y otro por cada vez que la misma persona, tres meses después, sale de clase radiante — tendríamos el parquet hecho de oro. La verdad, avalada por la experiencia y por la ciencia: <strong>a partir de los 50, bailar es de las mejores cosas que puedes hacer por tu cuerpo y por tu cabeza</strong>.</p>

<h2>lo que dice la ciencia</h2>
<p>Bailar es de las pocas actividades que entrena el cuerpo y el cerebro a la vez: memoria (las coreografías), coordinación, equilibrio, ritmo y decisión en tiempo real. Los estudios que comparan actividades en personas mayores dan a la danza un lugar de honor precisamente por esta combinación — y los médicos la recomiendan cada vez más para mantener la agilidad física y mental.</p>

<h2>lo que dice la experiencia</h2>
<p>Lo que vemos nosotras cada semana: mejora la postura en pocas semanas, los equilibrios ganan seguridad, la espalda se queja menos y — quizá lo más importante — <strong>la semana tiene una cita fija con una misma</strong>. La clase es una hora donde la cabeza solo puede estar allí: contando, escuchando, bailando. La mejor desconexión que existe.</p>

<h2>por dónde empezar</h2>
<p>Depende de lo que te pida el cuerpo. El <a href="/es/cuerpo-bienestar/">barre y el yoga</a> son puertas de entrada suaves y muy completas; el <a href="/es/baile-espanol/">baile español</a> y la danza oriental tienen una riqueza y una alegría que enganchan; y el clásico para adultos — sí, se puede empezar clásico de mayor — es elegancia pura a fuego lento. Todos los grupos de <a href="/es/danza-adultos/">adultos</a> tienen niveles de iniciación donde nadie espera que sepas nada.</p>

<h2>la única condición</h2>
<p>Venir. El resto — el nivel, la forma, la vergüenza de los primeros días — se resuelve solo con las semanas. La primera clase <a href="/es/blog/clase-de-prueba-gratuita/">es gratuita</a> y sin compromiso, y los horarios de mañana y tarde están en la <a href="/es/horarios/">parrilla</a>. El cuerpo que tienes es el cuerpo perfecto para empezar: es lo único que necesitas traer.</p>
""",
        "faqs_es": [
            ("¿puedo empezar a bailar de los 50 en adelante sin haber bailado nunca?",
             "Por supuesto: tenemos alumnas que empezaron de cero pasados los 50 y los 60. Los grupos de iniciación para adultos empiezan desde el principio de verdad, y el progreso llega antes de lo que crees."),
            ("¿qué disciplina va mejor para empezar de mayor?",
             "El barre y el yoga son las puertas más suaves; el baile español, la oriental y el clásico para adultos, las más ricas en técnica y tradición. La mejor es la que te dé ganas de volver."),
            ("¿y si tengo alguna limitación física?",
             "Cuéntanosla y adaptamos: las profesoras ajustan ejercicios continuamente. La danza bien enseñada suma salud, nunca resta."),
        ],
    },
    {
        "slug": "kpop-heels-joves",
        "slug_es": "kpop-heels-jovenes",
        "categoria": "estils",
        "categoria_es": "estilos",
        "data": "2026-04-22",
        "data_ca": "22 d'abril de 2026",
        "data_es": "22 de abril de 2026",
        "minuts": 4,
        "nom_wa": "k-pop",
        "nom_wa_es": "k-pop",
        "og": "blog-kpop.jpg",
        "img": "blog-kpop.jpg",
        "img_alt": "Unes sabates de taló per ballar heels sobre el parquet d'una sala amb llum càlida de tarda",
        "img_alt_es": "Unos zapatos de tacón para bailar heels sobre el parquet de una sala con luz cálida de tarde",
        "related_pagines": ["k-pop-heels", "hip-hop", "jazz", "horaris"],
        "related_posts": ["hip-hop-nens-adolescents"],

        "title": "k-pop i heels: les classes que fan venir els joves corrent · escola de dansa cristina colomé",
        "desc": "El k-pop i les heels són les disciplines que més creixen entre adolescents i joves adults: coreografies virals, point dance, empoderament i molta més tècnica de la que sembla.",
        "h1": "k-pop i heels: les classes que fan venir els joves corrents",
        "intro": "Hi ha dues paraules que fan brillar els ulls de mitja adolescència: k-pop i heels. I darrere del fenomen viral hi ha el que més ens agrada: tècnica, treball i una confiança que es veu créixer setmana a setmana.",
        "excerpt": "K-pop i heels són les disciplines que més creixen entre joves: coreografies virals, point dance, empoderament i més tècnica de la que sembla.",
        "cos": """
<p>Quan vam obrir els grups de <a href="/k-pop-heels/">k-pop i heels</a>, sabíem que agradarien. El que no sabíem és que es convertirien en la porta per on tota una generació entraria a la dansa. Adolescents que mai no s'haurien apuntat a ballet arriben pel k-pop — i acaben descobrint que ballar era el seu lloc.</p>

<h2>k-pop: la coreografia com a idioma</h2>
<p>El k-pop ha fet una cosa única: ha tornat a posar la coreografia al centre de la música pop. Cada cançó té el seu <strong>point dance</strong> — aquell pas signatura pensat perquè milions de fans l'imitin — i les formacions canvien amb una precisió mil·limètrica. A classe aprenem les coreografies dels grups del moment tal com són, i això vol dir treballar neteja, sincronia i memòria a un nivell que sorprendria qualsevol escèptic.</p>

<h2>heels: força sobre talons</h2>
<p>Les heels són una altra història i el mateix destí: ballar amb talons no és un caprici estètic, és <strong>un treball de força, equilibri i presència</strong> que transforma la manera de moure's — i de plantar-se al món. És una classe d'empoderament pur: esquena recta, mirada endavant i una seguretat que se'n va cap a la vida de fora de la sala.</p>

<h2>més tècnica de la que sembla</h2>
<p>Totes dues disciplines beuen del jazz, del hip-hop i fins i tot del vogue: aïllaments, línies, musicalitat, actitud. Qui ve «només» a ballar la cançó del moment s'emporta, sense adonar-se'n, una formació de dansa contemporània urbana molt completa. I qui vulgui anar més enllà té el <a href="/hip-hop/">hip-hop</a> i el <a href="/jazz/">jazz</a> a un passadís de distància.</p>

<h2>vine amb la cançó al cap</h2>
<p>Si tens (o tens a casa) algú que es passa el dia imitant coreografies davant del mirall, ja saps què li has de dir: que això, ben après i amb grup, és mil vegades millor. <a href="/classe-de-prova-gratuita/">Primera classe gratuïta</a>, horaris <a href="/horaris/">a la graella</a>, i els talons — per a heels — quan la professora digui que els peus estan a punt.</p>
""",
        "faqs": [
            ("a partir de quina edat es pot fer k-pop?",
             "Els grups de k-pop són juvenils: pensats per a adolescents i joves. Els més petits poden començar per hip-hop o jazz infantil i fer el salt quan toqui."),
            ("cal portar talons a la primera classe de heels?",
             "No: es comença treballant la tècnica amb esportives, i els talons s'incorporen quan la base de força i equilibri està construïda. La professora t'orientarà sobre quins talons comprar."),
            ("les coreografies són les originals dels grups de k-pop?",
             "Sí: aprenem les coreografies reals dels grups del moment, adaptant la dificultat al nivell del grup. La satisfacció de clavar el point dance de la teva cançó no té preu."),
        ],

        "title_es": "k-pop y heels: las clases que hacen venir corriendo a los jóvenes · escola de dansa cristina colomé",
        "desc_es": "El k-pop y las heels son las disciplinas que más crecen entre adolescentes y jóvenes adultos: coreografías virales, point dance, empoderamiento y mucha más técnica de la que parece.",
        "h1_es": "k-pop y heels: las clases que hacen venir corriendo a los jóvenes",
        "intro_es": "Hay dos palabras que hacen brillar los ojos de media adolescencia: k-pop y heels. Y detrás del fenómeno viral está lo que más nos gusta: técnica, trabajo y una confianza que se ve crecer semana a semana.",
        "excerpt_es": "K-pop y heels son las disciplinas que más crecen entre jóvenes: coreografías virales, point dance, empoderamiento y más técnica de la que parece.",
        "cos_es": """
<p>Cuando abrimos los grupos de <a href="/es/k-pop-heels/">k-pop y heels</a>, sabíamos que gustarían. Lo que no sabíamos es que se convertirían en la puerta por donde toda una generación entraría a la danza. Adolescentes que nunca se habrían apuntado a ballet llegan por el k-pop — y acaban descubriendo que bailar era su lugar.</p>

<h2>k-pop: la coreografía como idioma</h2>
<p>El k-pop ha hecho algo único: ha vuelto a poner la coreografía en el centro de la música pop. Cada canción tiene su <strong>point dance</strong> — ese paso firma pensado para que millones de fans lo imiten — y las formaciones cambian con una precisión milimétrica. En clase aprendemos las coreografías de los grupos del momento tal como son, y eso significa trabajar limpieza, sincronía y memoria a un nivel que sorprendería a cualquier escéptico.</p>

<h2>heels: fuerza sobre tacones</h2>
<p>Las heels son otra historia y el mismo destino: bailar con tacones no es un capricho estético, es <strong>un trabajo de fuerza, equilibrio y presencia</strong> que transforma la manera de moverse — y de plantarse en el mundo. Es una clase de empoderamiento puro: espalda recta, mirada al frente y una seguridad que se va hacia la vida de fuera de la sala.</p>

<h2>más técnica de la que parece</h2>
<p>Ambas disciplinas beben del jazz, del hip-hop e incluso del vogue: aislamientos, líneas, musicalidad, actitud. Quien viene «solo» a bailar la canción del momento se lleva, sin darse cuenta, una formación de danza urbana contemporánea muy completa. Y quien quiera ir más allá tiene el <a href="/es/hip-hop/">hip-hop</a> y el <a href="/es/jazz/">jazz</a> a un pasillo de distancia.</p>

<h2>ven con la canción en la cabeza</h2>
<p>Si tienes (o tienes en casa) a alguien que se pasa el día imitando coreografías delante del espejo, ya sabes qué decirle: que eso, bien aprendido y con grupo, es mil veces mejor. <a href="/es/blog/clase-de-prueba-gratuita/">Primera clase gratuita</a>, horarios <a href="/es/horarios/">en la parrilla</a>, y los tacones — para heels — cuando la profesora diga que los pies están a punto.</p>
""",
        "faqs_es": [
            ("¿a partir de qué edad se puede hacer k-pop?",
             "Los grupos de k-pop son juveniles: pensados para adolescentes y jóvenes. Los más pequeños pueden empezar por hip-hop o jazz infantil y dar el salto cuando toque."),
            ("¿hay que llevar tacones a la primera clase de heels?",
             "No: se empieza trabajando la técnica con deportivas, y los tacones se incorporan cuando la base de fuerza y equilibrio está construida. La profesora te orientará sobre qué tacones comprar."),
            ("¿las coreografías son las originales de los grupos de k-pop?",
             "Sí: aprendemos las coreografías reales de los grupos del momento, adaptando la dificultad al nivel del grupo. La satisfacción de clavar el point dance de tu canción no tiene precio."),
        ],
    },
]


# ── entradeta per a la HOME: tot en minúscula d'estil de la casa.
# El blog per dins manté les majúscules normals (decisió Xavi, 4 set 2026);
# aquesta funció només s'aplica quan l'entradeta viatja a la home.
import re as _re

_PROPIS_HOME = {'cristina', 'colomé', 'barcelona', 'sant', 'gervasi',
                'craywinckel', 'royal', 'academy', 'dance'}


def entradeta_min(t):
    def _baixa(m):
        w = m.group(2)
        if w.isupper() or w.lower() in _PROPIS_HOME:
            return m.group(0)
        return m.group(1) + w[0].lower() + w[1:]
    return _re.sub(r"(^|[.!?…]\s+)([A-ZÀÈÉÍÒÓÚÏÜÇÑÁ][\w'’-]*)", _baixa, t)
