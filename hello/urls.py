from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [    
    path('', views.loginForm),
    path('admin/', admin.site.urls),
    path('bet',views.betLotto),
]
