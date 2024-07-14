from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import random
from django.db.models import Q
from myapp.models import Person


def index(request):
    if not  request.user.is_authenticated:
        return HttpResponse('You cannot access the page')

    query = request.GET.get('query')

    if query is not None and query != "":
        persons = Person.objects.filter(Q(name__icontains=query ) | Q(phone__icontains=query))
    else:
        persons = Person.objects.all().order_by('-id') # use - for descending order
    
    total_person = Person.objects.all().count()
    # print(persons.query)
    print(persons)
    for person in persons:
        print(person.name)
        print(person.phone)
        print(person.email)

    print("INDEX CALLED")
    data = random.randint(0,50)

    context ={
        'person_list':persons,
        'total_person':total_person
    }
    return render(request,'index.html',context)

def about(request):

    return render(request,'base.html')
    
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


person_list = [
    {
        'name':"HARI SHARMA",
        'phone':"94949329",
        'email':"test@gmail.com"
    }

]
def services(request):
    name = request.GET.get('fullname')
    email = request.GET.get('email')
    phone = request.GET.get('phone')

    if (name != None and name != "") and (email != None and email != "") and (phone != None and phone !=""):
        message = f" Thank you for contacting us, your details are Name:{name}, Email:{email},Phone:{phone}"
        person_data = {
             'name':name,
        'phone':phone,
        'email':email
        } 
        person_list.append(person_data)

    else:
        message = ""
    context = {
        'message':message,
        'person_list':person_list
    }

    return render(request,'services.html',context)

# def dynamic(request,name):
#     print(name)
#     return HttpResponse("Dynamic page")

def dynamic(request,name):
    print(name)
    return HttpResponse(f"PROFILE PAGE OF {name}")
def add(request,num1,num2):

    return HttpResponse(f"The sum of {num1} and {num2} is {num1+num2}")


