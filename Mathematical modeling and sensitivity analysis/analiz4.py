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

# # Вывод результатов
# if result.success:
#     print("Оптимальное решение найдено!")
#     print("Количество ковров каждого типа:")
#     print(f"Ковер 'Зима': {result.x[0]:.2f}")
#     print(f"Ковер 'Сказка': {result.x[1]:.2f}")
#     print(f"Ковер 'Силуэт': {result.x[2]:.2f}")
#     print(f"Ковер 'Дымка': {result.x[3]:.2f}")
#     print(f"Максимальная стоимость продукции: {-result.fun:.2f} тыс. руб.")
# # Анализ чувствительности
#     print("\nАнализ чувствительности:")
#     print("Ценность дополнительного ресурса (теневые цены):")
#     for i, shadow_price in enumerate(result.ineqlin.marginals):
#         print(f"Ресурс {i + 1}: {shadow_price:.2f} тыс. руб./ед.")
#
#     # Увеличение ресурса "труд" на 12 единиц
#     print("\nУвеличение ресурса 'труд' на 12 единиц:")
#     b_new = [80 + 12, 480, 130]  # Увеличение запаса труда
#     result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='simplex')
#     if result_new.success:
#         print("Новое оптимальное решение найдено!")
#         print("Количество ковров каждого типа:")
#         print(f"Ковер 'Зима': {result_new.x[0]:.2f}")
#         print(f"Ковер 'Сказка': {result_new.x[1]:.2f}")
#         print(f"Ковер 'Силуэт': {result_new.x[2]:.2f}")
#         print(f"Ковер 'Дымка': {result_new.x[3]:.2f}")
#         print(f"Новая максимальная стоимость продукции: {-result_new.fun:.2f} тыс. руб.")
#     else:
#         print("Не удалось найти новое решение при увеличении ресурса 'труд'.")
#
#
#     # Изменение ограничений для анализа дефицита всех ресурсов
#     print("\nИзменение ограничений для дефицитности всех ресурсов:")
#     b_deficit = [70, 470, 120]  # Уменьшение запасов для создания дефицита
#     result_deficit = linprog(c, A_ub=A, b_ub=b_deficit, bounds=x_bounds, method='simplex')
#     if result_deficit.success:
#         print("Оптимальное решение при дефицитных ресурсах найдено!")
#         print("Количество ковров каждого типа:")
#         print(f"Ковер 'Зима': {result_deficit.x[0]:.2f}")
#         print(f"Ковер 'Сказка': {result_deficit.x[1]:.2f}")
#         print(f"Ковер 'Силуэт': {result_deficit.x[2]:.2f}")
#         print(f"Ковер 'Дымка': {result_deficit.x[3]:.2f}")
#         print(f"Максимальная стоимость продукции: {-result_deficit.fun:.2f} тыс. руб.")
#     else:
#         print("Не удалось найти решение при дефицитных ресурсах.")
#
# else:
#     print("Решение не найдено.")

if result.success:
    print("Оптимальное решение найдено!")
    print("Количество ковров каждого типа:")
    print(f"Ковер 'Зима': {result.x[0]:.2f}")
    print(f"Ковер 'Сказка': {result.x[1]:.2f}")
    print(f"Ковер 'Силуэт': {result.x[2]:.2f}")
    print(f"Ковер 'Дымка': {result.x[3]:.2f}")
    print(f"Максимальная стоимость продукции: {-result.fun:.2f} тыс. руб.")

    # Анализ чувствительности: ценность дополнительных ресурсов
    shadow_prices = result.ineqlin.marginals
    print("\nЦенность дополнительного ресурса (теневые цены):")
    resource_names = ["Труд", "Сырье", "Оборудование"]
    for i, shadow_price in enumerate(shadow_prices):
        print(f"{resource_names[i]}: {shadow_price:.2f} тыс. руб./ед.")

    # Вопрос b: экономическая выгода от увеличения ресурсов
    labor_cost_per_unit = 1.1  # Стоимость 1 дня труда в тыс. руб.
    equipment_cost_per_hour = 0.05  # Стоимость 1 часа работы оборудования в тыс. руб.

    print("\nЭкономическая выгода от увеличения ресурсов:")
    for i, shadow_price in enumerate(shadow_prices):
        if i == 0:  # Труд
            profitability = shadow_price - labor_cost_per_unit
        elif i == 2:  # Оборудование
            profitability = shadow_price - equipment_cost_per_hour
        else:  # Другие ресурсы
            profitability = shadow_price
        print(f"{resource_names[i]}: {profitability:.2f} тыс. руб./ед.")

    # Вопрос c: анализ при изменении стоимости дополнительного оборудования
    equipment_cost_per_hour = 0.35  # Новая стоимость часа работы оборудования
    profitability_equipment = shadow_prices[2] - equipment_cost_per_hour
    print("\nАнализ для оборудования при стоимости 350 руб./час:")
    if profitability_equipment > 0:
        print(f"Увеличение времени работы оборудования экономически выгодно, с прибылью: {profitability_equipment:.2f} тыс. руб./час.")
    else:
        print(f"Увеличение времени работы оборудования невыгодно, убыток: {profitability_equipment:.2f} тыс. руб./час.")
else:
    print("Решение не найдено.")
print("\nТретья задача анализа на чувствительность:")

# # a) Интервал изменения коэффициентов целевой функции
#     print("a) Интервалы изменения коэффициентов целевой функции:")
#     for i, coeff in enumerate(c):
#         coeff_increase = coeff
#         coeff_decrease = coeff
#
#         # Увеличение коэффициента
#         c_new = c.copy()
#         c_new[i] -= 0.01
#         result_increase = linprog(c_new, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
#         while result_increase.success and (result_increase.x == result.x).all():
#             coeff_increase -= 0.01
#             c_new[i] -= 0.01
#             result_increase = linprog(c_new, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
#
#         # Уменьшение коэффициента
#         c_new = c.copy()
#         c_new[i] += 0.01
#         result_decrease = linprog(c_new, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
#         while result_decrease.success and (result_decrease.x == result.x).all():
#             coeff_decrease += 0.01
#             c_new[i] += 0.01
#             result_decrease = linprog(c_new, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
#
#         print(f"Ковер {i + 1}: {coeff_decrease:.2f} до {coeff_increase:.2f}")
#
#     # b) Уменьшение прибыли при включении одного ковра
#     print("\nb) Уменьшение прибыли при включении одного ковра:")
#     for i in [0, 3]:  # Ковер первого и четвертого типа
#         print(f"\nКовер {i + 1}:")
#         b_new = b.copy()
#         A_new = A.copy()
#
#         # Уменьшаем доступные ресурсы на затраты для одного ковра
#         for j in range(len(b)):
#             b_new[j] -= A[j][i]
#
#         result_new = linprog(c, A_ub=A, b_ub=b_new, bounds=x_bounds, method='highs')
#         if result_new.success:
#             profit_loss = -result_new.fun - (-result.fun)
#             print(f"Уменьшение прибыли: {profit_loss:.2f} тыс. руб.")
#         else:
#             print("Не удалось найти решение после включения ковра.")
# else:
#     print("Решение не найдено.")
