from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, render_to_response

def viewDashboard(request):
    keywords = ['Game Theory', 'Prisoners Dilemma', 'Tournament']
    authors = ['Nikoleta Glynatsi', 'Prince Charles', 'Postman Pat', 'Madonna']
    journals = ['Management Science', 'Operations Research', 'EJOR']

    listView = loader.get_template("library/listView.html")

    journalsView = listView.render(context = {'blocktitle': "Popular Journals:", 'listitems':journals})
    authorsView  = listView.render(context = {'blocktitle': "Popular Authors:" , 'listitems':authors })
    keywordsView = listView.render(context = {'blocktitle': "Popular Keywords:", 'listitems':keywords})

    return render(request, 'library/base.html', {'dataview':[journalsView, authorsView, keywordsView]})
