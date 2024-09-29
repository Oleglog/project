from django.urls import path
from .views import register
from .views import login_view
from .views import logout_view
from .views import register, login_view, logout_view, profile, add_user, edit_user, delete_user, user_list

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('add/', add_user, name='add_user'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
    path('', user_list, name='user_list'),
    
]