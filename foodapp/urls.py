from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/<int:candidate_id>', views.candidate_detail, name='candidate_detail'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('support-cases/', views.support_cases, name='support_cases'),
    path('sales-orders/', views.sales_order, name='sales_order'),
    path('payroll/', views.payroll, name='payroll'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]