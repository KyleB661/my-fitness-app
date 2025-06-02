from django.db import models

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.date}"

    class Meta:
        ordering = ['-date']

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kg")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.sets}x{self.reps} @ {self.weight}kg"