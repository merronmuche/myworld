from django.contrib import admin

from members.models import Members

class MembersAdmin(admin.ModelAdmin):

    list_display = ['firstname', 'lastname', 'age']

admin.site.register(Members, MembersAdmin)