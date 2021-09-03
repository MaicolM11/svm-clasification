# mejor kernel
import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1) # caracteristicas
Y = data['NEOSPORA'] # clase 

for i in ['linear', 'poly', 'rbf', 'sigmoid']:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=844) # 20% para test
    clf = SVC(kernel = i) # instancia el algoritmo
    clf.fit(X_train, y_train) #se entrena
    print(i,clf.score(X_test, y_test))
