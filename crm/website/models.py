from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default='default@example.com')
    phone_no=models.CharField(max_length=15)
    address=models.CharField(max_length=200,default="Default address")
    city=models.CharField(max_length=50,default="Default city")
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)  

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")                 
    

