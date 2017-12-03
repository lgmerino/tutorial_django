"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import views
from catalog import views as catalog_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.HomeView.as_view(), name='HomeView'),

    url(r'^band/$', catalog_views.BandListView.as_view(), name='BandListView'),
    url(r'^band/create/$', catalog_views.BandCreateView.as_view(), name='BandCreateView'),
    url(r'^band/update/(?P<pk>[0-9]+)/$', catalog_views.BandUpdateView.as_view(), name='BandUpdateView'),
    url(r'^band/delete/(?P<pk>[0-9]+)/$', catalog_views.BandDeleteView.as_view(), name='BandDeleteView'),
]
