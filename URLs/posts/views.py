from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import datetime

# Create your views here.
def dummy_view(request, id):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now} and the id is {id} %s.</body></html>" 
    return HttpResponse(html)

def status_code_view(request, exception):
    return HttpResponseNotFound('web page not found, 404 error')

def entry_list(request):
    return render(request, 'posts/post_list.html', {})

def redirect_back_home(request):
    return redirect('/entries/1')