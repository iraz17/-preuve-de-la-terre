entier = input()

# Vérification de l'entrée si c'est un nombre
nombre = True
if len(entier)>0:
    if entier[0] == '-':
        entier = entier[1:]  # Retirez le signe négatif s'il y en a un
    for caractere in entier:
        if not caractere.isdigit():
            nombre = False
            break

if nombre:
    entier = int(entier)
    if entier % 2 == 0:
        print("pair")
    elif entier % 2 != 0:
        print("impair")
else:
    print("Tu ne me la mettras pas à l’envers.")