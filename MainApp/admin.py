from django.contrib import admin
from MainApp.models import Libro, Persona, Telefonino


class PersonaAdmin(admin.ModelAdmin):
    pass

class LibroAdmin(admin.ModelAdmin):
    pass

class TelefoninoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Telefonino, TelefoninoAdmin)
