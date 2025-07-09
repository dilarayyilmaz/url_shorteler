
from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_shortener_view, name='home'),
    path('<slug:slug>/', views.redirect_view, name='redirect'),
  path('api/urls/',views.get_all_urls, name='get_all_urls'),
path('api/delete/<int:id>/', views.delete_url, name='delete_url'),
path('api/create/', views.create_short_url, name='api-create'),
path('api/create/<path:original_url>/', views.create_short_url, name='api-create'),






]