from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    habits_quantity = models.PositiveIntegerField(default = 0)
    current_strike_count = models.PositiveIntegerField(default = 0)
    longest_strike = models.PositiveIntegerField(default = 0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path).convert('RGB')
        
        if img.height > 250 or img.width > 250:
            output_size = (250,250)
            img.thumbnail(output_size)
            img.save(self.image.path)
