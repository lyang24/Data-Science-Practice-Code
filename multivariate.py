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
loansData['Home.Ownership.ord'] = pd.Categorical(loansData['Home.Ownership']).codes
# I learned how to replace NAN with 0
loansData['Monthly.Income'].fillna(0, inplace=True)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Range']
income = loansData['Monthly.Income']
own = loansData['Home.Ownership.ord']
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x3 = np.matrix(income).transpose()
x4 = np.matrix(own).transpose()
x = np.column_stack([x1,x2,x3,x4])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()