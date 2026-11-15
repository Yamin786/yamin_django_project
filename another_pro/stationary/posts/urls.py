from django.urls import path
from .views import *

urlpatterns = [
    path('', postView , name='posts'),
    path('edits/<int:pk>' , editView , name='edit'),
    path('delete/<int:pk>' , deleteView , name='delete')
]