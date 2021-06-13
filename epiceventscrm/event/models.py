from django.db import models
from client.models import Client
from contact.models import Contact
from contract.models import Contract


class Event(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    status = models.BooleanField()
    attendees = models.IntegerField()
    notes = models.TextField(blank=True)

    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )
    support_contact_id = models.ForeignKey(
        Contact,
        on_delete=models.DO_NOTHING
    )
    contract_id = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE
    )
