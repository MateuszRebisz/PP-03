pin = str(input('Prosze podać czterocyfrowy kod pin: '))
poprawnypin = "0805"
proba = 1
while pin != poprawnypin and proba < 2:
    proba = proba + 1
    print(f'niepoprawny pin,prosze wprowadzić pin ponownie,pozostalo {3-proba} prób')
    pin = str(input('Prosze podać czterocyfrowy kod pin: '))
if pin == poprawnypin:
    print('kod pin jest poprawny')
else:
    print('niepoprawny pin, twoja karta zostala zablokowana')