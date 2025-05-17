
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render()) #Response correct spelling 's' not 'c'
    # Look for spelling mistake u do that to optern 'tempalte' it's template
    #if spell mistake the web loads on browser bt show varying textcd

