from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
#tasklist = ["foo", "bar", "baz"]
#tasklist = [] #start with empty

class NewTaskForm(forms.Form) :
    task = forms.CharField(label="New Tasks")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)  #input validation

def index(request) :
    if "tasks" not in request.session :
        request.session["tasklist"] = []

    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasklist"]
    })

def add(request) :
    if request.method == "POST" :
        getform = NewTaskForm(request.POST)
        if getform.is_valid() :
            task = getform.cleaned_data["task"] #call the task  variable in class
            #tasks.append(task)
            request.session["tasklist"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else :
            return render(request, "tasks/add.html", {
                "getform" : form
            })

    return render(request, "tasks/add.html", {
        "getform" : NewTaskForm()
    })
