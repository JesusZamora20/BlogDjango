from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'not reviewed'),
    ('E', 'error'),
    ('A', 'accepted'),
)

class Website(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)