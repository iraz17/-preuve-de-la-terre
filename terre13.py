a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxième entier : "))
c = int(input("Entrez le troisième entier : "))

def valeur_du_milieu(a, b, c):
    # Utilisation de l'opérateur ternaire pour déterminer la valeur du milieu
    milieu = 0
    if b <= a <= c or c <= a <= b:
        milieu = a
    elif a <= b <= c or c <= b <= a:
        milieu = b 
    else:
        milieu = c
    print("La valeur du milieu est :", milieu)

# Appeler la fonction pour afficher la valeur du milieu
valeur_du_milieu(a, b, c)


