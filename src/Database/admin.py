from django.contrib import admin

from .models import Doctor
admin.site.register(Doctor)


from .models import Patient
admin.site.register(Patient)

from .models import Reserve
admin.site.register(Reserve)

# Register your models here.
