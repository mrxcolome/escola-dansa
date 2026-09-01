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
        "img_alt": "La porta entreoberta d'una sala de dansa amb llum càlida, amb la barra i el mirall al fons",
        "img_alt_es": "La puerta entreabierta de una sala de danza con luz cálida, con la barra y el espejo al fondo",
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
]
