from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50,default=0)
    subcategory = models.CharField(max_length=50,default=0)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default="")
    description1 = models.CharField(max_length=300, default="")
    description2 = models.CharField(max_length=300, default="")
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
         return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    description = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Buy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    address = models.CharField(max_length=70, default="")
    state = models.CharField(max_length=70, default="")
    pin = models.CharField(max_length=70, default="")
    product_name = models.CharField(max_length=70, default="")
    price = models.CharField(max_length=70, default="")
    product_detail = models.CharField(default="", max_length=1000)
    product_detail1 = models.CharField(default="", max_length=1000)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name


