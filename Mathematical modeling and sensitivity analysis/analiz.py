from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Данные
profit = {1: 2000, 2: 3600, 3: 4000, 4: 3000, 5: 4400, 6: 6200}
cost = {1: 400, 2: 1100, 3: 940, 4: 760, 5: 1260, 6: 1800}
programmers = {1: 6, 2: 18, 3: 20, 4: 16, 5: 28, 6: 34}

# Создаем задачу линейного программирования
def solve_problem_with_constraints(constraints):
    model = LpProblem(name="software-optimization", sense=LpMaximize)

    # Бинарные переменные для каждого приложения
    x = {i: LpVariable(name=f"x{i}", cat="Binary") for i in range(1, 7)}

    # Целевая функция (максимизация прибыли)
    model += lpSum(profit[i] * x[i] for i in range(1, 7)), "Total_Profit"

    # Применяем ограничения
    for constraint in constraints:
        model += constraint(x)

    # Решение задачи
    model.solve()

    # Результаты
    solution = {f"P{i}": x[i].value() for i in range(1, 7)}
    total_profit = sum(profit[i] * x[i].value() for i in range(1, 7))
    return solution, total_profit

# Ограничения
def budget_constraint(x):
    return lpSum(cost[i] * x[i] for i in range(1, 7)) <= 3500

def programmers_constraint(x):
    return lpSum(programmers[i] * x[i] for i in range(1, 7)) <= 60

def p4_p5_constraint(x):
    return x[4] == x[5]

def p1_p2_constraint(x):
    return x[1] <= x[2]

def p3_p6_constraint(x):
    return x[3] + x[6] <= 1

def max_apps_constraint(x):
    return lpSum(x[i] for i in range(1, 7)) <= 3

# Анализ
scenarios = [
    ("Без ограничений", []),
    ("Только бюджет", [budget_constraint]),
    ("Только программисты", [programmers_constraint]),
    ("Только бюджет и программисты", [budget_constraint, programmers_constraint]),
    ("Только связь P4 и P5", [p4_p5_constraint]),
    ("Только связь P1 и P2", [p1_p2_constraint]),
    ("Только альтернатива P3 и P6", [p3_p6_constraint]),
    ("Только максимум 3 приложения", [max_apps_constraint]),
    ("Полный набор ограничений", [
        budget_constraint, programmers_constraint, p4_p5_constraint,
        p1_p2_constraint, p3_p6_constraint, max_apps_constraint
    ]),
    ("бюджет и программисты+ Связь P4 и P5", [budget_constraint, programmers_constraint, p4_p5_constraint]),
    ("бюджет и программисты+ Связь P1 и P2", [budget_constraint, programmers_constraint, p4_p5_constraint, p1_p2_constraint]),
    ("бюджет и программисты+ Альтернатива P3 и P6", [
        budget_constraint, programmers_constraint, p4_p5_constraint, p1_p2_constraint, p3_p6_constraint
    ]),
    ("бюджет и программисты+ Максимум 3 приложения", [
        budget_constraint, programmers_constraint, p4_p5_constraint, p1_p2_constraint, p3_p6_constraint, max_apps_constraint
    ]),
]

# Решение для каждого сценария
results = []
for name, constraints in scenarios:
    solution, total_profit = solve_problem_with_constraints(constraints)
    results.append((name, solution, total_profit))

# Вывод результатов
for name, solution, total_profit in results:
    print(f"{name}:\n  Решение: {solution}\n  Общая прибыль: {total_profit}\n")

