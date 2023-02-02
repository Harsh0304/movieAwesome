from django.shortcuts import render
from .models import Movies,categories
# Create your views here.
def index(request):
    movie=Movies.objects.all()
    cat=categories.objects.all()
    return render(request,'index.html',{'movie':movie,'categ':cat})

def base(request):
    return render(request,'base.html')

def profile(request,pid):
    data=Movies.objects.get(id=pid) 
    return render(request,'profile.html',{'data':data})    

def search(request):
    print(request)
    query=request.GET.get('query',False)
    #print(query)
    movie=Movies.objects.filter(title__icontains=query)
    params={'movie':movie}
    return render(request,'search.html',params)    