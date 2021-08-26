# creating my data-table models here
# cluster model for all cluster tables
import pandas as pd

# create a model for all clusters
from django.db import models

dataset = pd.read_csv('E://Prj-karshenasi/webApp_codes/files/edited_dataset.csv')


class Cluster(models.Model):
    skills = models.IntegerField(null=False, default=1)
    pre_skills = models.BooleanField(null=False, default=0)
    starting_point = models.IntegerField(null=False, default=1)
    English_level = models.IntegerField(null=False, default=1)
    time_interval = models.IntegerField(null=False, default=1)
    skill_pros = models.BooleanField(null=False, default=1, max_length=1)
    skill_profit = models.BooleanField(null=False, default=1, max_length=1)
    skill_attraction = models.BooleanField(null=False, default=1, max_length=1)
    i_e_parameter = models.CharField(max_length=1, null=False, default='I')
    s_n_parameter = models.CharField(max_length=1, null=False, default='S')
    t_f_parameter = models.CharField(max_length=1, null=False, default='T')
    p_j_parameter = models.CharField(max_length=1, null=False, default='P')
    clusters = models.FloatField(null=False, default=1)


# records added
# for index in range(len(dataset)):
#     new_class = Cluster()
#     new_class.skills = dataset.iloc[index, 1]
#     new_class.pre_skills = dataset.iloc[index, 2]
#     new_class.starting_point = dataset.iloc[index, 3]
#     new_class.English_level = dataset.iloc[index, 4]
#     new_class.time_interval = dataset.iloc[index, 5]
#     new_class.skill_pros = dataset.iloc[index, 6]
#     new_class.skill_profit = dataset.iloc[index, 7]
#     new_class.skill_attraction = dataset.iloc[index, 8]
#     new_class.i_e_parameter = dataset.iloc[index, 9]
#     new_class.s_n_parameter = dataset.iloc[index, 10]
#     new_class.t_f_parameter = dataset.iloc[index, 11]
#     new_class.p_j_parameter = dataset.iloc[index, 12]
#     new_class.clusters = dataset.iloc[index, 13]
#     new_class.save()
