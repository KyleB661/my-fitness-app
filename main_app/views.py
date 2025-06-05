from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'main_app/home.html'

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'main_app/workout_list.html', {'workouts': workouts})

@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    exercises = workout.exercises.all()
    return render(request, 'main_app/workout_detail.html', {
        'workout': workout,
        'exercises': exercises
    })

@login_required
def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'main_app/workout_form.html', {'form': form, 'action': 'Create'})

@login_required
def workout_update(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'main_app/workout_form.html', {'form': form, 'action': 'Update'})

@login_required
def workout_delete(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'main_app/workout_confirm_delete.html', {'workout': workout})

@login_required
def exercise_create(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = ExerciseForm()
    return render(request, 'main_app/exercise_form.html', {
        'form': form,
        'workout': workout,
        'action': 'Add'
    })

@login_required
def exercise_update(request, workout_id, exercise_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    exercise = get_object_or_404(Exercise, id=exercise_id, workout=workout)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'main_app/exercise_form.html', {
        'form': form,
        'workout': workout,
        'action': 'Edit'
    })

@login_required
def exercise_delete(request, workout_id, exercise_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    exercise = get_object_or_404(Exercise, id=exercise_id, workout=workout)
    if request.method == 'POST':
        exercise.delete()
        return redirect('workout_detail', workout_id=workout.id)
    return render(request, 'main_app/exercise_confirm_delete.html', {
        'exercise': exercise,
        'workout': workout
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('workout_list')
        else:
            error_message = 'Invalid sign up - try again'
    form = CustomUserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)