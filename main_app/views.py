from django.shortcuts import render
from .models import Game, Achievement
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.forms import HistoryForm


class GameCreate(CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'

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
  achievements_game_doesnt_have = Achievement.objects.exclude(id__in = game.achievements.all().values_list('id'))
  play_history = HistoryForm()
  return render(request, 'games/detail.html', {'game': game, 'play_history': play_history,'achievements': achievements_game_doesnt_have})
  
def assoc_achievement(request, game_id, achievement_id):
  # Note that you can pass a achievement's id instead of the whole object
  game.objects.get(id=game_id).achievements.add(achievement_id)
  return redirect('detail', game_id=game_id)

class GameUpdate(UpdateView):
  model = Game
  # Let's disallow the renaming of a Game by excluding the name field!
  fields = ['genre', 'description', 'ryear']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

class AchievementList(ListView):
  model = Achievement

class AchievementDetail(DetailView):
  model = Achievement

class AchievementCreate(CreateView):
  model = Achievement
  fields = '__all__'

class AchievementUpdate(UpdateView):
  model = Achievement
  fields = ['name', 'color']

class AchievementDelete(DeleteView):
  model = Achievement
  success_url = '/achievements/'