import pandas as pd  
import statsmodels.api as sm
import math

#upgraded version - thanks to my mentor kyle

# Train model
def train_model(fname):
  cleanloansData = pd.read_csv(fname)
  cleanloansData['IR_TF'] = cleanloansData['Interest.Rate'].map(lambda x: 0 if x < 12 else 1)
  cleanloansData['Intercept'] = 1.0
  # ind_vars = list(cleanloansData.columns.values)
  ind_vars = ['Amount.Requested', 'FICO.Range','Intercept' ]
  logit = sm.Logit(cleanloansData['IR_TF'], cleanloansData[ind_vars])
  result = logit.fit()
  coeff = result.params
	return coeff

def run_model(coeff, v, yz):
	p = 1.0/(1 + math.exp(coeff[2] + coeff[1] * yz - coeff[0] * v))
	print(p)

coeff = train_model('C:\\Users\Eric Yang\loansData_clean.csv')

run_model(coeff, 1000, 750)

# Expectations
run_model(coeff, 10000000, 250) # Should reject!
run_model(coeff, 10, 820) # Obviously accept!



# Get use case of the model as input
v = float(input("How much do you want to borrow "))
yz = float(input("what is your FICO score "))

run_model(coef, v, yz)
     