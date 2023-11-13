nombre = int(input())
i = 2

while i < nombre and nombre % i != 0 :
    i = i + 1

if i == nombre :
    est_premier = True

else :
    est_premier = False


if est_premier :

    print('Oui', nombre, 'est un nombre premier.')

else :

    print('Non', nombre,'n’est pas un nombre premier.')

