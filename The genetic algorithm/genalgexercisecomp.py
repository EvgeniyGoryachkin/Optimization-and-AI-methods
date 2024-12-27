import random
import numpy as np


# Целевая функция для x + y + z
def target_func2(x, y, z):
    return x + y + z


# Функция, выполняющая стековые команды
def execute_program(program, stack):
    # print(f"Начальный стек: {stack}")  # Вывод начального состояния стека
    for command in program:
        if command == 'DUP':
            stack.append(stack[-1])
        elif command == 'ADD':
            if len(stack) > 1:
                stack.append(stack.pop() + stack.pop())
        elif command == 'MUL':
            if len(stack) > 1:
                stack.append(stack.pop() * stack.pop())
        elif command == 'PUSH':
            stack.append(command[1])
        elif command == 'NOP':
            continue
        elif command == 'SWAP':
            if len(stack) > 1:
                stack[-1], stack[-2] = stack[-2], stack[-1]

        # Вывод размера стека и его содержимого после каждой операции
        sp = len(stack)  # Размер стека
        # print(f"Команда: {command}, Stack size: {sp}, Stack: {stack}")

    return stack[-1] if stack else None


# Инициализация популяции с случайными программами
# Создает начальную популяцию программ из случайно выбранных команд
# размер популяции 10, где каждая программа состоит из 8 команд
def initialize_population(pop_size, prog_length):
    commands = ['DUP', 'ADD', 'MUL', 'NOP', 'SWAP']
    population = []
    for _ in range(pop_size):
        program = [random.choice(commands) for _ in range(prog_length)]
        population.append(program)
    return population


# Оценка приспособленности
# то есть насколько хорошо программа выполняет свою задачу
# совпадает ли результат с тем, что мы ожидаем
def fitness(program, args, target_func):
    total_error = 0
    for x, y, z in args:
        stack = [x, y, z]
        result = execute_program(program, stack)
        expected = target_func(x, y, z)
        if result != expected:
            total_error += 1  # Будет штраф за каждый несоответствующий результат
    return total_error


# Селекция, здесь происходит выбор лучшей программы (родителей) из текущей популяции
# на основе их приспособленности (фитнеса), т. е где меньше ошибок
# лучшие программы выбираются для создания следующего поколения
def select(population, fitnesses, num_parents):
    selected = np.argsort(fitnesses)[:num_parents]
    return [population[i] for i in selected]


# Кроссовер создает новую программу из 2 выбранных решений
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1) # выбираем случайную точку
    child1 = parent1[:point] + parent2[point:] # путем среза создаем 1 часть потомка
    child2 = parent2[:point] + parent1[point:] # и вторую часть
    return child1, child2 # cкрещиваем их и получаем нового потомка

# Мутация добавляет случайные изменения в программу с некоторой вероятностью
def mutate(program, mutation_rate):
    commands = ['DUP', 'ADD', 'MUL', 'NOP', 'SWAP']
    new_program = program[:]
    for i in range(len(new_program)): 
        if random.random() < mutation_rate:
            new_program[i] = random.choice(commands)
    return new_program

# Генетический алгоритм
# Объявляет популяцию, оценивает её на каждом шаге, отбирает лучших
# создает новое поколение через кросовер и мутацию, повторяя процесс
# определенное количество раз
def genetic_algorithm(pop_size, prog_length, num_generations, mutation_rate, target_func, args):
    population = initialize_population(pop_size, prog_length)
    best_program = None
    best_fitness = float('inf')

    # цикл по поколениям
    for generation in range(num_generations):
        # для каждой программы находим фитнес (оцениваем приспособленность)
        fitnesses = [fitness(program, args, target_func) for program in population]

        # Если находим программу с фитнесом 0 (точное совпадение), выходим
        if min(fitnesses) == 0:
            best_program = population[np.argmin(fitnesses)]
            best_fitness = 0
            break
        # выбор родителей на основании их фитнеса и половины популяции
        selected_parents = select(population, fitnesses, pop_size // 2)
        next_generation = []

        for i in range(0, len(selected_parents), 2):
            if i + 1 < len(selected_parents):
                # кроссовер между родителями
                child1, child2 = crossover(selected_parents[i], selected_parents[i + 1])
                # мутация с некоторой вероятностью
                next_generation.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
            else:
                # мутация, если нет пары для скрещивания
                next_generation.append(mutate(selected_parents[i], mutation_rate))
        # обновление популяции на след. поколение 
        population = next_generation

    return best_program, best_fitness


# Параметры генетического алгоритма
pop_size = 10 # размер популяции (кол-во групп команд)
prog_length = 8 # длина программы из команд
num_generations = 10 # кол-во поколений, через которое пройдет алгоритм
mutation_rate = 0.1 # вероятность мутации
args = [(x, random.randint(1, 50), random.randint(1, 50)) for x in range(1, 50)]

best_program, best_fitness = genetic_algorithm(pop_size, prog_length, num_generations, mutation_rate, target_func2, args)

# Печать результатов
if best_fitness == 0:
    print("Найдена точная программа:")
    print(f"Программа: {best_program}")
    print("Результат выполнения программы для всех наборов аргументов:")

    for x, y, z in args:
        stack = [x, y, z]
        result = execute_program(best_program, stack)
        expected = target_func2(x, y, z)
        print(f"Для x={x}, y={y}, z={z} -> Программа: {best_program} -> Результат: {result}, Ожидаемое: {expected}")
else:
    print("Не удалось найти программу с точным совпадением.")
