from django.urls import path
from .views import CategoryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register("categories", CategoryView)

urlpatterns = [
] + router.urls

