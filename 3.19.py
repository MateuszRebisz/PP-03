wiekpsa = int(input("prosze podac wiek psa: "))

if wiekpsa == 1:
    a = 10.5
    print(f'{wiekpsa} rok to {a} "psich lat"')
elif wiekpsa ==2:
    b = round(2*10.5)
    print(f'{wiekpsa} lata to {b} "psich lat"')
elif wiekpsa >=3:
    c = round(21 + (wiekpsa - 2) * 4)
    print(f'{wiekpsa} to {c} "psich lat"')
    
    