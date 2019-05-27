from django import forms

class Formulaire(forms.Form):
	note_globale = forms.FloatField(min_value=20, max_value=100, widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_1 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_2 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))


	item_3 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	item_4 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))
	

	item_5 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_6 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_7 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_8 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))


	item_9 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_10 = forms.FloatField(min_value=1, max_value=5,widget=forms.NumberInput(
		attrs={
		'class' : 'form-control',
		}
		))

	item_inv = forms.BooleanField(required=False)

