def gallon_to_liter(gallon):
    return gallon * 3.785
    while True:
        gallon = float(input("Anna bensiinin määrä gallonoina (negatiivinen arvo lopettaa): "))

        if gallon < 0:
            print('ohjelma lopetetaan')
            break
    litra = gallon_to_liter(gallon)
    print(f'{gallon} gallona vastaa {litra:2f} litraa')
