from scipy.optimize import linprog

# Коэффициенты целевой функции (стоимость ковров)
c = [-3, -4, -3, -1]  # знак минус, так как задача максимизации

# Коэффициенты ограничений (ресурсы)
A = [
    [7, 2, 2, 6],  # Труд
    [5, 8, 4, 3],  # Сырье
    [2, 4, 1, 8]   # Оборудование
]

# Пределы для ресурсов
b = [80, 480, 130]

# Ограничения неотрицательности
x_bounds = [(0, None), (0, None), (0, None), (0, None)]

# Решение задачи
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Вывод основных результатов
if result.success:
    print("Оптимальное решение найдено!")
    print("Количество ковров каждого типа:")
    print(f"Ковер 'Зима': {result.x[0]:.2f}")
    print(f"Ковер 'Сказка': {result.x[1]:.2f}")
    print(f"Ковер 'Силуэт': {result.x[2]:.2f}")
    print(f"Ковер 'Дымка': {result.x[3]:.2f}")
    print(f"Максимальная стоимость продукции: {-result.fun:.2f} тыс. руб.")

    # Первая задача анализа на чувствительность
    print("\nПервая задача анализа на чувствительность:")

    # a) Максимальное снижение запаса ресурсов
    print("a) На сколько можно снизить запас ресурсов при сохранении оптимального значения целевой функции:")
    for i, resource_limit in enumerate(b):
        b_new = b.copy()
        b_new[i] -= 1
        while b_new[i] >= 0:
            result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='highs')
            if not (result_new.success and (result_new.x == result.x).all()):
                b_new[i] += 1
                break
            b_new[i] -= 1
        print(f"Ресурс {i + 1}: можно снизить до {b_new[i]:.2f} ед.")

    # b) Максимальное увеличение запаса ресурсов
    print("\nb) На сколько можно увеличить запас ресурсов для улучшения целевой функции:")
    max_steps = 100  # Ограничение на количество шагов увеличения ресурса
    for i, resource_limit in enumerate(b):
        b_new = b.copy()
        step_count = 0
        b_new[i] += 1
        result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='highs')
        while result_new.success and -result_new.fun > -result.fun and step_count < max_steps:
            b_new[i] += 1
            step_count += 1
            result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='highs')
        b_new[i] -= 1
        print(f"Ресурс {i + 1}: можно увеличить до {b_new[i]:.2f} ед. (ограничено {step_count} шагами)")

    # c) Изменение плана при увеличении ресурса "труд" на 12 ед.
    print("\nc) Как изменится стоимость и план при увеличении ресурса 'труд' на 12 ед.:")
    b_new = b.copy()
    b_new[0] += 12
    result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='highs')
    if result_new.success:
        print("Новое оптимальное решение найдено!")
        print("Количество ковров каждого типа:")
        print(f"Ковер 'Зима': {result_new.x[0]:.2f}")
        print(f"Ковер 'Сказка': {result_new.x[1]:.2f}")
        print(f"Ковер 'Силуэт': {result_new.x[2]:.2f}")
        print(f"Ковер 'Дымка': {result_new.x[3]:.2f}")
        print(f"Новая максимальная стоимость продукции: {-result_new.fun:.2f} тыс. руб.")
    else:
        print("Не удалось найти новое решение при увеличении ресурса 'труд'.")
else:
    print("Решение не найдено.")

