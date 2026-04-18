def a_la_b_mod_c(a,b,c):
    p=1
    a=a%c
    while b:
        if b%2==1:
            p=(p*a)%c
        a=(a*a)%c
        b//=2
    return p


def cmmdc(a,b):
    if a<0: a=-a
    if b<0: b=-b
    if a==0 or b==0:
        return a+b
    while b:
        r=a%b
        a=b
        b=r
    return a


def invers(a,b):
    if a<0: a=-a
    if b<0: b=-b
    copie=b
    xa=1
    xb=0

    while b:
        r=a%b
        xr=xa-(a//b)*xb
        a=b
        b=r
        xa=xb
        xb=xr

    if a==1:
        return xa%copie
    return None


def genereaza_cheie(p,e):
    if cmmdc(e,p-1)!=1:
        return None

    d=invers(e,p-1)
    return e,d


def massey_omura(p,P,eA,dA,eB,dB):
    print("Mesaj initial =",P)

    C1=a_la_b_mod_c(P,eB,p)
    print("C1 =",C1)

    C2=a_la_b_mod_c(C1,eA,p)
    print("C2 =",C2)

    C3=a_la_b_mod_c(C2,dB,p)
    print("C3 =",C3)

    P_final=a_la_b_mod_c(C3,dA,p)
    print("Mesaj recuperat =",P_final)

    return P_final


# exemplu
p=257
P=123

eA=17
eB=11

eA,dA=genereaza_cheie(p,eA)
eB,dB=genereaza_cheie(p,eB)

print("Cheile lui A:",eA,dA)
print("Cheile lui B:",eB,dB)

print()

massey_omura(p,P,eA,dA,eB,dB)