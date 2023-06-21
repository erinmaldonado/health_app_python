from django.db import models


# Create your models here.

class Symptom(models.Model):
    """A symptom the user is experiencing."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Notes about symptom"""
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)


class Meta:
    verbose_name_plural = 'entries'


def __str__(self):
    """Return a string representation of the model"""
    return f"{self.text[:50]}..."

