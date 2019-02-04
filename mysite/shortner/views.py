from django.shortcuts import render,Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Bitly
from django.views import View




def redirect(request, keys=None, *args, **kwargs):
    try:
        obj=Bitly.objects.get(keys=keys)
    except Bitly.DoesNotExist:
        raise Http404("Page not found")
    
    
    return HttpResponseRedirect(obj.website)

def index(request):
    
    if request.method=='GET':
        print(request.GET)
    if request.method=='POST':
        # print(request.POST)
        website = request.POST['website']
        
        obj, created=Bitly.objects.get_or_create(website=website)
        
        
        
        new_obj = Bitly.objects.get(website=obj)
        new_context={
                "object": new_obj,
                "created": created,
                }
        print(new_obj.keys)
        print(new_obj.website)
        
        render(request, "shortner/success.html",new_context)
            
        
        
    
    return render(request, 'shortner/index.html', {})
    


# Create your views here.
