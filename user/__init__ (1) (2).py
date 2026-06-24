from django.contrib import admin
from .models import User, PaymentDetails,RentalAdmin
from vehicle.models import RentalHistory

# Register your models here.
admin.site.register(User)
admin.site.register(PaymentDetails)
admin.site.register(RentalHistory,RentalAdmin)
