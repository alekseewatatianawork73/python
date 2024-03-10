# Графики для Y: гистограмма, полигон, ПРВ для равномерного распределения
import numpy as np
from scipy.stats import expon
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

# набор данных для гистограммы
x_all_hist = [52.52, 56.35, 60.18, 64.01, 67.84, 71.67, 75.50, 79.33]  # те x, к-рые слева от столбиков
x_left_hist = 52.52  # самое левое значение
x_right_hist = 83.16  # самое правое значение
y_all_hist = [0.031, 0.018, 0.018, 0.026, 0.042, 0.044, 0.039, 0.042]
width_hist = 3.83  # ширина интервала
# набор данных для полигона
x_all_pol = [54.44, 58.27, 62.10, 65.93, 69.76, 73.59, 77.42, 81.25]
y_all_pol = [0.031, 0.018, 0.018, 0.026, 0.042, 0.044, 0.039, 0.042]

# создание фигуры
fig = plt.figure(figsize=(10, 9))
p = fig.add_subplot()
# гистограмма
p.bar(x_all_hist, y_all_hist, width=width_hist, align="edge", color="orange", linewidth=1.0, edgecolor="black", label='гистограмма')
# полигон
p.plot(x_all_pol, y_all_pol, color="red", marker="o", label='полигон')

# ПРВ равномерного распределения
a, b = 52.52, 83.16  # параметры a и b
f_val = round(1 / (b - a), 3)  # 1 / (b - a), округленное до 3-х знаков после точки
p.plot([a, b], [f_val, f_val], color="green", linewidth=2.0, marker="o", label="ПРВ для равномерного распределения")
# все равно придётся фотошопить, все непонятные числа подбирались, чтобы лучше отобразить график
p.plot([a - 3, a - 0.30], [0, 0], linewidth=4.0, color="green")
p.scatter([a], [0.0004], marker="o", linewidth=1.5, color="white", edgecolors="black", s=50)
p.plot([b + 0.38, b + 3], [0, 0], linewidth=4.0, color="green")
p.scatter([b], [0.0004], marker="o", linewidth=1.5, color="white", edgecolors="black", s=50)

# легенда
plt.title("Графики для Y: гистограмма, полигон, ПРВ для равномерного распределения")
plt.ylabel("n_i/(n*w)")
plt.xlabel("y")
p.legend(loc='upper left')
# отметки
x_all_unique = list(set(x_all_hist + [x_right_hist] + x_all_pol))
y_all_unique = list(set(y_all_hist + y_all_pol))
p.xaxis.set_major_locator(FixedLocator(x_all_unique))
p.yaxis.set_major_locator(FixedLocator(y_all_unique))
# вывод
plt.show()
