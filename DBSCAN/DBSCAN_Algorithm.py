import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

# needed libraries installed and imported
# read data and remove user_ID
data = pd.read_csv('../files/edited_dataset.csv')

data = data.drop('شناسه پاسخ‌دهنده', axis=1)
data = data.drop(index=0)  # drop headers
data = data.drop(index=1)
# print(data.head())
data.to_csv('../files/edited_dataset.csv')
# Scaling the data to bring all the attributes to a comparable level
scaler = StandardScaler()  # create an object from StandardScaler
data_scaled = scaler.fit_transform(data)  # use fit_transform from the StandardScaler

# Normalizing the data:
# put the fitted data in a Gaussian distribution
data_normalized = normalize(data_scaled)

# Converting the numpy array into a pandas DataFrame
data_normalized = pd.DataFrame(data_normalized)
# reduce the dimension to visualize it better
pca = PCA(n_components=2)
data_principal = pca.fit_transform(data_normalized)
data_principal = pd.DataFrame(data_principal)
data_principal.columns = ['P1', 'P2']
# print(data_principal.head())

# build clusters and label them
# Numpy array of all the cluster labels assigned to each data point
db_default = DBSCAN(eps=0.1555, min_samples=2).fit(data_principal)
labels = db_default.labels_

# Building the label to colour mapping

# Building the colour vector for each data point
# # cvec = [colours1[label] for label in labels]
# color_map = []
# for i in range(0, max(labels) + 2):
#     r = lambda: random.randint(0, 255)
#     rgb_hex = ('#%02X%02X%02X' % (r(), r(), r()))
#     color_map.append(rgb_hex)
#
# cvec = [color_map[label] for label in labels]
# r = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[0])
# g = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[1])
# b = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[2])
# c = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[3])
# y = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[4])
# m = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[5])
# k = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[6])
# o = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[7])
# a = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[8])
# l = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[9])
# plt.figure(figsize=(9, 9))
# plt.scatter(data_principal['P1'], data_principal['P2'], c=cvec)
# plt.legend((r, g, b, c, y, m, k, o, a, l),
#            ('Label 0', 'Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5', 'Label 6', 'Label 7', 'Label 8', 'Label '
#                                                                                                                '-1'),
#            scatterpoints=1,
#            loc='upper left',
#            ncol=3,
#            fontsize=8)
# plt.show()
# saving clusters into the ../files/edited_dataset.csv
clusters = labels
df = pd.read_csv("../files/edited_dataset.csv")
df['clusters'] = clusters
df.to_csv("../files/edited_dataset.csv")
# add cluster column -- two indexing extra columns
