from django.urls import path
from .views import registerView ,loginView , homeView ,logoutView

urlpatterns = [
    path('' , registerView , name= 'register'),
    path('login/', loginView , name='login'),
    path('home/' , homeView , name = 'home'),
    path('logout/' , logoutView , name = 'logout')
]