from django.contrib import admin

from . import models

to_register = [
    models.Movie,
]

admin.site.register(to_register)
