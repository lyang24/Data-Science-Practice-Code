
import pandas as pd 

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines() #split string by line

data = [i.split(',') for i in data] #further split by comma

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

m1 = df['Alcohol'].mean() 

m2 = df['Alcohol'].median() 

#m3 = df['Alcohol'].mode()

m4 = max(df['Alcohol']) - min(df['Alcohol'])

m5 = df['Alcohol'].std() 

m6 = df['Alcohol'].var() 


m7 = max(df['Tobacco']) - min(df['Tobacco'])

m8 = df['Tobacco'].std() 

m9 = df['Tobacco'].var() 

m10 = df['Tobacco'].mean() 

m11 = df['Tobacco'].median()

#m12 = df['Tobacoo'].mode()
	


 

print("the mean for Alcohol and Tobacco in this dataset is: {} and {}".format(m1,m10))
print("the variance for Alcohol is {} and the variance for Tobacco in this dataset is {}".format(m6,m9))
print("In this dataset Alcohol range is {} and Tobacco range is {}".format(m4, m7))
print("the standard deviation for Alcohol and Tobacco in this dataset is: {} and {}".format(m5,m8))
print("the median for Alcohol and Tobacco in this dataset is: {} and {}".format(m2,m11))
#print("the mode for Alcohol and Tobacco in this dataset is: {} and {}".format(m3,m12))