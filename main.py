import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0
std_dev = 1
num_samples = 1000

# Генерация данных
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Гистограмма нормально распределённых данных')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True, alpha=0.3)
plt.show()


# Генерация двух наборов случайных данных
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='purple', alpha=0.7)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')
plt.grid(True, alpha=0.3)
plt.show()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt

# Настройка веб-драйвера (используем Firefox или Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Фоновый режим (удали, если хочешь видеть браузер)
driver = webdriver.Chrome(options=options)

url = "https://www.divan.ru/category/divany"
driver.get(url)

# Ждём загрузки страницы
time.sleep(5)

# Поиск элементов с ценами
price_elements = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

prices = []
for elem in price_elements:
    try:
        price_text = elem.text.replace(' ', '').replace('₽', '').strip()
        if price_text.isdigit():
            prices.append(int(price_text))
    except:
        continue

driver.quit()

# Сохранение в CSV
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('sofa_prices.csv', index=False)

# Анализ
average_price = df['Price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} ₽")

# Гистограмма цен
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(True, alpha=0.3)
plt.show()