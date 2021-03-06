from django.shortcuts import render
import sendmail
from django.http import HttpResponseRedirect
from markdown import markdown
from .forms import SubscribeForm
from generate import makeinvit

# Create your views here.

def Subscribtion(request):
	context={"form":SubscribeForm}
	form=SubscribeForm(request.POST)
	if form.is_valid():
		firstname=form.cleaned_data['firstname']
		familyname=form.cleaned_data['familyname']
		addresses=form.cleaned_data['email']

		sub=form.save(commit=False)
		sub.save()

		makeinvit(firstname,familyname)

		sendmail.sendmail(addresses,"Invitation PI Day","Felicitation, vous etes bien accepte.", "/var/www/pi/piday/subscription/result/"+firstname+familyname+".png")

		return render(request,'succes.html',context)
	else:
		print form.errors
		return render(request,'error.html',context)



