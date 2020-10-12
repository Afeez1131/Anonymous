from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f'{self.name} send {self.user} an Anonymous message {self.id}'

