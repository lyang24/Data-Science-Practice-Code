#cleaning data with pandas
import pandas as pd
#read tables
activity = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/activity_labels.txt', header=None, sep=' ', names=('ID','Activity'))
features = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/features.txt', sep=' ', header=None, names=('ID','Sensor'))
X_test = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/test/X_test.txt', sep='\s+', header=None)
y_test = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/test/y_test.txt', sep=' ', header=None, names=['activity'])
X_train = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/train/X_train.txt', sep='\s+', header=None)
y_train = pd.read_table('C:\Users\Eric Yang\Documents\UCI HAR Dataset/train/y_train.txt', sep=' ', header=None, names=['activity'])
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
from sklearn.ensemble import RandomForestClassifier

#allX.describe() #make sure there is no nan values

#train model to set a bench mark
model = RandomForestClassifier(n_estimators = 50, oob_score=True, random_state=42)

%time model.fit(X_train,y_train['activity'].values) 

model.oob_score_ #0.9787812840043526

y_pred_class = model.predict(X_test)


# valiadate model
#Accuracy
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class) #92%

#confusion matrix
confusion = metrics.confusion_matrix(y_test,y_pred_class)
print confusion
	#[[481  11   4   0   0   0]
	# [ 50 415   6   0   0   0]
	# [ 17  38 365   0   0   0]
	# [  0   0   0 440  51   0]
	# [  0   0   0  46 486   0]
	# [  0   0   0   0   0 537]]