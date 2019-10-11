# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image bar3 = "bar.jpg"
image Elise heureuse = "sprite female dark hair Smi01.png"
image Elise heureuse 2 = "sprite female dark hair Smi02.png"
image Elise triste = "sprite female dark hair Sad01.png"
image Elise triste 2 = "sprite female dark hair Sad02.png"
image Elise neutre = "sprite female dark hair Neu01.png"
image Elise neutre 2 = "sprite female dark hair Neu02.png"
image Elise neutre 3 = "sprite female dark hair Neu03.png"
image Elise ennuyee = "sprite female dark hair Ann01.png"
image Elise ennuyee 2 = "sprite female dark hair Ann02.png"
image Elise enervee = "sprite female dark hair Ang01.png"
image Astrid heureuse = "sprite female beauty spot Smi01.png"
image Astrid heureuse 2 = "sprite female beauty spot Smi02.png"
image Astrid triste = "sprite female beauty spot Sad01.png"
image Astrid surprise = "sprite female beauty spot Sym01.png"
image Astrid complice = "sprite female beauty spot Win01.png"
image Astrid inquiete = "sprite female beauty spot Wor01.png"
image Anicet ennuye = "Sprite Male Beauty Spot Blond Ann01.png"
image Anicet concentre = "Sprite Male Beauty Spot Blond Con01.png"
image Anicet triste = "Sprite Male Beauty Spot Blond Sad01.png"
image Anicet malade = "Sprite Male Beauty Spot Blond Smi01.png"
image Anicet complice = "Sprite Male Beauty Spot Blond Win01.png"
image Alrik inquiet = "Sprite Male Dark Hair Ang01.png"
image Alrik ennuye = "Sprite Male Dark Hair Ann01.png"
image Alrik timide = "Sprite Male Dark Hair Apo01.png"
image Alrik content = "Sprite Male Dark Hair Con01.png"
image Alrik neutre = "Sprite Male Dark Hair Neu01.png"
image Alrik triste = "Sprite Male Dark Hair Sad01.png"
image Alrik sur = "Sprite Male Dark Hair Sly01.png"
image Alrik sur2 = "Sprite Male Dark Hair Sly02.png"
image Alrik souriant = "Sprite Male Dark Hair Smi01.png"
image Alrik souriant 2 ="Sprite Male Dark Hair Smi02.png"
image arbre ="arbre 2.jpg"
image arbre soleil ="arbre bercé par le soleil.jpg"
image route foret ="route foret 1.jpg"
image route foret 2 ="route foret 2.jpg"
image route foret 3 ="route foret 3.jpg"
image fond noir ="fond noir.jpg"

init python:
    renpy.music.register_channel("nature", "sfx", True)

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Elise' , color="#c8ffc8")
define al = Character('Alrik', color="#c8ffc8")
define an = Character('Anicet', color="#c8ffc8")
define as = Character('Astrid', color="#c8ffc8")
define me = Character('Messager')

label start:
scene arbre soleil
pause 3
with Dissolve(.5)
scene route foret 2
play music "zic/forêt mystique.mp3"
pause 3
scene route foret
with Dissolve(.5)

"Ca fait depuis plus de cinq foutues heures que je me trouve à errer dans cette forêt sans fin. La lettre me dit de suivre le chemin ou les cailloux sont tous alignés sur la droite."
"C'est curieux comme repère, mais au moins j'ai la certitude qu'un chemin m'attend à l'autre bout. Même si je ne sais pas ou je me trouve, je continue de marcher."
"Mes pieds me font mal, je n'arrête pas de me fouler dans des branches, je passe mon temps à enjamber des trous, j'ai peur que le sol s'effondre. L'idiot derrière ce chemin ne m'a pas l'air doué d'esprit."

scene fond noir
with  Dissolve (.5)

"Je m'appelle Alrik."

show Alrik souriant

"J'ai 31 ans, je suis détective professionnel. Je travaille dans l'agence internationale des détectives."
"C'est une organisation internationale qui vise à professionaliser les détectives de tous les coins du monde."
"J'ai dû passer un concours difficile pour y arriver, je suis passé par une classe préparatoire de deux ans."
"Puis j'ai débuté ma formation durant trois années."
"Les détectives ont besoin de plusieurs qualités pour être recrutés, il y'a en quelque sorte un profil type."
"Il faut être: sérieux, intelligent, faire preuve de sang froid, d'impartialité. Mon but est d'être le plus objectif et rationnel possible."
"Pour cela tous les détectives suivent un code précis composé de cinq règles."
"1. Le détective ne doit jamais ignorer la raison de l'action."
"2. Le détective ne doit jamais faire justice lui-même."
"3. Le détective ne doit jamais suivre ses émotions."
"4. Le détective ne doit jamais s'impliquer dans les affaires extérieures de son enquête."
"5. Le détective doit finalement toujours rester rationnel."

show Alrik neutre

"Ces règles sont...comment dire....difficilement applicables. En fait certaines sont plus simples à respecter que d'autres."
"Ce code de conduite est très strict, il est dirigé sans cesse sur l'idée de rationnalité."
"Et moi dans cette histoire ?"

show Alrik sur

"Je respecte presque à la lettre ces commandements. Je trouve que je suis bien plus efficace dans mon travail de cette façon."

show Alrik souriant2

"Bien sûr mes proches m'insultent tous de robot, bon à effectuer des tâches mécaniquements ! J'accorde beaucoup d'importance au professionnalisme."
"Mais bon ça ne m'empêche pas d'effectuer mon métier sérieusement. J'y prend beaucoup plus de plaisir que ce qu'ils peuvent penser."
"Je fais parti de la section criminelle. J'enquête principalement sur des meurtres, parfois je dois aussi résoudre des vols."
"J'aime énormément de choses dans mon métier. D'abord je prend beaucoup de plaisir à enquêter."
"J'adore réfléchir, relier les éléments entre eux, déduire, tirer des conclusions logiques...tout ce processus est très stimulant."
"Ensuite, je fais de la justice dans un sens. J'apporte les éléments nécessaires à la juridiction afin qu'elle soit la plus juste possible."
"Mon métier me demande de sortir, je déteste rester enfermer à remplir des papiers derrière un bureau."
"Puis...mes enquêtes ne sont jamais lassantes. Les modes opératoires, les raisons qui motivent une action, ces éléments sont sans cesse différent d'une affaire à l'autre."
"C'est pour toutes ces valeurs que j'aime mon poste."

show Alrik timide

"Je ne travaille pas que pour ces raisons-ci évidemment. J'ai une famille."
"Je suis marié à une femme adorable, on s'est rencontré durant ma classe préparatoire."
"Elle a arrêté au bout d'une année, elle s'est rendue compte que ces études ne lui convenaient pas."
"Suite à cela elle s'est convertie dans l'éducation pour faire instit. Les enfants sont sa passion."
"En parlant d'enfants...j'en ai deux."
"J'ai une fille de 7 ans, un garçon de 4 ans."
"Ma famille, c'est ce que j'aime le plus au monde, je serais toujours la pour eux."



scene route foret 3
with Dissolve (1.5)


"La forêt était plutôt joli, voir une telle harmonie entre les rayons du soleil et les branches des arbres rend la ballade plus agréable."
"Bordel, il fait une telle chaleur, pire que les canicules en plein été. Je meurs, il fait bien 38° ! Pourtant on est en plein hiver...le soleil est toujours aussi haut dans le ciel."
"Il n'a pas changé de place. A cette heure-ci, il devrait faire nuit."
"Au fond ça ne me dérange pas. L'été est ma saison favorite."
"Je n'aime pas la nuit, c'est moche et inquiétant. Je ne suis pas fait pour vivre à des heures tardives."

scene arbre
with Dissolve (1)
"Alors profiter d'une ambiance estivale en plein milieu d'une belle forêt, alors que suis censé être en hiver...je dis pas non."

pause 3

"J'aime la randonnée. Je supporte pas de rester assis et oisif. Quand j'enquête, j'ai l'habitude de beaucoup bouger."
"J'ai installé un podomètre sur mon tel, j'ai l'habitude de le regarder tous les soirs quand je rentre chez moi."
"Je considère avoir passé une mauvaise journée si je n'ai pas fait 8 000 pas..."
"Un lieu ou le soleil règne en maître...aucun endroits sur terre n'est pareil. Cet endroit, cette terre lointaine, ce n'est pas chez moi."
"Peut-être que la lettre...l'histoire du Messager...tout ça...c'est véridique. Je commence de plus en plus à y croire, j'étais si sceptique au début."

stop music fadeout 2.0

"Putain je suis trop con de m'être embarqué dans un tel délire."


scene fond noir
with Dissolve(1)
play nature "zic/bruitage train.mp3"


"Ma tête.....aaaaaAARRGH...! Elle me fait si mal !!!!"
"Mais...il fait tout noir"
"Je me relève pour voir ou je me trouve. Je me déplace avec l'aide de mes bras en avant afin de ne pas me cogner. Je réussi à palper des murs tout autour de moi."
"Je suis donc dans une pièce très petite...une cabine on dirait bien. Le sol est fait de planches de bois."


show Alrik ennuye at right
with fade


"Il faut que je trouve une porte...."
"Rien, il n'y a rien. Je vais rester ici à broyer du noir...?"
"Une poignée, je suis sauf ! Il suffit d'appuyer dessus...ah..ça ne bouge pas..."
"Peut-être qu'en forcant...gggggh....merde la poignée s'est barrée !"
"Mon dieu, je vais rester ici combien de temps..."
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH"
"Je décide de crier de toutes mes forces et de frapper contre la porte dans l'espoir que quelqu'un vienne me sauver.."


play music "zic/track inquiétante.mp3" fadeout 5.0

pause 5

"Hein c'est quoi cette lueur au loin...."
"Dieu merci vous pouvez m'aider à me sortir de ce trou ! Mais...vous êtes qui en fait....c'est quoi ce masque qui cache votre visage..."

me "Je suis le Messager."
"Attends, t'es celui qui m'a foutu dans ce bordel ?"
me "Je suis chargé de la correspondance entre la Terre Interdite et ton monde."
"Donc tu es le responsable......"
me "Oui, pour préserver les terres, je dois te faire passer via la Cellule. C'est un protocole pour garder le secret, celui de la localisation des terres et du moyen de s'y rendre."
"J'ai jamais signé une seule fois pour m'embarquer dans un voyage pareil."
me "Bien sûr que si, tu te rappelles de la lettre ?"

"La lettre....c'est bon je me rappelle du texte !"

"Détective, je m'appelle Astrid, je souhaite solliciter votre aide. J'ai entendu parler de vos talents, je vous invite donc dans mon manoir, afin de percer son plus grand secret."

"Jadis, le peuple des Corvibo scella un trésor légendaire dans mon manoir. Ce dernier, dit-on, qu'il est d'une valeur inestimable. Il est capable d'accomplir un miracle qui dépasserait notre humanité."

"Ce butin est si précieux, que même les Corvibo  en étaient effrayés, d'ou le fait de l'avoir sceller."

"Or il se trouve que je possède mon manoir depuis des années, je souhaiterais mettre fin à ce mystère."

"J'ai longtemps cherché un détective pour m'aider, mon enquête vous a révélé."

"Cher Alrik, vous avez le privilège d'être la seule personne extérieure à être convié dans mon manoir. Bien sûr, une somme d'argent très conséquente est à la clé."

"Qui sait, vous pourriez profiter du trésor ?"

"Le Messager viendra vous cherchez si vous êtes intéressez, ne vous inquiétez pas, il vous trouvera et tout se passera bien."

"Lorsque vous serez arrivé dans la fôret, suivez le chemin de cailloux."

"Ce butin compte à mes yeux plus que tout. Ma vie a...comme changé depuis que j'ai débuté ma quête impossible."

"L'attrait pour le luxe est plus fort que tout. J'espère vous revoir bientôt Alrik, prenez ceci comme...un message à l'aide. J'ose espérer qu'un homme galant comme vous puisse accepter ma requête."


show Alrik inquiet at right


al "C'est bon, je me rappelle de cette lettre. C'était...absurde...mais en même temps, j'avais envie de voir sur place de quoi il résultait."
al "Je suis beaucoup trop curieux. On dirait que cette personne vit dans un autre monde, peut-être une folle."
al "Mon devoir était d'inspecter son cas, même si les chances d'une farce ratée sont élevées."
al "Sinon je dois résoudre cette enquête, mais que je sois embarqué dans un tel raffut, ce n'était pas précisé."
me "Je vous assure que tout ceci est sérieux"
al "Bah, c'est sûrement un simple tour de magie de votre part, monsieur le truand"
me "Réflechissez deux secondes détective, comment aurais-je pu vous trouvez, savoir que vous étiez en possession de cette lettre, pour ensuite vous faire atterrir ici ? Un moment il va falloir croire à cette histoire."
al "C'est de l'illusionisme."
me "Continuez ainsi, votre illusion d'être intelligent s'efface."


show Alrik ennuye at right


al "Euh...sinon on est oû ?"
me "Dans l'Arsiel pour les Terres Interdites."
al "Et voilà encore à jouer les fous."
me "Je semble ridicule, mais je vous en conjure de m'écouter. Ce n'est pas Astrid qui vous a choisi, c'est moi."

show Alrik neutre

al "J'écoute.."
me "Comme le dit la lettre, elle cherche le trésor. Mais son manoir se trouve dans sur les terres, personne ne peut y pénétrer."
me "Je suis la seul personne qui existe pouvant faire entrer ou sortir du monde. Même Dame Astrid ne sait pas faire cela"
me "Elle a insisté pour convier un détective, je suis donc parti en quête d'informations pour vous sélectionnez."
al "Vous avez récoltez ces infos comment ?"
me "Via les Veines. Je n'ai pas le temps d'expliquer leurs fonctionnements, mais ce sont des canaux d'informations."
al "Bon, si je dois faire cette enquête...je suppose que je n'ai pas le choix...je me casse comment d'ici ?"
me "Il faut attendre la fin du trajet. Aucun retour en arrière est possible dans l'Arsiel, à moins d'attendre la fin d'un cycle."
al "Bordel arrêtez avec ça ! Maintenant tu vas me dire ce que tu veux !"
me "Ce que je veux réellement...c'est que vous protégiez le trésor."
al "Pardon ?!"
me "Si les Corvibo ont caché cet artefact, c'est pour éviter qu'un grand mal s'abatte sur le monde si ce dernier venait à être découvert."
me "Dame Astrid est avide et égoïste, elle commence à devenir ravagée d'esprit par cette histoire de trésor. Elle a changé, le trésor monopolise ses pensées. A ce stade elle risque de détruire son manoir pour essayer de le trouver."
al "C'est pas censé être du fric ? En quoi ça serait dangeureux ?"
me "Personne ne connait la véritable nature du trésor qui est gardée secrète. Les Corvibo ont tout fait pour le protéger, c'est moi qui assure cette tâche maintenant. Si ils ont décidé de le cacher, c'est bien pour des raisons de sécurité."
al "Qui sont les Corvibo ?"
me "Le peuple qui jadis occupait les terres. Ils sont tous morts aujourd'hui..."
al "Et donc...c'est quoi la suite de votre histoire ?"

stop music fadeout 1.0


me "Je vous ai appelé car je sais que vous ne seriez pas tenté par l'appel du trésor, contrairement aux autres détectives cupides. Je sais que vous suivez les 5 commandements du détective. En plus vous êtes compétents, vous finiriez par le trouver."
al "Donc si je trouve sa location, je dois le protéger ?"
me "Oui...sinon le monde toucherait à sa fin, avec le retour du Kiev..."
al "Mais..qui es-tu..."
me "J'aurais aimé être un simple humain, sans responsabilités si conséquentes."

stop nature fadeout 1.0


me "Alrik, l'Arsiel vient d'arriver, il va être temps pour moi de vous laisser. Je vous souhaite bonne chance dans votre quête, le sort repose sur vous..."

hide Alrik neutre


scene arbre soleil
with Dissolve(3.5)
pause 5

al "Voilà comment je me suis retrouvé dans cette galère. Je me rappelle qu'une fois l'Arsiel arrivé, je pouvais ouvrir la porte....et...je suis sorti d'un tronc d'arbres."
al "Ma seule conclusion est la suivante: je ne suis pas dans un endroit rationnel."

scene fond noir
with Dissolve (3.5)
play music "zic/transition.mp3"
pause 11

return
