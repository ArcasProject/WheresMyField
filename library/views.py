from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, render_to_response

def viewDashboard(request):
	return render(request, 'library/index.html')