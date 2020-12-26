from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index', gig_index, name='index'),
    path('create', gig_create, name='create'),
    path('<int:id>/', gig_detail, name='detail'),
    path('<int:id>/update', gig_update, name='update'),
    path('<int:id>/delete', gig_delete, name='delete'),

]
