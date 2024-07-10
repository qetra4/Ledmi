"""
URL configuration for Rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from shop import views
from cart import cart_views
from cart import urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import finders

namespace = 'shop'

urlpatterns = [
    path('', views.index_show),
    path('shortfilms/', views.shortfilms_show),
    path('colorgrading/', views.colorgrading_show),
    path('rental/', views.rental_show),
    path('contacts/', views.contacts_show),
    path('form/', views.form_show),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^orders/', include(('orders.url', 'orders'), namespace='orders')),
    re_path(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    re_path(r'^shop/', include(('shop.url', 'shop'), namespace='shop')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Обработка статических и медиа файлов во время разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


