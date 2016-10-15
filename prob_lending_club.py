import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
loansdata = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansdata.dropna(inplace = True)
loansdata.boxplot(column = 'Amount.Funded.By.Investors')
plt.savefig('Loan-data-Boxplot.png')
loansdata.hist(column='Amount.Funded.By.Investors')
plt.show('Loan-data-histogram.png')
plt.figure()
graph = stats.probplot(loansdata['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.savefig('Loan-data-qq-plot.png')