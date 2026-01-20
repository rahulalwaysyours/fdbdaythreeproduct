from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        "a_list": [i for i in range(1,100)],
    })