from django.shortcuts import render
import stripe

# Create your views here.
def index(request):
	return render(request,'index.html')

def contact(request):
	return render(request,'contact.html')

