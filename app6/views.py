from django.shortcuts import render
from .models import Users
# Create your views here.
def user_list(request):
    users = Users.objects.order_by('-FirstName')
    context = {'users': users}
    return render(request,'users.html',context=context)

def index(request):
    return render(request,'index3.html')

