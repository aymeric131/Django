from django.contrib import admin

# Register your models here.

from listings.models import *

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','sold','year','type')

admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListingAdmin)