from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('sales/', views.sales_dealerships, name='sales_dealerships'),
    path('sales/<int:dealership_id>', views.sales_dealership, name='sales_dealership'),
    path('inventory/', views.inventory_dealerships, name='inventory_dealerships'),
    path('inventory/<int:dealership_id>', views.inventory_dealership, name='inventory_dealership'),
    path('inspections/', views.inspections_dealerships, name='inspections_dealerships'),
    path('inspections/<int:dealership_id>', views.inspections_dealership, name='inspections_dealership'),
    path('new_sale/<int:dealership_id>', views.new_sale, name='new_sale'),
    path('new_inventory/<int:dealership_id>', views.new_inventory, name='new_inventory'),
    path('new_inspection/<int:dealership_id>', views.new_inspection, name='new_inspection'),
    path('edit_sale/<int:sale_id>/', views.edit_sale, name='edit_sale'),
    path('edit_inventory/<int:inventory_id>/', views.edit_inventory, name='edit_inventory'),
    path('edit_inspection/<int:inspection_id>/', views.edit_inspection, name='edit_inspection'),
]