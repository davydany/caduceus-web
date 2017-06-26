from django.contrib import admin

from monitor_admin.models import Project, Request
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):

    pass

class RequestAdmin(admin.ModelAdmin):

    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Request, RequestAdmin)