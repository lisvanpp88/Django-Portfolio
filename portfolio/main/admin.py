from django.contrib import admin

# Register your models here.
from .models import Tag, Project, ProjectImage, Contact

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",) 

class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')    


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Contact, ContactAdmin)