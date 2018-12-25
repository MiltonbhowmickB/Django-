from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
	link_name = ["Link1","Link2","Link3"]
	online_link = ["https://www.google.com","https://www.facebook.com","https://www.w3schools.com"]
	name = "contact info"
	args = {'title':name, 'names':link_name, 'links':online_link}
	return render(request, 'accounts/attendance_html.html', args) 