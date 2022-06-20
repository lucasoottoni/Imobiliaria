from django.contrib import admin
from imobiliaria.models import Categoria, Pessoa, TipoImovel, Imovel, Fotos
from nested_inline.admin import NestedTabularInline, NestedModelAdmin



class FotosInline(admin.TabularInline):
    model = Fotos
    extra = 0

class ImovelAdmin(admin.ModelAdmin):
    inlines = [FotosInline]


admin.site.register(Categoria)
admin.site.register(Pessoa)
admin.site.register(TipoImovel)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Fotos)
