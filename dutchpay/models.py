from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from datetime import timedelta

class CustomUser(AbstractUser):
    bank_account = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

class Event(models.Model):
    subject = models.CharField(max_length=20)
    create_date = models.DateTimeField(default=timezone.now)

    def settle_payments(self):
        unsettled_payments = self.payments.filter(is_settled=False)
        for pay in unsettled_payments :
            payer = pay.payer
            members = pay.members.all()
            amount = pay.amount

            payer.balance -= amount
            payer.save()

            equal_share, remainder = divmod(amount, len(members))

            if remainder != 0 :
                for remain in range(remainder) :
                    lowest_remainder_user = min(members, key=lambda x: x.remainder_counts)
                    lowest_remainder_user.balance += 1
                    lowest_remainder_user.remainder_counts += 1
                    lowest_remainder_user.save()


            for member in members :
                member.balance += equal_share
                member.save()

            pay.is_settled = True
            pay.save()
    
    def make_bills(self) :
        members = self.members.all()
        while any(member.balance for member in members) :
            remitter = max(members, key=lambda a : a.balance)
            receiver = min(members, key=lambda b : b.balance)
            amount = remitter.balance

            remitter.balance -= amount
            remitter.save()
            receiver.balance += amount
            receiver.save()

            Remit.objects.create(
                remitter=remitter.user,
                receiver=receiver.user,
                amount=amount)


    def __str__(self):
        return self.subject
    
class Member(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='belong_to')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='members')
    balance = models.IntegerField(default=0)
    remainder_counts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Pay(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='payments')
    subject = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    payer = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, related_name='payments_made')
    members = models.ManyToManyField(Member, related_name='payments_included')
    amount = models.PositiveIntegerField(null=True)
    create_date = models.DateTimeField(default=timezone.now)
    is_settled = models.BooleanField(default=False)
    
    def __str__(self) :
        return self.event.subject +"/"+ self.subject
    
class Remit(models.Model):
    remitter = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='remits_to_send')
    receiver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='remits_to_receive')
    amount = models.PositiveIntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    days_until_deadline = models.IntegerField(default=3)
    deadline = models.DateTimeField(blank=True, null=True)
    is_settled = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.deadline = self.create_date + timedelta(days=self.days_until_deadline)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.remitter.username + "->" + self.receiver.username + "|" + str(self.amount)