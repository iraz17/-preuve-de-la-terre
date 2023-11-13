mot = input()
nombre = 0

try:
    val = int(mot)
    print("erreur")

except ValueError:

    if mot :
        for lettre in mot:
            nombre = nombre + 1
        print(nombre)
    else:
        print("erreur")
