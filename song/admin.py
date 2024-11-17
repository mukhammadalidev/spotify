from django.contrib import admin

from song.models import Song,Artist,PlayListSong,PlayList,Genre


# Register your models here.
admin.site.register(Song, admin.ModelAdmin)
admin.site.register(Artist, admin.ModelAdmin)
admin.site.register(PlayList, admin.ModelAdmin)
admin.site.register(PlayListSong, admin.ModelAdmin)
admin.site.register(Genre, admin.ModelAdmin)
