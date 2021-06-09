from django.db import models
from client.models import Client
from contact.models import Contact


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payment_due = models.DateTimeField(blank=True)
    client_id = models.ForeignKey(
        Client,
        related_name='contract_client_id',
        on_delete=models.CASCADE
    )
    sales_contact_id = models.ForeignKey(
        Contact,
        related_name='contract_contact_id',
        on_delete=models.DO_NOTHING
    )
