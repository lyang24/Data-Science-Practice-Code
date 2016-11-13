import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import metrics
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 4)
scores = []
#set up and tuning the model
for k in range(1, 15):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    y_predict = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test,y_predict))
print scores
# use k = 3

# retrain the model with entire dateset
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X,y)