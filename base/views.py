# create my views here
# render html files in template folder
from django.http import HttpResponseRedirect, HttpResponse
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


def about_us_view(request):
    explanation = "این سایت یک سایت توصیه گر است. هدف ما کمک به شما است تا بر اساس نتیجه ی تست شخصیت مایرزبریگز خود " \
                  "بتوانید مناسب ترین مهارت جهت فراگیری را انتخاب کنید. در صورتی که مهارتی را تسلط دارید نیز میتوانید " \
                  "از طریق بخش تکمیل پرسشنامه مارا در این مسیر یاری دهید "
    return render(request, 'about_us.html', {'explanation': explanation})


def contact_us_view(request):
    contact_info = {
        'Email': 'MrAdvisor.com@gmail.com',
        'Phone_Number': '09130177811',
    }
    return render(request, 'contact_us.html', {'contact_info': contact_info})
