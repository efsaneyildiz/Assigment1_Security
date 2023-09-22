def karatsuba(x: int,y: int):
    if (x<10) or (y<10):
        return x*y
    else:
        x = str(x)
        y = str(y)
        # print(x[:2])

        n = max(len(x),len(y))
        n2 =int(n/2)
        # print(n2)
        Xhi = int(x[:n2])
        Xlo = int(x[n2:])
        Yhi = int(y[:n2])
        Ylo = int(y[n2:])
        print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = karatsuba(Xhi,Yhi)*(10**n) + (karatsuba(Xhi,Ylo) + karatsuba(Xlo,Yhi))*(10**n2) + karatsuba(Xlo,Ylo)

        return Z

def Ext_eucl(a,b):
    if a == 0:
        return b,0,1

    gcd, x, y = Ext_eucl(b%a,a)
    r = y - (b//a) * x

    return gcd, r, x


def primary_mult(X: str,Y: str):
    P,result = 0,0
    X = '0' + X
    for y in reversed(Y):
        y = int(y)
        carry= 0

        for x in reversed(X):
            x = int(x)
            mult = (x*y) + carry
            print(f'y: {y}, x: {x}, carry: {carry}, mult: {mult}')
            carry = 0
            if mult >= 10:
                carry+=mult//10
                mult -= carry*10
                print(mult)
        result += mult * (10**P)
        P+=1
    return result

print(primary_mult('678','43'))





