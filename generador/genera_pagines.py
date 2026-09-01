# -*- coding: utf-8 -*-
"""
Generador de les pàgines de disciplina i de públic d'escoladansa.com.
Executa:  python genera_pagines.py
Escriu cada pàgina a WEB_2026/<slug>/index.html a partir de PAGINES + PLANTILLA.
Quan canviïn els horaris (curs nou) o el disseny, edita aquí i regenera-ho tot.
"""
import html
import json
import os
import urllib.parse

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # WEB_2026/
DOMINI = "https://escoladansa.com"
CURS = "2026–27"  # ⚠️ actualitzar cada curs
WHATSAPP_ACTIU = True  # WhatsApp Business del 934 17 98 86 operatiu des de l'1 set 2026
TEL = "934 17 98 86"
TEL_LINK = "+34934179886"

# slug català -> slug castellà (URL amb paraula clau en cada llengua)
SLUG_ES = {
    "ballet-classic": "ballet-clasico",
    "dansa-contemporania": "danza-contemporanea",
    "jazz": "jazz",
    "hip-hop": "hip-hop",
    "claque": "claque",
    "ball-espanyol": "baile-espanol",
    "dansa-oriental": "danza-oriental",
    "k-pop-heels": "k-pop-heels",
    "musical-interpretacio": "musical-interpretacion",
    "formacio-escenica": "formacion-escenica",
    "cos-benestar": "cuerpo-bienestar",
    "fit-dance": "fit-dance",
    "dansa-infantil": "danza-infantil",
    "dansa-adults": "danza-adultos",
    "horaris": "horarios",
    "preus": "precios",
}

# ─────────────────────────────────────────────────────────────────────────────
# CONTINGUT DE LES PÀGINES
# horaris: (dia, hora, grup, sala) — extret de la graella de l'index.html
# ─────────────────────────────────────────────────────────────────────────────

PAGINES = [
    {
        "slug": "ballet-classic",
        "nom": "ballet clàssic",
        "title": "classes de ballet clàssic a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de ballet clàssic a Sant Gervasi (Barcelona) per a totes les edats: iniciació, infantil, juvenil i adults. Puntes i preparació RAD. 1a classe gratuïta.",
        "h1": "ballet clàssic",
        "intro": "Tècnica, elegància i una base per a tota la vida. El ballet clàssic és la columna vertebral de l'escola: des de la iniciació fins a les puntes i la preparació d'exàmens.",
        "per_a_qui": "Tenim grups de clàssic per a totes les edats i nivells: infantils, juvenils i adults (des d'iniciació fins a avançat). Els més petits comencen amb la iniciació a la dansa, i el recorregut arriba fins a les classes de puntes i la preparació d'exàmens oficials RAD. No cal cap experiència prèvia per començar: t'ajudem a trobar el grup on et sentiràs a gust.",
        "beneficis": [
            ("postura i consciència corporal", "El clàssic treballa l'alineació, l'equilibri i el control del cos com cap altra disciplina."),
            ("disciplina i concentració", "La tècnica demana atenció i constància — i això es nota dins i fora de la sala."),
            ("la base de totes les danses", "Qui fa clàssic té més facilitat per al contemporani, el jazz i qualsevol altre estil."),
            ("musicalitat", "Aprendre a escoltar la música i moure-s'hi és un regal per sempre."),
        ],
        "horaris": [
            ("dilluns", "17.30", "clàssic infantil A", "sala C"),
            ("dilluns", "18.30", "clàssic puntes · juvenil B", "sala C"),
            ("dilluns", "19.30", "clàssic adults iniciació", "sala C"),
            ("dilluns", "19.30", "clàssic adults avançat", "sala H"),
            ("dimarts", "17.30", "clàssic juvenil A", "sala H"),
            ("dimarts", "18.30", "clàssic juvenil C", "sala H"),
            ("dimarts", "19.45", "clàssic adults intermedi", "sala C"),
            ("dimecres", "17.15", "clàssic juvenil B", "sala H"),
            ("dimecres", "18.30", "clàssic infantil B", "sala N"),
            ("dimecres", "18.30", "clàssic adults iniciació", "sala C"),
            ("dimecres", "19.30", "clàssic adults avançat", "sala H"),
            ("dijous", "17.30", "clàssic infantil C", "sala N"),
            ("dijous", "18.30", "clàssic juvenil C", "sala H"),
            ("dijous", "19.45", "clàssic adults intermedi", "sala C"),
        ],
        "faqs": [
            ("cal experiència per començar ballet clàssic?",
             "No. Hi ha grups d'iniciació tant per a infants com per a adults, i la primera classe de prova és gratuïta perquè ho comprovis sense compromís."),
            ("feu puntes i exàmens oficials?",
             "Sí: hi ha classe de puntes per a juvenils i preparem alumnes per als exàmens oficials RAD (Royal Academy of Dance)."),
            ("un adult pot començar ballet de zero?",
             "I tant — el grup d'adults iniciació està pensat exactament per a això. Mai no és tard per començar."),
            ("què cal portar a classe?",
             "Per a la classe de prova, roba còmoda i ajustada n'hi ha prou. Un cop t'hi apuntis, t'orientarem sobre mitges, maillot i sabatilles."),
        ],
        "related": ["dansa-contemporania", "jazz", "dansa-infantil", "dansa-adults"],
    },
    {
        "slug": "dansa-contemporania",
        "nom": "contemporani",
        "title": "classes de dansa contemporània a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de dansa contemporània a Sant Gervasi (Barcelona): moviment lliure i orgànic, tècnica i creació. Grups infantils, juvenils i adults. 1a classe gratuïta.",
        "h1": "dansa contemporània",
        "intro": "Moviment lliure i orgànic: la tècnica al servei de l'expressió. Al contemporani hi ha espai per crear, improvisar i trobar la teva pròpia manera de moure't.",
        "per_a_qui": "Oferim contemporani des d'infantil fins a adults, amb grups juvenils per nivells i grups d'adults intermedi i avançat. És una disciplina perfecta tant per a qui ve del clàssic i vol alliberar el moviment com per a qui comença i busca una dansa expressiva i actual.",
        "beneficis": [
            ("expressió i creativitat", "El contemporani et convida a crear i a dir coses amb el cos, no només a executar passos."),
            ("un cos fort i flexible", "Treball de terra, caigudes, espirals: força i mobilitat reals per a tot el cos."),
            ("connexió amb un mateix", "Respiració, pes, fluïdesa — una estona per escoltar-te i alliberar tensions."),
        ],
        "horaris": [
            ("dilluns", "20.30", "contemporani adults avançat", "sala H"),
            ("dimecres", "18.15", "contemporani juvenil B", "sala H"),
            ("dimecres", "20.30", "contemporani adults intermedi", "sala H"),
            ("dijous", "17.30", "contemporani juvenil A", "sala H"),
            ("dijous", "19.30", "contemporani juvenil C", "sala H"),
            ("divendres", "17.30", "contemporani infantil B", "sala H"),
            ("divendres", "18.30", "contemporani juvenil A", "sala H"),
        ],
        "faqs": [
            ("què es treballa en una classe de contemporani?",
             "Tècnica (treball de terra, espirals, salts), improvisació i creació coreogràfica, sempre adaptat al nivell del grup."),
            ("cal haver fet ballet abans?",
             "No és imprescindible. Una base de clàssic ajuda, però hi ha grups on pots començar de zero — la classe de prova gratuïta és la millor manera de comprovar-ho."),
            ("contemporani o clàssic: quin trio?",
             "Si busques estructura i tècnica pura, clàssic; si busques expressió i moviment lliure, contemporani. Moltes alumnes fan tots dos: es complementen molt bé."),
        ],
        "related": ["ballet-classic", "jazz", "dansa-adults", "dansa-infantil"],
    },
    {
        "slug": "jazz",
        "nom": "jazz",
        "title": "classes de dansa jazz a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de dansa jazz a Sant Gervasi (Barcelona): energia, ritme i coreografia per a infants, joves i adults. Primera classe de prova gratuïta.",
        "h1": "dansa jazz",
        "intro": "Energia, ritme i coreografies que enganxen. El jazz és la porta d'entrada perfecta a la dansa: dinàmic, musical i divertidíssim.",
        "per_a_qui": "És una de les disciplines amb més grups de l'escola: infantils per edats, juvenils i adults (des de bàsic fins a intermedi). Si t'agrada ballar amb música actual i aprendre coreografies amb estil, el jazz és el teu lloc.",
        "beneficis": [
            ("coordinació i ritme", "Coreografies que treballen memòria, musicalitat i coordinació de tot el cos."),
            ("energia i forma física", "Una classe de jazz és cardio disfressat de diversió."),
            ("confiança sobre la pista", "Aprens a ballar davant dels altres i a gaudir-ne — al festival de fi de curs es nota!"),
        ],
        "horaris": [
            ("dilluns", "17.00", "jazz infantil A", "sala C"),
            ("dilluns", "18.30", "jazz infantil D", "sala N"),
            ("dilluns", "18.30", "jazz adults bàsic", "sala H"),
            ("dimarts", "17.15", "jazz infantil A", "sala N"),
            ("dimecres", "17.30", "jazz infantil C", "sala N"),
            ("dijous", "20.30", "jazz adults intermedi", "sala H"),
            ("divendres", "17.30", "jazz juvenil A", "sala N"),
        ],
        "faqs": [
            ("a partir de quina edat es pot fer jazz?",
             "Tenim grups infantils des de ben petits, organitzats per edats. A la classe de prova gratuïta veurem quin grup li encaixa millor."),
            ("sóc adult i no he ballat mai: puc?",
             "Sí! El grup d'adults bàsic està pensat per començar de zero, amb bon rotllo i sense pressió."),
            ("quina diferència hi ha entre jazz i hip-hop?",
             "El jazz beu de la dansa acadèmica (línia, tècnica, musicalitat) amb música actual; el hip-hop ve de la cultura urbana, amb un llenguatge més de carrer. Prova tots dos i tria!"),
        ],
        "related": ["hip-hop", "ballet-classic", "dansa-infantil", "dansa-adults"],
    },
    {
        "slug": "hip-hop",
        "nom": "hip-hop",
        "title": "classes de hip-hop a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de hip-hop i danses urbanes a Sant Gervasi (Barcelona) per a nens, joves i adults, de d'iniciació a avançat. Primera classe de prova gratuïta.",
        "h1": "hip-hop",
        "intro": "Estils urbans, coreos actuals i molta actitud. El hip-hop és la disciplina preferida dels que volen ballar el que sona ara mateix.",
        "per_a_qui": "Des d'infantil fins a adults avançat, amb grups juvenils per nivells. Si el teu fill o filla balla tot el dia davant del mirall, o si tu mateix vols aprendre les coreos que veus a les xarxes, aquí és on començar.",
        "beneficis": [
            ("actitud i confiança", "El hip-hop treballa la presència: ballar amb seguretat es contagia a la resta de la vida."),
            ("forma física de veritat", "Potència, resistència i control — una classe urbana crema energia de valent."),
            ("cultura i comunitat", "Més que passos: musicalitat, estil propi i sentit de grup."),
        ],
        "horaris": [
            ("dilluns", "17.30", "hip-hop infantil B", "sala H"),
            ("dimarts", "18.30", "hip-hop infantil C", "sala N"),
            ("dimarts", "19.45", "hip-hop juvenil C", "sala H"),
            ("dimecres", "20.30", "hip-hop adults avançat", "sala N"),
            ("dijous", "17.30", "hip-hop juvenil B", "sala C"),
            ("dijous", "18.30", "hip-hop infantil A", "sala N"),
            ("divendres", "19.45", "hip-hop juvenil A", "sala H"),
        ],
        "faqs": [
            ("el meu fill no ha ballat mai: pot començar amb hip-hop?",
             "És una de les millors portes d'entrada: música que coneixen, moviments naturals i grups per edats. La primera classe de prova és gratuïta."),
            ("feu hip-hop per a adults?",
             "Sí, hi ha grup d'adults avançat els dimecres al vespre. Si el teu nivell és inicial, explica'ns-ho i et recomanem el millor encaix."),
            ("quins estils urbans treballeu?",
             "La base és el hip-hop amb obertura a altres estils urbans segons el grup i la coreografia. I si t'estira el k-pop o els heels, també en fem classes!"),
        ],
        "related": ["k-pop-heels", "jazz", "dansa-infantil", "dansa-adults"],
    },
    {
        "slug": "claque",
        "nom": "claqué",
        "title": "classes de claqué a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de claqué a Sant Gervasi (Barcelona): el ritme als peus, de juvenil a adults. Primera classe de prova gratuïta.",
        "h1": "claqué",
        "intro": "El ritme als peus. El claqué converteix el ballarí en músic: cada pas és percussió, i cada coreografia, una cançó.",
        "per_a_qui": "Grups juvenils i d'adults (intermedi). És una disciplina única: treballa el ritme com cap altra i engancha des del primer dia. Si t'agrada la música tant com ballar, el claqué et farà feliç.",
        "beneficis": [
            ("oïda i ritme musical", "Fer música amb els peus desenvolupa una musicalitat finíssima."),
            ("coordinació i agilitat", "Peus ràpids, ment desperta: el claqué és gimnàstica per al cervell."),
            ("una tradició amb molt de swing", "Del musical americà als escenaris d'avui — ballar claqué és pura elegància."),
        ],
        "horaris": [
            ("dimarts", "18.30", "claqué adults intermedi", "sala C"),
            ("dimarts", "19.45", "claqué juvenil A", "sala N"),
            ("dijous", "18.30", "claqué adults intermedi", "sala C"),
        ],
        "faqs": [
            ("necessito sabates de claqué per provar?",
             "Per a la classe de prova gratuïta no cal: vine amb calçat de sola dura i ja veuràs si t'enganxa (t'enganxarà)."),
            ("mai no he fet claqué: quin grup em toca?",
             "Parla amb nosaltres: segons la teva base de dansa i ritme et recomanarem el grup adequat, i el primer dia és de prova."),
            ("els nens poden fer claqué?",
             "El claqué el comencem a partir de l'etapa juvenil. Per als més petits recomanem començar per jazz, clàssic o hip-hop i fer el pas després."),
        ],
        "related": ["jazz", "musical-interpretacio", "dansa-adults"],
    },
    {
        "slug": "ball-espanyol",
        "nom": "ball espanyol",
        "title": "classes de ball espanyol a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de dansa espanyola a Sant Gervasi (Barcelona): tradició, caràcter i tècnica. Grups juvenils i adults. Primera classe de prova gratuïta.",
        "h1": "ball espanyol",
        "intro": "Tradició, caràcter i una tècnica amb segles d'història. La dansa espanyola és força, elegància i temperament sobre l'escenari.",
        "per_a_qui": "Grups juvenils i d'adults de nivell intermedi. Si t'atrau la nostra tradició de dansa — el braceig, el caràcter, la música espanyola — aquesta és la teva classe.",
        "beneficis": [
            ("caràcter i presència", "La dansa espanyola es balla amb tot el cos i amb tota l'ànima."),
            ("tècnica exigent i completa", "Braços, esquena, colpeig — un treball tècnic que complementa qualsevol altra dansa."),
            ("patrimoni viu", "Ballar espanyol és mantenir viva una tradició única al món."),
        ],
        "horaris": [
            ("dimecres", "19.30", "espanyol juvenil intermedi", "sala C"),
            ("dimecres", "20.30", "espanyol adults intermedi", "sala C"),
        ],
        "faqs": [
            ("puc començar sense nivell?",
             "Els grups actuals són de nivell intermedi, però parla amb nosaltres: valorem la teva base a la classe de prova gratuïta i et diem sincerament si t'hi pots incorporar."),
            ("què cal portar?",
             "Per provar, roba còmoda i sabata amb una mica de taló si en tens. Després t'orientarem sobre la sabata de dansa espanyola."),
        ],
        "related": ["ballet-classic", "dansa-oriental", "dansa-adults"],
    },
    {
        "slug": "dansa-oriental",
        "nom": "dansa oriental",
        "title": "classes de dansa oriental a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de dansa oriental (dansa del ventre) a Sant Gervasi (Barcelona): expressió, tècnica i feminitat. Grups juvenils i adults. 1a classe gratuïta.",
        "h1": "dansa oriental",
        "intro": "Expressió, sensualitat i una tècnica mil·lenària. La dansa del ventre treballa el cos des del centre i allibera com poques disciplines.",
        "per_a_qui": "Grups juvenils i d'adults de nivell avançat, als vespres. Si busques una dansa expressiva, elegant i amb una gran comunitat al darrere, la dansa oriental t'atraparà.",
        "beneficis": [
            ("control del centre del cos", "Aïllaments, ondulacions i vibracions: un treball de tècnica corporal finíssim."),
            ("expressió i autoestima", "Una dansa que celebra el cos tal com és i et reconcilia amb el mirall."),
            ("esquena i postura", "El treball d'ondulacions enforteix i flexibilitza tota la cadena posterior."),
        ],
        "horaris": [
            ("dimarts", "20.30", "dansa del ventre · juvenil avançat", "sala N"),
            ("dijous", "20.30", "dansa del ventre · adults avançat", "sala N"),
        ],
        "faqs": [
            ("mai no n'he fet: puc apuntar-m'hi?",
             "Els grups actuals són avançats, però vine a la classe de prova gratuïta i valorem el teu encaix — o t'avisem quan obrim grup d'iniciació."),
            ("què em poso per a la classe?",
             "Roba còmoda que et deixi veure el moviment del maluc (leggings i top o samarreta ajustada). El mocador de malucs te'l deixem el primer dia!"),
        ],
        "related": ["ball-espanyol", "fit-dance", "dansa-adults"],
    },
    {
        "slug": "k-pop-heels",
        "nom": "k-pop & heels",
        "title": "classes de k-pop i heels a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de k-pop i heels a Sant Gervasi (Barcelona): les coreografies del moment i actitud sobre talons. Primera classe de prova gratuïta.",
        "h1": "k-pop & heels",
        "intro": "Les coreos del moment i tota l'actitud. Del fenomen k-pop a l'empoderament del heels: dues classes per ballar com als videoclips.",
        "per_a_qui": "El k-pop és per a juvenils que somien amb les coreografies dels seus grups preferits; el heels, per a adults avançats que volen treballar actitud, línia i seguretat sobre talons.",
        "beneficis": [
            ("ballar el que t'agrada", "Coreografies reals dels artistes del moment: la motivació ve de sèrie."),
            ("actitud i seguretat", "El heels és una classe d'empoderament pur: postura, presència i confiança."),
            ("memòria coreogràfica", "Aprendre coreos completes entrena la memòria i la neteja de moviment."),
        ],
        "horaris": [
            ("dimarts", "20.30", "heels adults avançat", "sala H"),
            ("divendres", "17.30", "k-pop juvenil A", "sala C"),
        ],
        "faqs": [
            ("cal saber ballar per fer k-pop?",
             "No: les coreos s'aprenen pas a pas i el grup és juvenil. Si li agrada el k-pop, la motivació farà la resta. Primera classe gratuïta!"),
            ("quins talons necessito per al heels?",
             "Per provar, uns talons còmodes i estables que ja tinguis. Després t'aconsellarem el calçat ideal per ballar amb seguretat."),
        ],
        "related": ["hip-hop", "jazz", "dansa-adults"],
    },
    {
        "slug": "musical-interpretacio",
        "nom": "musical & interpretació",
        "title": "classes de teatre musical per a nens a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de musical i interpretació per a infants a Sant Gervasi (Barcelona): ballar, cantar i actuar. Primera classe de prova gratuïta.",
        "h1": "musical & interpretació",
        "intro": "Ballar, cantar i actuar: el triple somni del teatre musical, a l'abast dels més petits. Dansa-teatre per créixer sobre l'escenari.",
        "per_a_qui": "Grups infantils els divendres a la tarda. Perfecte per a nens i nenes amb vena artística que ho volen fer tot: moure's, cantar, interpretar personatges i perdre la vergonya dalt d'un escenari.",
        "beneficis": [
            ("expressió completa", "Cos, veu i emoció treballant junts — l'expressivitat es multiplica."),
            ("perdre la por escènica", "Actuar des de petits dóna una seguretat que dura tota la vida."),
            ("treball en equip", "Un musical es construeix entre tots: escoltar, esperar el torn, brillar junts."),
        ],
        "horaris": [
            ("divendres", "18.30", "musical infantil", "sala N"),
            ("divendres", "19.45", "interpretació infantil", "sala N"),
        ],
        "faqs": [
            ("el meu fill és tímid: li anirà bé?",
             "És justament on més floreixen els tímids: el joc teatral treu la vergonya sense pressió. Prova la primera classe gratuïta i ho veuràs."),
            ("cal saber cantar o ballar abans?",
             "Gens ni mica. Es treballa tot des de la base, jugant i per edats."),
        ],
        "related": ["formacio-escenica", "jazz", "dansa-infantil"],
    },
    {
        "slug": "formacio-escenica",
        "nom": "formació escènica",
        "title": "formació escènica per a joves a Barcelona · escola de dansa cristina colomé",
        "desc": "Formació escènica els divendres a la tarda a Sant Gervasi (Barcelona): jazz, hip-hop, claqué, cant i interpretació en un sol pack. 1a classe gratuïta.",
        "h1": "formació escènica",
        "intro": "L'entrenament complet de l'artista: jazz, hip-hop, claqué, cant i interpretació, tot en una mateixa tarda. Per a qui vol l'escenari de veritat.",
        "per_a_qui": "Els divendres a la tarda, en format pack, per a joves que volen una formació artística completa: ballar diversos estils, cantar i interpretar. La millor preparació per a musicals, càstings i escenaris — o simplement per gaudir-ho tot.",
        "beneficis": [
            ("formació 360°", "Cinc disciplines en una tarda: la polivalència que demana l'escenari actual."),
            ("un preu de pack", "Tot el divendres a la tarda per 85 €/mes — la manera més completa de formar-se."),
            ("esperit de companyia", "El grup dels divendres funciona com una petita companyia: pinya, projecte i escenari."),
        ],
        "horaris": [
            ("divendres", "17.15", "formació escènica · jazz, hip-hop, claqué, cant i interpretació", "sales H+N"),
        ],
        "faqs": [
            ("quant costa la formació escènica?",
             "El pack complet dels divendres val 85 € al mes (247 € si pagues el trimestre). La primera tarda de prova és gratuïta."),
            ("cal experiència prèvia?",
             "No: cal ganes. El format multidisciplinar permet que cadascú creixi des del seu punt de partida."),
        ],
        "related": ["musical-interpretacio", "jazz", "claque", "hip-hop"],
    },
    {
        "slug": "cos-benestar",
        "nom": "cos & benestar",
        "title": "ioga, barre i zumba a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de ioga, barre i zumba a Sant Gervasi (Barcelona): cuida't ballant, als matins i als vespres. Primera classe de prova gratuïta.",
        "h1": "cos & benestar",
        "intro": "Cuidar-se també és ballar. Ioga per respirar, barre per tonificar amb ADN de dansa i zumba per suar somrient.",
        "per_a_qui": "Per a adults de totes les edats i condicions físiques: el barre als matins (dilluns i dimecres a les 11 h), i el ioga i la zumba als vespres. Cap d'aquestes classes demana experiència — només ganes de trobar-te bé.",
        "beneficis": [
            ("barre: tonificació amb elegància", "El millor del ballet (postura, cames, core) sense necessitat de saber ballar."),
            ("ioga: respirar i desconnectar", "Flexibilitat, calma i una pausa de veritat en la setmana."),
            ("zumba: cardio amb somriure", "La classe on suar és una festa — ritmes llatins i energia amunt."),
        ],
        "horaris": [
            ("dilluns", "11.00", "barre", "sala C"),
            ("dimarts", "20.30", "ioga", "sala C"),
            ("dimecres", "11.00", "barre", "sala C"),
            ("dimecres", "19.30", "zumba", "sala N"),
            ("dijous", "20.30", "ioga", "sala C"),
        ],
        "faqs": [
            ("no he fet mai dansa: puc fer barre?",
             "El barre és per a tothom: s'inspira en el ballet però és una classe de tonificació, no de coreografia. Ideal per començar."),
            ("les classes de matí són per a qui?",
             "Per a qui té els matins lliures i vol començar el dia cuidant-se: el barre de dilluns i dimecres a les 11 h."),
        ],
        "related": ["fit-dance", "ballet-classic", "dansa-adults"],
    },
    {
        "slug": "fit-dance",
        "nom": "fit dance & femme empower",
        "title": "fit dance i femme empower a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de fit dance i femme empower a Sant Gervasi (Barcelona): suor, força i empoderament en grup. Primera classe de prova gratuïta.",
        "h1": "fit dance & femme empower",
        "intro": "Suor, força i empoderament en grup. Dues classes per posar-se en forma ballant i sortir de la sala amb l'autoestima pels núvols.",
        "per_a_qui": "Per a adults que volen entrenar ballant: el fit dance combina coreografia i condicionament físic; el femme empower (nivell intermedi) treballa actitud, força i seguretat en un ambient de sororitat total.",
        "beneficis": [
            ("posar-se en forma sense avorrir-se", "Quan l'entrenament és ballar, la constància ve sola."),
            ("força i actitud", "Treball físic real amb música alta i energia de grup."),
            ("comunitat", "Les classes d'empoderament creen pinya — vindràs per l'exercici i et quedaràs per la gent."),
        ],
        "horaris": [
            ("dilluns", "19.30", "fit dance", "sala N"),
            ("dilluns", "20.30", "femme empower · adults intermedi", "sala N"),
        ],
        "faqs": [
            ("quina forma física necessito?",
             "Cap en concret per al fit dance: cadascú va al seu ritme i la intensitat s'adapta. El femme empower demana una mica de rodatge."),
            ("què porto a classe?",
             "Roba esportiva, calçat còmode, aigua i tovallola. La resta la posa la música."),
        ],
        "related": ["cos-benestar", "dansa-oriental", "dansa-adults"],
    },
    # ── pàgines per públic ──────────────────────────────────────────────────
    {
        "slug": "dansa-infantil",
        "nom": "dansa per a nens i nenes",
        "title": "classes de dansa per a nens a Barcelona · escola de dansa cristina colomé",
        "desc": "Extraescolar de dansa per a nens i nenes a Sant Gervasi (Barcelona): iniciació, clàssic, jazz, hip-hop i més, per edats i nivells. 1a classe gratuïta.",
        "h1": "dansa per a nens i nenes",
        "intro": "L'extraescolar que no sembla una extraescolar: més de 25 anys ajudant nens i nenes a créixer ballant, a dos minuts de l'FGC Av. Tibidabo.",
        "per_a_qui": "De la iniciació a la dansa per als més petits fins als grups juvenils, tots els grups s'organitzen per edats i nivells i tenen continuïtat curs rere curs. Les classes són a la tarda, pensades per encaixar amb l'horari escolar de les famílies de Sant Gervasi, la Bonanova i el Putxet.",
        "beneficis": [
            ("psicomotricitat i postura", "La dansa desenvolupa coordinació, equilibri i consciència corporal en l'edat d'or per fer-ho."),
            ("confiança i expressió", "Ballar davant dels altres, actuar al festival de fi de curs — la seguretat que es guanya a la sala surt amb ells a la vida."),
            ("constància i esforç", "Aprendre una coreografia ensenya el valor de la pràctica millor que mil sermons."),
            ("amistats que duren", "Els grups fan pinya: molts dels nostres alumnes creixen junts des de ben petits."),
        ],
        "disciplines": [
            ("iniciació a la dansa", None, "el primer contacte amb el moviment i la música, per als més petits"),
            ("ballet clàssic", "ballet-classic", "la base de tot, des d'infantil fins a puntes i exàmens RAD"),
            ("jazz", "jazz", "energia i coreografia — la porta d'entrada més divertida"),
            ("hip-hop", "hip-hop", "estils urbans per als que ballen tot el dia a casa"),
            ("contemporani", "dansa-contemporania", "expressió i moviment lliure per a infants i juvenils"),
            ("musical & interpretació", "musical-interpretacio", "ballar, cantar i actuar els divendres"),
            ("k-pop", "k-pop-heels", "les coreos dels seus ídols, per a juvenils"),
            ("formació escènica", "formacio-escenica", "el pack complet d'artista dels divendres a la tarda"),
        ],
        "faqs": [
            ("a quina edat pot començar el meu fill o filla?",
             "Des de ben petits, amb els grups d'iniciació a la dansa. A la classe de prova gratuïta veiem quin grup li encaixa millor per edat i maduresa."),
            ("quant costa l'extraescolar de dansa?",
             "Les quotes infantils van dels 56 €/mes (1 dia per setmana) als 92 €/mes (4 dies), amb opció trimestral. La primera classe de prova és gratuïta."),
            ("com sabré si li agrada abans d'apuntar-lo?",
             "Per això la primera classe és gratuïta i sense compromís: el porteu, ho prova, i decidiu amb calma."),
            ("fan actuacions?",
             "Sí! Cada curs acaba amb el festival de fi de curs, el gran moment de l'any per a alumnes i famílies."),
        ],
        "related": ["ballet-classic", "jazz", "hip-hop", "musical-interpretacio"],
    },
    {
        "slug": "dansa-adults",
        "nom": "dansa per a adults",
        "title": "classes de dansa per a adults a Barcelona · escola de dansa cristina colomé",
        "desc": "Classes de dansa per a adults a Sant Gervasi (Barcelona): clàssic, contemporani, jazz, hip-hop, claqué i més, d'iniciació a avançat. 1a classe gratuïta.",
        "h1": "dansa per a adults",
        "intro": "Mai no és tard per començar a ballar — ni per tornar-hi. Grups d'adults de tots els nivells, als vespres i als matins, sense pressió i amb molt bon ambient.",
        "per_a_qui": "Tant si no has ballat mai com si ho vas deixar fa anys, tenim un grup per a tu: els vespres (de 18.30 a 21.30) hi ha clàssic, contemporani, jazz, hip-hop, claqué, espanyol, dansa oriental i heels per nivells — i els matins, barre per començar el dia amb energia. Sense exàmens ni pressió: ballar per gaudir-ne.",
        "beneficis": [
            ("desconnectar de veritat", "Una hora de dansa és una hora sense mòbil, sense feina i sense pantalles."),
            ("forma física sense gimnàs", "Cardio, força, flexibilitat i postura — tot ballant."),
            ("aprendre sempre", "El cervell adult agraeix reptes nous: coreografia, música i memòria en acció."),
            ("gent com tu", "Els grups d'adults són petites famílies: es ve a ballar i s'hi queda per la gent."),
        ],
        "disciplines": [
            ("ballet clàssic", "ballet-classic", "d'iniciació a avançat — també si comences de zero"),
            ("contemporani", "dansa-contemporania", "expressió i moviment lliure, intermedi i avançat"),
            ("jazz", "jazz", "grups bàsic i intermedi, energia pura"),
            ("hip-hop", "hip-hop", "urbà per a adults avançats"),
            ("claqué", "claque", "el ritme als peus, nivell intermedi"),
            ("ball espanyol", "ball-espanyol", "tradició i caràcter, nivell intermedi"),
            ("dansa oriental", "dansa-oriental", "dansa del ventre, nivell avançat"),
            ("heels", "k-pop-heels", "actitud sobre talons, nivell avançat"),
            ("ioga, barre i zumba", "cos-benestar", "cuidar-se ballant, matins i vespres"),
            ("fit dance & femme empower", "fit-dance", "entrenar ballant, en grup i amb actitud"),
        ],
        "faqs": [
            ("tinc més de 40/50/60 anys: puc començar?",
             "És clar que sí — a l'escola diem que ballem de 0 a 99. Tria una disciplina d'iniciació o el barre i comença al teu ritme."),
            ("quins horaris fan les classes d'adults?",
             "La majoria són als vespres, entre les 18.30 i les 21.30, perfectes per després de la feina. I el barre, els dilluns i dimecres a les 11 del matí."),
            ("quant costen les classes per a adults?",
             "Des de 60 €/mes (1 dia per setmana) fins a 104 €/mes (4 dies de classes de més d'una hora), amb opció trimestral. La primera classe de prova és gratuïta."),
        ],
        "related": ["ballet-classic", "dansa-contemporania", "cos-benestar", "claque"],
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# PLANTILLA
# ─────────────────────────────────────────────────────────────────────────────

CSS = """
:root{--negre:#0a0a0a;--gris-fosc:#121212;--blanc:#f5f2ef;--gris:#9b948d;--granat-viu:#950000;--granat-fosc:#4d0505;--ease:cubic-bezier(.22,1,.36,1);--text:clamp(1rem,1.4vw,1.15rem);--text-vermells:1rem;--vora:rgba(245,242,239,.14)}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;background:var(--negre)}
body{background:var(--negre);color:var(--blanc);font-family:'Montserrat',sans-serif;font-weight:400;line-height:1.65;overflow-x:clip}
body::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(55vmax 55vmax at 85% -10%,rgba(149,0,0,.25),transparent 65%),radial-gradient(45vmax 45vmax at -10% 80%,rgba(77,5,5,.3),transparent 70%)}
main,nav,footer{position:relative;z-index:1}
::selection{background:var(--granat-viu);color:var(--blanc)}
a{color:inherit;text-decoration:none}
h1,h2,h3{font-weight:800;text-transform:lowercase;letter-spacing:-.02em;line-height:1.1}
nav{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:18px 5vw;transition:background .4s,padding .4s}
nav.solida{background:rgba(10,10,10,.85);backdrop-filter:blur(14px);padding:10px 5vw;box-shadow:0 1px 0 var(--vora)}
.nav-marca{font-weight:800;text-transform:lowercase;font-size:var(--text);white-space:nowrap}
.nav-marca:hover{color:var(--granat-viu);transition:color .3s}
.nav-links{display:flex;gap:30px;font-size:var(--text);font-weight:600;text-transform:lowercase;letter-spacing:.06em}
.nav-links a{opacity:.85;transition:opacity .3s}
.nav-links a:hover{opacity:1}
/* selector d'idioma (desktop): desplegable en mouseover */
.idioma{position:relative;margin-left:5vw;margin-right:-2.5vw;cursor:pointer}
.idioma-etiq{opacity:.85;transition:opacity .3s}
.idioma:hover .idioma-etiq,.idioma:focus-within .idioma-etiq{opacity:1}
.idioma-menu{position:absolute;top:100%;right:0;padding-top:16px;display:none;min-width:150px}
.idioma:hover .idioma-menu,.idioma:focus-within .idioma-menu{display:block}
.idioma-menu a{display:block;background:var(--gris-fosc);border:1px solid var(--vora);padding:13px 18px;opacity:1;text-transform:none}
.idioma-menu a:first-child{border-radius:12px 12px 0 0;border-bottom:0}
.idioma-menu a:last-child{border-radius:0 0 12px 12px}
.idioma-menu a:hover{background:var(--granat-fosc)}
.idioma-menu a.actiu{color:var(--granat-viu);font-weight:800}
/* selector d'idioma (mòbil): cat / es fix a dalt a la dreta */
.idioma-mobil{display:none}
header.capsal{padding:150px 5vw 60px;max-width:1100px;margin:0 auto}
.molla{font-size:var(--text-vermells);letter-spacing:.08em;color:var(--gris);margin-bottom:26px;text-transform:lowercase}
.molla a{color:var(--gris);transition:color .3s}
.molla a:hover{color:var(--granat-viu)}
.molla span{color:var(--blanc)}
.etiqueta{display:inline-flex;align-items:center;gap:12px;font-size:var(--text-vermells);letter-spacing:.3em;text-transform:uppercase;color:var(--granat-viu);font-weight:600;margin-bottom:22px}
.etiqueta::before{content:"";width:34px;height:1px;background:var(--granat-viu)}
h1{font-size:clamp(2.4rem,6vw,4.4rem);margin-bottom:24px}
h1 em{font-style:normal;color:var(--granat-viu)}
.entradeta{font-size:var(--text);color:var(--gris);font-weight:400;max-width:680px}
section{padding:60px 5vw;max-width:1100px;margin:0 auto}
h2{font-size:clamp(2rem,4.6vw,3.8rem);margin-bottom:22px}
.text-gran{font-size:var(--text);color:var(--gris);font-weight:400;max-width:720px}
.beneficis{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:2px;background:var(--vora);margin-top:36px}
.benefici{background:var(--gris-fosc);padding:30px 26px;transition:background .4s}
.benefici:hover{background:var(--granat-fosc)}
.benefici h3{font-size:1.05rem;margin-bottom:10px}
.benefici p{font-size:var(--text);color:var(--gris);font-weight:400}
.classe-fila{font-size:var(--text);display:grid;grid-template-columns:110px 90px 1fr auto;gap:18px;align-items:center;padding:16px 0;border-bottom:1px solid var(--vora);transition:padding-left .25s var(--ease),background .25s}
.classe-fila:hover{padding-left:12px;background:rgba(149,0,0,.08)}
.classe-fila .dia{font-weight:600;text-transform:lowercase;color:var(--gris)}
.classe-fila .hora{font-weight:800;color:var(--granat-viu)}
.classe-fila .nom{font-weight:600;text-transform:lowercase}
.sala{font-size:var(--text-vermells);font-weight:800;letter-spacing:.12em;text-transform:uppercase;border:1px solid var(--vora);padding:5px 12px;border-radius:100px;color:var(--gris);white-space:nowrap}
.nota-curs{margin-top:20px;font-size:var(--text);color:var(--gris);font-weight:400}
.dia-titol{margin-bottom:6px}
.fila-h{display:grid;grid-template-columns:90px 1fr auto;gap:18px;align-items:center;padding:15px 0;border-bottom:1px solid var(--vora);font-size:var(--text);transition:padding-left .25s var(--ease),background .25s}
.fila-h:hover{padding-left:12px;background:rgba(149,0,0,.08)}
.fila-h .hora{font-weight:800;color:var(--granat-viu)}
.fila-h .nom{font-weight:600;text-transform:lowercase}
.fila-h .nom small{display:block;font-weight:400;color:var(--gris);font-size:var(--text);text-transform:none}
.taula-preus{width:100%;border-collapse:collapse;margin:10px 0 40px}
.taula-preus caption{text-align:left;font-weight:800;font-size:1.05rem;padding-bottom:14px;text-transform:lowercase;color:var(--blanc)}
.taula-preus th,.taula-preus td{padding:14px 12px;text-align:left;border-bottom:1px solid var(--vora);font-size:var(--text)}
.taula-preus th{font-size:var(--text-vermells);letter-spacing:.2em;text-transform:uppercase;color:var(--gris);font-weight:600}
.taula-preus td:first-child{font-weight:600}
.taula-preus .preu{color:var(--granat-viu);font-weight:800;white-space:nowrap}
.nota-curs a{color:var(--granat-viu);font-weight:600}
.disciplines-llista{margin-top:30px}
.disc-item{display:block;padding:20px 0;border-bottom:1px solid var(--vora);transition:padding-left .25s var(--ease)}
a.disc-item:hover{padding-left:12px}
.disc-item strong{text-transform:lowercase;font-size:1.05rem}
a.disc-item strong{color:var(--granat-viu)}
.disc-item span{display:block;color:var(--gris);font-weight:400;font-size:var(--text);margin-top:4px}
details.faq{border-bottom:1px solid var(--vora)}
.faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:18px;padding:20px 0;font-weight:600;font-size:1.05rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";color:var(--granat-viu);font-size:1.4rem;font-weight:400;flex-shrink:0;transition:transform .3s var(--ease)}
.faq[open] summary::after{transform:rotate(45deg)}
.faq .resposta{font-size:var(--text);color:var(--gris);font-weight:400;padding:0 0 22px;max-width:680px}
.cta-final{background:rgba(18,18,18,.7);border:1px solid var(--vora);border-radius:20px;padding:44px 5vw;text-align:center;margin:70px auto 0;max-width:1100px}
.cta-final h2{margin-bottom:14px}
.cta-final p{font-size:var(--text);color:var(--gris);font-weight:400;margin-bottom:28px}
.boto{display:inline-flex;align-items:center;gap:10px;padding:15px 32px;border-radius:100px;font-size:var(--text);font-weight:600;text-transform:lowercase;letter-spacing:.03em;transition:background .3s,border-color .3s;cursor:pointer;border:0;font-family:inherit;margin:6px}
.boto-ple{background:var(--granat-viu);color:var(--blanc)}
.boto-ple:hover{background:var(--granat-viu)}
.boto-buit{border:1px solid var(--vora);color:var(--blanc);background:transparent}
.boto-buit:hover{border-color:var(--blanc)}
.accions{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2px;background:var(--vora);margin-top:34px;border-radius:16px;overflow:hidden;text-align:left}
.accio{background:var(--gris-fosc);padding:24px 22px;display:flex;flex-direction:column;align-items:flex-start;gap:8px;transition:background .3s}
.accio:hover{background:var(--granat-fosc)}
.accio svg{width:26px;height:26px;fill:var(--granat-viu)}
.accio strong{text-transform:lowercase;font-size:1.05rem;font-weight:800}
.accio small{color:var(--gris);font-size:var(--text);font-weight:400;line-height:1.4}
.relacionats{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}
.relacionats a{border:1px solid var(--vora);border-radius:100px;padding:10px 22px;font-size:var(--text);font-weight:600;text-transform:lowercase;color:var(--gris);transition:all .3s}
.relacionats a:hover{border-color:var(--granat-viu);color:var(--blanc)}
footer.peu{border-top:1px solid var(--vora);padding:34px 5vw;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;font-size:var(--text);color:var(--gris);margin-top:80px}
footer.peu a.actiu{color:var(--blanc)}
/* selector d'idioma al peu: dropdown cap amunt (desktop) i cat/es (mobil) */
.idioma-peu{margin:0 0 0 3vw;display:inline-flex;position:relative;cursor:pointer;vertical-align:middle}
.idioma-peu .idioma-menu{top:auto;bottom:100%;padding-top:0;padding-bottom:14px}
.peu-idioma-mobil{display:none}
.reveal{opacity:0;transform:translateY(36px);transition:opacity .9s var(--ease),transform .9s var(--ease)}
.reveal.vist{opacity:1;transform:none}
@media (max-width:700px){
  :root{--text:1.15rem;--text-vermells:1rem}
  .nav-links{display:none}
  .idioma-mobil{display:flex;gap:8px;align-items:center;position:absolute;top:18px;right:5vw;z-index:120;font-size:var(--text);font-weight:400}
  .idioma-mobil a{color:var(--gris)}
  .idioma-mobil a.actiu{color:var(--blanc)}
  .idioma-mobil span{color:var(--gris)}
  .idioma-peu{display:none}
  .peu-idioma-mobil{display:flex;width:100%;justify-content:center;gap:6px;align-items:center;margin-top:8px}
  header.capsal{padding-top:110px}
  h2{font-size:2.35rem}
  .classe-fila{display:flex;flex-wrap:wrap;align-items:center;gap:2px 12px}
  .classe-fila .sala{flex:0 0 auto}
  .classe-fila .dia{width:100%}
  .classe-fila .nom{flex:1 1 auto}
  footer.peu{flex-direction:column;text-align:center;justify-content:center}
  .fila-h{grid-template-columns:66px 1fr auto;gap:10px}
  .taula-preus th,.taula-preus td{padding:12px 6px}
  .accions{grid-template-columns:repeat(2,1fr)}
  .accio:last-child:nth-child(odd){grid-column:1/-1}
  .accio{padding:20px 16px}
}
@media (prefers-reduced-motion:reduce){*{transition-duration:.01ms!important}.reveal{opacity:1;transform:none}}
"""

JS = """
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('solida',scrollY>40),{passive:true});
const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vist');obs.unobserve(e.target)}}),{threshold:.12,rootMargin:'0px 0px -6% 0px'});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));
"""


def esc(t):
    return html.escape(t, quote=True)


def bloc_horaris(p):
    if not p.get("horaris"):
        return ""
    files = "\n".join(
        f'      <div class="classe-fila"><span class="dia">{esc(d)}</span><span class="hora">{esc(h)}</span>'
        f'<span class="nom">{esc(g)}</span><span class="sala">{esc(s)}</span></div>'
        for d, h, g, s in p["horaris"]
    )
    return f"""
  <section class="reveal">
    <div class="etiqueta">curs {CURS}</div>
    <h2>horaris de {esc(p["nom"])}</h2>
{files}
    <p class="nota-curs">Consulta la <a href="/horaris/">graella completa de l'escola</a> amb tots els estils i sales. Per confirmar plaça: truca'ns al <a href="tel:{TEL_LINK}">{TEL}</a>, escriu-nos per <a href="https://wa.me/34934179886?text={urllib.parse.quote(f"Hola! M'agradaria informació sobre les classes de {p.get('nom_wa', p['nom'])} ")[:-3]}" target="_blank" rel="noopener">WhatsApp</a> o pel <a href="/#contacte">formulari de contacte</a>.</p>
  </section>"""


def bloc_disciplines(p):
    if not p.get("disciplines"):
        return ""
    items = []
    for nom, slug, descr in p["disciplines"]:
        if slug:
            items.append(
                f'      <a class="disc-item" href="/{slug}/"><strong>{esc(nom)} →</strong><span>{esc(descr)}</span></a>')
        else:
            items.append(
                f'      <div class="disc-item"><strong>{esc(nom)}</strong><span>{esc(descr)}</span></div>')
    return f"""
  <section class="reveal">
    <div class="etiqueta">estils</div>
    <h2>disciplines per triar</h2>
    <div class="disciplines-llista">
{chr(10).join(items)}
    </div>
  </section>"""


def bloc_beneficis(p):
    caixes = "\n".join(
        f'      <div class="benefici"><h3>{esc(t)}</h3><p>{esc(x)}</p></div>'
        for t, x in p["beneficis"]
    )
    return f"""
  <section class="reveal">
    <div class="etiqueta">per què t'agradarà</div>
    <h2>beneficis</h2>
    <div class="beneficis">
{caixes}
    </div>
  </section>"""


def cap(t):
    return t[0].upper() + t[1:]


def bloc_faqs(p):
    dets = "\n".join(
        f'    <details class="faq reveal"><summary>{esc(cap(q))}</summary><p class="resposta">{esc(a)}</p></details>'
        for q, a in p["faqs"]
    )
    return f"""
  <section>
    <div class="etiqueta reveal">preguntes freqüents</div>
    <h2 class="reveal">dubtes habituals</h2>
{dets}
  </section>"""


def bloc_relacionats(p):
    per_slug = {x["slug"]: x for x in PAGINES}
    enll = "\n".join(
        f'      <a href="/{s}/">{esc(per_slug[s]["nom"])}</a>'
        for s in p.get("related", []) if s in per_slug
    )
    return f"""
  <section class="reveal">
    <div class="etiqueta">segueix explorant</div>
    <h2>també et pot agradar</h2>
    <div class="relacionats">
{enll}
    </div>
  </section>"""


# ─────────────────────────────────────────────────────────────────────────────
# GRAELLA COMPLETA DEL CURS (font única per a /horaris/) — (hora, activitat, grup, sala)
# ─────────────────────────────────────────────────────────────────────────────
GRAELLA = {
    "dilluns": [
        ("11.00", "barre", "", "sala C"), ("17.00", "jazz", "infantil A", "sala C"),
        ("17.30", "hip-hop", "infantil B", "sala H"), ("17.30", "clàssic", "infantil A", "sala C"),
        ("18.30", "jazz", "adults bàsic", "sala H"), ("18.30", "jazz", "infantil D", "sala N"),
        ("18.30", "clàssic puntes", "juvenil B", "sala C"), ("19.30", "clàssic", "adults avançat", "sala H"),
        ("19.30", "fit dance", "", "sala N"), ("19.30", "clàssic", "adults iniciació", "sala C"),
        ("20.30", "contemporani", "adults avançat", "sala H"), ("20.30", "femme empower", "adults intermedi", "sala N"),
    ],
    "dimarts": [
        ("17.15", "jazz", "infantil A", "sala N"), ("17.30", "clàssic", "juvenil A", "sala H"),
        ("17.30", "iniciació dansa", "grup B", "sala C"), ("18.30", "clàssic", "juvenil C", "sala H"),
        ("18.30", "hip-hop", "infantil C", "sala N"), ("18.30", "claqué", "adults intermedi", "sala C"),
        ("19.45", "hip-hop", "juvenil C", "sala H"), ("19.45", "claqué", "juvenil A", "sala N"),
        ("19.45", "clàssic", "adults intermedi", "sala C"), ("20.30", "heels", "adults avançat", "sala H"),
        ("20.30", "dansa del ventre", "juvenil avançat", "sala N"), ("20.30", "ioga", "", "sala C"),
    ],
    "dimecres": [
        ("11.00", "barre", "", "sala C"), ("17.15", "clàssic", "juvenil B", "sala H"),
        ("17.30", "jazz", "infantil C", "sala N"), ("17.30", "iniciació dansa", "grup B", "sala C"),
        ("18.15", "contemporani", "juvenil B", "sala H"), ("18.30", "clàssic", "infantil B", "sala N"),
        ("18.30", "clàssic", "adults iniciació", "sala C"), ("19.30", "clàssic", "adults avançat", "sala H"),
        ("19.30", "zumba", "", "sala N"), ("19.30", "espanyol", "juvenil intermedi", "sala C"),
        ("20.30", "contemporani", "adults intermedi", "sala H"), ("20.30", "hip-hop", "adults avançat", "sala N"),
        ("20.30", "espanyol", "adults intermedi", "sala C"),
    ],
    "dijous": [
        ("17.30", "contemporani", "juvenil A", "sala H"), ("17.30", "clàssic", "infantil C", "sala N"),
        ("17.30", "hip-hop", "juvenil B", "sala C"), ("18.30", "clàssic", "juvenil C", "sala H"),
        ("18.30", "hip-hop", "infantil A", "sala N"), ("18.30", "claqué", "adults intermedi", "sala C"),
        ("19.30", "contemporani", "juvenil C", "sala H"), ("19.45", "clàssic", "adults intermedi", "sala C"),
        ("20.30", "jazz", "adults intermedi", "sala H"), ("20.30", "dansa del ventre", "adults avançat", "sala N"),
        ("20.30", "ioga", "", "sala C"),
    ],
    "divendres": [
        ("17.15", "formació escènica", "jazz, hip-hop, claqué, cant i interpretació", "sales H+N"),
        ("17.30", "contemporani", "infantil B", "sala H"), ("17.30", "jazz", "juvenil A", "sala N"),
        ("17.30", "k-pop", "juvenil A", "sala C"), ("18.30", "contemporani", "juvenil A", "sala H"),
        ("18.30", "musical", "infantil", "sala N"), ("19.45", "hip-hop", "juvenil A", "sala H"),
        ("19.45", "interpretació", "infantil", "sala N"),
    ],
}

# TARIFES DEL CURS (font única per a /preus/) — files: (concepte, 1 dia, 2, 3, 4)
TARIFA_MENSUAL = [
    ("infantil", "56 €", "68 €", "80 €", "92 €"),
    ("adults · fins 1 h", "60 €", "73 €", "85 €", "99 €"),
    ("adults · més d'1 h", "65 €", "81 €", "92 €", "104 €"),
]
TARIFA_TRIMESTRAL = [
    ("infantil", "162 €", "197 €", "232 €", "267 €"),
    ("adults · fins 1 h", "174 €", "212 €", "247 €", "288 €"),
    ("adults · més d'1 h", "189 €", "235 €", "267 €", "302 €"),
]
TARIFA_ALTRES = [
    ("matrícula alumnes antics", "65 €"),
    ("matrícula nous alumnes", "70 €"),
    ("formació escènica kids & teens", "85 €/mes · 247 €/trim"),
    ("balls de saló (10 sessions)", "180 €/persona"),
]

ICONA_TEL = '<path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/>'
ICONA_WA = '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>'
ICONA_FORM = '<path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>'
ICONA_PIN = '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 1 1 0-5 2.5 2.5 0 0 1 0 5z"/>'
MAPS_DIR = "https://www.google.com/maps/dir/?api=1&amp;destination=Escola%20de%20Dansa%20Cristina%20Colom%C3%A9%2C%20Carrer%20de%20Craywinckel%2025%2C%2008022%20Barcelona"


def accio(href, icona, titol, detall, extern=False):
    blank = ' target="_blank" rel="noopener"' if extern else ''
    return (f'      <a class="accio" href="{href}"{blank}>'
            f'<svg viewBox="0 0 24 24" aria-hidden="true">{icona}</svg>'
            f'<strong>{titol}</strong><small>{detall}</small></a>')


def accions_cta(p):
    targetes = [accio(f"tel:{TEL_LINK}", ICONA_TEL, "truca'ns", TEL)]
    if WHATSAPP_ACTIU:
        text = urllib.parse.quote(f"Hola! M'agradaria informació sobre les classes de {p.get('nom_wa', p['nom'])}")
        targetes.append(accio(f"https://wa.me/34934179886?text={text}", ICONA_WA,
                              "whatsapp", "resposta al moment", extern=True))
    targetes.append(accio("/#escriu-nos", ICONA_FORM, "formulari", "explica'ns què busques"))
    targetes.append(accio(MAPS_DIR, ICONA_PIN, "com arribar?", "craywinckel, 25", extern=True))
    return '    <div class="accions">\n' + '\n'.join(targetes) + '\n    </div>'


def json_ld(p):
    if p.get("ld"):
        return p["ld"]
    url = f"{DOMINI}/{p['slug']}/"
    graph = [
        {
            "@type": "Course",
            "@id": url + "#curs",
            "name": f"Classes de {p['nom']} a Barcelona",
            "description": p["desc"],
            "url": url,
            "inLanguage": "ca",
            "provider": {
                "@type": "School",
                "name": "Escola de Dansa Cristina Colomé",
                "url": DOMINI + "/",
                "telephone": "+34934179886",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Carrer de Craywinckel, 25",
                    "addressLocality": "Barcelona",
                    "postalCode": "08022",
                    "addressCountry": "ES",
                },
            },
            "offers": {
                "@type": "Offer",
                "category": "Quota mensual",
                "priceCurrency": "EUR",
                "price": "56",
                "description": "Quotes mensuals des de 56 €. Primera classe de prova gratuïta.",
            },
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "inici", "item": DOMINI + "/"},
                {"@type": "ListItem", "position": 2, "name": "activitats", "item": DOMINI + "/#activitats"},
                {"@type": "ListItem", "position": 3, "name": p["nom"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": cap(q),
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faqs"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=1)


def cos_estandard(p):
    return f"""
  <section class="reveal">
    <div class="etiqueta">per a qui</div>
    <h2>a qui va dirigida</h2>
    <p class="text-gran">{esc(p["per_a_qui"])}</p>
  </section>
{bloc_beneficis(p)}{bloc_horaris(p)}{bloc_disciplines(p)}
  <section class="reveal">
    <div class="etiqueta">tarifes</div>
    <h2>preus</h2>
    <p class="text-gran">Les classes funcionen per quota mensual o trimestral segons els dies per setmana: des de 56 €/mes (infantil) i 60 €/mes (adults). Consulta <a href="/preus/" style="color:var(--granat-viu);font-weight:600">totes les tarifes del curs</a> — i recorda que la primera classe de prova és gratuïta.</p>
  </section>
{bloc_faqs(p)}{bloc_relacionats(p)}"""


def cos_horaris():
    dies = []
    for dia, files in GRAELLA.items():
        fs = "\n".join(
            f'      <div class="fila-h"><span class="hora">{esc(h)}</span>'
            f'<span class="nom">{esc(nom)}{f"<small>{esc(grup)}</small>" if grup else ""}</span>'
            f'<span class="sala">{esc(sala)}</span></div>'
            for h, nom, grup, sala in files
        )
        dies.append(f'''
  <section class="reveal">
    <h2 class="dia-titol">{dia}</h2>
{fs}
  </section>''')
    return "".join(dies) + f'''
  <section class="reveal">
    <p class="text-gran">Cada activitat té la seva pàgina amb horaris, beneficis i preguntes: mira-les totes a <a href="/#activitats" style="color:var(--granat-viu);font-weight:600">activitats</a>. I si tens dubtes de nivell o de grup, truca'ns al <a href="tel:{TEL_LINK}" style="color:var(--granat-viu);font-weight:600">{TEL}</a> i t'orientem.</p>
  </section>'''


def taula(caption, capcalera, files):
    cap_html = f"<thead><tr>{''.join(f'<th>{esc(c)}</th>' for c in capcalera)}</tr></thead>" if capcalera else ""
    cos = "\n".join(
        "      <tr>" + f"<td>{esc(f[0])}</td>" + "".join(f'<td class="preu">{esc(v)}</td>' for v in f[1:]) + "</tr>"
        for f in files
    )
    return f'''
    <table class="taula-preus">
      <caption>{esc(caption)}</caption>
      {cap_html}
      <tbody>
{cos}
      </tbody>
    </table>'''


def cos_preus():
    capc = ["", "1 dia", "2 dies", "3 dies", "4 dies"]
    return f'''
  <section class="reveal">
{taula("quota mensual", capc, TARIFA_MENSUAL)}
{taula("quota trimestral", capc, TARIFA_TRIMESTRAL)}
{taula("matrícula i altres", None, TARIFA_ALTRES)}
    <p class="text-gran" style="margin-top:30px">També oferim <strong>classes particulars</strong>, classes especials per a celebracions (casaments, comiats, aniversaris) i tallers de cap de setmana o de vacances (Nadal, Setmana Santa i estiu). I novetat: vine a celebrar el teu aniversari amb nosaltres!</p>
  </section>'''


LD_BREADCRUMB = lambda nom, slug: json.dumps({
    "@context": "https://schema.org",
    "@graph": [{
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "inici", "item": DOMINI + "/"},
            {"@type": "ListItem", "position": 2, "name": nom, "item": f"{DOMINI}/{slug}/"},
        ],
    }],
}, ensure_ascii=False, indent=1)

PAGINES += [
    {
        "slug": "horaris",
        "nom": "horaris",
        "title": f"horaris de les classes · curs {CURS} · escola de dansa cristina colomé",
        "desc": f"Tots els horaris de les classes de dansa del curs {CURS} a l'escola Cristina Colomé (Sant Gervasi, Barcelona): dia a dia, per activitat, grup i sala.",
        "h1": "horaris",
        "intro": f"La graella completa del curs {CURS}, dia a dia: tardes per a infantils i juvenils, vespres per a adults i matins de barre. Sales H, N i C.",
        "etiqueta_capsal": f"curs {CURS} · graella completa",
        "molla_mig": "",
        "nom_wa": "dansa",
        "cos": None,  # s'omple més avall (necessita les funcions)
        "ld": None,
    },
    {
        "slug": "preus",
        "nom": "preus",
        "title": f"preus i tarifes · curs {CURS} · escola de dansa cristina colomé",
        "desc": f"Tarifes del curs {CURS} de l'escola de dansa Cristina Colomé (Barcelona): quotes mensuals i trimestrals segons dies per setmana, matrícula i cursos especials. 1a classe gratuïta.",
        "h1": "preus",
        "intro": f"Les tarifes del curs {CURS}: paga per mes o per trimestre, amb 1, 2, 3 o 4 dies de classe a la setmana. La primera classe de prova és gratuïta.",
        "etiqueta_capsal": f"curs {CURS} · tarifes",
        "molla_mig": "",
        "nom_wa": "dansa",
        "cos": None,
        "ld": None,
    },
]
PAGINES[-2]["cos"] = cos_horaris()
PAGINES[-2]["ld"] = LD_BREADCRUMB("horaris", "horaris")
PAGINES[-1]["cos"] = cos_preus()
PAGINES[-1]["ld"] = LD_BREADCRUMB("preus", "preus")

# og:image pròpia per a les disciplines amb clip real de l'escola (fotogrames del Dia de la Dansa)
OG_PROPIS = {
    "jazz": "og-jazz.jpg",
    "dansa-contemporania": "og-dansa-contemporania.jpg",
    "hip-hop": "og-hip-hop.jpg",
    "dansa-oriental": "og-dansa-oriental.jpg",
    "formacio-escenica": "og-formacio-escenica.jpg",
}
for _p in PAGINES:
    if _p["slug"] in OG_PROPIS:
        _p["og"] = f"{DOMINI}/assets/{OG_PROPIS[_p['slug']]}"


def genera(p):
    url = f"{DOMINI}/{p['slug']}/"
    lang = p.get("lang", "ca")
    if lang == "ca":
        url_ca = url
        url_es = f"{DOMINI}/es/{SLUG_ES[p['slug']]}/"
    else:
        url_ca = f"{DOMINI}/{p['slug_ca']}/"
        url_es = url
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ca" href="{url_ca}">
<link rel="alternate" hreflang="es" href="{url_es}">
<link rel="alternate" hreflang="x-default" href="{url_ca}">
<meta name="theme-color" content="#0a0a0a">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Escola de Dansa Cristina Colomé">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{p.get("og", DOMINI + "/assets/og-escola.jpg")}">
<meta property="og:locale" content="{'es_ES' if lang == 'es' else 'ca_ES'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{p.get("og", DOMINI + "/assets/og-escola.jpg")}">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="512x512" href="/assets/favicon-512.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,600;0,800;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">
{json_ld(p)}
</script>
</head>
<body>

<nav id="nav">
  <a class="nav-marca" href="/">escola de dansa cristina colomé</a>
  <div class="nav-links">
    <a href="/#escola">l'escola</a>
    <a href="/#activitats">activitats</a>
    <a href="/horaris/">horaris</a>
    <a href="/preus/">preus</a>
    <a href="/#newsletter">newsletter</a>
    <a href="/#contacte">contacte</a>
    <div class="idioma" tabindex="0">
      <span class="idioma-etiq">idioma</span>
      <div class="idioma-menu">
        <a href="{url_ca}" hreflang="ca"{' class="actiu"' if lang == 'ca' else ''}>Català</a>
        <a href="{url_es}" hreflang="es"{' class="actiu"' if lang == 'es' else ''}>Castellano</a>
      </div>
    </div>
  </div>
</nav>

<div class="idioma-mobil" aria-label="Idioma">
  <a href="{url_ca}"{' class="actiu"' if lang == 'ca' else ''}>cat</a><span>/</span><a href="{url_es}"{' class="actiu"' if lang == 'es' else ''}>es</a>
</div>

<main>
  <header class="capsal">
    <p class="molla"><a href="/">inici</a> · {p.get("molla_mig", '<a href="/#activitats">activitats</a> · ')}<span>{esc(p["nom"])}</span></p>
    <div class="etiqueta">{p.get("etiqueta_capsal", "classes a barcelona · sant gervasi")}</div>
    <h1>{esc(p["h1"])}</h1>
    <p class="entradeta">{esc(p["intro"])}</p>
  </header>
{p.get("cos") or cos_estandard(p)}
  <div class="cta-final reveal">
    <h2>vine a provar-ho: la primera classe és gratis</h2>
    <p>Tria com t'estimes més: truca'ns, escriu-nos o vine a veure'ns. Sense compromís, t'ajudem a trobar el grup perfecte.</p>
{accions_cta(p)}
  </div>
</main>

<footer class="peu">
  <span>escola de dansa cristina colomé</span>
  <span>craywinckel, 25 · 08022 barcelona · <a href="tel:{TEL_LINK}">{TEL}</a><span class="idioma idioma-peu" tabindex="0"><span class="idioma-etiq">idioma</span><span class="idioma-menu"><a href="{url_ca}" hreflang="ca"{' class="actiu"' if lang == 'ca' else ''}>Català</a><a href="{url_es}" hreflang="es"{' class="actiu"' if lang == 'es' else ''}>Castellano</a></span></span><span class="peu-idioma-mobil"><a href="{url_ca}"{' class="actiu"' if lang == 'ca' else ''}>cat</a><span>/</span><a href="{url_es}"{' class="actiu"' if lang == 'es' else ''}>es</a></span></span>
</footer>

<script>{JS}</script>
</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# VERSIÓ EN CASTELLÀ (/es/) — contingut a traduccions_es.py, cadenes fixes aquí
# ─────────────────────────────────────────────────────────────────────────────
from traduccions_es import TRADUCCIONS_ES  # noqa: E402


def _trad_grup(s):
    for a, b in [("adults bàsic", "adultos básico"), ("adults avançat", "adultos avanzado"),
                 ("adults intermedi", "adultos intermedio"), ("adults iniciació", "adultos iniciación"),
                 ("juvenil avançat", "juvenil avanzado"), ("juvenil intermedi", "juvenil intermedio"),
                 ("grup ", "grupo "), ("jazz, hip-hop, claqué, cant i interpretació",
                                       "jazz, hip-hop, claqué, canto e interpretación")]:
        s = s.replace(a, b)
    return s


TRAD_ACT = {"clàssic": "clásico", "clàssic puntes": "clásico puntas", "iniciació dansa": "iniciación danza",
            "contemporani": "contemporáneo", "espanyol": "español", "dansa del ventre": "danza del vientre",
            "ioga": "yoga", "interpretació": "interpretación", "formació escènica": "formación escénica"}
TRAD_DIES = {"dilluns": "lunes", "dimarts": "martes", "dimecres": "miércoles",
             "dijous": "jueves", "divendres": "viernes"}


def cos_horaris_es():
    dies = []
    for dia, files in GRAELLA.items():
        fs = "\n".join(
            f'      <div class="fila-h"><span class="hora">{esc(h)}</span>'
            f'<span class="nom">{esc(TRAD_ACT.get(nom, nom))}{f"<small>{esc(_trad_grup(grup))}</small>" if grup else ""}</span>'
            f'<span class="sala">{esc(sala.replace("sales", "salas"))}</span></div>'
            for h, nom, grup, sala in files
        )
        dies.append(f'''
  <section class="reveal">
    <h2 class="dia-titol">{TRAD_DIES[dia]}</h2>
{fs}
  </section>''')
    return "".join(dies) + f'''
  <section class="reveal">
    <p class="text-gran">Cada actividad tiene su propia página con horarios, beneficios y preguntas: míralas todas en <a href="/es/#activitats" style="color:var(--granat-viu);font-weight:600">actividades</a>. Y si tienes dudas de nivel o de grupo, llámanos al <a href="tel:{TEL_LINK}" style="color:var(--granat-viu);font-weight:600">{TEL}</a> y te orientamos.</p>
  </section>'''


def cos_preus_es():
    capc = ["", "1 día", "2 días", "3 días", "4 días"]
    men = [("infantil",) + f[1:] if f[0] == "infantil" else
           ("adultos · hasta 1 h",) + f[1:] if "fins" in f[0] else
           ("adultos · más de 1 h",) + f[1:] for f in TARIFA_MENSUAL]
    tri = [("infantil",) + f[1:] if f[0] == "infantil" else
           ("adultos · hasta 1 h",) + f[1:] if "fins" in f[0] else
           ("adultos · más de 1 h",) + f[1:] for f in TARIFA_TRIMESTRAL]
    alt = [("matrícula antiguos alumnos", TARIFA_ALTRES[0][1]),
           ("matrícula nuevos alumnos", TARIFA_ALTRES[1][1]),
           ("formación escénica kids & teens", TARIFA_ALTRES[2][1].replace("mes", "mes").replace("trim", "trim")),
           ("bailes de salón (10 sesiones)", TARIFA_ALTRES[3][1].replace("persona", "persona"))]
    return f'''
  <section class="reveal">
{taula("cuota mensual", capc, men)}
{taula("cuota trimestral", capc, tri)}
{taula("matrícula y otros", None, alt)}
    <p class="text-gran" style="margin-top:30px">También ofrecemos <strong>clases particulares</strong>, clases especiales para celebraciones (bodas, despedidas, cumpleaños) y talleres de fin de semana o de vacaciones (Navidad, Semana Santa y verano). Y novedad: ¡ven a celebrar tu cumpleaños con nosotros!</p>
  </section>'''


LD_BREADCRUMB_ES = lambda nom, slug_es: json.dumps({
    "@context": "https://schema.org",
    "@graph": [{
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "inicio", "item": DOMINI + "/es/"},
            {"@type": "ListItem", "position": 2, "name": nom, "item": f"{DOMINI}/es/{slug_es}/"},
        ],
    }],
}, ensure_ascii=False, indent=1)

# contingut generat de les pàgines custom ES
TRADUCCIONS_ES["horaris"]["cos"] = cos_horaris_es()
TRADUCCIONS_ES["horaris"]["ld"] = LD_BREADCRUMB_ES("horarios", "horarios")
TRADUCCIONS_ES["preus"]["cos"] = cos_preus_es()
TRADUCCIONS_ES["preus"]["ld"] = LD_BREADCRUMB_ES("precios", "precios")

_WA_CA = urllib.parse.quote("Hola! M'agradaria informació sobre les classes de ")
_WA_ES = urllib.parse.quote("¡Hola! Me gustaría información sobre las clases de ")

_FIXOS_ES = None


def fixos_es():
    """Parelles (ca, es) per a les cadenes fixes de la plantilla. Ordre: enllaços primer."""
    global _FIXOS_ES
    if _FIXOS_ES is not None:
        return _FIXOS_ES
    parelles = [(f'href="/{ca}/"', f'href="/es/{es}/"') for ca, es in SLUG_ES.items()]
    parelles += [
        ('href="/#activitats"', 'href="/es/#activitats"'),
        ('href="/#escola"', 'href="/es/#escola"'),
        ('href="/#contacte"', 'href="/es/#contacte"'),
        ('href="/#escriu-nos"', 'href="/es/#escriu-nos"'),
        ('href="/#newsletter"', 'href="/es/#newsletter"'),
        ('class="nav-marca" href="/"', 'class="nav-marca" href="/es/"'),
        ('<p class="molla"><a href="/">inici</a>', '<p class="molla"><a href="/es/">inicio</a>'),
        (">l'escola</a>", '>la escuela</a>'),
        ('>activitats</a>', '>actividades</a>'),
        ('>horaris</a>', '>horarios</a>'),
        ('>preus</a>', '>precios</a>'),
        ('>contacte</a>', '>contacto</a>'),
        ('classes a barcelona · sant gervasi', 'clases de danza en barcelona · sant gervasi'),
        ('<div class="etiqueta">per a qui</div>', '<div class="etiqueta">para quién</div>'),
        ('<h2>a qui va dirigida</h2>', '<h2>a quién va dirigida</h2>'),
        ('<div class="etiqueta">per què t\'agradarà</div>', '<div class="etiqueta">por qué te gustará</div>'),
        ('<h2>beneficis</h2>', '<h2>beneficios</h2>'),
        (f'<div class="etiqueta">curs {CURS}</div>', f'<div class="etiqueta">curso {CURS}</div>'),
        ('<h2>horaris de ', '<h2>horarios de '),
        ("graella completa de l'escola</a> amb tots els estils i sales. Per confirmar plaça: truca'ns al",
         'parrilla completa de la escuela</a> con todos los estilos y salas. Para confirmar plaza: llámanos al'),
        (', escriu-nos per <a', ', escríbenos por <a'),
        ('>WhatsApp</a> o pel <a', '>WhatsApp</a> o por el <a'),
        ('>formulari de contacte</a>.', '>formulario de contacto</a>.'),
        ('<div class="etiqueta">estils</div>', '<div class="etiqueta">estilos</div>'),
        ('<h2>disciplines per triar</h2>', '<h2>disciplinas para elegir</h2>'),
        ('<div class="etiqueta reveal">preguntes freqüents</div>', '<div class="etiqueta reveal">preguntas frecuentes</div>'),
        ('<h2 class="reveal">dubtes habituals</h2>', '<h2 class="reveal">dudas habituales</h2>'),
        ('<div class="etiqueta">segueix explorant</div>', '<div class="etiqueta">sigue explorando</div>'),
        ('<h2>també et pot agradar</h2>', '<h2>también te puede gustar</h2>'),
        ('<div class="etiqueta">tarifes</div>', '<div class="etiqueta">tarifas</div>'),
        ('<h2>preus</h2>', '<h2>precios</h2>'),
        ('Les classes funcionen per quota mensual o trimestral segons els dies per setmana: des de 56 €/mes (infantil) i 60 €/mes (adults). Consulta <a href="/es/precios/" style="color:var(--granat-viu);font-weight:600">totes les tarifes del curs</a> — i recorda que la primera classe de prova és gratuïta.',
         'Las clases funcionan por cuota mensual o trimestral según los días por semana: desde 56 €/mes (infantil) y 60 €/mes (adultos). Consulta <a href="/es/precios/" style="color:var(--granat-viu);font-weight:600">todas las tarifas del curso</a> — y recuerda que la primera clase de prueba es gratuita.'),
        ('<h2>vine a provar-ho: la primera classe és gratis</h2>', '<h2>ven a probarlo: la primera clase es gratis</h2>'),
        ("<p>Tria com t'estimes més: truca'ns, escriu-nos o vine a veure'ns. Sense compromís, t'ajudem a trobar el grup perfecte.</p>",
         '<p>Elige como prefieras: llámanos, escríbenos o ven a vernos. Sin compromiso, te ayudamos a encontrar el grupo perfecto.</p>'),
        ("<strong>truca'ns</strong>", '<strong>llámanos</strong>'),
        ("<strong>formulari</strong><small>explica'ns què busques</small>", '<strong>formulario</strong><small>cuéntanos qué buscas</small>'),
        ('<strong>com arribar?</strong>', '<strong>¿cómo llegar?</strong>'),
        ('<small>resposta al moment</small>', '<small>respuesta al momento</small>'),
        (_WA_CA, _WA_ES),
        # JSON-LD: breadcrumb i idioma
        ('"name": "inici", "item": "https://escoladansa.com/"', '"name": "inicio", "item": "https://escoladansa.com/es/"'),
        ('"name": "activitats", "item": "https://escoladansa.com/#activitats"', '"name": "actividades", "item": "https://escoladansa.com/es/#activitats"'),
        ('"inLanguage": "ca"', '"inLanguage": "es"'),
    ]
    # etiquetes dels xips de "relacionats": nom CA -> nom ES
    for slug, t in TRADUCCIONS_ES.items():
        nom_ca = next((x["nom"] for x in PAGINES if x["slug"] == slug), None)
        if nom_ca and t.get("nom") and nom_ca != t["nom"]:
            parelles.append((f'/">{nom_ca}</a>', f'/">{t["nom"]}</a>'))
    _FIXOS_ES = parelles
    return parelles


def genera_es(p):
    t = TRADUCCIONS_ES[p["slug"]]
    p2 = {**p, **t, "lang": "es", "slug_ca": p["slug"], "slug": f"es/{SLUG_ES[p['slug']]}"}
    if p2.get("horaris"):
        def _tc(g):
            for k in sorted(TRAD_ACT, key=len, reverse=True):
                g = g.replace(k, TRAD_ACT[k])
            return _trad_grup(g)
        p2["horaris"] = [(TRAD_DIES[d], h, _tc(g), s.replace("sales", "salas"))
                         for d, h, g, s in p2["horaris"]]
    pagina = genera(p2)
    for a, b in fixos_es():
        pagina = pagina.replace(a, b)
    return pagina


def main():
    for p in PAGINES:
        carpeta = os.path.join(ARREL, p["slug"])
        os.makedirs(carpeta, exist_ok=True)
        desti = os.path.join(carpeta, "index.html")
        with open(desti, "w", encoding="utf-8") as f:
            f.write(genera(p))
        # versió en castellà
        if p["slug"] in TRADUCCIONS_ES:
            carpeta_es = os.path.join(ARREL, "es", SLUG_ES[p["slug"]])
            os.makedirs(carpeta_es, exist_ok=True)
            with open(os.path.join(carpeta_es, "index.html"), "w", encoding="utf-8") as f:
                f.write(genera_es(p))
    n_es = len([p for p in PAGINES if p["slug"] in TRADUCCIONS_ES])
    print(f"{len(PAGINES)} pàgines CA + {n_es} pàgines ES generades a {ARREL}")


if __name__ == "__main__":
    main()
