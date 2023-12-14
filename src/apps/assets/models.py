from django.db import models
from django.urls import reverse


class Asset(models.Model):

    description = models.TextField(max_length=300)

    asset_file = models.FileField(upload_to='assetfiles/')

    date_created = models.DateField(blank=True, null=True)

    # def get_absolute_url(self):
        # return "/asset/%i/" % self.id

    def get_absolute_url(self):
        return reverse('asset_detail', args=[str(self.id)])
    
    def __str__(self):
        
        return self.description
