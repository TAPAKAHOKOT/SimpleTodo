# Generated by Django 5.2.3 on 2025-06-24 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('is_completed', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('onfire', 'On fire'), ('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], null=True)),
                ('repeat_after_minutes', models.IntegerField(blank=True, null=True)),
                ('task_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='tasks.tasklist')),
            ],
        ),
    ]
