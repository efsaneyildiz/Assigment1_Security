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
        # print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = (karatsuba(Xhi, Yhi) * (10 ** ((n2) * 2)) + (karatsuba(Xhi, Ylo) + karatsuba(Xlo, Yhi)) * (10 ** n2) + karatsuba(
            Xlo, Ylo))


        return Z


def Ext_eucl(a,b):
    if a == 0:
        return (0, 1, b)

    x1, y1, gcd = Ext_eucl(getRemainder(b,a), a)

    x = y1 - (b // a) * x1
    y = x1
    # print(x,y,gcd)
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
            # print(f'y: {y}, x: {x}, carry: {carry}, mult: {mult}')
            carry = 0
            if mult >= 10:
                carry+=mult//10
                mult -= carry*10
                # print(mult)
            number = str(mult) + number
            # print(number)
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


# def addition(X: str, Y: str)->int:
#     result, sum, carry = '', 0, 0
#
#     maximum = f'0{max(int(X), int(Y))}'
#     minimum = str(min(int(X), int(Y)))
#
#     max_len = max(len(X), len(Y))
#     X = X.zfill(max_len)
#     Y = Y.zfill(max_len)
#
#     for i in range(1,len(maximum)):
#         x = maximum[-i]
#         y = minimum[-i]
#         sum = int(x)+int(y)+carry
#         carry = 0
#         if sum>=10:
#             carry =sum//10
#             sum -= carry*10
#         result = f"{sum}{result}"
#     return int(result)

def addition(X: str, Y: str) -> str:
    result, carry = '', 0

    max_len = max(len(X), len(Y))
    X = X.zfill(max_len)
    Y = Y.zfill(max_len)

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



# x,y = '2500', '35'
# x,y = '8736821739281083012839018732921379812739', '0912839012736123812372830198230172391723861237'
# print(f'{int(x)+int(y) == int(addition(x,y))}\nCorrect Answer: {int(x)+int(y)}\nYour answer: {addition(x,y)}')




