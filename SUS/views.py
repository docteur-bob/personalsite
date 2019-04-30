from django.shortcuts import render,get_object_or_404
from SUS.forms import Formulaire
from lib.SUS import Rang_sus
from django.views.generic import TemplateView

# Create your views here.
class SUShome(TemplateView):
	template_name = "SUS/formulaire.html"
	template_res = "SUS/result.html"
	
	def get(self, request):
		form = Formulaire()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = Formulaire(request.POST)
		if form.is_valid():
			ng = Rang_sus(float(form.cleaned_data['note_globale']))
			i1 = form.cleaned_data['item_1']
			i2 = form.cleaned_data['item_2']
			i3 = form.cleaned_data['item_3']
			i4 = form.cleaned_data['item_4']
			i5 = form.cleaned_data['item_5']
			i6 = form.cleaned_data['item_6']
			i7 = form.cleaned_data['item_7']
			i8 = form.cleaned_data['item_8']
			i9 = form.cleaned_data['item_9']
			i10 = form.cleaned_data['item_10']




		args = {'form' : form,
				'ng' : ng,
				'i1' : i1,
				'i2' : i2,
				'i3' : i3,
				'i4' : i4,
				'i5' : i5,
				'i6' : i6,
				'i7' : i7,
				'i8' : i8,
				'i9' : i9,
				'i10' : i10
				}

		
		return render(request, self.template_res, args)
