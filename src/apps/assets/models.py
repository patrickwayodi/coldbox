from django.db import models
from django.urls import reverse


class Asset(models.Model):

    asset_file = models.FileField(upload_to='assetfiles/')

    description = models.CharField(max_length=5000)

    date = models.DateField(blank=True, null=True)

    # def get_absolute_url(self):
        # return "/asset/%i/" % self.id

    def get_absolute_url(self):
        return reverse('asset_detail', args=[str(self.id)])
    
    def __str__(self):
        
        return self.file_name
