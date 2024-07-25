jouer=True
nombre_user=0
tentative =1
print('bonjour')
while jouer ==True :
    import random;
    nombre_secret= random.randint(1,100)
    cherche=True
    tentative =1
    print(nombre_secret)
    while cherche==True :
        nombre_user=int(input('Veuiller entrer un nombre entre 1 et 100 pour trouver le nombre secret :'))
        if nombre_user<nombre_secret :
            print(' Le nombre secret est superieur à : ',nombre_user)
        elif nombre_user>nombre_secret :
            print('Le nombre secret est inferieir à : ',nombre_user)
        else :
            print(f'✔ Bravo ! c est bien : {nombre_secret} et tu as trouvé en : {tentative} coup(s) 👍')
            cherche = False
            choix = input('Veux-tu continuer O/N ?')
            if choix.lower() !='o':
                jouer =False
        tentative+=1
print('😜 Au revoir !😜') # pour les emoji windows+;
