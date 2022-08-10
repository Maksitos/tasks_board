# Generated by Django 4.0.6 on 2022-08-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_board_app', '0003_task_timezone_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (1, 'In progress'), (1, 'In QA'), (1, 'Ready'), (1, 'Done')], default=1),
        ),
    ]