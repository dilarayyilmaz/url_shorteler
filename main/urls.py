
from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_shortener_view, name='home'),
    path('<slug:slug>/', views.redirect_view, name='redirect'),
]