from django.shortcuts import render
from .forms import FormModel
# Create your views here.
def index(request):
    return render(request,'index5.html')

def formPage(request):
    form = FormModel()

    if request.method == 'POST':
        form = FormModel(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid form")

    return render(request,'formpage.html',{'form':form})