import time
from modular_arithmetic import getRemainder

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
        Xhi = int(x[:n2])
        Xlo = int(x[n2:])
        Yhi = int(y[:n2])
        Ylo = int(y[n2:])
        print(f'Xhigh: {Xhi} Xlow: {Xlo} Yhigh: {Yhi} Ylow: {Ylo}')
        Z = karatsuba(Xhi,Yhi)*(10**n) + (karatsuba(Xhi,Ylo) + karatsuba(Xlo,Yhi))*(10**n2) + karatsuba(Xlo,Ylo)

        return Z

# def Ext_eucl(a:int,b:int)->(int,int,int):
#     if a == 0:
#         return b, 0, 1      #"answer-a": (b),  "answer-b": "1", "answer-gcd": (b)
#
#
#     gcd, x, y = Ext_eucl(getRemainder(b, a), a)
#
#     new_a = y - (b//a) * x
#     new_b = x
#     # print(new_a, new_b, gcd)
#     return new_a, new_b, gcd     # "answer-a": (new_a), "answer-b": (new_b), "answer-gcd": gcd
def Ext_eucl(a,b):
    if a == 0:
        return (0, 1, b)

    x1, y1, gcd = Ext_eucl(b % a, a)

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














