from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('home_sklad', views.create_prod, name='home_sklad'),
    path('about_news', views.create, name='about_news'),
    path('<int:pk>', views.NewsDetail.as_view(), name='about_views')

]