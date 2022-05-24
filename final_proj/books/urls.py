from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import BookView,JournalView

router = DefaultRouter()
router.register(r'books',BookView,basename='book')
router.register(r'journals',JournalView,basename='journal')

urlpatterns = [
    path('',include(router.urls))
]
