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
data = pd.read_csv('../files/edited_dataset1.csv')

data = data.drop('شناسه پاسخ‌دهنده', axis=1)
data = data.drop(index=0)  # drop headers
data = data.drop(index=1)
print(data.head())
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
db_default = DBSCAN(eps=0.12, min_samples=2).fit(data_principal)
labels = db_default.labels_

# Building the label to colour mapping

# Building the colour vector for each data point
# cvec = [colours1[label] for label in labels]
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
# s = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[10])
# f = plt.scatter(
#     data_principal['P1'], data_principal['P2'], marker='o', c=color_map[11])
# plt.figure(figsize=(9, 9))
# plt.scatter(data_principal['P1'], data_principal['P2'], c=cvec)
plt.show()
# saving clusters into the ../files/edited_dataset.csv
clusters = labels
df = pd.read_csv("../files/edited_dataset.csv")
# calculate personality type
# i-e s-n t-f p-j
for pointer in range(len(df)):
    i_e_row = df.iloc[[pointer], [9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65]]
    i_e_counter = i_e_row[i_e_row.values == 1].shape[0]

    i_e_different = abs(15 - i_e_counter)
    dataframe = df
    if i_e_different < i_e_counter:
        dataframe.iloc[[pointer], [9]] = 'I'
    else:
        dataframe.iloc[[pointer], [9]] = 'E'

    s_n_row = df.iloc[[pointer], [10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66]]
    s_n_counter = s_n_row[s_n_row.values == 1].shape[0]
    s_n_different = abs(15 - s_n_counter)
    if s_n_different < s_n_counter:
        dataframe.iloc[[pointer], [10]] = 'S'
    else:
        dataframe.iloc[[pointer], [10]] = 'N'

    t_f_row = df.iloc[[pointer], [11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67]]
    t_f_counter = t_f_row[t_f_row.values == 1].shape[0]
    t_f_different = abs(15 - t_f_counter)
    if t_f_different < t_f_counter:
        dataframe.iloc[[pointer], [11]] = 'T'
    else:
        dataframe.iloc[[pointer], [11]] = 'F'

    p_j_row = df.iloc[[pointer], [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68]]
    p_j_counter = p_j_row[i_e_row.values == 1].shape[0]
    p_j_different = abs(15 - p_j_counter)
    if p_j_different < p_j_counter:
        dataframe.iloc[[pointer], [12]] = 'P'
    else:
        dataframe.iloc[[pointer], [12]] = 'J'
# # end of calculate
df.drop(df.iloc[:, 13:69], axis=1, inplace=True)
df['clusters'] = clusters
df.to_csv("../files/edited_dataset.csv")
# add cluster column -- two indexing extra columns
