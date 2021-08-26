from django.shortcuts import render , HttpResponse
from datetime import datetime
from HOME.models import Contact

# Create your views here.
def index(request):
    return render(request,'home.html')

def gallery(request):
    return render(request,'gallery.html')

def aboutme(request):
    return render(request,'aboutme.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        reason = request.POST.get('reason')
        contact = Contact(name=name , email=email , phone=phone , reason=reason , date=datetime.today())
        contact.save()
    
    return render(request,'contactme.html')