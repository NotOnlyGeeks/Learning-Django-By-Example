from django.shortcuts import render
from .models import Users


# Create your views here.
def index(request):
    return render(request, 'index4.html')

def usersView(request):
    users = Users.objects.order_by('-FirstName')
    context = {'users': users}
    return render(request, 'users1.html', context=context)
