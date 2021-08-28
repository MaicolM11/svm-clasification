import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d

cmap   = matplotlib.colors.ListedColormap( [ 'g', 'r' ] )

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1)
Y = data['NEOSPORA']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=844) # 20% para test

clf = SVC()
clf.fit(X_train, y_train)
print("Accuracy:", clf.score(X_test, y_test))


pca = PCA(n_components = 3).fit(X_train)
pca_2d = pca.transform(X_train)

#gamma = 1
#Xr = np.exp(-gamma*(pca_2d ** 2).sum(1))
#z = [i for i in range(800)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_2d[:, 0], pca_2d[:, 1], pca_2d[:, 2], c = y_train, marker='.', cmap=cmap, label = 'Neospora true')
ax.legend()
plt.show()
