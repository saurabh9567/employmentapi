from django.urls import path, include
from rest_framework import routers
from .views import CandidateViewset
router = routers.DefaultRouter()

router.register('api', CandidateViewset)

urlpatterns = [
    path('', include(router.urls)),
]