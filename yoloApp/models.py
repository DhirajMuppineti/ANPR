from django.db import models
class MultipleImage(models.Model):
    car = models.FileField()
    segmentedImg = models.TextField(blank=True)
    plate_number = models.CharField(max_length=15)
