from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello Raindolf, Do you love Django")

def welcome(request):
	return HttpResponse("In Ghana we say Akwaaba")
