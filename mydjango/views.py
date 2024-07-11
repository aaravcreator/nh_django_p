from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import random


def index(request):
    print("INDEX CALLED")
    data = random.randint(0,50)
    return HttpResponse(f"HELLO FROM DJANGO!! {data}")

def about(request):

    return render(request,'about.html')
    
def contact(request):
    name = "DJANGO SITE"
    email = "django@gmail.com"
    phone = "9855637727"

    alternate_numbers = [
        '938238283','83283234',
        '48484848'
    ]

    context = {
        'name':name,
        'email':email,
        'phone':phone,
        'alternate_numbers':alternate_numbers,
        'display_email':True
    }

    return render(request,'contact.html',context)

def services(request):
    print(request.GET.get('fullname'))
    return render(request,'services.html')

# def dynamic(request,name):
#     print(name)
#     return HttpResponse("Dynamic page")

def dynamic(request,name):
    print(name)
    return HttpResponse(f"PROFILE PAGE OF {name}")
def add(request,num1,num2):

    return HttpResponse(f"The sum of {num1} and {num2} is {num1+num2}")


