from django.urls import path

from .views import Login, logout


app_name = 'login'

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path("logout/", logout, name="logout"),
    
]