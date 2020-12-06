from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio.html', views.portfolio, name='portfolio'),

]
