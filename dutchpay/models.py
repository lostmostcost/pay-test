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
    members = models.ManyToManyField(CustomUser)
    generated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

class Pay(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='payments')
    subject = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    payer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='payments_made')
    members = models.ManyToManyField(CustomUser, related_name='payments_included')
    amount = models.PositiveIntegerField(null=True)
    create_date = models.DateTimeField(default=timezone.now)
    days_until_deadline = models.IntegerField(default=3)
    deadline = models.DateTimeField(blank=True)
    is_settled = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.deadline = self.create_date + timedelta(days=self.days_until_deadline)
        super().save(*args, **kwargs)
    
    def __str__(self) :
        return self.event.subject +"/"+ self.subject
    
class Remit(models.Model):
    remitter = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='remits_to_send')
    receiver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='remits_to_receive')
    amount = models.PositiveIntegerField()
    is_settled = models.BooleanField(default=False)