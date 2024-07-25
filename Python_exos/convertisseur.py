jour :int=0 
heure:int=0
minute:int=0
seconde:int=0
total_seconde=int(input('Entrez le nombre de seconde à convertir'))
if total_seconde>86400 :
    jour=total_seconde//86400
    total_seconde%=86400
if total_seconde>3600 :
    heure =total_seconde//3600
    total_seconde%=3600
if total_seconde>60 :
    minute=total_seconde//60
    total_seconde%=60

seconde=total_seconde
print(jour,heure,minute,seconde,sep=" : ")
