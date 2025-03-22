from django.shortcuts import render, redirect
from todolist1.models import Todolist

# Create your views here.
def todolist(request):
    if (request.method=="POST"):
        data = request.POST
        newtask = data.get("task")

        if newtask:
            Todolist.objects.create(task = newtask)
            return redirect("/")
        
    # print(Todolist.objects.all())
    alltask = Todolist.objects.all()
    context = {"tasks" : alltask}
        
    return render(request, "todo.html" , context=context)