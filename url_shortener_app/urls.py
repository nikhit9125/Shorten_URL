from django.urls import path
from .import views
from .views import *



urlpatterns=[
    path('URL_shortener/',views.URL_Shortener,name='URL_shortener'),
    # path('<str:shorten_url>/', views.redirect_to_original, name='redirect_to_original'),

]
