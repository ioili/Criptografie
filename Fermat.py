import math

def fermat_factorizare(n):

    r = int(math.sqrt(n))

    if r*r == n:
        return r, r

    t = r + 1

    while True:

        s2 = t*t - n
        s = int(math.sqrt(s2))

        if s*s == s2:
            a = t - s
            b = t + s
            return a, b

        t += 1


n = int(input("Dati numarul n: "))

a,b = fermat_factorizare(n)

print("n =", n)
print("Factorii sunt:", a, "si", b)
#pentru 5959 afiseaza 59 si 101