import numpy as np


# Функция Расстригина
def rastrigin(x, y, A=10):
    return A * 2 + (x ** 2 - A * np.cos(2 * np.pi * x)) + (y ** 2 - A * np.cos(2 * np.pi * y))


# Генетический алгоритм
def genetic_algorithm(pop_size=100, generations=200, mutation_rate=0.1):
    # Инициализация популяции: случайные значения в области [-5.5, 5.5]
    population = np.random.uniform(-5.5, 5.5, (pop_size, 2))
    best_solution = None
    best_fitness = float('inf')

    for generation in range(generations):
        # Вычисление фитнесс-функции
        fitness = np.array([rastrigin(ind[0], ind[1]) for ind in population])

        # Обновление лучшего решения
        min_fitness_idx = np.argmin(fitness)
        if fitness[min_fitness_idx] < best_fitness:
            best_fitness = fitness[min_fitness_idx]
            best_solution = population[min_fitness_idx]

        # Селекция: метод турнира
        selected = []
        for _ in range(pop_size):
            i, j = np.random.choice(pop_size, 2, replace=False)
            winner = population[i] if fitness[i] < fitness[j] else population[j]
            selected.append(winner)
        selected = np.array(selected)

        # Скрещивание: однородный (uniform) кроссовер
        offspring = []
        for i in range(0, pop_size, 2):
            if i + 1 < pop_size:
                parent1, parent2 = selected[i], selected[i + 1]
                alpha = np.random.rand(2)  # вероятность для каждого гена
                child1 = alpha * parent1 + (1 - alpha) * parent2
                child2 = (1 - alpha) * parent1 + alpha * parent2
                offspring.append(child1)
                offspring.append(child2)
        offspring = np.array(offspring)

        # Мутация: случайное изменение генов
        for individual in offspring:
            if np.random.rand() < mutation_rate:
                mutation = np.random.uniform(-0.5, 0.5, 2)
                individual += mutation
                # Ограничение в области поиска
                individual = np.clip(individual, -5.5, 5.5)

        # Обновление популяции
        population = offspring

    return best_solution, best_fitness


# Запуск
best_solution, best_fitness = genetic_algorithm()

print(f"Лучшее решение: x = {best_solution[0]:.4f}, y = {best_solution[1]:.4f}")
print(f"Значение функции: f(x, y) = {best_fitness:.4f}")
