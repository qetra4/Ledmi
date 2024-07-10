from django.urls import re_path, path
from . import cart_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', cart_views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_views.cart_remove, name='cart_remove'),
]