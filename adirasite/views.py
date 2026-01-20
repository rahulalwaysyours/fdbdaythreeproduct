from django.shortcuts import render

#controllers
def index(request):
    return render(request, 'home.html', {
        "a_list": [i for i in range(1,100)],
    })

def about(request):
    return render(request, 'about.html')