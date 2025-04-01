from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random 

def index(request):
    lucky_number = random.randint(100,999)
    vegetables = ["Tomotoes",'Potatoes','Chillies']
    context = {'lucky_number':lucky_number,'vegetables':vegetables}

    for vegetable in vegetables:
        print(vegetable)
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def dynamic_url(request,id):
    print(f"This is the value that we got in func--> {id}")
    return render(request,'dynamic_url.html',context={'id':id})