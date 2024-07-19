from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


from django.db import connections
from django.db.utils import OperationalError

def check_db_connection():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True
    return connected

# Вызовите эту функцию и выведите результат, чтобы проверить подключение
print("Database connected:", check_db_connection())

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})

    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
