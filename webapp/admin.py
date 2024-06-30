from django.contrib import admin
from .models import Pets
from .models import Adopt
from .models import Volunteer

# Register your models here.
admin.site.register(Pets)
admin.site.register(Adopt)
admin.site.register(Volunteer)