from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect
from dutchpay.models import Event, Member, Pay, Remit
from .serializers import EventSerializer, MemberSerializer, PaySerializer, RemitSerializer

class EventsListAPI(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'pk'

class MembersListAPI(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    
    def get_queryset(self):
        event = self.kwargs['event_pk']
        queryset = Member.objects.filter(event=event)
        return queryset

class MemberDeatilAPI(generics.RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        event = self.kwargs['event_pk']
        queryset = Member.objects.filter(event=event)
        return queryset

class PaysListAPI(generics.ListCreateAPIView):
    serializer_class = PaySerializer

    def get_queryset(self):
        event = self.kwargs['event_pk']
        queryset = Pay.objects.filter(event=event)
        return queryset

class PayDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaySerializer

    def get_queryset(self):
        event = self.kwargs['event_pk']
        queryset = Pay.objects.filter(event=event)
        return queryset
    
class RemitListAPI(generics.ListAPIView):
    serializer_class = RemitSerializer

    def get_queryset(self):
        event = self.kwargs['event_pk']
        queryset = Remit.objects.filter(is_settled=False, event=event)
        return queryset

def settle_payments(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    event.settle_payments()
    event.make_bills()
    return redirect(f"http://127.0.0.1:8000/api/events/{event_pk}/")