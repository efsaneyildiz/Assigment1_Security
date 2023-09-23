def getRemainder(num, divisor):
    q = num//divisor
    num -= divisor*q
    return num
# modulo function
print(getRemainder(17, -3))
print(17%-3)

def mod_addition(x, y, m):
    num_added = x + y
    return getRemainder(num_added, m)
# modular addition
print(mod_addition(12, 5, 3))

def mod_substraction(x, y, m):
    num_subs = x - y
    return getRemainder(num_subs, m)
# modular substraction
print(mod_substraction(60, 13, 2))

def mod_reduction(x:str, m: str):
    x_len = len(x)
    m_len = len(m)
    org_m = m
    while m_len != x_len:
        m += '0'
        m_len = len(m)
    x_int = int(x)
    m_int = int(m)
    if x_int < m_int:
        m_int //= 10
    result =  x_int - m_int
    print(f'{x_int} - {m_int} = {result}')
    if result < int(org_m):
        return result
    else:
        return mod_reduction(str(result), org_m)
# modular reduction
print(mod_reduction('21811', '61'))

def Ext_eucl(a,b):
    if a == 0:
        return b,0,1

    gcd, x, y = Ext_eucl(b%a,a)
    r = y - (b//a) * x

    return gcd, r, x

def mod_inversion(x, m):
    g, x, y = Ext_eucl(x, m)
    if g != 1:
        return ''
    else:
        return getRemainder(x, m)
# modular inverse
print(mod_inversion(17, 43))

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

def mod_multiplication(x, y, m):
    result = karatsuba(x, y)
    return mod_reduction(str(result), str(m))
# modular multiplication
print(mod_multiplication(426, 964, 235))