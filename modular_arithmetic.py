def getRemainder(num: str, divisor: str)->int:
    q = int(num)//int(divisor)
    result = int(num) - int(divisor)*int(q)
    return result
# modulo function
print(getRemainder(17, -3))
print(17%-3)

def mod_addition(x: str, y: str, m: str)->int:
    num_added = int(x) + int(y)
    return getRemainder(str(num_added), m)
# modular addition
print(mod_addition(12, 5, 3))

def mod_substraction(x: str, y: str, m: str)->int:
    num_subs = int(x) - int(y)
    return getRemainder(str(num_subs), m)
# modular substraction
print(mod_substraction(60, 13, 2))

def mod_reduction(x:str, m: str)->int:
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

def Ext_eucl(a: str,b: str)->[int, int, int]:
    a_int = int(a)
    b_int = int(b)
    if a_int == 0:
        return b_int,0,1

    gcd, x, y = Ext_eucl(str(b_int%a_int),a)
    r = y - (b_int//a_int) * x

    return gcd, r, x

print(Ext_eucl(161, 112))
def mod_inversion(x: str, m: str)->int:
    g, x, y = Ext_eucl(x, m)
    if g != 1:
        return 0
    else:
        return getRemainder(x, m)
# modular inverse
print(mod_inversion(17, 43))

def karatsuba(x: int,y: int)->int:
    if (x<10) or (y<10):
        return x*y
    else:
        x = str(x)
        y = str(y)
        # print(x[:2])

        n = max(len(x),len(y))
        n2 =int(n/2)

        # print(n2)
        Xhi = int(x)// 10**(n2)
        Xlo = getRemainder(int(x),10)**n2
        Yhi = int(y)//10**n2
        Ylo = getRemainder(int(y),10)**n2
        print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = (karatsuba(Xhi,Yhi)*(10**((n2)*2)) + (karatsuba(Xhi,Ylo) + karatsuba(Xlo,Yhi))*(10**n2) + karatsuba(Xlo,Ylo))

        return Z

def mod_multiplication(x:str, y:str, m:str):
    result = karatsuba(int(x), int(y))
    print(result)
    return mod_reduction(str(result),m)
# modular multiplication
print(mod_multiplication(364, 48, 9))
