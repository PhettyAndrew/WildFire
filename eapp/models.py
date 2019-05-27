from django.db import models

# Create your models here.
class Event(models.Model):
    event_creator = models.CharField(max_length=40)
    event_password = models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    venue=models.CharField(max_length=40)
    date=models.DateField()
    time=models.TimeField()
    charges=models.CharField(max_length=40)
    contact=models.IntegerField()
    banner=models.ImageField()
    description=models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    event_name=models.ForeignKey(Event, on_delete=models.CASCADE)
    user_name=models.CharField(max_length=40)
    comment = models.TextField(max_length=100000000000)

    def __str__(self):
        return self.user_name

