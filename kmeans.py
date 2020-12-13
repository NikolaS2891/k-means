import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_excel('Book1.xlsx') # load data

kmeans = KMeans(n_clusters=3) # select number of clusters

# get clusters
y = kmeans.fit_predict(data[['Feat_1', 'Feat_2', 'Feat_3', 'Feat_4']])
data['Cluster'] = y

print(data)