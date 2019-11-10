from django.contrib import admin

# Register your models here.

from .models import Author, Scenario, Plugin

admin.site.register(Author)
admin.site.register(Scenario)
admin.site.register(Plugin)

# Ends here.
