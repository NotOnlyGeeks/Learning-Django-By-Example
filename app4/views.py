from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'insert me':'This is my picture!'}
    return render(request,'index.html',context=context)



