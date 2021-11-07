a = int(input('Prosze podać liczbę, podanie 0 konczy prosbe o podanie liczby: '))
ilosc = 0
suma = 0
saryt = 0
while a != 0:
    suma = suma + a
    ilosc = ilosc + 1
    a = int(input('Prosze podać liczbę, podanie 0 konczy prosbe o podanie liczby: '))

saryt = float(suma/ilosc)  
print(f' ilość={ilosc} , suma = {suma}, średnia arytmetyczna = {saryt}')
    

    
    