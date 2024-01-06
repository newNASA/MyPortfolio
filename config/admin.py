from django.contrib import admin
from .models import My_info, My_skills, My_social, Interests, My_projects
# Register your models here.

admin.site.register(My_social)
admin.site.register(My_info)
admin.site.register(My_skills)
admin.site.register(Interests)
admin.site.register(My_projects)
