import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.dispatch import receiver
from django.db.models.signals import post_save
from twilio.rest import Client


# Create your models here.
class Sparepart(models.Model):
    '''
    class to create instances of spareparts
    '''
    part_image=CloudinaryField('image',blank=True,null=True)
    part_price = models.DecimalField(decimal_places=2,max_digits=20)
    part_name = models.CharField(max_length=20)
    part_type=models.CharField(max_length=40,null=True)

    def _str_(self):
        return self.part_name

    def save_sparepart(self):
        self.save() 

    def delete_sparepart(self):
        self.delete() 

        
    @classmethod 
    def get_spareparts(cls):
       spares=Sparepart.objects.all()
       return spares

    @classmethod
    def search_spares(cls,search_term):
        parts = cls.objects.filter(part_name__icontains=search_term)
        return parts
class Phone(models.Model):
    '''
    class to create instances of phones
    '''
    phone_image=CloudinaryField('image',blank=True,null=True)
    phone_type = models.CharField(max_length=20)
    phone_model=models.CharField(max_length=20,null=True)
    description=models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    contact=models.CharField(max_length=40,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='phone',primary_key=True)




    def _str_(self):
        return self.phone_type

    def save_phone(self):
        self.save() 

    def delete_phone(self):
        self.delete() 

        
    @classmethod 
    def get_phones(cls):
       phones=Phone.objects.all()
       return phones

    @classmethod
    def search_phones(cls,search_term):
        parts = cls.objects.filter(phone_type__icontains=search_term)
        return parts

class Laptop(models.Model):
    '''
    class to create instances of phones
    '''
    lap_image=CloudinaryField('image',blank=True,null=True)
    lap_type = models.CharField(max_length=20)
    lap_model=models.CharField(max_length=20,null=True)
    description=models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    contact=models.CharField(max_length=40,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='laptop',primary_key=True)



    def _str_(self):
        return self.lap_type

    def save_laptop(self):
        self.save() 

    def delete_laptop(self):
        self.delete() 

        
    @classmethod 
    def get_laptops(cls):
       laptops=Laptop.objects.all()
       return laptops

    @classmethod
    def search_laptops(cls,search_term):
        parts = cls.objects.filter(lap_type__icontains=search_term)
        return parts

#defining a simple class
class Message(models.Model):
    #integer field
    test_result = models.PositiveIntegerField()

    #string representation
    def __str__(self):
        return str(self.test_result)
    def save(self, *args, **kwargs):
        #if test_result is less than 80 execute this
        if self.test_result < 80:
            #twilio code
            account_sid = 'ACaeaf4bacd8228f9133b846bb56c8a164'
            auth_token = 'dc5c1ffa32e82ec3ca906af1944e3241'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hi, your gadget was successfully fixed, {self.test_result}. Great job',
                                        from_='+16304739731',
                                        to='0724835573' 
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)




