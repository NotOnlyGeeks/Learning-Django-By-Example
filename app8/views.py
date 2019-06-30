from django.shortcuts import render
from .forms import FormName

# Create your views here.
def index(request):
    return render(request,'index5.html')

def formPage(request):
    form = FormName()

    if request.method =='POST':
        form = FormName(request.POST)

        if form.is_valid():
            firstName = form.cleaned_data['FirstName']
            lastName = form.cleaned_data['LastName']
            email = form.cleaned_data['Email']
            print('FirstName',firstName)
            print('LastName',lastName)
            print('Email',email)

    return render(request,'formpage.html',{'form':form})


