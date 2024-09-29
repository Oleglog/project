from django.shortcuts import render, redirect
from library.models import Book
from .models.phone import Phone
from .models.smart_watch import Smart_watch
from .models.headphones import Headphones
from django.db.models import Q
from app3.forms import SearchForm

# Create your views here.

def get_info(request):
    book = Book.objects.get(id=1)
    return render(request, 'base1.html', context= {
        'book': book,
    })

def get_author(request):
    book_author = Book.objects.filter(author__name= "ШАХМАТАШКИН")
    return render(request, 'author.html', context= {
        'book_author': book_author,
    })

def get_home(request):
    return render (request, 'home.html', {
        
    }
    )

def get_about(request):
    return render (request, 'about.html', {

    })

def get_products(request):
    phone_items = Phone.objects.all()
    smart_watch = Smart_watch.objects.all()
    headphones = Headphones.objects.all()
    return render (request, 'products.html', {
        'phone_items': phone_items,
        'smart_watch_items': smart_watch,
        'headphones_items': headphones,
    })

def get_phone_detail(request, pk):
    phone = Phone.objects.get(pk=pk)
    return render(request, 'detail_phone.html', context= {
        'phone' :phone
    })

def get_headphones_detail(request, pk):
    Headphone = Headphones.objects.get(pk=pk)
    return render(request, 'detail_headphones.html', context= {
        'headphone' :Headphone
    })

def get_smart_watch_detail(request, pk):
    smart_watch = Smart_watch.objects.get(pk=pk)
    return render(request, 'smart_watch_detail.html', context= {
        'smart_watch' :smart_watch
    })



def search(request):
    form = SearchForm()
    phones_results = []
    headphones_results = []
    smart_watchs_results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            phones_results = Phone.objects.filter(title__icontains=query)
            headphones_results = Headphones.objects.filter(title__icontains=query)
            smart_watchs_results = Smart_watch.objects.filter(title__icontains=query)

    return render(request, 'search.html', {
        'form': form,
        'phones_results':phones_results,
        'headphones_results':headphones_results,
        'smart_watchs_results':smart_watchs_results,
    })




