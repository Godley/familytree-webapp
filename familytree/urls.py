from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:user_id>', views.identify, name='identify'),
]