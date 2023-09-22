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

def mod_substraction(x, y, m):
    num_subs = x - y
    return getRemainder(num_subs, m)
# modular substraction
print(mod_substraction(60, 13, 2))

def mod_reduction(x:str, m: str):
    x_len = len(x)
    m_len = len(m)
    org_m = m
    while m_len != x_len:
        m += '0'
        m_len = len(m)
    x_int = int(x)
    m_int = int(m)
    if x_int < m_int:
        m_int //= 10
    result =  x_int - m_int
    print(f'{x_int} - {m_int} = {result}')
    if result < int(org_m):
        return result
    else:
        return mod_reduction(str(result), org_m)


print(mod_reduction('21811', '61'))