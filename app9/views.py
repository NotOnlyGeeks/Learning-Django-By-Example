from django.shortcuts import render
from .forms import FormName

# Create your views here.
def index(request):
    return render(request,'index5.html')

def formPage(request):

    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)


    return render(request,'formpage.html',{'form':form})

