from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.webp',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img=Image.open(self.image.path)
    #     print(img.height,img.width)
    #     if img.height>512 or img.width>512:
    #         output_size=(512,512)
    #         img.thumbnail(output_size)
    #         img=img.convert("RGB")
    #         img.save(self.image.path)


        


# Create your models here.
