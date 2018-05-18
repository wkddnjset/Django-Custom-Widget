from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^country/$', country_list, name='country_list'),
]