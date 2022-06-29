from django.contrib import admin
from .models import Register,Ownsale,Ownrent
from .models import Office_Staff

admin.site.register(Register)
admin.site.register(Ownsale)
admin.site.register(Ownrent)
admin.site.register(Office_Staff)
