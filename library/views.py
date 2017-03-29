from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, render_to_response
from .machine_learning.ml_journals import MachineLearning

from .forms import SearchForm

def viewDashboard(request):
    keywords = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            keywords = keywords.split(' ')

    ml = MachineLearning()
    ml.getData(keywords)

    keywords = ml.link_keywords
    authors = ml.author_connections
    journals = ml.journals

    listView = loader.get_template("library/listView.html")

    journalsView = listView.render(context = {'blocktitle': "Popular Journals:", 'listitems':journals})
    authorsView  = listView.render(context = {'blocktitle': "Popular Authors:" , 'listitems':authors })
    keywordsView = listView.render(context = {'blocktitle': "Popular Keywords:", 'listitems':keywords})

    return render(request, 'library/base.html', {'form' : SearchForm(), 'dataview':[journalsView, keywordsView, authorsView]})
