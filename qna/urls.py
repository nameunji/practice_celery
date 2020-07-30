from django.urls import path
from .views import QnaView

urlpatterns = [
    path('', QnaView.as_view())
]
