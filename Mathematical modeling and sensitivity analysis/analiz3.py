import pulp

# Инициализация задачи
model = pulp.LpProblem("BankLoanPortfolio", pulp.LpMaximize)

# Переменные
x1 = pulp.LpVariable('x1', lowBound=0)  # Кредиты физическим лицам
x2 = pulp.LpVariable('x2', lowBound=0)  # Кредиты на покупку авто
x3 = pulp.LpVariable('x3', lowBound=0)  # Кредиты на покупку жилья
x4 = pulp.LpVariable('x4', lowBound=0)  # Сельскохозяйственные кредиты
x5 = pulp.LpVariable('x5', lowBound=0)  # Коммерческие кредиты

# Целевая функция
model += 0.126*x1 + 0.1209*x2 + 0.1164*x3 + 0.11875*x4 + 0.098*x5, "Total_Profit"

# Ограничения
model += x1 + x2 + x3 + x4 + x5 == 12, "Total_Loans"
model += x4 + x5 >= 4.8, "Agri_and_Commercial_Loans"
model += x3 >= x1 + x2, "Housing_Loan_Constraint"
model += 0.1*x1 + 0.07*x2 + 0.03*x3 + 0.05*x4 + 0.02*x5 <= 0.48, "Bad_Debt_Limit"

# Решение задачи
model.solve()

# Вывод результатов
print("Status:", pulp.LpStatus[model.status])
print(f"x1 (Personal Loans): {x1.varValue} million $")
print(f"x2 (Auto Loans): {x2.varValue} million $")
print(f"x3 (Housing Loans): {x3.varValue} million $")
print(f"x4 (Agricultural Loans): {x4.varValue} million $")
print(f"x5 (Commercial Loans): {x5.varValue} million $")
print(f"Total Profit: {pulp.value(model.objective)} million $")

