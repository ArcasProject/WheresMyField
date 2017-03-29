from django.http import HttpResponse
from django.template import loader

def viewDashboard(request):
    template = loader.get_template('library/index.html')
    return HttpResponse(template.render())
