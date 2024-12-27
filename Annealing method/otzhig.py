import numpy as np

# Новая целевая функция
def custom_function(xy):
    x, y = xy
    return 20 + (x ** 2) - (y ** 2) - (10 * np.cos(2 * np.pi * x)) - (10 * np.cos(2 * np.pi * y))

def simulated_annealing(func, bounds, n_iterations, step_size, temp):
    # Инициализация с случайной точки в пределах границ
    best = bounds[:, 0] + np.random.rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    best_eval = func(best)

    curr, curr_eval = best, best_eval
    scores = [best_eval]

    for i in range(n_iterations):
        # Генерация новой кандидатуры
        candidate = curr + np.random.randn(len(bounds)) * step_size
        candidate = np.clip(candidate, bounds[:, 0], bounds[:, 1])
        candidate_eval = func(candidate)

        # Обновление лучшего решения
        if candidate_eval < best_eval:
            best, best_eval = candidate, candidate_eval
            scores.append(best_eval)

        # Метрополисовый критерий
        diff = candidate_eval - curr_eval
        t = temp / float(i + 1)
        metropolis = np.exp(-diff / t)

        # Принятие нового решения
        if diff < 0 or np.random.rand() < metropolis:
            curr, curr_eval = candidate, candidate_eval

    return best, best_eval, scores

# Параметры задачи
bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])  # Двумерное пространство
n_iterations = 1000
step_size = 0.1
temp = 10

# Поиск решения с помощью имитации отжига
best_solution, best_eval, scores = simulated_annealing(custom_function, bounds, n_iterations, step_size, temp)

print(best_solution, best_eval)




