from django.contrib import admin
from .models import Task, Timetable, Purpose, TaskList


admin.site.register(Task)
admin.site.register(Timetable)
admin.site.register(Purpose)
admin.site.register(TaskList)

