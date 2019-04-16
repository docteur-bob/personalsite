from django.shortcuts import render, get_object_or_404
from .models import Page_projet, Curivitae

# Create your views here.
def landingpage(request):
	projets = Page_projet.objects.filter()
	cv = Curivitae.objects.filter()
	return render(request,'book/landingpage.html',{'projets' : projets, 'cv' : cv})

def page_projet(request,tag):
	projets = get_object_or_404(Page_projet, tag=tag)
	return render(request, 'book/page_projet.html',{'projets' : projets})
