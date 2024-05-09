from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "hell/index.html")

def Hell(request, name):
    return render(request, "hell/Hell.html",
                  {"name": name.capitalize()
})


