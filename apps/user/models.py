from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class Profile(AbstractUser):
    AVATAR_DEFAULT = 'default_avatar.png'
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending')
    ]

    avatar = models.ImageField(upload_to='avatars/', default=AVATAR_DEFAULT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.username

    def is_student(self):
        return self.groups.filter(name='Student').exists()

    def is_librarian(self):
        return self.groups.filter(name='Librarian').exists()

def create_groups(sender, **kwargs):
    Group.objects.get_or_create(name='Student')
    Group.objects.get_or_create(name='Librarian')

models.signals.post_migrate.connect(create_groups)
