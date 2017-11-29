from django.shortcuts import render
from . forms import FormcallForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
def formcall(request):
	form = FormcallForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		print ( request.POST )
		print (form.cleaned_data)
		data = form.cleaned_data
		print (data['name'] )
		new_form = form.save()

	return render(request, 'formcall/main.html', locals() )	