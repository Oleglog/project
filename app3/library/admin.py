from django.contrib import admin
from library.models import Book, Publisher, Author
from .models.phone import Phone
from .models.smart_watch import Smart_watch
from .models.headphones import Headphones
# Register your models here.

admin.site.register(Phone)
admin.site.register(Headphones)
admin.site.register(Smart_watch)

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class AdminPulisher(admin.ModelAdmin):
    pass
