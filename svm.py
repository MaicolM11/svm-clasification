import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn import metrics
from sklearn.decomposition import PCA

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1)
Y = data['NEOSPORA']

# 1000 
# 900 - 100
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=111)
pca = PCA(n_components = 3).fit(X_train)
pca_2d = pca.transform(X_train)

clf = SVC(kernel='linear')
clf.fit(pca_2d, y_train)

test_2d = pca.transform(X_test)

y_pred = clf.predict(test_2d)

# 0.54 - 0
#  

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

plt.scatter(pca_2d[:, 0], pca_2d[:, 1], c=y_train, s=1000, cmap='autumn')
plt.show()
"""
test_no = [[3,1,1,0,1,0,1,1,0,0]]  # no
test_si = [[3,2,1,1,1,0,1,0,0,0]]
test_si2 = [[3,1,1,0,0,)1,1,0,0,0]]

x = clf.predict(test_no) #Debe llegar en forma: [ [ x ] ] 
print(x)
x = clf.predict(test_si) #Debe llegar en forma: [ [ x ] ] 
print(x)
x = clf.predict(test_si2) #Debe llegar en forma: [ [ x ] ] 
print(x)

"""