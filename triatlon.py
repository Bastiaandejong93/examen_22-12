def Triatlon(geslacht,kmLopen,kmfietsen,kmZwemmen):
    geslacht=input('Wat is je geslacht?: Man/Vrouw')
    if geslacht.upper()=='MAN':
        kmLopen = int(input('Hoeveel Km gelopen?: '))
        kmFietsen = int(input('Hoeveel Km gefiest?; '))
        kmZwemmen = int(input('Hoeveel Km gezwommen?; '))
    elif geslacht.upper()=='VROUW':
        kmLopen = int(input('Hoeveel Km gelopen?; '))
        kmFietsen = int(input('Hoeveel Km gefiest?; '))
        kmZwemmen = int(input('Hoeveel Km gezwommen?; '))
    else:
        print('Foutive invoer! Wat is je geslacht?: Man/Vrouw')
        geslacht = input('Wat is je geslacht?: Man/Vrouw')

    if geslacht.upper()=='MAN' and kmLopen>=20 and kmFietsen>=10 and kmZwemmen>=3:
        print('u bent geslaagd')
    elif geslacht.upper()=='MAN' and kmLopen>=50 and kmFietsen>=5 and kmZwemmen>=2:
         print('u bent geslaagd')
    elif geslacht.upper()=='MAN' and kmLopen>=45 and kmFietsen>=7 and kmZwemmen>=2:
        print('u bent geslaagd')
    elif geslacht.upper()=='VROUW' and kmLopen>=15 and kmFietsen>=8 and kmZwemmen>=3:
        print('u bent geslaagd')
    elif geslacht.upper()=='VROUW' and kmLopen>=25 and kmFietsen>=10 and kmZwemmen>=2:
        print('u bent geslaagd')
    elif geslacht.upper()=='VROUW' and kmLopen>=40 and kmFietsen>=8 and kmZwemmen>=2:
        print('u bent geslaagd')
    else:
        print('u bent niet geslaagd')

Triatlon((),1,15,5)