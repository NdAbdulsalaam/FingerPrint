from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HomeView, UserRegistrationView, UserLoginView, UserProfileView, user_logout,
    ContactView, ParticipantAddView, ParticipantListView
)

router = DefaultRouter()

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('logout/', user_logout, name='user-logout'),
    path('contact/', ContactView.as_view(), name='user-contact'),
    path('participants/add/', ParticipantAddView.as_view(), name='add-participant'),
     path('participants/', ParticipantListView.as_view(), name='list-participant'),
    # path('', include(router.urls)),
]

