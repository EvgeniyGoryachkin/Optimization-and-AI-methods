from scipy.optimize import linprog
import numpy as np

# Функция для оптимизации портфеля с изменением общего бюджета

def optimize_portfolio(total_investment):
    # Коэффициенты доходности (умножены на -1 для минимизации)
    c = [-0.15, -0.12, -0.09, -0.11, -0.08, -0.06]

    # Матрица ограничений (левая часть)
    A_eq = [[1, 1, 1, 1, 1, 1]]  # Ограничение: общая сумма инвестиций = total_investment

    A_ub = [
        [0, 0, 0, 0, 0, -1],             # Ограничение на срочный вклад (x_S >= 100)
        [-1, -1, 3, 0, 0, 0],            # Ограничение: 4x_C >= x_A + x_B + x_C
        [-1, -1, -1, 1, 1, 0],           # Ограничение: x_D + x_K >= x_A + x_B + x_C
        [0, 0, 1, 0, 1, 1]               # Ограничение: x_C + x_K + x_S <= 125
    ]

    # Правая часть ограничений
    b_eq = [total_investment]  # Сумма инвестиций
    b_ub = [-100, 0, 0, 125]

    # Границы переменных (неотрицательность)
    bounds = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None)]

    # Решение задачи линейного программирования
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    if result.success:
        optimal_income = -result.fun  # Доход переведен в положительное значение
        portfolio = result.x
    else:
        optimal_income = None
        portfolio = None

    return portfolio, optimal_income

# Исследуем влияние увеличения общего бюджета
budgets = np.arange(500, 1001, 100)  # От 500 до 1000 тыс. руб. с шагом 100 тыс. руб.
results = [(budget, *optimize_portfolio(budget)) for budget in budgets]

# Вывод результатов
for budget, portfolio, income in results:
    print(f"\nОбщий бюджет: {budget} тыс. руб.")
    if portfolio is not None:
        print(f"Портфель: Акции А: {portfolio[0]:.2f} тыс. руб., Акции В: {portfolio[1]:.2f} тыс. руб., "
              f"Акции С: {portfolio[2]:.2f} тыс. руб., Долгосрочные облигации: {portfolio[3]:.2f} тыс. руб., "
              f"Краткосрочные облигации: {portfolio[4]:.2f} тыс. руб., Срочный вклад: {portfolio[5]:.2f} тыс. руб.")
        print(f"Ожидаемый доход: {income:.2f} тыс. руб.")
    else:
        print("Решение не найдено.")
