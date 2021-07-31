# creating my data-table models here
# cluster model for all cluster tables
import pandas as pd

# create models from each cluster
from django.db import models

dataset = pd.read_csv('../files/edited_dataset.csv')
dataset = dataset.drop(labels='Unnamed: 0', axis='1')
cluster_numbers = dataset['clusters'].value_counts()

# https://stackoverflow.com/questions/5036357/single-django-model-multiple-tables
# def getModel():
#     class Clusters(models.Model):
#
#         class Meta:
#             db_table =
#
#     return Clusters
