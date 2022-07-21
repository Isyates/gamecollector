from django.db import models
from django.urls import reverse

PLATFORM = (
  ('PC', 'PC'),
  ('Xbox', 'Xbox Series X'),
  ('PS5', 'Playstation 5'),
  ('Switch', 'Nintendo Switch')
)


class Achievement(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  
# Create your models here.
class Game(models.Model):  # Note that parens are optional if not inheriting from another class
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    ryear = models.IntegerField()
    achievements = models.ManyToManyField(Achievement)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
      return reverse('detail', kwargs = {'game_id': self.id})

class History(models.Model):
  date = models.DateField('Last Played')
  play_history = models.CharField(
    max_length = 20,
    choices = PLATFORM,
    default = PLATFORM[0][0]
  )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  def __str__(self):
    return f'game last played on {self.get_play_history_display()} on {self.date}'


