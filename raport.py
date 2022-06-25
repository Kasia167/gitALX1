
kalorieP = 19
wagaP = 350
kalorieP350 = (kalorieP * wagaP)/100

bialkoP = 1
bialkoP350 = (bialkoP * wagaP)/100

tluszczP = 0
tluszczP350 = (tluszczP * wagaP)/100

wegleP = 4
wegleP350 = (wegleP * wagaP)/100

cenaP = 0.57
cenaP350 = (cenaP * wagaP)/100


kalorieM = 248
wagaM = 325
kalorieM325 = (kalorieM * wagaM)/100

bialkoM = 18
bialkoM325 = (bialkoM * wagaM)/100

tluszczM = 19
tluszczM325 = (tluszczM * wagaM)/100

wegleM = 2
wegleM325 = (wegleM * wagaM)/100

cenaM = 3.832
cenaM325 = (cenaM * wagaM)/100

kalorieS = 13
wagaS = 350
kalorieS350 = (kalorieS * wagaS)/100

bialkoS = 1
bialkoS350 = (bialkoS* wagaS)/100

tluszczS = 0
tluszczS350 = 0

wegleS = 2
wegleS350 = (wegleS * wagaS)/100


cenaS = 0.315
cenaS350 = (cenaS * wagaS)/100

sumaK = kalorieS350 + kalorieP350 + kalorieM325
sumaB = bialkoP350 + bialkoM325 + bialkoS350
sumaT = tluszczS350 + tluszczP350 + tluszczM325
sumaW = wegleS350 + wegleP350 + wegleM325
sumaKs = cenaS350 + cenaM325 + cenaP350

print(f"Produkt Pomidor: Kalorie {kalorieP350}, Białko {bialkoP350}, Tłuszcz {tluszczP350}, Węglowoddany {wegleP350}, Koszt: {cenaP350}")
print(f"Produkt Mozarella: Kalorie {kalorieM325}, Białko {bialkoM325}, Tłuszcz {tluszczM325}, Węglowoddany {wegleM325}, Koszt: {cenaM325}")
print(f"Produkt Sałata: Kalorie {kalorieS350}, Białko {bialkoS350}, Tłuszcz {tluszczS350}, Węglowoddany {wegleS350}, Koszt: {cenaS350}")
print(f"Podsumowanie: Kalorie {sumaK} kcl, Białko {sumaB} g, Tłuscz {sumaT} g, Weęglowodany {sumaW} g, Koszt całkowity {sumaKs}zł")
#pomidor = Salatka()




#print(pomidor.kalorie, pomidor.bialko, pomidor.tluszcz)
