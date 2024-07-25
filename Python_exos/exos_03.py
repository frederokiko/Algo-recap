# Créez un programme qui gère les commandes de café en fonction des différentes options telles que la taille, le type de
#café, les extras, etc. Utilisez des correspondances pour traiter chaque option et calculer le prix total de la commande.

# choix_taille =input('g,m,p')
# choix_extras =input('s,l,c')
# total=0
# match choix_taille:
#     case 'g':
#         total+=3
#     case 'm':
#         total+=2.5
#     case 'p':
#         total+=2
#     case _:
#         print('mauvais choix')

# match choix_extras:
#     case 's':
#         total+=0.20
#         total+=0.50
#     case 'c':
#         total+=1
#     case _:
#         print('mauvais choix')

# print('prix total = ',total,' €')

# Créez un programme qui convertit une note numérique en une note alphabétique en utilisant une échelle de notation
# standard. Utilisez des correspondances pour déterminer la note alphabétique correspondante en fonction de la note
# numérique.

# note=int(input("Entre une note : "))
# if (note>=18 and note<=20):
#     print('TB')
# elif note>=15:
#     print('B')
# elif note>=10:
#     print('S')
# elif note>=5:
#     print('I')
# else:
#     print('TI')

# Créez un programme qui génère un nombre aléatoire (import random) et permet à l'utilisateur de deviner ce nombre.
# Utilisez des correspondances pour comparer la devinette de l'utilisateur avec le nombre généré et fournir des indices

# import random;
# nombre_a_trouver =random.randint(1,100)
# print(nombre_a_trouver)
# nombre_user=int(input('entre un nombre : '))
# if nombre_user>nombre_a_trouver:
#     print('le bon nombre est plus petit')
# elif nombre_user<nombre_a_trouver:
#     print('le bon nombre est plus grand')
# else:
#     print('Bravo , tu as gagné')

# Créez un programme qui calcule l'indice de masse corporelle (IMC) d'une personne en fonction de son poids et de sa
# taille. Utilisez des correspondances pour interpréter et catégoriser l'IMC résultant en différentes catégories de poids.
# Maigreur extrême – dénutrition	Moins de 16.5	
# Maigreur	De 16.5 à 18.5	Accru
# Corpulence normale	De 18.5 à 25	
# Surpoids ou pré-obésité	De 25 à 30	
# Obésité modérée (classe I)	De 30 à 35	
# Obésité sévère (classe II)	De 35 à 40	
# Obésité morbide (classe III)	Plus de 40

# poids=int(input('Entrez votre poids en Kg : '))
# taille=float(input('Entrez votre taille en Metre'))
# imc=poids//(taille*taille)
# print('votre indice est de : ',imc)
# if imc>40:
#     print('Obésité morbide')
# elif imc>=35:
#     print('Obésité sévère')
# elif imc>=30:
#     print('Obésité modérée')
# elif imc>=25:
#     print('Surpoids ou pré-obésité')
# elif imc>=18.5:
#     print('Corpulence normale')
# elif imc>=16.5:
#     print('Maigreur')
# else:
#     print('Maigreur extrême – dénutrition')

# Créez un programme qui permet à l'utilisateur de choisir un menu pour chaque repas (petit-déjeuner, déjeuner, dîner)
# parmi des options préétablies. Après la sélection, il affiche les choix de l'utilisateur pour chaque repas et résume
# l'ensemble des repas de la journée.

# petit_dej=int(input('croissant : 1 | pain au chocolat : 2 | jus d orange : 3'))
# dejeuner =int(input('sandwich : 1 | salade : 2 | pates bolo : 3'))
# repas=int(input('steak frites : 1 | Moules : 2 | Ragoutoutou : 3'))
# match petit_dej:
#     case 1:
#         print('vous avez choisis un croissant')
#         ptdej='Croissant'
#     case 2:
#         print('vous avez choisis un Pain au chocolat')
#         ptdej='Pain au chocolat'
#     case 3:
#         print('vous avez choisis un Jus d orange')
#         ptdej='Jus d orange'
# match dejeuner:
#     case 1:
#         print('vous avez choisis un Sandwich')
#         dej='Sandwich'
#     case 2:
#         print('vous avez choisis une Salade')
#         dej='Salade'
#     case 3:
#         print('vous avez choisis une Pates bolo')
#         dej='Pates bolo'
# match repas:
#     case 1:
#         print('vous avez choisis un Steack/frites')
#         rep='Steack/frites'
#     case 2:
#         print('vous avez choisis des Moules')
#         rep='Moules'
#     case 3:
#         print('vous avez choisis une Ragoutoutou')
#         rep='Ragoutoutou'
# print(f'vous avez mangé ce matin :{ptdej} et dejeuné :{dej} et eu en repas :{rep}')

# Créez un programme qui génère des citations aléatoires à partir d'un nombre aléatoire. L'utilisateur devrait pouvoir
# choisir un thème et le programme générera une citation aléatoire correspondante. Utilisez des correspondances pour
# gérer les différents thèmes et générer les citations appropriées.

# humour=["Les devoirs, c'est comme les taxes : on ne les aime pas, mais on ne peut pas y échapper.",
# "Pourquoi les élèves aiment-ils les vacances ? Parce qu'ils ne doivent plus faire semblant d'écouter.",
# "Si l'école était une série, le professeur serait le méchant principal.",
# "Un livre d'histoire dit à un manuel de maths : 'Au moins, moi, je raconte une histoire.'",
# "Pourquoi les élèves aiment-ils tant le sport ? Parce que c'est le seul cours où ils peuvent courir après quelque chose qu'ils aiment vraiment."]
# animaux=["Pourquoi les chats aiment-ils les ordinateurs ? Parce qu'ils peuvent se coucher sur le clavier et recevoir des caresses en retour.",
# "Un escargot dit à une limace : 'Eh, t’as oublié ta maison !'","Les poissons ne savent pas dire bonjour, ils n’ont pas de mains pour faire coucou.",
# "Pourquoi les chiens n’aiment-ils pas les ordinateurs ? Parce qu’ils ne peuvent pas les mordre.",
# "Si les oiseaux savaient parler, ils passeraient leur temps à se moquer des gens."]
# sportif=["Un footballeur sans ballon, c'est comme un mime sans public.",
# "Pourquoi les joueurs de tennis adorent les chiens ? Parce qu'ils courent toujours après la balle.",
# "Un nageur, c’est juste un homme qui a trouvé un moyen de ne pas marcher.",
# "Pourquoi les golfeurs portent-ils deux pantalons ? Au cas où ils feraient un trou dans un.",
# "Le rugby, c'est comme le foot, mais avec plus de boue et moins de dentistes."]
# technologie=["Pourquoi les ordinateurs n'aiment-ils pas sortir sous la pluie ? Parce qu'ils attrapent des virus.",
# "Un geek ne va jamais au restaurant, il commande tout en ligne.",
# "Pourquoi les programmeurs aiment-ils tant les montagnes russes ? Parce que ça leur rappelle leur code : plein de bugs.",
# "Les ordinateurs sont comme les vieilles voitures : ils plantent toujours au mauvais moment.",
# "Un disque dur dit à une RAM : 'Pourquoi es-tu toujours si volatile ?'"]
# import random;
# nombre =random.randint(0,4)
# print('Choisis une categorie !!')
# choix_user=int(input('humour(1) : animaux (2) : sportif (3) : technologie (4)'))
# match choix_user:
#     case 1:
#         print(humour[nombre])
#     case 2:
#         print(animaux[nombre])
#     case 3:
#         print(sportif[nombre])
#     case 4:
#         print(technologie[nombre])
#     case _:
#         print('Mauvais choix !!!')