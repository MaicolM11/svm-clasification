import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn import metrics
from sklearn.decomposition import PCA
from mpl_toolkits import mplot3d


data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1)
Y = data['NEOSPORA']

# 1000 
# 900 - 100
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=111)
pca = PCA(n_components = 2).fit(X_train)
pca_2d = pca.transform(X_train)

clf = SVC(kernel='poly')
clf.fit(pca_2d, y_train)

test_2d = pca.transform(X_test)

y_pred = clf.predict(test_2d)

# 0.54 - 0
#  

gamma = 1
Xr = np.exp(-gamma*(pca_2d ** 2).sum(1))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
cmap   = matplotlib.colors.ListedColormap( [ 'g', 'r' ] )
z = [i for i in range(800)]
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(pca_2d[:, 0], pca_2d[:, 1], Xr, c=y_train, marker='.', cmap=cmap)
plt.show()