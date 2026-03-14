import random

def cmmdc(a,b):
    if a<0: a=-a
    if b<0: b=-b
    if a==0 or b==0: return a+b
    while b:
        r=a%b
        a=b
        b=r
    return a

def a_la_b_mod_c(a,b,c):
    p=1
    a=a%c
    while b:
        if(b%2==1):
            p=(p*a)%c
        a=(a*a)%c
        b//=2
    return p


def jacobi(a,n):
    if n<=0 or n%2==0:
        return 0

    a=a%n
    rezultat=1

    while a!=0:

        while a%2==0:
            a//=2
            if n%8==3 or n%8==5:
                rezultat=-rezultat

        a,n=n,a

        if a%4==3 and n%4==3:
            rezultat=-rezultat

        a%=n

    if n==1:
        return rezultat
    return 0


def test_Solovay_Strassen(n,nr_incercari):

    if n==2:
        return True
    if n<2 or n%2==0:
        return False

    for i in range(nr_incercari):

        b=random.randint(2,n-2)

        if cmmdc(b,n)!=1:
            return False

        stanga=a_la_b_mod_c(b,(n-1)//2,n)

        dreapta=jacobi(b,n)

        if dreapta==-1:
            dreapta=n-1

        if stanga!=dreapta%n:
            return False

    return True


n=int(input("Dati numarul n: "))
nr_incercari=int(input("Dati numarul de incercari: "))

if test_Solovay_Strassen(n,nr_incercari):
    print(f"Numarul {n} poate fi prim")
else:
    print(f"Numarul {n} este compus")

#pentru 561 afiseaza compus
