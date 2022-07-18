from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Home</h1>')

# About Route
def about(request):
  return render(request, 'about.html')

# Games Index Route
def games_index(request):
  return render(request, 'games/index.html', { 'games': games })