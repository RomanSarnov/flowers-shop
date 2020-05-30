from django.urls import path
from .views import CreateFeedbackView, AddNewsletterView


urlpatterns = [
    path('feedback/', CreateFeedbackView.as_view(), name='feedback'),
    path('newsletter/', AddNewsletterView.as_view(), name='newsletter')
]