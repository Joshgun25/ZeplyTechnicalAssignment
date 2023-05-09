from django.urls import path

from .views import list_addresses, generate_address, retrieve_address

urlpatterns = [
    path('generate_address/', generate_address, name='generate_address'),
    path('list_addresses/', list_addresses, name='list_addresses'),
    path('retrieve_address/<int:id>/', retrieve_address, name='retrieve_address'),
]