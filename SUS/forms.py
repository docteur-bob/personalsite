from django import forms

class Formulaire(forms.Form):
	note_globale = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_1 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_2 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_2_inv = forms.BooleanField(required=False)

	item_3 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_4 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	
	item_4_inv = forms.BooleanField(required=False)

	item_5 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_6 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_6_inv = forms.BooleanField(required=False)

	item_7 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_8 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_8_inv = forms.BooleanField(required=False)

	item_9 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_10 = forms.FloatField(widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_10_inv = forms.BooleanField(required=False)

