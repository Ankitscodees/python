from scipy.stats import ttest_ind
import numpy as np

# Generate two random datasets
np.random.seed(42)
data1 = np.random.normal(loc=5.0, scale=1.5, size=100)  # Mean=5.0, Std=1.5
data2 = np.random.normal(loc=5.5, scale=1.2, size=100)  # Mean=5.5, Std=1.2

# Perform an independent t-test
t_stat, p_value = ttest_ind(data1, data2)

# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpret the result
if p_value < 0.05:
    print("Reject the null hypothesis: The means are significantly different.")
else:
    print("Fail to reject the null hypothesis: The means are not significantly different.")
