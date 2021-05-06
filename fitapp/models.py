"""
*  REFERENCES
*
*  Title: Creating Comments System With Django
*  Author: Django Central
*  URL: https://djangocentral.com/creating-comments-system-with-django/
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    current = models.IntegerField(default=0) # bar part of progress bar
    maximum = models.IntegerField(default=100) # maximum length bar can be
    def __str__(self):
        return f'{self.user.username} Profile'

EXERCISE_CHOICES = (
    ('pushup','pushup'),
    ('situp', 'situp'),
    ('pullup','pullup'),
    ('squat','squat'),
    ('burpee','burpee'),
    ('lift','lift'),
    ('run','run'),
    ('stretches','stretches'),
    ('other','other'),
)

INTENSITY_CHOICES = (
    ('light','light'),
    ('moderate', 'moderate'),
    ('vigorous','vigorous'),
)

DEFAULT_duration = 1
MAX_duration = 500
MIN_duration = 0

#DURATION should be slider
#DATE should be found using datepicker

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# logs model
class Logs(models.Model):
    exercise = models.CharField(max_length=10, choices=EXERCISE_CHOICES, default='other')#, help_text="title.")
    date = models.DateField()
    duration = models.PositiveSmallIntegerField( name=('duration'), default=DEFAULT_duration,validators=[MinValueValidator(MIN_duration), MaxValueValidator(MAX_duration)])
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES, default='light')
    area = models.CharField(max_length=10)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.date + ":" + self.exercise + "\n"

# begin Creating Comments code #
class Comment(models.Model):
    post = models.ForeignKey(Logs,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    #email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
# end Creating Comments code #


