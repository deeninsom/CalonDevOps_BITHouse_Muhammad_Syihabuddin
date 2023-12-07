from django.urls import path
from .views import CategoryListCreateView, CategoryListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>', CategoryListCreateView.as_view()),
]