from django.urls import path

from .views import pay_view

urlpatterns = [
    path('', pay_view, name='pay-view'),
]
