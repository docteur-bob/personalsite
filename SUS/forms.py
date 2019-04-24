from django import forms

class Formulaire(forms.Form):
	note_globale = forms.CharField()
	item_1 = forms.FloatField()
	item_2 = forms.FloatField()
	item_3 = forms.FloatField()
	item_4 = forms.FloatField()
	item_5 = forms.FloatField()
	item_6 = forms.FloatField()
	item_7 = forms.FloatField()
	item_8 = forms.FloatField()
	item_9 = forms.FloatField()
	item_10 = forms.FloatField()