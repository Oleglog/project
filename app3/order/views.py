from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest
from cart.cart import CartSession
from .forms import OrderForm
from .models import OrderItem
from django.urls import reverse

# Create your views here.

@login_required(login_url='login')
def create_order(requset:HttpRequest):
    cart = CartSession(requset.session)
    if requset.method =="POST":
        form = OrderForm(requset.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_user = requset.user
            order.save()
            for item_cart in cart:
                OrderItem.objects.create(order=order, phone=item_cart['phone'], quantity=item_cart['quantity']).save()
            cart.clear()
            return redirect(reverse('profile'))
    else:
        form = OrderForm()        
                