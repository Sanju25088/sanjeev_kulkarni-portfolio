from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    Personal_Information,
    Education,
    Technical_Skils,
    Internship,
    Key_Projects,
    Certifications,
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Profile', {'fields': ('user_type', 'profile_image')}),
    )
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')


admin.site.register(Personal_Information)
admin.site.register(Education)
admin.site.register(Technical_Skils)
admin.site.register(Internship)
admin.site.register(Key_Projects)
admin.site.register(Certifications)
