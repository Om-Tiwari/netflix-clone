# Generated by Django 4.1.4 on 2023-03-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profiles',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='age_limit',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
