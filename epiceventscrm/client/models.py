from django.db import models
from contact.models import Contact


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact_id = models.ForeignKey(
        Contact,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        client = self.first_name + ' ' +\
            self.last_name + ' ' + self.company_name
        return client
