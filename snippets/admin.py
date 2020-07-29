from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'language', 'style', 'created')
    list_filter = ('owner', 'created')
    search_fields = ('title', 'code')

    readonly_fields = ('highlighted_html',)
    exclude = ('highlighted',)

    def highlighted_html(self, obj):
        return mark_safe(obj.highlighted)
