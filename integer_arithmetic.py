
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

print(karatsuba(1234,8765))







