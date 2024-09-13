import numpy as np

def rastrigin(x):
    return 10 + x ** 2 - 10 * np.cos(2 * np.pi * x)
def func(x):
    return (x - np.cos(x)) ** 2


def golden_section_search(f, a, b, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2
    invphi = (1 / (phi))

    c = b - invphi * (b - a)
    d = a + invphi * (b - a)

    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        c = b - invphi * (b - a)
        d = a + invphi * (b - a)
    return (b + a) / 2

a, b = -5, 5
min_x = golden_section_search(rastrigin, a, b)
# min_x = golden_section_search(func, a, b)
min_value = rastrigin(min_x)
# min_value = func(min_x)

print(f"Минимум функции находится в точке x = {min_x}, значение функции = {min_value}")

