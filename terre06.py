nombre = int(input())
nombre1 = int(input())

if nombre1 != 0:
    résultat = nombre // nombre1
    reste = nombre % nombre1
    
    print(résultat, end="")
    print(reste, end="")
else :
 print("erreur")
