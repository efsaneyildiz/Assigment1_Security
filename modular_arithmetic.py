def getRemainder(num, divisor):
    q = num//divisor
    num -= divisor*q
    return num
# modular reduction
print(getRemainder(17, -3))
print(17%-3)

def mod_addition(x, y, m):
    num_added = x + y
    return getRemainder(num_added, m)
# modular addition

print(mod_addition(12, 5, 3))