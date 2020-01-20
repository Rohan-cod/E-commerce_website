from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    brief_desc=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    full_desc=models.CharField(max_length=500,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=70,default="")
    selection=models.CharField(max_length=150,default="")
    phone=models.CharField(max_length=70,default="")
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name