from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class msg (models.Model):
    #receiver = Users()
    subject = models.CharField(max_length=500, null=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '%(class)s_requests_created')
    reciever = models.ForeignKey(User, on_delete = models.CASCADE, related_name = '%(class)s_requests_assigned')

    def __str__(self):
        return "Title: " + self.subject + "\n " + self.content


