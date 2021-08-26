from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import pandas as pd 

data_url = "Neospora.csv"

data = pd.read_csv(data_url)

for i in range(0, 10):
    static = data.columns[i]
    for j in range( i + 1, 11):
        plt.scatter(data[static], data[data.columns[j]], c = data['NEOSPORA'], s =50)
        plt.xlabel(static)
        plt.ylabel(data.columns[j])
        plt.show()    