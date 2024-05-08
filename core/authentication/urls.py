from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('register/',views.register_page,name='register'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('signup', views.signup, name='signup_html'),
    path('findRent', views.findRent, name='findRent_html'),
    path('findLease', views.findLease, name='findLease_html'),
    path('postRent', views.postRent, name='postRent_html'),
    path('postLease', views.postLease, name='postLease_html'),
]