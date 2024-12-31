import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randn(100) for _ in range(5)]

plt.boxplot(data, vert=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', color='blue'))
plt.title("Box Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
