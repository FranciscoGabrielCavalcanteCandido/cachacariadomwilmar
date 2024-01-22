from django.urls import path
from .views import IndexView, SobreView

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
]