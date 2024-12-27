import numpy as np

def rastrigin(x, y):
    return 20 + (x ** 2) - (y ** 2) -  (10 * np.cos(2 * np.pi * x)) - (10 * np.cos(2 * np.pi * y))

def monte_carlo_search(f, a, b, n=10000):
    random_points = [(np.random.uniform(a, b), np.random.uniform(a, b)) for _ in range(n)]
    function_values = np.array([f(x, y) for (x, y) in random_points])
    min_index = np.argmin(function_values)

    return random_points[min_index], function_values[min_index]


a, b = -5, 5

min_x, min_value = monte_carlo_search(rastrigin, a, b)

print(f"Минимум функции Растригина методом Монте-Карло находится в точке x = {min_x}, значение функции = {min_value}")
