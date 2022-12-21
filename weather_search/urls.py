from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Search

urlpatterns = [
    path('', login_required(Search.as_view()), name='dashboard')
]