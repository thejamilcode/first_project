from django.shortcuts import render,HttpResponse
from tution.models import Contact
def Home(request):
    name = ["jamil","kamil","ramim","suhana",'afruja']
    context = {
        'name':name,
    }
    return render(request,"home.html",context)

