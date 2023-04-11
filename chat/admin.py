from django.contrib import admin
from .models import Channel, UserChannel, ChannelMessage


class ChannelMessageInline(admin.TabularInline):
    model = ChannelMessage
    extra = 1

class UserChannelInline(admin.TabularInline):
    model = UserChannel
    extra = 1

class ChannelAdmin(admin.ModelAdmin):
    inlines = [ChannelMessageInline, UserChannelInline ]

    class Meta: 
        model = Channel

admin.site.register(Channel, ChannelAdmin)
admin.site.register(UserChannel)
admin.site.register(ChannelMessage)
