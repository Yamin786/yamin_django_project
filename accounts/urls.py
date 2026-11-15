from django.urls import path
from . import views


urlpatterns = [
    
    path('login/', views.login_view , name = 'login'),
    path('register/' , views.registration_view , name='register'),
    path('error/' , views.error , name='error'),
    path('', views.home_view , name= 'home'),
    path('logout/', views.logout_view , name='logout'),
    path('accinfo/',views.apiView , name='apiview')
]