from django.urls import path
from .views import StatusListCreateView, StatusDetailView

urlpatterns = [
    path('status/', StatusListCreateView.as_view()),
    path('status/<int:pk>', StatusDetailView.as_view()),
]