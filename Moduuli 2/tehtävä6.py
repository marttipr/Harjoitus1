leiviskat=float(input('anna leviskät: '))
naulat=float(input('anna naulat: '))
luoti=float(input('anna luodit: '))

# ensin selvitetään kuinka paljon meillä on nauloja
naulatTot = leiviskat * 20 + naulat

# sitten selvitetään kuinka paljon meilä on luoteja
luoditTot = naulatTot * 32 + luoti

# kun tiedämme määrän niin lasketaan massa ensin grammoina
grammatTot = luoditTot * 13.3

kg = grammatTot // 1000
gr = grammatTot % 1000
print(f'Massa nykymittojen mukaan: {kg} kg ja {gr:.2f} grammaa')