from django.contrib import admin
from city_handbook_app.models import Establishment, EstCategory, City

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    pass

@admin.register(EstCategory)
class EstCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
