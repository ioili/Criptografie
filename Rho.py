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


def pollard_rho(n):

    if n%2==0:
        return 2

    x=random.randint(2,n-1)
    y=x
    c=random.randint(1,n-1)

    d=1

    while d==1:

        x=(x*x+c)%n
        y=(y*y+c)%n
        y=(y*y+c)%n

        d=cmmdc(abs(x-y),n)

        if d==n:
            return None

    return d


n=int(input("Dati numarul n: "))

factor=pollard_rho(n)

if factor:
    print("Factor gasit:",factor)
    print("Celalalt factor:",n//factor)
else:
    print("Nu s-a gasit factor")