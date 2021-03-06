
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .forms import SubmitUrlForm
from .models import URL
import re

from analytics.models import ClickEvent

class HomeView(View):
    def get(self, request):
        the_form = SubmitUrlForm()
        context = {
            "title": "tu.com",
            "form": the_form
        }
        return render(request, "shortner/home.html", context) 

    def post(self, request):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "tu.com",
            "form": form
        }
        template = "shortner/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            print(new_url[:8])
        
            if  new_url[:8]!="https://":
                new_url="https://"+new_url
            print(new_url)
            obj, created = URL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exist.html"
    
        return render(request, template ,context)


def kirr_redirect_view(request,sc):
    print(sc)
    #obj = URL.objects.filter(shortcode=sc).first()
    obj = get_object_or_404(URL, shortcode=sc)
    

    return redirect(obj.url)

  



class KirrCBView(View):
    def get(self, request,sc):
        obj = get_object_or_404(URL, shortcode=sc)
        return redirect(obj.url)

# class URLRedirectView(View):
#     def get(self, request, sc=None, *args, **kwargs):
#         qs = URL.objects.filter(shortcode__iexact=sc)
#         if qs.count() != 1 and not qs.exists():
#             raise Http404
#         obj = qs.first()
#         print(ClickEvent.objects.create_event(obj))
#         return redirect(obj.url)