from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    first_name = models.CharField(max_length=100, default=None, null=True, blank=True)
    last_name = models.CharField(max_length=100, default=None, null=True, blank=True)
    score = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.first_name} {self.last_name} a eu {self.score}'
