from django.db import models
from django.contrib.auth.models import User

STATE_CHOICE=(("KERALA","KERALA"),
                ("TAMILNADU","TAMILNADU"),
                ("KARNADAKA","KARNADAKA")
)
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=30,choices=STATE_CHOICE)


STATUS_CHOICE=(('Accepted','Accepted'),
                ('packed','packed'),
                ('on the way','on the way'),
                ('delivered','delivered'),
                ('cancel','cancel')
                )

CATEGORY_CHOICES=(
('M','Mobile'),
('L','Laptop'),
('TW','Top Wear'),
('BW','Bottom wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=30)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    
class Orderplaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    ordered_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='pending')

