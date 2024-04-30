import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
x = df["Χ"]
y = df["Ψ"]
plt.scatter(x, y)
plt.plot(x, y)
plt.grid()
plt.show()