import numpy as np
from scipy.optimize import minimize_scalar


def rastrigin(x):
    return 20 + x ** 2 - x ** 2 -  10 * np.cos(2 * np.pi * x) - 10 * np.cos(2 * np.pi * x)

a, b = -5, 5
result = minimize_scalar(rastrigin, bounds=(a, b), method='bounded')

min_x = result.x
min_value = rastrigin(min_x)

print(f"Минимум функции Растригина находится в точке x = {min_x}, значение функции = {min_value}")

