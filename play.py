import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare your data
# Let's simulate some time-series data
time_periods = np.arange(0, 10) # 10 time periods
sales_product_A = np.array([50, 55, 60, 58, 65, 70, 72, 68, 75, 80])
sales_product_B = np.array([40, 42, 45, 50, 52, 58, 60, 65, 62, 70])
sales_product_C = np.array([30, 35, 32, 38, 40, 45, 42, 48, 50, 55])

plt.figure(figsize=(10, 6))
plt.plot(time_periods, sales_product_A, label='Product A', color='blue', linestyle='-', marker='o')
plt.plot(time_periods, sales_product_B, label='Product B', color='red', linestyle='--', marker='x')
plt.plot(time_periods, sales_product_C, label='Product C', color='green', linestyle=':', marker='s')

plt.title('Sales Trends with Custom Styles')
plt.xlabel('Time Period')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()