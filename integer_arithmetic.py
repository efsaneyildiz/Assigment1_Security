import time

def getRemainder(num: str, divisor: str)->int:
    q = int(num)//int(divisor)
    result = int(num) - int(divisor)*int(q)
    return result


def karatsuba(x: str,y: str)->int:
    """
       Perform multiplication using the Karatsuba algorithm.
       Args:
           x (str): The first integer to be multiplied.
           y (str): The second integer to be multiplied.
       Returns:
           int: The result of multiplying the two integers using the Karatsuba algorithm.
    """
    x = int(x)
    y = int(y)
    if (x<10) or (y<10):
        return x*y
    else:
        x = str(x)
        y = str(y)

        n = max(len(x),len(y))
        n2 =int(n/2)

        Xhi = int(x)// 10**(n2)
        Xlo = int(x) - Xhi * 10**n2
        Yhi = int(y)//10**n2
        Ylo = int(y) - Yhi * 10**n2
        Z = (karatsuba(Xhi, Yhi) * (10 ** ((n2) * 2)) + (karatsuba(Xhi, Ylo) + karatsuba(Xlo, Yhi)) * (10 ** n2) + karatsuba(
            Xlo, Ylo))


        return Z


def Ext_eucl(a,b):
    """
      Extended Euclidean algorithm to find the greatest common divisor (gcd)
      and Bézout coefficients of two integers a and b.
      Args:
          a: The first integer.
          b: The second integer.
      Returns:
          - The Bézout coefficient x.
          - The Bézout coefficient y.
          - The greatest common divisor (gcd) of a and b.
    """
    if a == 0:
        return (0, 1, b)

    x1, y1, gcd = Ext_eucl(getRemainder(b,a), a)

    x = y1 - (b // a) * x1
    y = x1
    return (x, y, gcd)

def primary_mult(X: str,Y: str)->int:
    """
    Perform primary multiplication of two integers represented as strings.
    Args:
        X (str): The first integer in string representation.
        Y (str): The second integer in string representation.
    Returns:
        int: The result of multiplying X and Y as an integer.
    """
    Negative = False
    if X[0] == '-':
        X = X[1:]
        Negative = (Negative != True)
    if Y[0] == '-':
        Y = Y[1:]
        Negative = (Negative != True)

    P,result = 0,0
    X = '0' + X

    for y in reversed(Y):
        y = int(y)
        carry= 0
        number = ''
        for x in reversed(X):
            x = int(x)
            mult = (x*y) + carry
            carry = 0
            if mult >= 10:
                carry+=mult//10
                mult -= carry*10
            number = str(mult) + number
        result += int(number) * (10**P)
        P+=1

    if Negative:return -1*result
    else: return result

def calculate_runtime(func, *args, **kwargs):
    """
    Measure the runtime of a given function and return the result and elapsed time.
    Args:
        func (callable): The function to measure the runtime for.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    Returns:
        A tuple containing the result of the function and the elapsed time (in seconds).
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def subtract(x: str, y: str):
    """
    A function assumes that x and y are non-negative integers represented as strings.
    It performs subtraction digit by digit, handling borrowing as needed.
    Subtract one non-negative integer (y) from another non-negative integer (x).
    Args:
        x (str): The minuend (the number to subtract from).
        y (str): The subtrahend (the number to subtract).
    Returns:
        str: The result of subtracting y from x as a string.
    """
    # Base case: If y is empty, return x
    if not y:
        return x

    # Get the last digits of x and y as integers
    last_x = int(x[-1])
    last_y = int(y[-1])
    # Subtract the last digits, taking borrowing into account
    difference = last_x - last_y

    # If the result is negative, borrow from the next digit
    if difference < 0:
        # Find the previous digit in x
        i = len(x) - 2
        while i >= 0 and x[i] == '0':
            x = x[:i] + '9' + x[i + 1:]
            i -= 1

        # Subtract 1 from the previous digit
        x = x[:i] + str(int(x[i]) - 1) + x[i + 1:]

        # Add 10 to the difference to correct the borrowing
        difference += 10

    # Recursively subtract the rest of the numbers
    rest_difference = subtract(x[:-1], y[:-1])
    # Combine the results
    return rest_difference + str(difference)

def addition(X: str, Y: str) -> str:
    """
    A function assumes that X and Y are non-negative integers represented as strings.
    It performs addition digit by digit, handling carry as needed.
    Add two non-negative integers represented as strings.
    Args:
        X (str): The first non-negative integer to add.
        Y (str): The second non-negative integer to add.
    Returns:
        str: The result of adding X and Y as a string.
    """
    result, carry = '', 0

    max_len = max(len(X), len(Y))
    for i in range(max_len - 1, -1, -1):
        x_digit = int(X[i])
        y_digit = int(Y[i])

        digit_sum = x_digit + y_digit + carry
        carry = digit_sum//10
        digit_sum = getRemainder(digit_sum, 10)

        result = str(digit_sum) + result

    if carry:
        result = str(carry) + result

    return result

def addition_and_subtraction(X: str,Y: str, type: str):
    """
     A function performs addition or subtraction based on the provided type.
    It handles both positive and negative integers.
     Perform addition or subtraction of two integers represented as strings.
     Args:
        X (str): The first integer as a string.
        Y (str): The second integer as a string.
        type (str): The operation type ('addition' or 'subtraction').
    Returns:
        The result of the addition or subtraction as a string.
    """
    negative_x = False
    negative_y = False

    if X[0] == '-':
        negative_x = True
        X = X[1:]
    if Y[0] == '-':
        negative_y = True
        Y = Y[1:]

    max_len = max(len(X), len(Y))
    X = X.zfill(max_len)
    Y = Y.zfill(max_len)
    if type =='addition':
        if negative_x and negative_y:
            return f'-{addition(X, Y)}'
        elif negative_x:
            return f'-{subtract(X,Y)}'
        elif negative_y:
            return subtract(X,Y)
        else:
            return addition(X,Y)
    if type == 'subtraction':
        if negative_x and negative_y:  # (-x) - (-y)
            return f'-{subtract(X,Y)}'
        elif negative_x:               # (-x)- y
            return f'-{addition(X, Y)}'
        elif negative_y:               # x - (-y)
            return addition(X,Y)
        else:                          # x - y
            return subtract(X,Y)








