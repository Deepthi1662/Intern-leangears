from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User



class Blog(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=150) 
    content = models.TextField() # Text
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details')
