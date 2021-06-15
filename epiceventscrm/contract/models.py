from django.db import models
from django.db.models.base import Model
from client.models import Client
from contact.models import Contact


class Status(models.Model):
    status_name = models.CharField(max_length=20)

    def __str__(self):
        return  self.status_name

    class Meta:
        verbose_name_plural = 'Status'


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey(
        Status,
        related_name='Status',
        on_delete=models.PROTECT
    )
    amount = models.FloatField()
    contract_text = models.TextField(blank=False)
    payment_due = models.DateTimeField(blank=True, null=True)
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    sales_contact_id = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        contract = str(self.id) + ' ' +self.client_id.company_name + ' ' +\
            str(self.date_created.strftime('%d %m %Y')) + ' '
        return contract
