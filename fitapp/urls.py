from django.urls import path
from . import views


app_name = 'fitapp'
urlpatterns = [
    path('progress/', views.ProgressBar, name='progress'),
    path('Logs/', views.LogReq, name='Logs'),
    path('viewLogs/', views.viewLogs, name='viewLogs'),
    path('achievements/', views.Achievements, name='achievements'),
    path('achievements/update/<int:user_id>', views.update, name='update'),
    path('viewLogs/<int:logs_id>', views.log, name='log'),
    path('viewLogs/<int:logs_id>/comment', views.post_detail, name='post_detail'),
    path('Logs/updatelogs/<int:user_id>', views.updatelogs, name='updatelogs'),
    path('viewLogs/<int:logs_id>/deleteLog', views.deleteLog, name='deleteLog'),
    path('viewLogs/<int:logs_id>/shareable', views.shareable, name='shareable'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('userLogs/<int:user_id>', views.userLogs, name='userLogs')
]