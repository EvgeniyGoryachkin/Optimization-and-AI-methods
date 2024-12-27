import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

# Генерация нелинейной функции с пиками
def target_function(x):
    return (
        50 * np.exp(-((x - 2) ** 2) / 0.5) +  # Первый пик
        20 * np.exp(-((x - 6) ** 2) / 2.0) +  # Второй пик
        10 * np.exp(-((x + 4) ** 2) / 1.0)    # Третий пик
    )

# Генерация данных с шумом
np.random.seed(42)
X = np.linspace(-10, 10, 500).reshape(-1, 1)  # Координатная ось
Y = target_function(X) + np.random.normal(0, 2, X.shape)  # Добавление небольшого шума

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Создание и обучение нейронной сети
model = MLPRegressor(hidden_layer_sizes=(100, 50, 25), activation='relu', solver='adam',
                     max_iter=3000, random_state=42, tol=1e-6, verbose=True)

model.fit(X_train, Y_train.ravel())

# Предсказание по всем данным
Y_pred = model.predict(X)

# Визуализация результатов
plt.figure(figsize=(12, 8))

# График исходной функции
plt.plot(X, target_function(X), label='Исходная функция', color='blue', linewidth=2)

# Точки с шумом
plt.scatter(X_train, Y_train, color='brown', label='Тренировочные точки', s=10)

# Аппроксимация нейросетью
plt.plot(X, Y_pred, label='Аппроксимация нейросетью', color='red', linestyle='--', linewidth=2)

# Настройки графика
plt.title ("Применение нейросети для построения нелинейной регрессии функции."
, fontsize=14)
plt.xlabel("X", fontsize=12)
plt.ylabel("Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
