import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

scores = []
for i in range (1,10):
    svc = svm.SVC(kernel = 'linear', C = i)
    svc.fit(X_train, y_train)
    results = svc.predict(X_test)
    scores.append(accuracy_score)
#  bias and variance trade off
