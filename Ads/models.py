from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.utils import timezone

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    features = models.ManyToManyField(Features, related_name="models")
    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.IntegerField()
    contact = models.IntegerField()
    description = models.TextField(max_length=255)
    published_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="ads")
    def __str__(self):
        return self.title


class SecondRide(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    ads = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="secondrides")
    def __str__(self):
        return self.name