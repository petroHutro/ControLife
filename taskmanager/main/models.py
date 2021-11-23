from django.db import models


class Task(models.Model):
    name = models.CharField('Task', max_length=100)
    time = models.TimeField('Time')

    def __str__(self):
        return self.name


class Timetable(models.Model):
    DAY_WEEK = {
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday')
    }
    name = models.CharField('Day', max_length=2, choices=DAY_WEEK)
    task = models.ManyToManyField(Task)


class Purpose(models.Model):
    name = models.CharField('Name', max_length=100)
    task = models.ManyToManyField(Task)
    start = models.DateTimeField('Start', auto_now_add=True)
    finish = models.DateTimeField('Finish', auto_now_add=True)
    planed = models.DateTimeField('Planed')


class TaskList(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    data = models.DateField('Data')

