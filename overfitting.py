import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

np.random.seed(414)

# Gen toy data
x = np.linspace(0, 15, 1000)
y = 3 * np.sin(x) + np.random.normal(1 + x, .2, 1000)


train_x, train_y = x[:700], y[:700]
test_x, test_y = x[700:], y[700:]

train_df = pd.DataFrame({'x': train_x, 'y': train_y})
test_df = pd.DataFrame({'x': test_x, 'y': test_y})



poly_1 = smf.ols(formula='y ~ 1 + x', data=train_df).fit()
# poly_1.summary() #R-squared:	0.642 #Liner fit
poly_1.predict(x_new)

poly_2 = smf.ols(formula='y ~ 1 + x + I(x**2)', data=train_df).fit()
#poly_2.summary() #R-squared:	0.666 # Quadratic Fit
poly_2.predict(x_new)

poly_3 = smf.ols(formula='y ~ 1 + x + I(x**2)', data=test_df).fit()
#poly_3.summary()

poly_4 = smf.ols(formula='y ~ 1 + x + I(x**2) + I(x**3)', data=test_df).fit()
#poly_3.summary()
x_new = pd.DataFrame({'x': [11]})
#x_new.head()
poly_2.predict(x_new) #array([ 13.27946907])

poly_1.predict(x_new) #array([ 9.18211145])