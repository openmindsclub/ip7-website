from django.shortcuts import render
from subscription.forms import SubscribeForm
def home(request):

	template="index.html"

	context={"form":SubscribeForm}
	return render(request, template, context)

