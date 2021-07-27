import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.dispatch import receiver
from django.db.models.signals import post_save

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

