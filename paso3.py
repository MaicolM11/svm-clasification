# mejor random state
import numpy as np
import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1) # caracteristicas
Y = data['NEOSPORA'] # clase 

x = [i for i in range(0,1001, 1)]

scores = []

for i in x:
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = i) # 20% para test
    clf = SVC() # instancia el algoritmo
    clf.fit(X_train, y_train) #se entrena
    score = clf.score(X_test, y_test)  # se prueba
    scores.append(score)

maximo = max(scores)
index=np.argmax(scores)
print(maximo)
print(index)

plt.plot(x, scores,'bo-')
plt.title("Percent Correct: Best random state" )
plt.xlabel("Random state")
plt.ylabel("Percent Correct")
plt.show()
