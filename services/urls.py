from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('index', gig_index, name='index'),
    path('create', gig_create, name='create'),
    path('<int:id>/', gig_detail, name='detail'),
    path('<int:id>/update', gig_update, name='update'),
    path('<int:id>/delete', gig_delete, name='delete'),
    path('register/', register, name='register'),
    path('customer_register/', customer_register.as_view(),
         name='customer_register'),
    path('employee_register/', employee_register.as_view(),
         name='employee_register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_view, name='logout'),
]
