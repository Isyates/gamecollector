from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index , name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name = 'games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/assoc_achievement/<int:achievement_id>/', views.assoc_achievement, name='assoc_achievement'),
    path('games/<int:game_id>/add_photo/', views.add_photo, name = 'add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    
]