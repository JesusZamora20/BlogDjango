from django.urls import path, re_path
from .views import dummy_view, status_code_view, entry_list, redirect_back_home

app_name = 'posts'

urlpatterns = [
    path('', redirect_back_home, name='entry-list'),
    path('<int:id>/', dummy_view, name='entry-detail'),
    re_path('(?P<id>[0-9]{4}/(?P<slug>[\w-]+)/$)', dummy_view, name='entry-detail'),
    path('<id>/delete/', dummy_view, name='entry-delete'),
    path('<id>/update/', dummy_view, name='entry-update'),
]