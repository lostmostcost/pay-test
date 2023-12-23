from django.urls import path
from django.views.generic import TemplateView

app_name = 'dutchpay'

urlpatterns = [
    path('', TemplateView.as_view(template_name='dutchpay/index.html')),
]