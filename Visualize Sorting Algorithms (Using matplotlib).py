import random
import matplotlib.pyplot as plt

def bubble_sort_visual(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            plt.bar(range(len(arr)), arr, color='blue')
            plt.pause(0.05)
            plt.clf()
    plt.show()

data = [random.randint(1, 100) for _ in range(10)]
bubble_sort_visual(data)
