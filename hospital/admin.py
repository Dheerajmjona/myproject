from django.contrib import admin
from .models import Departments, Doctors, Booking, Contact

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','doc_name','p_name','p_phone','p_email','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message')
admin.site.register(Contact,ContactAdmin)