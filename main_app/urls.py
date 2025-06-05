from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/create/', views.workout_create, name='workout_create'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('workouts/<int:workout_id>/update/', views.workout_update, name='workout_update'),
    path('workouts/<int:workout_id>/delete/', views.workout_delete, name='workout_delete'),
    path('workouts/<int:workout_id>/exercises/create/', views.exercise_create, name='exercise_create'),
    path('workouts/<int:workout_id>/exercises/<int:exercise_id>/update/', views.exercise_update, name='exercise_update'),
    path('workouts/<int:workout_id>/exercises/<int:exercise_id>/delete/', views.exercise_delete, name='exercise_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]