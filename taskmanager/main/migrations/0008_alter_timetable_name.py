# Generated by Django 3.2.9 on 2021-11-20 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211121_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(choices=[('Tu', 'Tuesday'), ('Su', 'Sunday'), ('Sa', 'Saturday'), ('Mo', 'Monday'), ('Th', 'Thursday'), ('We', 'Wednesday'), ('Fr', 'Friday')], max_length=2, verbose_name='Day'),
        ),
    ]
