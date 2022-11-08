from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save , pre_save
from django.core.validators import MinValueValidator , MaxValueValidator
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.text import slugify


class Visitor(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    identication = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=50)
    slug_name = models.SlugField(blank=True ,  null = True)
    email = models.EmailField(blank=True ,  null = True)
    phone = models.CharField(max_length=11,validators = [RegexValidator(regex = r"^[0][5][0|2|3|4|5|9][-][0-9]{7}$" ,message="Phone number must be entered in the right format: 05X-XXXXXXX .")],blank=True ,  null = True)
    address = models.CharField(max_length=100 , blank=True ,  null = True)
    city = models.CharField(max_length=100 , blank=True ,  null = True)
    country = models.CharField(max_length=10 , blank=True ,  null = True)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)] ,blank=True ,  null = True)
    url = models.CharField(max_length = 3000, blank=True ,  null = True)
    creation_date = models.DateField(auto_now_add=True )
    

    
    def __str__(self):
        return f"""ID: {self.identication}, 
        Name: {self.slug_name} , 
        Email: {self.email} ,
        Phone Number: {self.phone} ,
        Address: {self.address} , 
        City: {self.city} , 
        Country: {self.country} , 
        Age: {self.age} ,
        Upload File: {self.url} ,
        Created At: {self.creation_date}"""


    def save(self,*args,**kwargs):
        self.slug_name = slugify(self.name)
        super(Visitor,self).save(*args,**kwargs)


def post_profile_group(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            Visitor.objects.create(user_id = instance.id)
            Group.objects.get(name='Visitors').user_set.add(instance)
post_save.connect(receiver=post_profile_group, sender=User)

