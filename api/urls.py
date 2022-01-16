from uuid import UUID
from django.urls import path
from .views import *

urlpatterns = [
    path('', getUuid, name='get_all_the_Models'),
]
