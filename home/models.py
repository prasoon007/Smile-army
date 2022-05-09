from io import DEFAULT_BUFFER_SIZE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class category(models.Model):
    cat_name = models.CharField(max_length=250)
    cover_pic = models.FileField(upload_to="cat_pics")
    description = models.TextField()
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name
        
class Services(models.Model):
    name=models.CharField(max_length=50)
    feeder=models.ForeignKey(User, on_delete=models.CASCADE)
    cate=models.ForeignKey(category,on_delete=models.CASCADE)
    desc=models.TextField()
    image=models.ImageField(upload_to="pics")
    address=models.TextField(default="LKO")
    Available_qunatitiy=models.IntegerField(default=5)

    def __str__(self):
        return self.name


class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    status=models.BooleanField(default="False")
    imaging=models.ForeignKey(Services, on_delete=models.CASCADE)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now=True,null=True)

    def ___str__(self):
        return self.user.username 

class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.BigIntegerField(null=True,unique=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'message from ' + self.name.username