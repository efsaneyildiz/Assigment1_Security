from integer_arithmetic import karatsuba, addition


def getRemainder(num: str, divisor: str) -> int:
    """ finds the remainder of a division by performing a floor division and
    then computing the following formula:
    Dividend = (Divisor × Quotient) + Remainder
    Hence, this function simple performs the modulo operation.
    """
    q = int(num) // int(divisor)
    result = int(num) - int(divisor) * int(q)
    return result


def mod_addition(x: str, y: str, m: str) -> int:
    """
    adds the two integers x and y with the addition function from integer arithmetic and
    takes the modulo m of this addition with the getRemainder function
    """
    num_added = addition(x,y)
    return getRemainder(str(num_added), m)


# modular addition

def mod_subtraction(x: str, y: str, m: str) -> int:
    """
    Subtracts the two integers x and y and
    takes the modulo m of this subtraction with the getRemainder function
    """
    num_subs = int(x) - int(y)
    return getRemainder(str(num_subs), m)


# modular substraction

def mod_reduction(x: str, m: str) -> int:
    """
    performs x mod m by modular reduction.
    considers the case where m is 0
    """
    m_int = int(m)

    if m_int == 0:
        return None
    else:
        result = getRemainder(x, m)
    return result


# modular reduction

def Ext_eucl(a: str, b: str) -> [int, int, int]:
    """ recursively calculates the greatest common divisor of two integers
    by the extended euclidian algorithm
    """
    a_int = int(a)
    b_int = int(b)
    if a_int == 0:
        return b_int, 0, 1

    gcd, x, y = Ext_eucl(str(b_int % a_int), a)
    r = y - (b_int // a_int) * x

    return gcd, r, x


def mod_inversion(x: str, m: str) -> int:
    """ calculates the modular inversion.
    checks the gcd of x and m with the Extended Euclidian algorithm and if it is
    not equal to 1, there is no inverse. If it is 1, calculates the modulo m by
    the getRemainder function.
    """
    g, x, y = Ext_eucl(x, m)
    if g != 1:
        return None
    else:
        return getRemainder(x, m)





def mod_multiplication(x: str, y: str, m: str) -> int:
    """
    computes the multiplication x*y by the Karatsuba method
    and calculates the modulo m of this multiplication by
    the modular reduction function.
    """
    result = karatsuba(int(x), int(y))
    return mod_reduction(str(result), m)
