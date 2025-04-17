from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random 
from home.forms import ContactForm
#import requests

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
    form = ContactForm()
    context = {'form': form}
    return render(request,'contact.html',context)


def dynamic_url(request,id):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    context = {'form': form}
    print(f"This is the value that we got in func--> {id}")
    return render(request,'dynamic_url.html',context)


#HTML forms 

def request_product(request):
    return render(request,'request.html')