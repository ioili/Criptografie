"""def a_la_b_mod_c(a,b,c):
    p=1
    a=a%c
    while b:
        if(b%2==1):
            p=(p*a)%c
        a=(a*a)%c
        b//=2
    return p

print(a_la_b_mod_c(2,40,105))
"""

def citeste_alfabet(fisier_alfabet):
    with open(fisier_alfabet, "r", encoding="utf-8 ") as f:
        alfabet = f.read().strip()

    alfabet = tuple(alfabet)
    return alfabet


def transforma_in_baza_10(numar, alfabet):
    rezultat=0
    N=len(alfabet)
    for letter in numar:
        rezultat=rezultat*N +alfabet.index(letter)
    return rezultat

alfabet=citeste_alfabet("alfabet.txt")
print(alfabet)
n = transforma_in_baza_10("ZECE", alfabet)
print(n)

