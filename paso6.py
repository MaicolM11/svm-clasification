# otras metricas
import pandas as pd 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data_url = "Neospora.csv"
data = pd.read_csv(data_url)

X = data.drop('NEOSPORA', axis=1) # caracteristicas
Y = data['NEOSPORA'] # clase 

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=844) # 20% para test
clf = SVC() # instancia el algoritmo
clf.fit(X_train, y_train) #se entrena

y_pred = clf.predict(X_test)

## MATRIZ DE CONFUSION

matriz = confusion_matrix(y_test, y_pred)
print('Matriz de Confusión:')
print(matriz)


## METRICAS

VP=matriz[0][0]
VN=matriz[1][1]
FP=matriz[1][0]
FN=matriz[0][1]
#Exactitud
accuracy=((VP+VN)/((VP+VN)+(FN+FP)))
#Sensibilidad
sensibility=(VP/(VP+FN))
#Precision
precision=(VP/(VP+FP))
#Puntuación f1
f1=2*((precision*sensibility)/(precision+sensibility))

print('Accuracy: ', accuracy*100)
print('Sensibility: ', sensibility*100)
print('Precision: ', precision*100)
print('F1 Score: ', f1)


## PREDICCIONES

"""
4,3,0,1,1,1,1,1,1,0,0
3,1,1,1,1,0,1,0,0,0,1
3,0,1,1,0,0,0,0,0,0,0
3,2,0,1,0,0,0,0,0,0,0
3,3,1,1,0,0,1,1,0,0,0
"""

falsos = [[[4,3,1,1,1,1,1,1,0,0]], [[3,2,1,0,0,0,0,0,0,0]]]
positivos = [[[3,1,1,1,0,1,0,0,0,1]], [[3,0,1,0,0,0,0,0,0,0]], [[3,3,1,0,0,1,1,0,0,0]]]

for f in falsos:
    print(f, 'Prediccion: ' + str(clf.predict(f)), 'Pertenece a 0')
for v in positivos:
    print(f, 'Prediccion: ' + str(clf.predict(v)), 'Pertenece a 1')
