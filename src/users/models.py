from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField("The name of the person",max_length=30)
    last_name = models.CharField("The last name of the person",max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="cars of the user")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'not reviewed'),
    ('E', 'error'),
    ('A', 'accepted'),
)

class Website(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_released_last_week(self):
        if self.release_date < datetime.date(2025, 2,24):
            return "released before last week"
        else:
            return "released this week" 
    
    @property
    def get_full_name(self):
        return f"This is the full name of the website: {self.name}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/websites/{self.id}/"
    
    def save(self, *args, **kwargs):
        print("Saving...")
        super().save(*args, **kwargs)

class Car(models.Model):
    name = models.CharField(max_length=30, primary_key=True)