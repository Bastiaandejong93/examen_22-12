#Categorie A : Ford Fiesta(1), Volkwagen polo(2) 45 euro per dag ex btw
#Categorie B: Ford Focus(3), Audi A3(4), Mercedes A klasse(5) 55 euro per dag ex btw
#Categorie C: Audi A4(6), Bmw 3(7), Mercedes C klasse 95(8)75 euro per dag ex btw
def BTW_berekenen(factuur):
    prijs_incl=factuur*1.21
    btw=prijs_incl-factuur
    print(round(btw, 2))
    print(round(prijs_incl,2))



factuur=0
opties_autos=['Ford Fiesta(1)/Volkwagen polo(2)','Ford Focus(3)/Audi A3(4)/Mercedes A klasse(5)','Audi A4(6)/Bmw 3(7)/Mercedes C klasse(8)']
aantal_dagen=int(input('Hoeveel dagen wil je een auto huren? '))
keuze_auto = int(input('Welke Auto wil je huren?: 1,2,3,4,5,6,7,8?'))

if keuze_auto==1 or keuze_auto==2:
    factuur=factuur+45
elif keuze_auto==3 or keuze_auto==4or keuze_auto==5:
    factuur=factuur+55
elif keuze_auto==6 or keuze_auto==7or keuze_auto==8:
    factuur=factuur+75
else:
    print('Foutive invoer! Welke Auto wil je huren?: 1,2,3,4,5,6,7,8? ',opties_autos )

verzekering=input('welke Vezekering wil je Standaard of Omnium?: S/O')
if verzekering.upper()=='S':
    factuur=factuur*1.2+20
elif verzekering.upper()=='O':
    factuur=factuur*1.3+25
else:
    print('Foutive invoer! welke Vezekering wil je Standaard of Omnium?: S/O')

aantal_km=int(input('Hoeveel km gereden?:'))
if aantal_km<=100:
    print('€',factuur,BTW_berekenen(factuur))
    BTW_berekenen(factuur)
elif aantal_km>=100:
    factuur=factuur+((aantal_km-100)*0.12)

print('€',factuur ,BTW_berekenen(factuur))













