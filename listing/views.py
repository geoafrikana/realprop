from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'listing/index.html')

def list_property(request):
    return render(request, 'listing/list_property.html')