# Generated by Django 3.2.9 on 2021-11-20 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_timetable_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='name',
            field=models.CharField(choices=[('Th', 'Thursday'), ('Fr', 'Friday'), ('We', 'Wednesday'), ('Sa', 'Saturday'), ('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday')], max_length=2, verbose_name='Day'),
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.task')),
            ],
        ),
    ]