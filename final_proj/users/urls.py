from django.urls import path
from .views import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/',LoginView.as_view()),
    path('token/',TokenObtainPairView.as_view())
]
