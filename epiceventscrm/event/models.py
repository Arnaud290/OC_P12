from django.db import models
from client.models import Client
from contact.models import Contact
from contract.models import Contract


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_date = models.DateTimeField()
    status = models.BooleanField(default=True)
    attendees = models.IntegerField()
    notes = models.TextField(blank=True)

    client_id = models.ForeignKey(
        Client,
        related_name='event_client_id',
        on_delete=models.CASCADE
    )
    support_contact_id = models.ForeignKey(
        Contact,
        related_name='support_contact_id',
        on_delete=models.DO_NOTHING
    )
    contract_id = models.ForeignKey(
        Contract,
        related_name='event_contract_id',
        on_delete=models.CASCADE
    )
