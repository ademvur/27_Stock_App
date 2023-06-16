from django.urls import path
from .views import CategoryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register("categories", CategoryView)
router.register("brands", BrandView)
router.register("firms", FirmView)

urlpatterns = [
] + router.urls

