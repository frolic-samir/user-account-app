from django.urls import path
from . import views as v

urlpatterns = [
    path('register/', v.register, name='register'),
    path('login/', v.loginMe, name='login'),
    path('logout/', v.logoutMe, name='logout'),

    path('', v.home, name='home'),
]
