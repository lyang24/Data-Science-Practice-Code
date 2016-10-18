import pandas as pd  
import statsmodels.api as sm
import math

def loan_function():
	cleanloansData = pd.read_csv('https://github.com/lyang24/Thinkful/blob/master/loansData_clean.csv')
	cleanloansData['IR_TF'] = cleanloansData['Interest.Rate'].map(lambda x: 0 if x < 12 else 1)
	cleanloansData['Intercept'] = 1.0
	# ind_vars = list(cleanloansData.columns.values)
	ind_vars = ['Amount.Requested', 'FICO.Range','Intercept' ]
	logit = sm.Logit(cleanloansData['IR_TF'], cleanloansData[ind_vars])
	result = logit.fit()
	coeff = result.params
	negcoeff = [ (-x) for x in coeff]
	v = float(input("How much do you want to borrow "))
	yz = float(input("what is your FICO score "))
	p = 1/(1 + math.exp(negcoeff[2] + negcoeff[0] * yz - negcoeff[1] * v))
        return  "the probility getting the loan is {}".format(p) 
        if p > .7:
            print("you will get the loan automatically")
        else:
            print("you will not get the loan automatically")