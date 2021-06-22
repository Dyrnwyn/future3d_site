"""future3d_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from feedback.views import contact_us
from manage_product.views import download_json
from faq.views import faq

urlpatterns = [
    path('product/', include('manage_product.urls')),
    path('admin/manage_product/download_json/', download_json),
    path('governance/', admin.site.urls),
    path('contact_us/', contact_us),
    path('faq/', faq),
    path('magazine/', include('eshop.urls')),
    path('ar/', include('ar.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
