from django.urls import path
from . import views

urlpatterns = [
    path('', views.toolcatalogue, name='tool catalogue'),
    path('tool/<int:pk>/', views.ToolDetailView.as_view(), name='tooldetails'),
]