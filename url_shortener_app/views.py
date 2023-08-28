from django.shortcuts import render,redirect
from .models import *
from urllib.parse import unquote

# Create your views here.
import random
import string

def generate_short_code():
     characters = string.ascii_uppercase + string.digits

     return ''.join(random.choice(characters) for _ in range(8))

def URL_Shortener(request):
    current_domain=request.scheme + "://" + request.get_host()+"/"

    if request.method=='POST':
        originalurl=request.POST['Orginal_URL']

        try:
            existing_url=URL.objects.get(original_url=originalurl)
            # print(existing_url)
            context={ 
                'current_domain':current_domain,
                'shorten_url':existing_url.short_url,
                'original_url':originalurl
            }
            return render(request,'url_shortener_app/home.html',context)
        except:
            short_code=generate_short_code()
            new_url=URL(original_url=originalurl,short_url=short_code)

            new_url.save()
            context={
                'current_domain':current_domain,
                'shorten_url':short_code,
                'original_url':originalurl
 
          }


            return render(request,'url_shortener_app/home.html',context)
    return render(request,'url_shortener_app/home.html')

def redirect_to_original(request,shorten_url):
    try:
        url=URL.objects.get(short_url=shorten_url)
        return redirect(url.original_url)

    except URL.DoesNotExist:  

     return render(request,'url_shortener_app/home.html',{'error':'Short URL Not Found'})
    
