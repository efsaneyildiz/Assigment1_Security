irreducible = []

# Degree 2 polynomials
for a in range(1, 3):
    for b in range(3):
        for c in range(3):
            polynomial = f'{a}X^2+{b}X+{c}'
            # Check if the polynomial is irreducible
            is_irreducible = True
            for x in range(3):
                y = (a * (x**2) + b * x + c) % 3  # Evaluate the polynomial modulo 3
                if y == 0:
                    is_irreducible = False
                    break
            if is_irreducible:
                irreducible.append(polynomial)

# Degree 3 polynomials
for a in range(1, 3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                polynomial = f'{a}X^3+{b}X^2+{c}X+{d}'
                # Check if the polynomial is irreducible
                is_irreducible = True
                for x in range(3):
                    y = (a * (x**3) + b * (x**2) + c * x + d) % 3  # Evaluate the polynomial modulo 3
                    if y == 0:
                        is_irreducible = False
                        break
                if is_irreducible:
                    irreducible.append(polynomial)

# Print irreducible polynomials
for polynomial in irreducible:
    print(polynomial)
print(len(irreducible))