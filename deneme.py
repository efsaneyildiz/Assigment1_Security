
def Ext_eucl(a,b):
    if a == 0:
        return (0, 1, b)

    x1, y1, gcd = Ext_eucl(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return (x, y, gcd)




