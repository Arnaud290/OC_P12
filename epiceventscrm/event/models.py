from django.db import models
from client.models import Client
from contact.models import Contact
from contract.models import Contract


class Status(models.Model):
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name_plural = 'Status'


class Event(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    status_id = models.ForeignKey(Status, on_delete=models.PROTECT)
    attendees = models.IntegerField()
    notes = models.TextField(blank=True)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    support_contact_id = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    contract_id = models.ForeignKey(Contract, on_delete=models.PROTECT)
