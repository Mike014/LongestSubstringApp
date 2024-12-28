from django.db import models

# Create your models here.
class SubstringResult(models.Model):
    input_string = models.CharField(max_length=255)
    length_of_longest_substring = models.IntegerField()
