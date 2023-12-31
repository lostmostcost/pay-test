from rest_framework import generics
from dutchpay.models import Event, Member, Pay, Remit
from .serializers import EventSerializer, MemberSerializer, PaySerializer, RemitSerializer

class EventsListAPI(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MembersListAPI(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    
    def get_queryset(self):
        event = self.kwargs['event']
        queryset = Member.objects.filter(event=event)
        return queryset

class MemberDeatilAPI(generics.RetrieveAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        queryset = Member.objects.filter(event=event)
        return queryset

class PaysListAPI(generics.ListCreateAPIView):
    serializer_class = PaySerializer

    def get_queryset(self):
        event = self.kwargs['event']
        queryset = Pay.objects.filter(event=event, is_settled=False)
        return queryset

class PayDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaySerializer

    def get_queryset(self):
        event = self.kwargs['event']
        queryset = Pay.objects.filter(event=event)
        return queryset
    
class RemitListAPI(generics.ListAPIView):
    queryset = Remit.objects.filter(is_settled=False)
    serializer_class = RemitSerializer