import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y1 = np.random.randint(1, 10, len(x))
y2 = np.random.randint(1, 10, len(x))
y3 = np.random.randint(1, 10, len(x))

plt.stackplot(x, y1, y2, y3, labels=['Series 1', 'Series 2', 'Series 3'], colors=['skyblue', 'lightgreen', 'salmon'])
plt.title("Stacked Area Plot")
plt.legend(loc='upper left')
plt.show()
