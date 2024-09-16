from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactView, AddVolunteerView, SuccessView

router = DefaultRouter()

urlpatterns = [
    path('', AddVolunteerView.as_view(), name='add-volunteer'),
    path('success', SuccessView.as_view(), name='success'),
    path('contact/', ContactView.as_view(), name='contact-volunteer'),
    # path('', include(router.urls)),
]

