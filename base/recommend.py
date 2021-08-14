from itertools import count

from django.db.models import Count

from base.models import Cluster


class Recommend:
    def __init__(self, personality_factors):
        self.personality_factors = personality_factors

    @staticmethod
    def convert_skills(list_skills):
        recommend = []
        for index in range(len(list_skills)):
            if 1 in list_skills[index].values():
                recommend.append('HTML,CSS')
            elif 2 in list_skills[index].values():
                recommend.append('Javascript')
            elif 3 in list_skills[index].values():
                recommend.append('PHP')
            elif 4 in list_skills[index].values():
                recommend.append('Asp.net')
            elif 5 in list_skills[index].values():
                recommend.append('Wordpress')
            elif 6 in list_skills[index].values():
                recommend.append('Python')
        return recommend

    def calculate_similarity(self):
        clusters_counter = Cluster.objects.values('clusters').count()
        similarity_rate = 0
        Cluster_group = Cluster.objects.all()
        for cluster in range(-1, clusters_counter - 2):
            count_i = len(Cluster_group.filter(clusters=cluster).filter(i_e_parameter='I'))
            count_e = len(Cluster_group.filter(clusters=cluster).filter(i_e_parameter='E'))
            count_t = len(Cluster_group.filter(clusters=cluster).filter(t_f_parameter='T'))
            count_f = len(Cluster_group.filter(clusters=cluster).filter(t_f_parameter='F'))
            count_s = len(Cluster_group.filter(clusters=cluster).filter(s_n_parameter='S'))
            count_n = len(Cluster_group.filter(clusters=cluster).filter(s_n_parameter='N'))
            count_p = len(Cluster_group.filter(clusters=cluster).filter(p_j_parameter='P'))
            count_j = len(Cluster_group.filter(clusters=cluster).filter(p_j_parameter='J'))
            if count_i > count_e:
                if self.personality_factors[0] == 'I':
                    similarity_rate = 25 + similarity_rate
            elif count_e > count_i:
                if self.personality_factors[0] == 'E':
                    similarity_rate = similarity_rate + 25
            if count_s > count_n:
                if self.personality_factors[1] == 'S':
                    similarity_rate = 25 + similarity_rate
            elif count_n > count_s:
                if self.personality_factors[1] == 'N':
                    similarity_rate = similarity_rate + 25
            if count_t > count_f:
                if self.personality_factors[2] == 'T':
                    similarity_rate = similarity_rate + 25
            elif count_f > count_t:
                if self.personality_factors[2] == 'F':
                    similarity_rate = similarity_rate + 25
            if count_p > count_j:
                if self.personality_factors[3] == 'P':
                    similarity_rate = similarity_rate + 25
            elif count_j > count_p:
                if self.personality_factors[3] == 'J':
                    similarity_rate = similarity_rate + 25
            # check the most repeated factors for each clusters
            # save them in variables and compare

            if similarity_rate >= 70:
                skills = list(Cluster_group.filter(clusters=cluster).values('skills').distinct())
                return self.convert_skills(skills)
        skills = list(Cluster.objects.values('skills').annotate(count=Count('skills')).order_by("-count"))
        skills = skills[0]
        return self.convert_skills([skills])
