from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass


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
    def pertence_ao_grupo_Editores( request, model_admin):
        if request.user.is_admin:
            a=readonly_fields = ('categoria',)
            return a

    def get_queryset(self):
        return super().get_queryset().filter(categoria='Politica')


@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}



