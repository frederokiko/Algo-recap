temperature =20

if temperature>=20 :
    print('il fait chaud')

age=19

match age:
    case 18:
        print('majeur')
    case 67:
        print('retraite')
    case _:
        print('toute autres valeur')

# ternaire
majorite ='vrai' if True else 'faux'

#random 

import random;
random.randint(1,100)