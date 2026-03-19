from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('tech/', views.tech, name='tech'),
    path('nontech/', views.nontech, name='nontech'),

    path('budget/', views.budget, name='budget'),
    path('food/', views.food, name='food'),
    path('soundstage/', views.soundstage, name='soundstage'),
    path('photography/', views.photography, name='photography'),
    path('decoration/', views.decoration, name='decoration'),
    path('discipline/', views.discipline, name='discipline'),
    path('gifts/', views.gifts, name='gifts'),

    # non-tech
    path('insta/', views.insta, name='insta'),
    path('ludo/', views.ludo, name='ludo'),
    path('chess/', views.chess, name='chess'),
    path('lucky/', views.lucky, name='lucky'),
    path('freefire/', views.freefire, name='freefire'),
    path('rangoli/', views.rangoli, name='rangoli'),
    path('volleyball/', views.volleyball, name='volleyball'),

    # tech
    path('portfolio/', views.portfolio, name='portfolio'),
    path('poster/', views.poster, name='poster'),
    path('projectexpo/', views.projectexpo, name='projectexpo'),
    path('startup/', views.startup, name='startup'),
    path('livecoding/', views.livecoding, name='livecoding'),
    path('debugging/', views.debugging, name='debugging'),
    path('quiz/', views.quiz, name='quiz'),
    path('syntax/', views.syntax, name='syntax'),
]