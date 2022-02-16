from datetime import datetime
from django.shortcuts import render
from app.models import Contact

def index(request):
    return render(request, 'index.html')

def aboutranchi(request):
    return render(request, 'aboutranchi.html')

def waterfalls(request):
    return render(request, 'waterfalls.html')

def valley(request):
    return render(request, 'valley.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')



