# Generated by Django 5.1.1 on 2024-09-19 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('incomplete', 'Incomplete'), ('onprogress', 'On Progress')], default='incomplete', max_length=10),
        ),
    ]
