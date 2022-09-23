from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save , pre_save
from django.core.validators import MinValueValidator , MaxValueValidator
from datetime import datetime
from django.utils import timezone
from django.core.validators import RegexValidator


class Visitor(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11,validators = [RegexValidator(regex = r"^[0][5][0|2|3|4|5|9][-][0-9]{7}$" ,message="Phone number must be entered in the right format: 05X-XXXXXXX .")],blank=True ,  null = True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)] ,blank=True ,  null = True)
    url = models.URLField(blank=True ,  null = True)
    creation_date = models.DateField(default=timezone.now , blank = True)
    

    # class Meta:
    #     unique_together = ['first_name', 'last_name', 'email', 'phone']

    
    def __str__(self):
        return f"""Name: {self.first_name} {self.last_name} , 
        Email: {self.email} ,
        Phone Number: {self.phone} ,
        Address: {self.address} , 
        City: {self.city} , 
        Country: {self.country} , 
        Age: {self.age} ,
        Upload File: {self.url} ,
        Created At: {self.creation_date}"""



def post_profile_group(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            Visitor.objects.create(user_id = instance.id)
            Group.objects.get(name='Visitors').user_set.add(instance)
post_save.connect(receiver=post_profile_group, sender=User)

