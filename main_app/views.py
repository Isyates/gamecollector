from django.shortcuts import render
from .models import Game



# Define the home view
def home(request):
  return render(request, 'home.html')

# About Route
def about(request):
  return render(request, 'about.html')

# Games Index Route
def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', {'game': game})