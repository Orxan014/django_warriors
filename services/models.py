from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Gigs(models.Model):
    #user = models.ForeignKey('auth.User', related_name='posts')
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
