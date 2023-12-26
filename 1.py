import numpy as np
import matplotlib.pyplot as plt
def my_function(x):
    return -x**np.cos(5*x)

x_values = np.arange(0, 10.1, 0.1)

y_values = my_function(x_values)

plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=2, label=r'$-x^{\cos(5x)}$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графік функції $-x^{\cos(5x)}$')
plt.grid(True)
plt.legend()
plt.show()