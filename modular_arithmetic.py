def getRemainder(num: str, divisor: str)->int:
    q = int(num)//int(divisor)
    result = int(num) - int(divisor)*int(q)
    return result

def mod_addition(x: str, y: str, m: str)->int:
    num_added = int(x) + int(y)
    return getRemainder(str(num_added), m)
# modular addition

def mod_subtraction(x: str, y: str, m: str)->int:
    num_subs = int(x) - int(y)
    return getRemainder(str(num_subs), m)
# modular substraction

def mod_reduction(x:str, m: str)->int:
    m_int = int(m)

    if m_int == 0:
        return None
    else:
     result = getRemainder(x, m)
    return result

# modular reduction

def Ext_eucl(a: str,b: str)->[int, int, int]:
    a_int = int(a)
    b_int = int(b)
    if a_int == 0:
        return b_int,0,1

    gcd, x, y = Ext_eucl(str(b_int%a_int),a)
    r = y - (b_int//a_int) * x

    return gcd, r, x

def mod_inversion(x: str, m: str)->int:
    g, x, y = Ext_eucl(x, m)
    if g != 1:
        return None
    else:
        return getRemainder(x, m)

def karatsuba(x: int,y: int)->int:
    if (x<10) or (y<10):
        return x*y
    else:
        x = str(x)
        y = str(y)

        n = max(len(x),len(y))
        n2 =int(n/2)

        Xhi = int(x)// 10**(n2)
        Xlo = getRemainder(int(x),10)**n2
        Yhi = int(y)//10**n2
        Ylo = getRemainder(int(y),10)**n2
        # print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = (karatsuba(Xhi,Yhi)*(10**((n2)*2)) + (karatsuba(Xhi,Ylo) + karatsuba(Xlo,Yhi))*(10**n2) + karatsuba(Xlo,Ylo))

        return Z

def mod_multiplication(x:str, y:str, m:str):
    result = karatsuba(int(x), int(y))
    return mod_reduction(str(result),m)
