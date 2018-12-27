from django.shortcuts import render, HttpResponse
from accounts.forms import RegistrationForm

# Create your views here.

def home(request):
	link_name = ["Link1","Link2","Link3"]
	online_link = ["https://www.google.com","https://www.facebook.com","https://www.w3schools.com"]
	name = "contact info"
	zips = zip(link_name, online_link)
	args = {'title':name, 'names':link_name, 'links':online_link, 'zipped':zips}
	return render(request, 'accounts/attendance_html.html', args)

def register(request): 
	if request.method == ['POST']:
		form = RegistrationForm[request.POST]
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)