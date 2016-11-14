import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/ideal-weight/ideal_weight.csv')

#data cleaning
x = list(df.columns.values)
for i in range(len(x)):
    x[i] = x[i].replace("'", "")
df.columns = x

df['sex'] = df['sex'].astype(str)
df['sex'] = df['sex'].apply(lambda x: x.replace("'", ""))
df['sex'] = pd.Categorical(df['sex']).codes # 1 - male, 0  - female

#how to display 2 histogram???
#df.hist(column='ideal')
#df.hist(column='actual')
#plt.legend(loc='upper right')
#plt.show()

# build model
# inspritions - df_X = df[df.AScan.notnull()][['total_length', 'vowel_ratio', 'twoLetters_lastName']].values
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
x = df[['sex']].values
y = df[['actual', 'ideal', 'diff']].values
clf.fit(y,x)

#test model
print(clf.predict([[145, 160, -15]])) # male
print(clf.predict([[160, 145, 15]])) # female 
# makes sense guys wants to get bigger, girl wants to stay fit

#How many points were mislabeled? How many points were there in the dataset, total?
#not sure how to answer
