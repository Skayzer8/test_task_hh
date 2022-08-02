from django.urls import path

from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.hello_user, name='hello_page')
]
