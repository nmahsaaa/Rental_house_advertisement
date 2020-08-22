from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class ads(models.Model):
    score = models.IntegerField(null=True)
    title = models.CharField(max_length=500, null=True)
    location = models.CharField(max_length=1000, null=True)
    image = models.ImageField(default='ad-default.jpg', upload_to='Ads_Pix')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    available = models.BooleanField(null=True)
    room_no = models.IntegerField(null=True)
    description = models.TextField()
    smokeFree = models.BooleanField(null=True)
    city = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=5000, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title #+ "\n Score: " + self.score + "\n Rooms: " + self.room_no + "\n About: " + self.description + "\n Address: " + self.address

    def get_absolute_url(self):
        return reverse('Advertisements-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(ads, self).save(*args, **kwargs)
        img = Image.open(self.image.path)