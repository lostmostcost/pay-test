from rest_framework import serializers
from dutchpay.models import Event, Member, Pay, Remit

class EventSerializer(serializers.ModelSerializer):
    class Meta :
        model = Event
        fields = ['pk', 'subject', 'create_date']

class MemberSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta :
        model = Member
        fields = ['pk','user','username', 'event', 'balance', 'remainder_counts']

    def get_username(self, obj) :
        return obj.user.username

class PaySerializer(serializers.ModelSerializer):
    class Meta :
         model = Pay
         fields = ['event', 'subject', 'description', 'payer', 'members', 'amount', 'create_date', 'is_settled']

class RemitSerializer(serializers.ModelSerializer):
    class Meta :
        model = Remit
        fields = ['event', 'remitter', 'receiver', 'amount', 'days_until_deadline', 'deadline', 'is_settled']