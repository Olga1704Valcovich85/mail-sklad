from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('home_sklad', views.create, name='home_sklad'),
    path('about_news', views.about, name='about_news'),

]