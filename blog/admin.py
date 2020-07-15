from django.contrib import admin
from .models import prescription_form
from .models import Medicine


admin.site.register(prescription_form)
admin.site.register(Medicine)

admin.site.site_header = "ESD Administration"
