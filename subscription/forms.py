from django import forms
from .models import Subscribe

class SubscribeForm(forms.ModelForm):
	class Meta:
        	model = Subscribe
		widgets = {
	            'email' : forms.TextInput(attrs = {'placeholder': ' Votre e-mail' , 'name':'email'}),
	            'firstname' : forms.TextInput(attrs = {'placeholder': ' Votre prenom'}),
	            'familyname' : forms.TextInput(attrs = {'placeholder': ' Votre nom'}),
		    'occupation' : forms.TextInput(attrs = {'placeholder': ' Quelle est votre occupation (soyez precis s\'il vous plait.)' , 'style': "width:767px;"}),
        	    }
