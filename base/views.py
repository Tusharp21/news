from django.shortcuts import render
from .fetch  import fetch 

# Create your views here.

def index(request):
    if request.GET.get('name')!= None:
        # Category ='all'
        Category =request.GET.get('name')
    else:
        Category = 'all'
    data = fetch(Category)
    
    
    return render(request,'index.html',{'data':data})
