from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','usuario','email')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)    
   
   
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}


class FotoDeNoticiaInline(admin.TabularInline):
    model = FotoDeNoticia
    extra = 1


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    inlines = (FotoDeNoticiaInline,)
    date_hierarchy = 'data_de_publicacao'
    list_filter = ('categoria',)


@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}



