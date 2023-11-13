alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lettres = input("une lettre de l'alphabet:")
elementLettre = alphabet.index(lettres)
for i in range(elementLettre, len(alphabet)):
    print(alphabet[i], end="",)







#print(alphabet[alphabet.index(lettre):])