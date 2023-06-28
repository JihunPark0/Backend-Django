#admin site that allows us to have CRUD access to our db
from django.contrib import admin
from customers.models import Customer

admin.site.register(Customer)