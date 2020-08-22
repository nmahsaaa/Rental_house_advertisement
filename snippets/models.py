from django.db import models
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    title = models.CharField(max_length=500, null=True)
    score = models.IntegerField(null=True)
    description = models.TextField()
    city = models.CharField(max_length=500, null=True)
    price = models.IntegerField(null=True)

    class Meta:
        ordering = ['city']