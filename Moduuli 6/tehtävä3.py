def gallon_to_liter(gallon):
    return gallon * 3.785

def paohjelma():
    while True:
        gallon = float(input("Anna bensiinin määrä gallonoina (negatiivinen arvo lopettaa): "))
        if gallon < 0:
            print('ohjelma lopetetaan')
        break
    liter = gallon_to_liter(gallon)
    print(f'{gallon} gallonaa vastaa {liter} litraa')
paohjelma()
