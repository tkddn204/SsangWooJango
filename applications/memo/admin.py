from django.contrib import admin

from applications.memo.models import Memo, Bbs


class MemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'last_modified', 'reply_count')


class BbsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created',)

admin.site.register(Memo, MemoAdmin)
admin.site.register(Bbs, BbsAdmin)
