"""ecomSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('342-dssr-2321-5453-fgdrt-4535-23cx/', admin.site.urls),
    path('', views.home, name='home'),

    path('contact/', include('contact.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),

    path('404', views.error_404_view),
    path('500', views.error_500_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ecomSite.views.error_404_view'
handler500 = 'ecomSite.views.error_500_view'