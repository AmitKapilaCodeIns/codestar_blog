from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores information about the blog or author
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title
    
    
class CollaborateRequest(models.Model):
    """
    Stores collaboration requests from users
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"