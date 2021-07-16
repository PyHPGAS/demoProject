from django.contrib import admin
from django.utils.safestring import mark_safe
from myusers.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'img', 'dob','gender')
    list_display_links = ("user",)
    # search_fields = ("name", "id")
    # list_filter = ("name", "status", "featured")
    fields = (('user',), 'image', ('dob', 'gender'), 'user_image')
    # icon_name = 'apps'
    readonly_fields = ["user_image"]
    # fieldsets = [
    #     (None, {'fields': ['id', 'name', 'image']}),
    #     ('Advance information', {'fields': ['status', 'featured', 'created_at', 'updated_at'], 'classes':['collapse']}),
    # ]

    def user_image(self, obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url,))

    def img(self, obj):
        return mark_safe('<img src="{url}",  width="50px" height="50px" />'.format(url=obj.image.url))

admin.site.register(UserProfile, UserProfileAdmin)