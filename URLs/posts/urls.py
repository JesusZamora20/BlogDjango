from django.urls import path
from .views import dummy_view

urlpatterns = [
    path('', dummy_view, name='entry-list'),
    path('<id>/', dummy_view, name='entry-detail'),
    path('<id>/delete/', dummy_view, name='entry-delete'),
    path('<id>/update/', dummy_view, name='entry-update'),
]