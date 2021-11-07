x = int(input("Prosze podac wspolrzedna x: "))
y = int(input("Prosze podac wspolrzedna y: "))

if x > 0 and y > 0:
    print(f'Punkt P({x},{y}) znajduje sie w I ćwiartce')
elif x < 0 and y > 0:
    print(f'Punkt P({x},{y}) znajduje sie w II ćwiartce')
elif x < 0 and y < 0:
    print(f'Punkt P({x},{y}) znajduje sie w III ćwiartce')
elif x > 0 and y > 0:
    print(f'Punkt P({x},{y}) znajduje sie w IV ćwiartce')
elif x == 0 and y != 0:
    print(f'Punkt P({x},{y}) znajduje sie na osi ox')
elif x != 0  and y == 0:
    print(f'Punkt P({x},{y}) znajduje sie na osi oy')
elif x == 0 and y == 0:
    print(f'Punkt P({x},{y}) znajduje sie na na poczatku ukladu wspolrzednych)')