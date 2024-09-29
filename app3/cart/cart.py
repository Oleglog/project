from django.contrib.sessions.backends.base import SessionBase
from library.models.phone import Phone
from decimal import Decimal

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'

    def __init__(self, session: dict) -> None:
        self.session: dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)

        if not self.cart:
            self.cart = self.session[self.CART_SESSION_ID] = {}

    def __iter__(self):
        phone_ids = self.cart.keys()
        phones = Phone.objects.filter(id__in=phone_ids)

        cart = self.cart.copy()

        for phone in phones:
            cart[str(phone.id)]['phone'] = phone

        for item in cart.values():
            item['price'] = float(item['price'])  # Преобразуем цену в float для сериализации
            item['total_price'] = item['price'] * item['quantity']  # Общая цена
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
        
    def save(self):
        self.session.modified = True

    def add(self, phone, quantity=1, update_quantity=False):
        phone_id = str(phone.id)

        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0, 'price': float(phone.price)}  # Преобразуем Decimal в float

        if update_quantity:
            self.cart[phone_id]['quantity'] = quantity
        else:
            self.cart[phone_id]['quantity'] += quantity
        
        self.save()

    def remove(self, phone):
        phone_id = str(phone.id)

        if phone_id in self.cart:
            if self.cart[phone_id]['quantity'] > 1:
                self.cart[phone_id]['quantity'] -= 1
            else:
                del self.cart[phone_id]  # Если количество равно 1, удаляем элемент из корзины

        self.save()

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())  # Используйте float для общего итога

    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()