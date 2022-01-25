import datetime
from django.db.models.fields import (
    DateField, DateTimeField, DurationField, Field, IntegerField, TimeField,
)
from django.utils import timezone
from django.db import models
from quizes.models import Quiz


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=120)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_answer(self):
        pass
