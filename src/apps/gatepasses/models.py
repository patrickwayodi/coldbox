from django.db import models
from django.urls import reverse


class Gatepass(models.Model):

    description = models.TextField(max_length=300)

    date_created = models.DateField(blank=True, null=True)

    # def get_absolute_url(self):
        # return "/gatepass/%i/" % self.id

    def get_absolute_url(self):
        return reverse('gatepass_detail', args=[str(self.id)])

    def __str__(self):
        return self.description
