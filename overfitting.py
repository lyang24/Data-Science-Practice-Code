import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn import metrics
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
y1 = poly_1.predict(test_df)

poly_2 = smf.ols(formula='y ~ 1 + x + I(x**2)', data=train_df).fit()
#poly_2.summary() #R-squared:	0.666 # Quadratic Fit
y2 = poly_2.predict(test_df)

plt.plot(x, y, label='original')
plt.plot(test_x, y1, label='linear')
plt.plot(test_x, y2, label='quadratic')
plt.show()

print metrics.accuracy_score(y[700:], y1)
print metrics.accuracy_score(y[700:], y2)
#value error