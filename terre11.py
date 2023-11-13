time = input('ajouter une heure:')
x = int(time[:2])
y = time[2:]

if x <= 12:
    print(time)

else:
    x = x - 12
    print(x, y)



