from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.start, name='home'),
    path('timetable', views.week, name='timetable'),
    path('purpose', views.purpose, name='purpose'),

    path('todolist', views.todolist, name='list'),
    path('dell_list/<int:idl>/<int:idt>', views.dell_list, name='dell_list'),
    path('create_list', views.create_list, name='create_list'),

    path('create_task', views.create_task, name='create_task'),
    path('create_purpose', views.create_purpose, name='create_purpose'),

    path('add_task_week/<int:d>', views.add_task, name="add_task_week"),
    path('add_task_list', views.add_task_list, name="add_task_list"),

    path('change_week', views.change_week, name='change_week'),
    path('change_week/del/<int:idd>/<int:it>', views.dell_task, name="dell_task"),

    path('change_purpose/<int:idp>', views.change_purpose, name="change_purpose"),
    path('change_purpose/del/<int:idp>/<int:idt>', views.dell_purpose, name="dell_purpose"),
    path('change_purpose/add/<int:idp>', views.add_task_purpose, name="add_task_purpose")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
