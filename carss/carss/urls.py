"""carss URL Configuration

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
# import settings for media folder
from django.conf import settings
# import static for media folder
from django.conf.urls.static import static

urlpatterns = [
    # path() - arg1: route, arg2: include('app_name.urls')
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('listings/', include('listings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# settings for media folder url
