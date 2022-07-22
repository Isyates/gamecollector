from django.shortcuts import render, redirect
from .models import Game, Achievement, Photo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from.forms import HistoryForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'gamecollector-iy-90'

class GameCreate(CreateView):
  model = Game
  fields = '__all__'
  success_url = '/games/'
  def form_valid(self, form):
  # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
  # Let the CreateView do its job as usual
    return super().form_valid(form)

# Define the home view
def home(request):
  return render(request, 'home.html')

# About Route
def about(request):
  return render(request, 'about.html')

# Games Index Route
@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', {'games': games})

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  achievements_game_doesnt_have = Achievement.objects.exclude(id__in = game.achievements.all().values_list('id'))
  play_history = HistoryForm()
  return render(request, 'games/detail.html', {'game': game, 'play_history': play_history,'achievements': achievements_game_doesnt_have})

@login_required
def assoc_achievement(request, game_id, achievement_id):
  # Note that you can pass a achievement's id instead of the whole object
  Game.objects.get(id=game_id).achievements.add(achievement_id)
  return redirect('detail', game_id=game_id)

@login_required
def add_photo(request, game_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, game_id=game_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', game_id=game_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class GameUpdate(LoginRequiredMixin,UpdateView):
  model = Game
  # Let's disallow the renaming of a Game by excluding the name field!
  fields = ['genre', 'description', 'ryear']

class GameDelete(LoginRequiredMixin,DeleteView):
  model = Game
  success_url = '/games/'

class AchievementList(LoginRequiredMixin,ListView):
  model = Achievement

class AchievementDetail(LoginRequiredMixin,DetailView):
  model = Achievement

class AchievementCreate(LoginRequiredMixin,CreateView):
  model = Achievement
  fields = '__all__'

class AchievementUpdate(LoginRequiredMixin,UpdateView):
  model = Achievement
  fields = ['name', 'color']

class AchievementDelete(LoginRequiredMixin,DeleteView):
  model = Achievement
  success_url = '/achievements/'