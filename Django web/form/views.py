from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

form = []

class NewTaskForm(forms.Form):
    form = forms.CharField(label = "New Task")

# Create your views here.

def index(request):
    return render(request, "form/start.html", {
        "form" : form
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data["form"]
            form.append(form)
            return HttpResponseRedirect(reverse("form:start"))
        else:
            return render(request, "form/add.html", {
                "form": form
            })
    return render(request, "form/add.html",{
        "form": NewTaskForm()
    })