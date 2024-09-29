from django.shortcuts import render

# Create your views here.

def get_hello(request):
    return render (request, 'hello.html', {
        'title': 'Hello',
    })