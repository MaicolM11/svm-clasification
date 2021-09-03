import matplotlib.pyplot as plt
import matplotlib
import pandas as pd 

data_url = "Neospora.csv"

data = pd.read_csv(data_url)
cmap   = matplotlib.colors.ListedColormap( [ 'g', 'r' ] )
z = [i for i in range(1000)]

for i in range(0, 10):
    static = data.columns[i]
    for j in range( i + 1, 11): 
        x = data[static]
        y = data[data.columns[j]]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, c=data['NEOSPORA'], marker='.', cmap=cmap , label = 'Negativo para neospora')
        ax.legend()
        plt.xlabel(static)
        plt.ylabel(data.columns[j])
        plt.show() 

