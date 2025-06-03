from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm

def home(request):
    return render(request, 'main_app/home.html')

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'main_app/workout_list.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    exercises = workout.exercises.all()
    return render(request, 'main_app/workout_detail.html', {
        'workout': workout,
        'exercises': exercises
    })

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'main_app/workout_form.html', {'form': form, 'action': 'Create'})

def workout_update(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', workout_id=workout.id)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'main_app/workout_form.html', {'form': form, 'action': 'Update'})

def workout_delete(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')

def exercise_create(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
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

def exercise_update(request, workout_id, exercise_id):
    workout = get_object_or_404(Workout, id=workout_id)
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

def exercise_delete(request, workout_id, exercise_id):
    workout = get_object_or_404(Workout, id=workout_id)
    exercise = get_object_or_404(Exercise, id=exercise_id, workout=workout)
    if request.method == 'POST':
        exercise.delete()
        return redirect('workout_detail', workout_id=workout.id)
    return render(request, 'main_app/exercise_confirm_delete.html', {
        'exercise': exercise,
        'workout': workout
    })