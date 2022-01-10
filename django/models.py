from django.db import models

# Create your models here.
class book(models.Model):
    bookname1=models.CharField(max_length=20)
    des1=models.CharField(max_length=50)
    images=models.ImageField(upload_to='pro_img',blank=True)

    def __str__(self):
        return str(self.bookname1)

class member(models.Model):
    us=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    phn=models.IntegerField(default='')
    email=models.EmailField(default='')

    def __str__(self):
        return self.us


