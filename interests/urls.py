from django.urls import path, include
from . import views
from rest_framework import routerss

router = routers.DefaultRouter()
router.register('interests',views.InterestsView)


urlpatterns = [
    path('',include(router.urls))
]
