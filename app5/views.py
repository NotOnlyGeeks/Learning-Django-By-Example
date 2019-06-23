from django.shortcuts import render
from .models import AccessRecord,Webpage,Topic


# Create your views here.
def index(request):
    websites=AccessRecord.objects.order_by('-date')
    context={'websites': websites}
    return render(request, 'index2.html', context=context)

