from django.contrib import admin
from .models import Gigs, User, Comment, Customer, Employee
# Register your models here.
admin.site.register(Gigs)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Comment)



