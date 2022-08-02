from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls', namespace='hello')),
]

handler404 = 'hello.views.page_not_found'