from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    # Cria um filtro de hierarquia com datas
    # enviando a lista de manyTomany
    list_display = ('user', 'specialtiesList', 'addressesList',)
    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)