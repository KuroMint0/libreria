from django.contrib import admin
from .models import Editorial, Libro

# Register your models here.

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'pais', 'telefono')
    search_fields = ('nombre', 'pais')
    list_filter = ('pais',)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'precio_formateado', 'editorial')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_publicacion', 'editorial')

    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return f"${obj.precio:,}".replace(',', '.') 

    