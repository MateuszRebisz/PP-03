liczba = int(input("Podaj liczbę w zł: "))
i5 = 0
i2 = 0
i1 = 0
        
while liczba >=0:
    if liczba >=5:
      i5 = int(liczba/5)
      liczba = int(liczba-5*i5)
    elif liczba >=2:
        i2 = int(liczba/2)
        liczba = int(liczba-2*i2)
    elif liczba >=1:
        i1 = int(liczba/1)
        liczba = int(liczba-1*i1)
    elif liczba == 0:
        break
print(f'The amount of PLN 18 in coins:\n 5 zl - {i5}\n 2 zl - {i2}\n 1 zl - {i1}')


    



