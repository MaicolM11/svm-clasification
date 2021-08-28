from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pandas as pd 

data_url = "Neospora.csv"

data = pd.read_csv(data_url)


fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = data['ABORTO']
y = data['MUERTE_EMBRIONARIA']
z = [i for i in range(1000)]

ax1.scatter(x, y, z, c=data['NEOSPORA'], marker='o')

plt.show()