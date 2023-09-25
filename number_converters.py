from modular_arithmetic import getRemainder

def to_decimal(number: str, radix)->str:
    keys = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"][:radix]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15][:radix]

    rd_dictionary = dict(zip(keys,values))
    integer = 0
    negative = number[0] == '-'

    if negative:
        number = number[1:]

    for i in range(1, len(number)+1):
        n = rd_dictionary[number[-i]]                  # ith last digit incerases every iteration

        power = i-1
        integer += n * (radix ** power)
    if negative:
        return '-' + str(integer)
    return str(integer)




def to_radix(n: int, radix: int) -> str:
    hex_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:radix]

    def recursive_conversion(num):
        if num == 0:
            return ""
        else:
            return recursive_conversion(num // radix) + hex_chars[getRemainder(num, radix)]

    if n is None:
        return None

    if not isinstance(n, int) or not isinstance(radix, int):
        raise ValueError("Both inputs must be integers")

    if n >= 0:
        if n == 0:
            return "0"
        else:
            return recursive_conversion(n)
    else:
        n = abs(n)
        return "-" + recursive_conversion(n)
