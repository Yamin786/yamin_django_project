
from .views import comment_view
from django.urls import path 

urlpatterns = [

    path('', comment_view , name='comments'),
    
]