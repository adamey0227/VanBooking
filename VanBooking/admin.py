from django.contrib import admin

# Register your models here.

from.models import Student, Driver, Booking

admin.site.register(Student)
admin.site.register(Driver)
admin.site.register(Booking)