from sklearn import svm
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
from sklearn.cross_validation import cross_val_score
svc = svm.SVC(kernel='linear')
scores = cross_val_score(svc, X, y, cv=5, scoring = 'accuracy') 
print scores.mean()
#0.98