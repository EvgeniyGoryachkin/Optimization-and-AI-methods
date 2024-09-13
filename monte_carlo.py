import numpy as np

def rastrigin(x):
    return 20 + (x ** 2) - (x ** 2) -  (10 * np.cos(2 * np.pi * x)) - (10 * np.cos(2 * np.pi * x))

def monte_carlo_search(f, a, b, num_samples=10000):
    random_points = np.random.uniform(a, b, num_samples)
    function_values = np.array([f(x) for x in random_points])
    min_index = np.argmin(function_values)
    return random_points[min_index], function_values[min_index]


a, b = -5, 5

min_x, min_value = monte_carlo_search(rastrigin, a, b)

print(f"Минимум функции Растригина методом Монте-Карло находится в точке x = {min_x}, значение функции = {min_value}")
