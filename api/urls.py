from django.urls import path
from .views import EventsListAPI, EventDetailAPI, MembersListAPI, MemberDeatilAPI, PaysListAPI, PayDetailAPI, RemitListAPI, settle_payments


app_name = 'api'

urlpatterns = [
    path("events/", EventsListAPI.as_view()),
    path("events/<int:pk>/", EventDetailAPI.as_view()),
    path("events/<int:event_pk>/settle/", settle_payments),
    path("event/<int:event_pk>/bills/", RemitListAPI.as_view()),
    path("events/<int:event_pk>/members/", MembersListAPI.as_view()),
    path("events/<int:event_pk>/members/<int:member_pk>/", MemberDeatilAPI.as_view()),
    path("events/<int:event_pk>/pays/", PaysListAPI.as_view()),
    path("events/<int:event_pk>/pays/<int:pay_pk>/", PayDetailAPI.as_view()),
]