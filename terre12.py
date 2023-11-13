time = input('ajouter une heure:')
x = int(time[:2])
y = time[2:]
z = str(time[-2:])

if z == "PM" and x == 12:
        x = x-12
        print(x, y)

elif z == "PM":
    x = x + 12
    print(x, y)

else:
    print(time)