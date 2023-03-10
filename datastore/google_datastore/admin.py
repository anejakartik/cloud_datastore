from django.contrib import admin
from .models import Tablea
# Register your models here.

class TableA_Admin(admin.ModelAdmin):

    list_display = ('id','created_on','operation','property_type','place_name','place_with_parent_names','country_name','state_name','geonames_id','lat_lon','lat','lon','price','currency','price_aprox_local_currency','price_aprox_usd','surface_total_in_m2','surface_covered_in_m2','price_usd_per_m2','price_per_m2','floor','rooms','expenses','properati_url','description','title','image_thumbnail')
    search_fields = ('id','state_name', 'title')
    list_filter = ('property_type','state_name')
    empty_value_display = '-empty-'

admin.site.register(Tablea,TableA_Admin)