from django.http import HttpResponse
import uuid
from django.shortcuts import render

from shortner.models import Url

def index(request):
    return render(request, 'index.html')

# convert the long url to a short url
def do(request):
    if request.method == 'POST':
        url = request.POST['long_url']
        url_short_code = str(uuid.uuid4())[:6]
        new_url = Url(long_url = url, url_short_id = url_short_code)
        new_url.save()
        return HttpResponse(url_short_code)
