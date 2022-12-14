# Generated by Django 4.0.6 on 2022-08-01 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('New', 'New'), ('In progress', 'In progress'), ('In QA', 'In QA'), ('Ready', 'Ready'), ('Done', 'Done')], max_length=12)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='creatorUser', to=settings.AUTH_USER_MODEL)),
                ('performer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='performerUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
