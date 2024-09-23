# Generated by Django 5.1.1 on 2024-09-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_avatar_remove_profile_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_avatar.png', upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending')], default='active', max_length=10),
        ),
    ]
