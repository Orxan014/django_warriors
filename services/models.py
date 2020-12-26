from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cover_photo = models.ImageField(blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(null=True, blank=True, unique=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='custom', primary_key=True)
    #phone_number = models.CharField(max_length=20)
    #adress = models.CharField(max_length=20)
    # location =


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='worker', primary_key=True)
    #phone_number = models.CharField(max_length=20)
    birthday = models.DateField( null=True, blank=True)
    #


class Gigs(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'id': self.id})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('services:create', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('services:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('services:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-publishing_date', 'id']


class Comment(models.Model):
    work = models.ForeignKey(
        'services.Gigs', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    content = models.TextField(verbose_name='add_comment')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
