
from scipy.spatial.distance import cdist, pdist
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/un/un.csv')
#df.count()

X = df.drop(df.columns[:6], axis=1)
X = X.drop(X.columns[4:], axis = 1) #how to extract columns better?
X = X.dropna()

import numpy as np
from sklearn.cluster import KMeans
k_range = (1,10)
kmeans = [KMeans(n_clusters=number, random_state=42).fit(X) for number in k_range] #train model
centroids = [i.cluster_centers_ for i in kmeans] #compute centriods

k_euclid_distance = [cdist(X, cent, 'euclidean') for cent in centroids] #each point to each cluster center
dist = [np.min(ke,axis = 1) for ke in k_euclid_distance] 

wcss = [sum(d**2) for d in dist] #Total within-cluster sum of squares

tss = sum(pdist(X)**2)/X.shape[0] #Total sum of squares

bss = tss - wcss #between-cluster sum of squares