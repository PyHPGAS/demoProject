from django.contrib import admin
from address.models import Country, State, City
# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','status')
    list_display_links = ("name",)
    search_fields = ("name",)
    list_filter = ("status",)

admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('country','name','status')
    list_display_links = ("name",)
    search_fields = ("name",'country')
    list_filter = ("status",'country')

admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('state','name','status')
    list_display_links = ("name",)
    search_fields = ("name",'state')
    list_filter = ("status",'state')

admin.site.register(City, CityAdmin)
