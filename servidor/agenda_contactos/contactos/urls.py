"""agenda_contactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static

from agenda_contactos import settings
from contactos.views import ContactosList, ContactosCreate, ContactosGet, ContactosEdit, ContactosDelete, \
    ImagenContactoUpload

urlpatterns = [

    url(r'^list/$', ContactosList.as_view(), name='list'),
    url(r'^add/$', ContactosCreate.as_view(), name='add'),
    url(r'^get/(?P<pk>[\d]+)/$', ContactosGet.as_view(), name='get'),
    url(r'^edit/(?P<pk>[\d]+)/$', ContactosEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[\d]+)/$', ContactosDelete.as_view(), name='delete'),
    url(r'^image/(?P<id>[\d]+)/$', ImagenContactoUpload.as_view(), name='image_upload'), #FIXED

]


