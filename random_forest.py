#cleaning data with pandas
import pandas as pd
#read tables
activity = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/activity_labels.txt', header=None, sep=' ', names=('ID','Activity'))
features = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/features.txt', sep=' ', header=None, names=('ID','Sensor'))
X_test = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/test/X_test.txt', sep='\s+', header=None)
y_test = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/test/y_test.txt', sep=' ', header=None, names=['SubjectID'])
X_train = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/train/X_train.txt', sep='\s+', header=None)
y_train = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/train/y_train.txt', sep=' ', header=None, names=['SubjectID'])
Sub_train = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/train/subject_train.txt', header=None, names=['SubjectID'])
Sub_test = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/test/subject_test.txt', header=None, names=['SubjectID'])
#one big ah-ha moment sep = '' generate an error instead use sep = ' '
#some times\t would cause system to not read part of the path

#restore the original data
allX = pd.concat([X_test, X_train], ignore_index = True)
ally = pd.concat([y_test, y_train], ignore_index = True)
sensorNames = features['Sensor']  
allX.columns = sensorNames  # just in case i want to train_test_split in future
X_train.columns = sensorNames
X_test.columns = sensorNames
allSub = pd.concat([Sub_train, Sub_test], ignore_index=True)
fdata = pd.concat([allX, allSub], axis=1) 


allY = y_train.append(y_test, ignore_index=True)

import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestRegressor

#allX.describe() #make sure there is no nan values

#train model to set a bench mark
model = RandomForestRegressor(n_estimators = 50, oob_score=True, random_state=42)

#C:\Users\Eric Yang\Anaconda2\lib\site-packages\ipykernel\__main__.py:1: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
# if __name__ == '__main__':

#so I did this
%time model.fit(X_train,y_train['SubjectID'].values) #taking forever
#Wall time: 1min 45s
model.oob_score_ #0.98762452551065538

#blackbox approach??
