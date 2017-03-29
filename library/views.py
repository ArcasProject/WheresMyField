from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, render_to_response

def viewDashboard(request, slug):
	keywords = ['Game Theory', 'Prisoners Dilemma', 'Tournament']
	authors = ['Nikoleta Glynatsi', 'Prince Charles', 'Postman Pat', 'Madonna']
	journals = ['Management Science', 'Operations Research', 'EJOR']
	return render(request, 'library/index.html', {'keywords':keywords, 'authors':authors, 'journals':journals, 'slug':slug})