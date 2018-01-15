from django.db import models
from django.utils import timezone

class Word(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    added_date = models.DateTimeField(default=timezone.now)
    complexity = models.DecimalField(max_digits=7, decimal_places=6)

    def __str__(self):
        return self.word
