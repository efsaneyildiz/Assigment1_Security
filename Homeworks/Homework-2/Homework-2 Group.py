# n = 936
# a = 127
# order_n = n-1



def brute_force(base,n):
    k=1
    while True:
        if pow(base, k, n) == 1:
            break
        k += 1

    print("The order of 127 modulo 936 is:", k)
base, n = 127,936

brute_force(base, n)



from math import gcd

def order_mod_prime(a, p):
    if a % p == 0:
        return 0
    k = 1
    result = a % p
    while result != 1:
        result = (result * a) % p
        k += 1
    return k

def lcm(numbers):
    result = 1
    for number in numbers:
        result = (result * number) // gcd(result, number)
    return result

def prime_factors(n,base):
    prime_factors = [2, 3, 13]

    orders = [order_mod_prime(base, p) for p in prime_factors]
    order_mod_n = lcm(orders)

    print("The order of", base, "modulo", n, "is:", order_mod_n)

prime_factors(n,base)

