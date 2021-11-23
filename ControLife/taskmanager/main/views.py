from django.shortcuts import render, redirect
from django.http import Http404
from .models import Task, Timetable, Purpose, TaskList
from .forms import TaskForm, PurposeForm, ListAdd
from datetime import datetime


def start(request):
    return render(request, 'main/start.html')


def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            error = 'The form is not correct'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_task.html', context)


def week(request):
    Monday = Timetable.objects.filter(name__exact='Mo')
    Tuesday = Timetable.objects.filter(name__exact='Tu')
    Wednesday = Timetable.objects.filter(name__exact='We')
    Thursday = Timetable.objects.filter(name__exact='Th')
    Friday = Timetable.objects.filter(name__exact='Fr')
    Saturday = Timetable.objects.filter(name__exact='Sa')
    Sunday = Timetable.objects.filter(name__exact='Su')
    week = (
        Monday, Tuesday, Wednesday, Thursday,
        Friday, Saturday, Sunday
    )
    week_n = (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )
    return render(request, 'main/week.html', {'title': 'Week', 'week': week, 'week_n': week_n})


def change_week(request):
    Monday = Timetable.objects.filter(name__exact='Mo')
    Tuesday = Timetable.objects.filter(name__exact='Tu')
    Wednesday = Timetable.objects.filter(name__exact='We')
    Thursday = Timetable.objects.filter(name__exact='Th')
    Friday = Timetable.objects.filter(name__exact='Fr')
    Saturday = Timetable.objects.filter(name__exact='Sa')
    Sunday = Timetable.objects.filter(name__exact='Su')
    week = (
        Monday, Tuesday, Wednesday, Thursday,
        Friday, Saturday, Sunday
    )
    week_n = (
        'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'
    )
    n = (1, 2, 3, 4, 5, 6, 7)
    return render(request, 'main/change_week.html', {'title': 'Week', 'week': week, 'week_n': week_n, 'n': n})


def dell_task(request, idd, it):
    d = Timetable.objects.get(id=idd)
    d.task.remove(Task.objects.get(id=it))
    return redirect(request.META.get('HTTP_REFERER'))


def add_task(request, d):
    if 1 > d < 7:
        raise Http404('Wrong!')
    task = Task.objects.all()
    if request.method == 'POST':
        if request.POST['task']:
            post = request.POST['task']
            day = Timetable.objects.get(id=d)
            day.task.add(Task.objects.get(id=post))

    return render(request, 'main/add_task_week.html', {'title': 'Week', 'task': task})


def todolist(request):
    week = (
        'Mo',
        'Tu',
        'We',
        'Th',
        'Fr',
        'Sa',
        'Su'
    )
    now = datetime.today().strftime('%A')
    day = Timetable.objects.filter(name__exact=week[datetime.today().weekday()])
    task = TaskList.objects.all()
    return render(request, 'main/todolist.html', {'title': 'ToDoList', 'task': task, 'day': day, 'now': now})


def add_task_list(request):
    task = Task.objects.all()
    if request.method == 'POST':
        if request.POST['task']:
            post = request.POST['task']
            TaskList.objects.create(task=Task.objects.get(id=post))

    return render(request, 'main/add_task_list.html', {'title': 'List', 'task': task})


def dell_list(request, idl, idt):
    taskl = TaskList.objects.get(id=idl).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def create_list(request):
    error = ''
    if request.method == 'POST':
        form = ListAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            error = 'Форма не верная'
    form = ListAdd()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_list.html', context)


def purpose(request):
    cel = Purpose.objects.all()
    return render(request, 'main/purpose.html', {'title': 'Purpose', 'cel': cel})


def change_purpose(request, idp):
    d = Purpose.objects.get(id=idp)
    return render(request, 'main/change_purpose.html', {'title': 'Purpose', 'd': d})


def add_task_purpose(request, idp):
    task = Task.objects.all()
    if request.method == 'POST':
        if request.POST['task']:
            post = request.POST['task']
            day = Purpose.objects.get(id=idp)
            day.task.add(Task.objects.get(id=post))

    return render(request, 'main/add_task_purpose.html', {'title': 'Purpose', 'task': task, 'id': idp})


def create_purpose(request):
    error = ''
    if request.method == 'POST':
        form = PurposeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            error = 'Форма не верная'
    form = PurposeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_purpose.html', context)


def dell_purpose(request, idp, idt):
    d = Purpose.objects.get(id=idp)
    d.task.remove(Task.objects.get(id=idt))
    return redirect(request.META.get('HTTP_REFERER'))



