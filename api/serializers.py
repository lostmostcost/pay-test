from rest_framework import serializers
from ..dutchpay.models import Event, Member, Pay, Remit

class EventSerializer(serializers.ModelSerializer):
    class Meta :
        model = Event
        fields = ['subject', 'creat_date']

class MemberSerializer(serializers.ModelSerializer):
    class Meta :
        model = Member
        fields = ['user', 'event', 'balance', 'remainder_counts']

class PaySerializer(serializers.ModelSerializer):
    class Meta :
         model = Pay
         fields = ['event', 'subject', 'description', 'payer', 'members', 'amount', 'create_date', 'is_settled']

class RemitSerializer(serializers.ModelSerializer):
    class Meta :
        model = Remit
        fields = ['remitter', 'receiver', 'amount', 'days_until_deadline' 'deadline', 'is_settled']