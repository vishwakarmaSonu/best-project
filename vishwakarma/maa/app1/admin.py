from django.contrib import admin
from .models import Booking
admin.site.register(Booking)



from .models import product
admin.site.register(product)

from .models import Tag
admin.site.register(Tag)

from .models import Order
admin.site.register(Order)

from .models import name
admin.site.register(name)


from .models import contact
admin.site.register(contact)
# Register your models here.
