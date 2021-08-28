import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1) # caracteristicas
Y = data['NEOSPORA'] # clase 

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20) # 20% para test
clf = SVC() # instancia el algoritmo
clf.fit(X_train, y_train) #se entrena
score = clf.score(X_test, y_test)  # se prueba
print(score)    