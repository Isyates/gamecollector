from django.db import models

# Create your models here.
class Game(models.Model):  # Note that parens are optional if not inheriting from another class
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    ryear = models.IntegerField()

    def __str__(self):
      return self.name
