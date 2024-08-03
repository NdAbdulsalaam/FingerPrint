from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeView, UserRegistrationView, UserLoginView, UserProfileView, user_logout,
    ContactView,
)

router = DefaultRouter()

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', user_logout, name='user-logout'),
    path('contact/', ContactView.as_view(), name='user-contact'),
    
    # path('', include(router.urls)),
]

