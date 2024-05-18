from django.shortcuts import render
from.models import Slider

def index(request):

    sliders = Slider.objects.all()
    print(sliders)
    return render(request, 'spaceAgency_app/index.html', {'sliders': sliders})
    

