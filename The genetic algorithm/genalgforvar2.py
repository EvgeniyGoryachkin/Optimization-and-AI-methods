import random
import numpy as np

# Операторы и константы
OPERATORS = ['+', '-', '*', '/']
CONSTANTS = [1, 2, 3]


# Узел дерева
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Оператор или значение
        self.left = left  # Левое поддерево
        self.right = right  # Правое поддерево

    def evaluate(self, x):
        """Вычисляет значение дерева для заданного x."""
        if self.value == 'x':
            return x
        elif self.value in CONSTANTS:
            return self.value
        elif self.value in OPERATORS:
            left_val = self.left.evaluate(x) if self.left else 0
            right_val = self.right.evaluate(x) if self.right else 0
            try:
                return eval(f"{left_val} {self.value} {right_val}")
            except ZeroDivisionError:
                return float('inf')
        return 0

    def __str__(self):
        """Возвращает строковое представление дерева."""
        if self.value in OPERATORS:
            return f"({self.left} {self.value} {self.right})"
        return str(self.value)


# Генерация случайного дерева
def generate_random_tree(depth=3):
    if depth == 0:
        # Возврат случайного листа (переменная или константа)
        return Node(random.choice(['x'] + CONSTANTS))
    # Случайное решение: создать лист или оператор
    if random.random() > 0.5:  # Вероятность закончить дерево раньше
        return Node(random.choice(['x'] + CONSTANTS))
    operator = random.choice(OPERATORS)
    return Node(operator, generate_random_tree(depth - 1), generate_random_tree(depth - 1))


# Фитнесс-функция
def fitness(tree, target_function, inputs):
    error = 0
    for x in inputs:
        try:
            error += abs(tree.evaluate(x) - target_function(x))
        except:
            error += float('inf')  # Наказываем за некорректные операции
    return error


# Скрещивание деревьев
def crossover(tree1, tree2):
    if random.random() < 0.5:
        return tree2
    if tree1.value in OPERATORS:
        return Node(tree1.value, crossover(tree1.left, tree2), tree1.right)
    return tree1


# Мутация дерева
def mutate(tree, depth=3):
    if depth == 0 or tree is None:
        # Если достигли предела глубины, заменяем дерево на случайное
        return generate_random_tree(depth)
    if random.random() < 0.2:  # Вероятность мутации узла
        return generate_random_tree(depth)
    # Рекурсивная мутация поддеревьев
    return Node(
        tree.value,
        mutate(tree.left, depth - 1) if tree.left else None,
        mutate(tree.right, depth - 1) if tree.right else None
    )


# Генетический алгоритм
def genetic_algorithm(target_function, generations=50, population_size=100, inputs=np.linspace(-10, 10, 20)):
    population = [generate_random_tree() for _ in range(population_size)]
    best_tree = None
    best_fitness = float('inf')

    for generation in range(generations):
        # Оценка фитнеса
        fitnesses = [fitness(tree, target_function, inputs) for tree in population]

        # Сохранение лучшего решения
        min_fitness_idx = np.argmin(fitnesses)
        if fitnesses[min_fitness_idx] < best_fitness:
            best_fitness = fitnesses[min_fitness_idx]
            best_tree = population[min_fitness_idx]

        # Селекция (турнирная)
        selected = []
        for _ in range(population_size):
            i, j = random.sample(range(population_size), 2)
            selected.append(population[i] if fitnesses[i] < fitnesses[j] else population[j])

        # Скрещивание и мутация
        offspring = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(selected, 2)
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            offspring.extend([child1, child2])

        population = offspring

    return best_tree, best_fitness


# Целевая функция
def target_function(x):
    return x ** 2 + 3 * x + 2


# Запуск алгоритма
best_tree, best_fitness = genetic_algorithm(target_function)

print("Лучшее дерево:", best_tree)
print("Фитнесс:", best_fitness)
