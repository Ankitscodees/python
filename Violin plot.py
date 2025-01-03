import matplotlib.pyplot as plt
import numpy as np

# Generate random data for 4 groups
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# Create the violin plot
plt.violinplot(data, showmeans=True, showmedians=True)

# Add titles and labels
plt.title("Violin Plot Example")
plt.xlabel("Group")
plt.ylabel("Values")
plt.xticks([1, 2, 3, 4], ["Group 1", "Group 2", "Group 3", "Group 4"])

plt.show()
