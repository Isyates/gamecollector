from django.db import models

# Create your models here.
class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, genre, description, ryear):
    self.title = title
    self.genre = genre
    self.description = description
    self.ryear = ryear

games = [
  Game('Dark Souls', 'Action RPG', 'The game that started the "SoulsLike" subgenre', 2011),
  Game('Sim City 4', 'Simulation', 'The game that brought city building back to the mainstream', 2003),
  Game('League of Legends', 'MOBA', 'Built the idea of esports to what it is today', 2009)
]