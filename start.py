print("Hello world!")
# git-scm.com
# git commit -m "initial commit"
# git config --local user.name DamianM
#git config --

def main():
    """ parametry: ...""" # tzw. docstring
    print("Hello world!")

# pep8 pep0008
# dlugaNazwaFunkcji NIE
# dluga_nazwa_funkcji
# Guido van Rossum


# Ctrl + / -komentuj/odkomentuj
# Shift + alt + strzalaka
# łańcuch znaków
imie = "Ala"
imie = 'Ala'
imie = """Ala ma 
kota a
kot jest
głodny."""

print(type(imie))
imie = str("ala") #konstruktor
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
#isinstance() sprawdzam czy zmienna jest danego typu
# <class 'str'>
# <class 'int'>
# <class 'bool'>
# <class 'NoneType'>

print("ala " + "ma kota.")
# print("ala " + "ma" + 5 + "kotów.") błąd
print("ala " + "ma " + str(5) + " kotów.")
print(5)
ilosc_kotow = 5
print("ala " + "ma {} kotów.".format(ilosc_kotow))
print("ala "+ f"ma {ilosc_kotow} kotów.")
print("ala ma {1} {0} {2} kotów.".format(4,5,7))
print("ala ma {1} {0} {2} kotów.".format(4,5,7))
liczba = 6.252345235
print(f"Liczba {liczba:.2f}") # 2 miejsca dziesiętne
# http://pyformat.info

print(imie[0])
#imie[0]="O" nie jest mutowalny/ nie mozna zmienic znaków

imie = imie.lower()
print(imie)

#liczby

liczba = 1 #spacja przed i po kazdy operatorze
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) #dzielenie bez reszty
print(1 ** 2) # potęgowanie
print(1 % 2) # modulo

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.30f}")

# listy

lista = []
lista2 = [1, 2, 3]
lista3 = [1, "ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] # wartość 3, indeks 2
lista4 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lista4[1][1] # 5 


# słownik

slownik = {}
slownik2 = {"klucz" : "wartość"}
slownik3 = {0: "Adam"}
slownik2["klucz"] = "cośtam"
slonwik3[0]
slownik2.keys()
slownik2.values()

if liczba in [1 ,2 ,3, 10]:
    print("jest na liście")
else:
    print("Nie ma na liście")

fsfsdfsdf