def karsi_parittomia (luvut):
    parilliset_luvut = [luku for luku in luvut if luku % 2 ==0]
    return parilliset_luvut
def paohjelma():
    lukulista = [1,2,3,4,5,6,7,8,9,10]
    karsittu_lista = karsi_parittomia(lukulista)
    print(f'Alkuperäinen lista: {lukulista}')
    print(f'Karsittu lista (vain parilliset luvut): {karsittu_lista} ')

paohjelma()
