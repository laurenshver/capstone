from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('remove/<str:key>/', views.remove_from_cart, name="remove_from_cart"),
    path('assign-customer-to-order', views.assign_customer_to_order, name="assign_customer_to_order"),
    path('select_customer/<str:custID>/<int:rating>/<str:type>/<str:name>/<str:contact>/<str:identifier>/', views.select_customer, name="select_customer"),
    path('remove-customer/', views.delete_customer_session, name="remove_customer"),
    path('order-procurement', views.procurement, name="procurement"),
    path('review-order', views.review_order, name="review_order"),
    path('create-new-order', views.create_new_order, name="create_new_order"),
    path('order-placed/<int:pk>/', views.order_placed, name="order_placed"),
]