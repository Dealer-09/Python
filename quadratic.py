import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
if a == 0:
    print("Error! Not a quadratic equation")
else:
    d = (b * b) - (4 * a * c)
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"The two distinct real roots are {root1:.2f} and {root2:.2f}")

    elif d == 0:
        root = -b / (2 * a)
        print(f"The quadratic equation has one real root: {root:.2f}")

    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        print(f"The two complex roots are {real:.2f} + {imag:.2f}i and {real:.2f} - {imag:.2f}i")
