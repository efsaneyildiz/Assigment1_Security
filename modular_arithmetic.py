from integer_arithmetic import karatsuba


def getRemainder(num: str, divisor: str) -> int:
    q = int(num) // int(divisor)
    result = int(num) - int(divisor) * int(q)
    return result


def mod_addition(x: str, y: str, m: str) -> int:
    num_added = int(x) + int(y)
    return getRemainder(str(num_added), m)


# modular addition

def mod_subtraction(x: str, y: str, m: str) -> int:
    num_subs = int(x) - int(y)
    return getRemainder(str(num_subs), m)


# modular substraction

def mod_reduction(x: str, m: str) -> int:
    m_int = int(m)

    if m_int == 0:
        return None
    else:
        result = getRemainder(x, m)
    return result


# modular reduction

def Ext_eucl(a: str, b: str) -> [int, int, int]:
    a_int = int(a)
    b_int = int(b)
    if a_int == 0:
        return b_int, 0, 1

    gcd, x, y = Ext_eucl(str(b_int % a_int), a)
    r = y - (b_int // a_int) * x

    return gcd, r, x


def mod_inversion(x: str, m: str) -> int:
    g, x, y = Ext_eucl(x, m)
    if g != 1:
        return None
    else:
        return getRemainder(x, m)





def mod_multiplication(x: str, y: str, m: str) -> int:
    result = karatsuba(int(x), int(y))
    return mod_reduction(str(result), m)
