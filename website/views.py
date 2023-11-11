from email import message
from django.contrib import messages
# from pyexpat.errors import messages
from django.shortcuts import render
from .models import Member
from .forms import Memberform

# Create your views here.
def index(request):
    all_member = Member.objects.all

    return render(request,'home.html',{'all': all_member})

def register(request):
    if request.method == "POST":
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("Your form has been submited succeffully"))
        return render(request, 'register.html',{})
    else:
        return render(request, 'register.html',{})