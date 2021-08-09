# create my views here
# render html files in template folder
from django.template.context_processors import request
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
