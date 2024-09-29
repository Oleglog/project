from django.shortcuts import render
from .cart import CartSession
from django.http import HttpRequest
from library.models.phone import Phone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Create your views here.

def cart_add(request: HttpRequest, phone_id):
    cart = CartSession(request.session)
    phone = get_object_or_404(Phone, id=phone_id)
    cart.add(phone=phone)

    return redirect(reverse('cart_detail'))

def cart_remove(request: HttpRequest, phone_id):
    cart = CartSession(request.session)
    phone = get_object_or_404(Phone, id=phone_id)
    cart.remove(phone=phone)
    return redirect(reverse('cart_detail'))

def cart_detail(request: HttpRequest):
    cart = CartSession(request.session)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def update_cart(request, phone_id):
    cart = CartSession(request.session)  # Получаем корзину

    if request.method == 'POST':
        action = request.POST.get('action')

        phone = get_object_or_404(Phone, id=phone_id)

        if action == 'increase':
            cart.add(phone)  # Добавить один экземпляр товара
        elif action == 'decrease':
            cart.remove(phone)  # Удаляет один экземпляр товара

        return redirect('cart_detail')  # Перенаправляем на страницу корзины после обновления
    

def clear_cart(request):
    if request.method == 'POST':
        cart = CartSession(request.session)
        cart.clear()  # Метод для очистки корзины
        return redirect('cart_detail')

