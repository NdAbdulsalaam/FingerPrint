from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ContactView, AddVolunteerView, SuccessView


urlpatterns = [
    path('', AddVolunteerView.as_view(), name='add-volunteer'),
    path('success/', SuccessView.as_view(), name='success'),
    path('contact/', ContactView.as_view(), name='contact-volunteer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
