from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class new_profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no=models.BigIntegerField(default=0)
    upload_on=models.DateTimeField(auto_now_add=True)
    profile_picture=models.ImageField(upload_to="pics",default="default/download.jpg")
    address=models.TextField(blank=True)
    pin=models.IntegerField(default=0000)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    aadhar_id=models.BigIntegerField(default=0)
    regname=models.CharField(max_length=25)
    

    def __str__(self):
        return self.user.username



