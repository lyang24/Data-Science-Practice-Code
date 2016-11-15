import numpy as np
import pandas as pd  
import statsmodels.api as sm
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData['FICO.Range'] = loansData['FICO.Range'].apply(lambda x: x.split('-')[0])
loansData['FICO.Range'] = loansData['FICO.Range'].astype(float)
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
loansData['Loan.Length'] =loansData['Loan.Length'].map(lambda x: x.rstrip(' months'))
loansData['Loan.Length'] =loansData['Loan.Length'].astype(int)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

from sklearn.model_selection import KFold
kf = KFold(n_splits=10)


model = sm.OLS(y[train], X[train])

for train, test in kf.split(X):
    model = sm.OLS(y[train], X[train]).fit()
    y_predicted = model.predict(X[test])
    y_actual = y[test]
    #loop MSE & r**2
    print ((y_actual - y_predicted)**2).mean()