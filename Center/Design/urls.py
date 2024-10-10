from django.urls import path
from .views import home, about, contact, contact_submit, privacy_policy, terms_of_service, faq

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/submit/', contact_submit, name='contact_submit'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),
    path('faq/', faq, name='faq'),
]
