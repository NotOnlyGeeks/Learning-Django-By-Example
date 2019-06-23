from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'insert_me': 'My name is Prajwal'}
    return render(request, 'index2.html', context=context)

