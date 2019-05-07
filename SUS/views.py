from django.shortcuts import render,get_object_or_404
from SUS.forms import Formulaire
from lib.SUS import Rang_sus, Item
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
			i1 = Item(float(form.cleaned_data['item_1']), 1, ng.note, ng.rang,"off")
			i2 = Item(float(form.cleaned_data['item_2']), 2, ng.note, ng.rang, form.cleaned_data['item_2_inv'])
			i3 = Item(float(form.cleaned_data['item_3']), 3, ng.note, ng.rang, "off")
			i4 = Item(float(form.cleaned_data['item_4']), 4, ng.note, ng.rang, form.cleaned_data['item_4_inv'])
			i5 = Item(float(form.cleaned_data['item_5']), 5, ng.note, ng.rang, "off")
			i6 = Item(float(form.cleaned_data['item_6']), 6, ng.note, ng.rang, form.cleaned_data['item_6_inv'])
			i7 = Item(float(form.cleaned_data['item_7']), 7, ng.note, ng.rang, "off")
			i8 = Item(float(form.cleaned_data['item_8']), 8, ng.note, ng.rang, form.cleaned_data['item_8_inv'])
			i9 = Item(float(form.cleaned_data['item_9']), 9, ng.note, ng.rang, "off")
			i10 = Item(float(form.cleaned_data['item_10']), 10, ng.note, ng.rang, form.cleaned_data['item_10_inv'])
			lst_item = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]




		args = {'form' : form,
				"ng" : ng,
				"lst_item" : lst_item,
				}

		
		return render(request, self.template_res, args)
