from django.urls import path
from .views import register, homepage, login,logout


urlpatterns = [
    path('', homepage, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout')
]