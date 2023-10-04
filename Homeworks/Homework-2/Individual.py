keys = 'a b c d e f g'.split()
values = '1 7 3 4 9 7 0'.split()
d = dict(zip(keys, values))
print(d)

n = int(d['f']+d['b']+d['a']+d['g']+d['c']+d['e']+d['d'])
print(n)


# Function to calculate Euler's totient function φ(n)
def euler_totient(n):
    result = n  # Initialize result as n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Modulus 'n'
# n = 7710394
n = 1783777
# Calculate φ(n)
phi_n = euler_totient(n)

print("The number of elements in Z∗(", n, ") is:", phi_n)
