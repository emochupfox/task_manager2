from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    STATUS_CHOICES = [  # Defines available status options
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Overdue', 'Overdue'),
    ]
    
    id = models.AutoField(primary_key=True) # Auto-incrementing primary key
    title = models.CharField(max_length=100) # Task title (required)
    description = models.TextField(blank=True, null=True) # Optional task description
    due_date = models.DateField() # Date the task is due
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') # Task status

    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < now().date():
            self.status = 'Overdue'
        elif self.status != 'Completed':
            self.status = 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    