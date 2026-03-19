from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path("upload_temp_image/", views.upload_temp_image, name="upload_temp_image"),
    path("delete_temp_image", views.delete_temp_image, name="delete_temp_image"),
    path("", views.show_products, name="show_products"),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update/<int:product_id>/', views.product_update, name='product_update'),
]