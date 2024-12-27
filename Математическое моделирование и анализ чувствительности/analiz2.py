from scipy.optimize import linprog

# Коэффициенты целевой функции (отрицательные для максимизации дохода)
c = [-15, -12, -9, -11, -8, -6]

# Матрица ограничений и вектор правой части
A_eq = [
    [1, 1, 1, 1, 1, 1]  # x_A + x_B + x_C + y_L + y_S + z = 500
]
b_eq = [500]

A_ub = [
    [0, 0, 0, 0, 0, -1],             # z >= 100 (переписывается как -z <= -100)
    [-0.25, -0.25, 0.75, 0, 0, 0],   # x_C >= 0.25(x_A + x_B + x_C)
    [-1, -1, -1, 1, 1, 0],           # y_L + y_S >= x_A + x_B + x_C
    [0, 0, 0, 0, 1, 1],              # y_S + z <= 125
    [1, 1, 1, -1, -1, 0],            # x_A + x_B + x_C <= y_L + y_S (баланс акций и облигаций)
]
b_ub = [-100, 0, 0, 125, 0]

# Границы для переменных (все >= 0)
bounds = [(0, None)] * 6
budget = 600
# Решение задачи линейного программирования
for i in range(4):
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    # Вывод результатов
    investment = result.x
    max_income = -result.fun

    # Печать результатов
    investment_labels = [
        "Акции A", "Акции B", "Акции C",
        "Долгосрочные облигации", "Краткосрочные облигации", "Срочный вклад"
    ]

    output = "\n".join([f"{label}: {amount:.2f} тыс. руб." for label, amount in zip(investment_labels, investment)])
    output += f"\n\nМаксимальный годовой доход: {max_income:.2f} тыс. руб."

    print(output)
    b_eq = [budget if b_eq == b_eq else b_eq]
    budget += 100

