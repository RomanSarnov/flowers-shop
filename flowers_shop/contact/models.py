from django.db import models


class Feedback(models.Model):
    subject = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    email = models.EmailField()
    copy = models.BooleanField()

    def __str__(self):
        return self.subject


class Newsletter(models.Model):
    email = models.EmailField(unique=True)


