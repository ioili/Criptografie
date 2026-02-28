def cmmdc(a,b ):
    if a<0: a=-a
    if b<0: b=-b
    if a==0 or b==0: return a+b
    while b:
        r=a%b; a=b; b=r;
    return a
print (cmmdc(2171, 2613))


def invers(a,b):
    if a<0: a=-a
    if b<0: b=-b
    copy=b
    xa=1; xb=0
    while b:
        r=a%b
        xr=xa-(a//b)*xb
        a=b; b=r
        xa=xb; xb=xr
    if a==1: return xa%copy
    return None

print(invers(122,343))

#Euler
def phi(n):
    result=n
    p=2
    while p*p<=n:
        if n%p==0:
            # eliminăm toți factorii p
            while n%p==0:
                n//=p
            result-=result//p
        p+=1
    if n>1:
        result-=result//n
    return result

print(phi(1000))

#Euclid_extins
def euclid_extins(a, b):
    xa=(1, 0)  # x_a
    xb=(0, 1)  # x_b

    while b!=0:
        q=a//b
        r=a-q*b
        xr=(xa[0]-q*xb[0], xa[1]-q*xb[1])

        a=b
        b=r
        xa=xb
        xb=xr

    return a,xa[0],xa[1]

# Exemplu
a=44332
b=22334

d, u, v=euclid_extins(a, b)

print("cmmdc =",d)
print("u =",u)
print("v =",v)
print("Verificare:", a*u+b*v)