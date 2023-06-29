#print(len("Kamil Synoradzki"))
#def Chapter(dzien, miesiac, rok):
#    return dzien + miesiac + rok
#print(Chapter(28,6,2023))

lista = ["Kamil"]

#razem = "asdf"
#print(razem)

#def przedstaw_sie(imie, nazwisko):
#    razem = imie+" "+nazwisko 
#    return razem.title()

#print("Napisze że Iwoje imie i nazwisko to : "+przedstaw_sie("kamil","synoradzki"))
#print(razem)

def zaaktualizuj_liste(l,imie):
    l.append(imie)
    #return l
'''
zaaktualizuj_liste(lista,"Dorota")
zaaktualizuj_liste(lista,"Karolina")
zaaktualizuj_liste(lista,"Magda")
zaaktualizuj_liste(lista,"Paulina")
'''

uczestnicy = ['Kamil', 'Dorota', 'Karolina', 'Magda', 'Paulina']
lista_uczestnikow = []

for uczestnik in uczestnicy:
    #lista_uczestnikow.append(uczestnik)
    zaaktualizuj_liste(lista_uczestnikow,uczestnik)
print(lista_uczestnikow)

#razem = "zmieniło się"
#print(razem)

