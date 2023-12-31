from django.urls import path
from .views import EventsListAPI, EventDetailAPI, MembersListAPI, MemberDeatilAPI, PaysListAPI, PayDetailAPI, RemitListAPI


app_name = 'api'

urlpatterns = [
    path("events/", EventsListAPI.as_view()),
    path("events/<int:pk>/", EventDetailAPI.as_view()),
    path("events/<int:event>/members/", MembersListAPI.as_view()),
    path("events/<int:event>/members/<int:pk>/", MemberDeatilAPI.as_view()),
    path("events/<int:event>/pays/", PaysListAPI.as_view()),
    path("events/<int:event>/pays/<int:pk>/", PayDetailAPI.as_view()),
    path("bills/", RemitListAPI.as_view()),
]