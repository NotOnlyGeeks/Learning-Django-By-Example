from django.shortcuts import render

# Create your views here.
def index(request):
    context={'insert_me': 'This is the message!'}
    return render(request,'index.html',context=context)


