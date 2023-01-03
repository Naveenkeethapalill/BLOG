from django.db import models
class Post(models.Model):
    title=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)
    content=models.TextField(max_length=1000)
    def __str__(self):
        return self.title
