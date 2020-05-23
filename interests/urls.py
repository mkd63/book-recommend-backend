from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('interests', views.InterestsView)

urlpatterns = [
    path('',include(router.urls))
]
