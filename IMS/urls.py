from django.urls import path
from . import views


urlpatterns = [
    path('show/',views.ShowProduct.as_view(),name='show_product'),
]
