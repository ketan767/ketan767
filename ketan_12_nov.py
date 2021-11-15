import pandas as pd
import numpy as np
data = pd.read_csv("iris.csv")
print("mean =",data["sepal.width"].mean())
print("mode =",data["petal.length"].mode())
print("median =",data["sepal.width"].median(),"\n")

print("***Using numpy***")
print("mean =",np.mean(data["sepal.width"]))
print("median =",np.median(data["sepal.width"]))
