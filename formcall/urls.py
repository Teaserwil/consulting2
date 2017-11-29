from django.conf.urls import url, include
from django.contrib import admin
from formcall import views


urlpatterns = [
    url(r'^main/', views.formcall , name = 'main'),
]
