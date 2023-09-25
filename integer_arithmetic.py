import time

def getRemainder(num: str, divisor: str)->int:
    q = int(num)//int(divisor)
    result = int(num) - int(divisor)*int(q)
    return result


def karatsuba(x: int,y: int)->int:

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
    if a == 0:
        return (0, 1, b)

    x1, y1, gcd = Ext_eucl(getRemainder(b,a), a)

    x = y1 - (b // a) * x1
    y = x1
    return (x, y, gcd)

def primary_mult(X: str,Y: str)->int:
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
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time


def subtract(x: str, y: str):
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








