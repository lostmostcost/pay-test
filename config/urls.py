from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dutchpay.urls', namespace='dutchpay')),
    path('api/', include('pay_api.urls', namespace='pay_api')),
]
