from django.urls import path
from Management import views



urlpatterns = [
    path('',views.management,name='management'),
]