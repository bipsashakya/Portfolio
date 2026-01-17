from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from app import models
from app.models import Contact
# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to My Portfolio!")

# def home(request):
#     return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        print('post')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        print(name,email,phone,message)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'length of name should be greater than 1 and less than 30')
            return render(request,'home.html')
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'length of email should be greater than 1 and less than 30')
            return render(request,'home.html')
        if len(phone)>2 and len(phone)<12:
            pass
        else:
            messages.error(request,'Invalid number.Try again')
            return render(request,'home.html')
        if len(message)>1 and len(message)<500:
            pass
        else:
            messages.error(request,'Not a valid message')
            return render(request,'home.html')
        
        ins=models.Contact(name=name,email=email,phone=phone,message=message)
        ins.save()
        messages.success(request,'Your message has been sent successfully')
        print("Data saved successfully")
        print('The request is now passed')

    return render(request,'home.html')  