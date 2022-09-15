import uuid

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect, get_object_or_404
from shortner.models import Url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.template import loader
import socket

def index(request):
    return render(request, 'index.html')

# convert the long url to a short url
def do(request):
    if request.method == 'POST':
        url = request.POST['long_url']
        val = URLValidator()
        try:
            # validate the url
            val(url)
            # create url short id
            url_short_code = str(uuid.uuid4())[:6]
            # create new url class 
            new_url = Url(long_url = url, url_short_id = url_short_code)
            # save new url to the database
            new_url.save()
            return HttpResponseRedirect(reverse('shortner:yuppi', args=(url_short_code,)))
        except ValidationError:
            return HttpResponse('Sorry, this is not a valid url.')

def successfully_created(request, url_short_code):
    print('url_short_code', url_short_code)
    # get url by url_short_code
    url_from_database = get_object_or_404(Url, url_short_id = url_short_code)
    context = {
        'url': url_from_database,
    }
    return render(request, 'successful.html', context)

def go(request, url_short_code):
    # get url from the database
    url_from_database = get_object_or_404(Url, url_short_id = url_short_code)
    # redirect to the long url
    return redirect(url_from_database.long_url)
