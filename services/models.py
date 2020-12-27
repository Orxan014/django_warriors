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
    cover_photo = models.ImageField(upload_to='User_images/',default='1024.jpg', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)

# we have to maximize Customer model


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='customer', primary_key=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    #adress = models.CharField(max_length=20)
    # location =

# we have to maximize Employee model


class Employee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='employee', primary_key=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    #

# employee can offer their services


class Gigs(models.Model):
    connect_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Title")
    content = RichTextField(verbose_name="Content")
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'id': self.id})

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


class Wanted_Task(models.Model):
    task_name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, default=None)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)
    task_count = models.IntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    task_link = models.URLField(blank=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateField(blank=False)

    def __str__(self):
        return self.task_name


class UserRating(models.Model):
    task = models.OneToOneField(Employee, on_delete=models.CASCADE)
    emp = models.ForeignKey(Customer, related_name='rating_by',on_delete=models.CASCADE)
    e_rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    def __str__(self):
        return str(self.task.id) + "--" + str(self.emp.user.username)


class Notification(models.Model):
    _from = models.ForeignKey(
        Customer, related_name="msgfrom", on_delete=models.CASCADE)
    _to = models.ForeignKey(
        Customer, related_name='msgto', on_delete=models.CASCADE)
    message = models.CharField(default=None, max_length=300)
    has_read = models.BooleanField(default=False)
    sending_time = models.DateTimeField(auto_now_add=True, blank=True)
    recieving_time = models.DateTimeField(default=None, blank=True, null=True)
