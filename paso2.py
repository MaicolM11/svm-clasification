# mejor porcentaje x,y
import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1) # caracteristicas
Y = data['NEOSPORA'] # clase 

x = [i for i in range(100)]
for i in [0.1, 0.2, 0.3, 0.4]:
    scores = []
    for j in x:
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=i) # 20% para test
        clf = SVC() # instancia el algoritmo
        clf.fit(X_train, y_train) #se entrena
        scores.append(clf.score(X_test, y_test))  # se prueba

    plt.plot(x, scores,'bo-')
    plt.title("Percent Correct: Accuracy of Predictions with "+ str(i*100) +"% of test" )
    plt.xlabel("Ciclo")
    plt.ylabel("Percent Correct")
    plt.show()
