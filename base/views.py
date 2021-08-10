# create my views here
# render html files in template folder
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PersonalityFactors
from .recommend import Recommend

personality = None


def get_personality(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalityFactors(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            personality = form.cleaned_data['p_factors']
            recommends = Recommend(personality)
            user_recommends = recommends.calculate_similarity()
            # redirect to a new URL:
            return render(request, 'recommend.html', {'user_recommends': user_recommends})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonalityFactors()

    return render(request, 'home.html', {'form': form})
