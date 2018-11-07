from django.contrib import admin
from datetime import date
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

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


class NoticiasListFilter(admin.SimpleListFilter):
    # Título legível por humanos que será exibido no
    # barra direita de administração logo acima das opções de filtro.
    title = 'Noticias por data'

    # Parâmetro para o filtro que será usado na consulta de URL.
    parameter_name = 'intervalo_data'

    def lookups(self, request, model_admin):
        """
        Retorna uma lista de tuplas. O primeiro elemento em cada
        tupla é o valor codificado para a opção que
        aparecem na consulta de URL. O segundo elemento é o
        nome legível para a opção que aparecerá
        na barra lateral direita.
        """
        return (
            ('2018-1',  _('2018 janeiro')),
            ('2018-2',  _('2018 fevereiro')),
            ('2018-3',  _('2018 março')),
            ('2018-4',  _('2018 abril')),
            ('2018-5',  _('2018 maio')),
            ('2018-6',  _('2018 junho')),
            ('2018-7',  _('2018 julho')),
            ('2018-8',  _('2018 agosto')),
            ('2018-9',  _('2018 setembro')),
            ('2018-10', _('2018 outubro')),
            ('2018-11', _('2018 novembro')),
            ('2018-12', _('2018 dezembro')),
        )

    def queryset(self, request, queryset):
        """
        Retorna o queryset filtrado com base no valor
        fornecido na string de consulta e recuperável via
        `self.value ()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '2018-1':
            return queryset.filter(data_de_publicacao__gte=date(2018, 1, 1),
                                    data_de_publicacao__lte=date(2018, 1, 31))
        if self.value() == '2018-2':
            return queryset.filter(data_de_publicacao__gte=date(2018, 2, 1),
                                    data_de_publicacao__lte=date(2018, 2, 28))
        if self.value() == '2018-3':
            return queryset.filter(data_de_publicacao__gte=date(2018, 3, 1),
                                    data_de_publicacao__lte=date(2018, 3, 31))                                   
        if self.value() == '2018-4':
            return queryset.filter(data_de_publicacao__gte=date(2018, 4, 1),
                                    data_de_publicacao__lte=date(2018, 4, 30))
        if self.value() == '2018-5':
            return queryset.filter(data_de_publicacao__gte=date(2018, 5, 1),
                                    data_de_publicacao__lte=date(2018, 5, 31))
        if self.value() == '2018-6':
            return queryset.filter(data_de_publicacao__gte=date(2018, 6, 1),
                                    data_de_publicacao__lte=date(2018, 6, 30))
        if self.value() == '2018-7':
            return queryset.filter(data_de_publicacao__gte=date(2018, 7, 1),
                                    data_de_publicacao__lte=date(2018, 7, 31))
        if self.value() == '2018-8':
            return queryset.filter(data_de_publicacao__gte=date(2018, 8, 1),
                                    data_de_publicacao__lte=date(2018, 8, 31))
        if self.value() == '2018-9':
            return queryset.filter(data_de_publicacao__gte=date(2018, 9, 1),
                                    data_de_publicacao__lte=date(2018, 9, 30))
        if self.value() == '2018-10':
            return queryset.filter(data_de_publicacao__gte=date(2018, 10, 1),
                                    data_de_publicacao__lte=date(2018, 10, 31))
        if self.value() == '2018-11':
            return queryset.filter(data_de_publicacao__gte=date(2018, 11, 1),
                                    data_de_publicacao__lte=date(2018, 11, 30))
        if self.value() == '2018-12':
            return queryset.filter(data_de_publicacao__gte=date(2018, 12, 1),
                                    data_de_publicacao__lte=date(2018, 12, 31))                                                                                                                                                                                                                                                                                         
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    inlines = (FotoDeNoticiaInline,)
    date_hierarchy = ('data_de_publicacao')
    list_filter = ('categoria', NoticiasListFilter)


@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}



