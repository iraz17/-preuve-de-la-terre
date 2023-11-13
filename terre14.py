def est_liste_triee(lst):
    if sont_tous_des_entiers(lst):
        croissant = True
        decroissant = True

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                croissant = False
            if lst[i] < lst[i + 1]:
                decroissant = False

        return croissant or decroissant
    else:
        return False

# Fonction pour vérifier si tous les éléments de la liste sont des entiers
def sont_tous_des_entiers(lst):
    try:
        for element in lst:
            int(element)  # Tente de convertir l'élément en un entier
    except (ValueError, TypeError):
        return False
    return True

# Exemple d'utilisation
elements = input("Entrez les éléments de la liste séparés par des espaces : ").split()
try:
    liste = [int(e) for e in elements]
    if sont_tous_des_entiers(liste):
        if est_liste_triee(liste):
            print("Triée !")
        else:
            print("Pas triée !")
    else:
        print("erreur.")
except ValueError:
    print("Erreur : La liste contient des éléments non entiers.")