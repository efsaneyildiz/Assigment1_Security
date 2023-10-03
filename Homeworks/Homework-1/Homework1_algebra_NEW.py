
irreducibles = []
count = 0
irr_2 = 0
irr_3 = 0

for a in range(1, 3):
    for b in range(3):
        for c in range(3):
            determinant = b**2 - 4*a*c
            count+=1
            if determinant%3 ==0:
                f = f'{a}X^2+{b}X+{c}'
                irreducibles.append(f)
                irr_2 += 1


for a in range(1, 3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                determinant = 18*a*b*c*d -4*(b**3)*d + (b**2) * (c**2) - 4*a*(c**3) - 27*(a**2)*(d**2)
                count+=1
                if determinant%3 <=0:
                    f = f'{a}X^3+{b}X^2+{c}X+{d}'
                    irreducibles.append(f)
                    irr_3 += 1






